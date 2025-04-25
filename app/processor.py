import pandas as pd
from datetime import time

# Function to safely convert to Timedelta
def convert_to_timedelta(time_str):
    """Convert time string in 'HH:MM:SS' format to Timedelta object."""
    try:
        return pd.to_timedelta(time_str)
    except Exception as e:
        print(f"Error converting {time_str}: {e}")
        return pd.NaT  # Return Not a Time (NaT) for invalid formats

# Load and preprocess the CSV
def load_data(csv_path):
    df = pd.read_csv(csv_path)

    # Convert necessary columns to datetime
    datetime_cols = ['ChatStartTime', 'ChatEndTime', 'AgentAssignmentTimestamp']
    for col in datetime_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')  # This handles invalid dates and coerces them to NaT

    # Check for NaT in 'ChatStartTime' and drop those rows or handle accordingly
    df = df.dropna(subset=['ChatStartTime'])

    # Convert 'AgentFirstResponseTime' to Timedelta, handling invalid formats
    df['AgentFirstResponseTime'] = df['AgentFirstResponseTime'].apply(convert_to_timedelta)

    # Add week column using a safe method to avoid errors
    df['Week'] = df['ChatStartTime'].dt.to_period("W").apply(
        lambda r: r.start_time.strftime('%d %b') + " - " + (r.end_time - pd.Timedelta(days=1)).strftime('%d %b')
    )

    return df

# Calculate Chat Metrics
def calculate_chat_metrics(df):
    grouped = df.groupby('Week')
    chat_data = []

    # Overall row
    overall = {
        "Week": "Overall",
        "Incoming Chats": df['RoomCode'].nunique(),
        "Unique Users": df['UserId'].nunique(),
        "Closed By Bot": df[df['ClosedBy'] == 'System'].shape[0],
        "Bot Deflection %": df[df['ClosedBy'] == 'System'].shape[0] / df['RoomCode'].nunique(),
        "Closed By Agents": df[df['ClosedBy'] != 'System'].shape[0],
    }
    chat_data.append(overall)

    # Weekly rows
    for week, group in grouped:
        incoming = group['RoomCode'].nunique()
        closed_by_bot = group[group['ClosedBy'] == 'System'].shape[0]
        closed_by_agents = group[group['ClosedBy'] != 'System'].shape[0]
        
        chat_data.append({
            "Week": week,
            "Incoming Chats": incoming,
            "Unique Users": group['UserId'].nunique(),
            "Closed By Bot": closed_by_bot,
            "Bot Deflection %": closed_by_bot / incoming if incoming else 0,
            "Closed By Agents": closed_by_agents,
        })

    # Convert to DataFrame
    chat_df = pd.DataFrame(chat_data)

    # Sum totals and average for overall row
    overall = chat_df.iloc[0]
    chat_df.iloc[0] = [
        overall["Week"],
        chat_df["Incoming Chats"].sum(),
        chat_df["Unique Users"].sum(),
        chat_df["Closed By Bot"].sum(),
        chat_df["Bot Deflection %"].mean(),
        chat_df["Closed By Agents"].sum(),
    ]

    return chat_df

# Calculate Agent Metrics
def calculate_agent_metrics(df):
    agents = df[~df['ClosedBy'].isin(['System', 'Bot'])]['ClosedBy'].unique()
    df_agents = df[df['ClosedBy'].isin(agents)].copy()
    grouped = df_agents.groupby(['Week', 'ClosedBy'])
    agent_rows = []

    for (week, agent), group in grouped:
        chat_resolution_time = (group['ChatEndTime'] - group['ChatStartTime']).dt.total_seconds()

        # CSAT Score handling
        csat_scores = group['CsatScore'].dropna()
        pos = csat_scores[csat_scores.isin([4, 5])].count()
        neg = csat_scores[csat_scores.isin([1, 2, 3])].count()
        overall_csat = pos / (pos + neg) if (pos + neg) else None

        # Business Hours
        business_hours = group[ 
            group['ChatStartTime'].dt.time.between(time(10, 0), time(17, 0))
        ]
        bh_scores = business_hours['CsatScore'].dropna()
        bh_pos = bh_scores[bh_scores.isin([4, 5])].count()
        bh_neg = bh_scores[bh_scores.isin([1, 2, 3])].count()
        bh_csat = bh_pos / (bh_pos + bh_neg) if (bh_pos + bh_neg) else None

        # Outside Business Hours
        obh_scores = group[~group['ChatStartTime'].dt.time.between(time(10, 0), time(17, 0))]['CsatScore'].dropna()
        obh_pos = obh_scores[obh_scores.isin([4, 5])].count()
        obh_neg = obh_scores[obh_scores.isin([1, 2, 3])].count()
        obh_csat = obh_pos / (obh_pos + obh_neg) if (obh_pos + obh_neg) else None

        agent_rows.append({
            "Week": week,
            "Agent Name": agent,
            "Chats Resolved": group.shape[0],
            "Avg Agent First Response Time (seconds)": group['AgentFirstResponseTime'].mean().total_seconds(),
            "Avg Agent Chat Resolution Time (seconds)": chat_resolution_time.mean(),
            "Average Agent CSAT Score": overall_csat,
            "Business Hours CSAT [ Business Hours: 10AM - 5PM]": bh_csat,
            "Outside Business Hours CSAT": obh_csat
        })

    agent_df = pd.DataFrame(agent_rows)

    # Overall row
    overall_group = df_agents
    resolution_time = (overall_group['ChatEndTime'] - overall_group['ChatStartTime']).dt.total_seconds()
    csat = overall_group['CsatScore'].dropna()
    pos = csat[csat.isin([4, 5])].count()
    neg = csat[csat.isin([1, 2, 3])].count()
    overall_csat = pos / (pos + neg) if (pos + neg) else None

    bh = overall_group[overall_group['ChatStartTime'].dt.time.between(time(10, 0), time(17, 0))]
    bh_csat = bh['CsatScore'].dropna()
    bh_pos = bh_csat[bh_csat.isin([4, 5])].count()
    bh_neg = bh_csat[bh_csat.isin([1, 2, 3])].count()
    bh_score = bh_pos / (bh_pos + bh_neg) if (bh_pos + bh_neg) else None

    obh = overall_group[~overall_group['ChatStartTime'].dt.time.between(time(10, 0), time(17, 0))]
    obh_csat = obh['CsatScore'].dropna()
    obh_pos = obh_csat[obh_csat.isin([4, 5])].count()
    obh_neg = obh_csat[obh_csat.isin([1, 2, 3])].count()
    obh_score = obh_pos / (obh_pos + obh_neg) if (obh_pos + obh_neg) else None

    overall_agent_row = {
        "Week": "Overall",
        "Agent Name": "All Agents",
        "Chats Resolved": overall_group.shape[0],
        "Avg Agent First Response Time (seconds)": overall_group['AgentFirstResponseTime'].mean().total_seconds(),
        "Avg Agent Chat Resolution Time (seconds)": resolution_time.mean(),
        "Average Agent CSAT Score": overall_csat,
        "Business Hours CSAT [ Business Hours: 10AM - 5PM]": bh_score,
        "Outside Business Hours CSAT": obh_score
    }

    return pd.concat([pd.DataFrame([overall_agent_row]), agent_df], ignore_index=True)

# Calculate Miscellaneous Metrics [Bonus]
def calculate_miscellaneous_metrics(df):
    df['ChatHour'] = df['ChatStartTime'].dt.hour
    df['ChatHalfHour'] = df['ChatStartTime'].dt.minute // 30 * 30  # 0 or 30 minutes mark
    
    half_hourly_chats = df.groupby(['ChatHour', 'ChatHalfHour']).size().reset_index(name='Number of chats')
    half_hourly_chats['Time Bucket'] = half_hourly_chats['ChatHalfHour'].apply(lambda x: f'{x:02d}:00 - {x+30:02d}:00')
    
    # Drop the unnecessary columns
    half_hourly_chats = half_hourly_chats.drop(columns=['ChatHour', 'ChatHalfHour'])
    
    # Reorder the columns if needed (optional)
    half_hourly_chats = half_hourly_chats[['Time Bucket', 'Number of chats']]
    # 2. Calculate Active Time, Free Time, and Cumulative Time for each agent
    agent_metrics = []
    agents = df[~df['ClosedBy'].isin(['System', 'Bot'])]['ClosedBy'].unique()
    
    for agent in agents:
        agent_df = df[df['ClosedBy'] == agent].sort_values(by='ChatStartTime')
        free_time = []
        active_time = []
        cumulative_time = []

        prev_end_time = None
        total_active_time = pd.Timedelta(0)
        total_free_time = pd.Timedelta(0)
        total_cumulative_time = pd.Timedelta(0)
        
        for _, row in agent_df.iterrows():
            if prev_end_time:
                free_time_duration = row['ChatStartTime'] - prev_end_time
                free_time.append(free_time_duration)
                total_free_time += free_time_duration

            active_time_duration = row['ChatEndTime'] - row['ChatStartTime']
            active_time.append(active_time_duration)
            total_active_time += active_time_duration

            cumulative_time_duration = row['ChatEndTime'] - row['ChatStartTime']
            cumulative_time.append(cumulative_time_duration)
            total_cumulative_time += cumulative_time_duration

            prev_end_time = row['ChatEndTime']
        
        agent_metrics.append({
            'Agent Name': agent,
            'Free Time': str(total_free_time),
            'Active Time': str(total_active_time),
            'Cumulative Time': str(total_cumulative_time)
        })

    miscellaneous_metrics = pd.DataFrame(agent_metrics)

    return half_hourly_chats, miscellaneous_metrics

# Master function to generate all metrics
def generate_all_metrics(csv_path):
    df = load_data(csv_path)
    chat_df = calculate_chat_metrics(df)
    agent_df = calculate_agent_metrics(df)
    half_hourly_chats, miscellaneous_df = calculate_miscellaneous_metrics(df)
    return chat_df, agent_df, half_hourly_chats, miscellaneous_df

# Save all metrics to Excel
def save_to_excel(chat_df, agent_df, half_hourly_chats, miscellaneous_df, output_path="Metrics_Report.xlsx"):
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        chat_df.to_excel(writer, sheet_name='Chat Metrics', index=False)
        agent_df.to_excel(writer, sheet_name='Agent Metrics', index=False)
        half_hourly_chats.to_excel(writer, sheet_name='Miscellaneous Metrics [Bonus]', index=False)
        miscellaneous_df.to_excel(writer, sheet_name='Agent Metrics Time', index=False)

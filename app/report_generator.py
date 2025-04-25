import pandas as pd
def save_to_excel(chat_df, agent_df, half_hourly_chats, miscellaneous_df, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        chat_df.to_excel(writer, sheet_name="Chat Metrics", index=False)
        agent_df.to_excel(writer, sheet_name="Agent Metrics", index=False)
        half_hourly_chats.to_excel(writer, sheet_name="Miscellaneous Metrics Bonus", index=False)
        miscellaneous_df.to_excel(writer, sheet_name="Agent Metrics Time", index=False)

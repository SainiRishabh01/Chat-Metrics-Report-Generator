import streamlit as st
from app.processor import generate_all_metrics  # Assuming your generate_all_metrics function combines everything
from app.report_generator import save_to_excel  # Assuming save_to_excel saves the metrics to an Excel file

# Streamlit app code
def main():
    st.title("Chat Metrics Report Generator")

    # File uploader to upload the CSV file
    uploaded_file = st.file_uploader("Upload Chat Data CSV", type="csv")

    if uploaded_file:
        # Write the uploaded file to a temporary location
        with open("temp.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Generate the metrics (Chat, Agent, and Miscellaneous)
        chat_df, agent_df, half_hourly_chats, miscellaneous_df = generate_all_metrics("temp.csv")

        # Save the generated metrics to an Excel file
        output_path = "Chat_Metrics_Report.xlsx"
        save_to_excel(chat_df, agent_df, half_hourly_chats, miscellaneous_df, output_path)

        # Create a download button for the generated report
        with open(output_path, "rb") as f:
            st.download_button(
                label="📥 Download Report",
                data=f,
                file_name=output_path,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()

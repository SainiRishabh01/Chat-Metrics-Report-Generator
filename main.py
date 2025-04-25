
from app.processor import generate_metrics
from app.report_generator import save_to_excel

if __name__ == "__main__":
    # Path to your data dump file
    csv_path = "data_dump.csv"
    output_path = "generated_report.xlsx"

    chat_metrics_df, agent_metrics_df = generate_metrics(csv_path)
    save_to_excel(chat_metrics_df, agent_metrics_df, output_path)
    print(f"Report saved to {output_path}")

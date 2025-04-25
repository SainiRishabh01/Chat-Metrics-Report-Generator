Chat Metrics Report Generator
This project processes a chat data dump (CSV file) to generate various metrics related to chat interactions and agent performance. The metrics are compiled into an Excel report, which can be downloaded using a Streamlit web application or generated directly via a Python script.
Features
Chat Metrics: Tracks the number of incoming chats, unique users, chats closed by bots, bot deflection percentage, and chats closed by agents.

Agent Metrics: Measures agent performance based on metrics like chat resolution time, CSAT score, and performance during business and non-business hours.

Miscellaneous Metrics: Includes half-hourly chat statistics and agent active, free, and cumulative times.

Excel Report: Generates a well-organized Excel report with separate sheets for different types of metrics.

Requirements
Python 3.x

Necessary libraries:

pandas

openpyxl

streamlit

xlsxwriter

To install the required libraries, run the following command:
pip install -r requirements.txt
Project Structure

project/
├── app/
│   ├── processor.py             # Data processing logic and metric calculations
│   ├── report_generator.py      # Logic to save the metrics into an Excel file
│   └── __init__.py
├── data_dump.csv                # Chat data CSV (ignored by .gitignore)
├── main.py                      # Entry point for generating the report via CLI
├── requirements.txt             # List of required Python libraries
├── streamlit_app.py             # Streamlit web app for generating and downloading report

How to Use
1. Using the Command Line Script
Run the main.py script to generate a report directly from the command line:

python main.py
This will read the data_dump.csv file, generate the metrics, and save them in a file called generated_report.xlsx.

2. Using the Streamlit Web Application
Run the Streamlit app using the following command:

streamlit run streamlit_app.py
Open the URL displayed in the terminal (typically http://localhost:8501) in your web browser.

Upload the data_dump.csv file via the file uploader.

The app will generate and allow you to download the metrics report as an Excel file.

Metrics Breakdown
Chat Metrics:
Incoming Chats
Unique Users
Closed by Bot
Bot Deflection Percentage
Closed by Agents

Agent Metrics:
Avg Agent First Response Time (seconds)
Avg Agent Chat Resolution Time (seconds)
Average Agent CSAT Score
Business Hours CSAT [10AM - 5PM]
Outside Business Hours CSAT

Miscellaneous Metrics (Bonus):
Half-Hourly Chats
Active Time, Free Time, and Cumulative Time for each agent.

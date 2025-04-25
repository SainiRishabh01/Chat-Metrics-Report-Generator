# 📊 Chat Metrics Report Generator: Unveiling Insights from Your Customer Interactions

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-4-brightgreen.svg)](requirements.txt)

Gain a comprehensive understanding of your chat interactions and agent performance with the **Chat Metrics Report Generator**. This powerful tool processes your raw chat data (in CSV format) to deliver actionable insights through a meticulously crafted Excel report. Whether you prefer the convenience of a web interface or the directness of a command-line script, this project has you covered.

## ✨ Key Features at a Glance

* **🔍 Comprehensive Chat Metrics:** Track essential indicators like the total number of **incoming chats**, the reach of **unique users**, the efficiency of bot interactions (**chats closed by bots** and **bot deflection percentage**), and the workload handled by human **agents**.
* **👩‍💻 Agent Performance Analytics:** Evaluate your team's effectiveness with key metrics such as **average chat resolution time**, **Customer Satisfaction (CSAT) scores**, and performance nuances during and outside standard **business hours**.
* **📈 Granular Miscellaneous Metrics:** Dive deeper with **half-hourly chat volume statistics** and detailed **agent activity analysis**, including active time, free time, and cumulative time spent.
* **<0xF0><0x9F><0x93><0x81> Professionally Organized Excel Reports:** Receive your insights in a well-structured Excel file, with clear and distinct sheets for each category of metrics, making analysis a breeze.
* **🌐 Flexible Usage:** Generate reports either through an intuitive **Streamlit web application** for easy file upload and download or directly via a **Python script** for streamlined automation.

## ⚙️ System Requirements

* **Python:** Ensure you have Python 3.x installed on your system.

## 📦 Dependencies

The following Python libraries are essential for this project:

* `pandas`
* `openpyxl`
* `streamlit`
* `xlsxwriter`

Install all the necessary dependencies effortlessly by running:

project/
├── app/
│   ├── processor.py          # 🧠 Core logic for data processing and metric calculations
│   ├── report_generator.py   # 💾 Functionality to save calculated metrics to Excel
│   └── __init__.py
├── data_dump.csv             # 💾 Your chat data in CSV format (will be ignored by Git)
├── main.py                   # 🚀 Command-line interface entry point for report generation
├── requirements.txt          # 📜 List of Python dependencies
├── streamlit_app.py          # 🌐 Streamlit web application for interactive report generation


 Getting Started
There are two convenient ways to generate your chat metrics report:

1. 💻 Using the Command Line Script
For direct and automated report generation, use the main.py script:

Bash
python main.py
Upon execution, this command will:
Read and process the data from your data_dump.csv file.
Calculate all the defined chat and agent metrics.
Generate a comprehensive report saved as generated_report.xlsx in the project directory.
2. 🌐 Using the Streamlit Web Application
For a user-friendly, interactive experience, leverage the Streamlit web application:
Launch the App: Open your terminal and run:
Bash
streamlit run streamlit_app.py
Access in Browser: A URL will be displayed in your terminal (typically http://localhost:8501). Open this link in your web browser.

Upload Your Data: You'll find a file uploader within the application. Simply upload your data_dump.csv file.

Generate and Download: The application will process your data, generate the metrics report, and provide a convenient button to download the report as an Excel file.

📊 Metrics Breakdown
Here's a closer look at the valuable insights you'll gain:

Chat Metrics:
Incoming Chats: The total number of chat conversations initiated.
Unique Users: The count of distinct users who engaged in chat.
Closed by Bot: The number of chats successfully resolved by automated bots.
Bot Deflection Percentage: The proportion of chats handled by bots versus the total number of incoming chats, indicating bot effectiveness. $\qquad \text{Bot Deflection Percentage} = \frac{\text{Number of Chats Closed by Bot}}{\text{Total Incoming Chats}} \times 100%$
Closed by Agents: The number of chats that required human agent intervention and were resolved by them.
Agent Metrics:
Avg Agent First Response Time (seconds): The average time taken by an agent to provide the initial response to a user's message.
Avg Agent Chat Resolution Time (seconds): The average duration from the start of a chat to its final resolution by an agent.
Average Agent CSAT Score: The mean Customer Satisfaction score provided by users after interacting with agents.
Business Hours CSAT [10AM - 5PM]: The average CSAT score specifically for interactions occurring between 10:00 AM and 5:00 PM.
Outside Business Hours CSAT: The average CSAT score for interactions taking place outside the defined business hours.
Miscellaneous Metrics (Bonus Insights):
Half-Hourly Chats: A breakdown of the number of chats initiated within each 30-minute interval throughout the day, revealing peak activity times.
Agent Activity Analysis: For each agent, track the total time spent active in chats, the time they were free or available, and the cumulative total time recorded within the dataset.

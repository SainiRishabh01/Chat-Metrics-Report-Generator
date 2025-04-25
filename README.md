<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Metrics Report Generator</title>
    <style>
        body {
            font-family: sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #007bff;
        }
        h1 {
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        h2 {
            margin-top: 30px;
            padding-bottom: 5px;
            border-bottom: 1px solid #ccc;
        }
        h3 {
            margin-top: 20px;
        }
        p {
            margin-bottom: 15px;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
            margin-bottom: 15px;
        }
        li {
            margin-bottom: 5px;
        }
        strong {
            font-weight: bold;
        }
        code {
            background-color: #e9e9e9;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #e9e9e9;
            padding: 10px;
            border-radius: 3px;
            overflow-x: auto;
            font-family: monospace;
        }
        .feature-item {
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #fff;
        }
        .requirement-item {
            margin-bottom: 8px;
        }
        .project-structure pre {
            margin-left: 20px;
        }
        .metric-formula {
            font-style: italic;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>📊 Chat Metrics Report Generator</h1>
    <p>Gain a comprehensive understanding of your chat interactions and agent performance with the <strong>Chat Metrics Report Generator</strong>. This powerful tool processes your raw chat data (in CSV format) to deliver actionable insights through a meticulously crafted Excel report. Whether you prefer the convenience of a web interface or the directness of a command-line script, this project has you covered.</p>

    <h2>✨ Key Features at a Glance</h2>
    <ul>
        <li class="feature-item"><strong>🔍 Comprehensive Chat Metrics:</strong> Track essential indicators like the total number of incoming chats, the reach of unique users, the efficiency of bot interactions (chats closed by bots and bot deflection percentage), and the workload handled by human agents.</li>
        <li class="feature-item"><strong>👩‍💻 Agent Performance Analytics:</strong> Evaluate your team's effectiveness with key metrics such as average chat resolution time, Customer Satisfaction (CSAT) scores, and performance nuances during and outside standard business hours.</li>
        <li class="feature-item"><strong>📈 Granular Miscellaneous Metrics:</strong> Dive deeper with half-hourly chat volume statistics and detailed agent activity analysis, including active time, free time, and cumulative time spent.</li>
        <li class="feature-item"><strong><0xF0><0x9F><0x93><0x81> Professionally Organized Excel Reports:</strong> Receive your insights in a well-structured Excel file, with clear and distinct sheets for each category of metrics, making analysis a breeze.</li>
        <li class="feature-item"><strong>🌐 Flexible Usage:</strong> Generate reports either through an intuitive Streamlit web application for easy file upload and download or directly via a Python script for streamlined automation.</li>
    </ul>

    <h2>⚙️ System Requirements</h2>
    <ul>
        <li class="requirement-item"><strong>Python:</strong> Ensure you have Python 3.x installed on your system.</li>
    </ul>

    <h2>📦 Dependencies</h2>
    <p>The following Python libraries are essential for this project:</p>
    <ul>
        <li><code>pandas</code>: For robust data manipulation and analysis.</li>
        <li><code>openpyxl</code>: To handle the creation and modification of Excel files.</li>
        <li><code>streamlit</code>: To build the interactive web application.</li>
        <li><code>xlsxwriter</code>: An alternative Excel writing library, potentially used for advanced formatting.</li>
    </ul>
    <p>Install all the necessary dependencies effortlessly by running:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>📂 Project Structure</h2>
    <div class="project-structure">
        <pre><code>project/
├── app/
│   ├── processor.py          # 🧠 Core logic for data processing and metric calculations
│   ├── report_generator.py   # 💾 Functionality to save calculated metrics to Excel
│   └── __init__.py
├── data_dump.csv             # 💾 Your chat data in CSV format (will be ignored by Git)
├── main.py                   # 🚀 Command-line interface entry point for report generation
├── requirements.txt          # 📜 List of Python dependencies
├── streamlit_app.py          # 🌐 Streamlit web application for interactive report generation</code></pre>
    </div>

    <h2>🚀 Getting Started</h2>
    <p>There are two convenient ways to generate your chat metrics report:</p>

    <h3>1. 💻 Command Line Interface (CLI)</h3>
    <p>For direct and automated report generation, use the <code>main.py</code> script:</p>
    <pre><code>python main.py</code></pre>
    <p>Upon execution, this command will:</p>
    <ul>
        <li>Read and process the data from your <code>data_dump.csv</code> file.</li>
        <li>Calculate all the defined chat and agent metrics.</li>
        <li>Generate a comprehensive report saved as <code>generated_report.xlsx</code> in the project directory.</li>
    </ul>

    <h3>2. 🌐 Streamlit Web Application</h3>
    <p>For a user-friendly, interactive experience, leverage the Streamlit web application:</p>
    <ol>
        <li><strong>Launch the App:</strong> Open your terminal and run:
            <pre><code>streamlit run streamlit_app.py</code></pre>
        </li>
        <li><strong>Access in Browser:</strong> A URL will be displayed in your terminal (typically <code>http://localhost:8501</code>). Open this link in your web browser.</li>
        <li><strong>Upload Your Data:</strong> You'll find a file uploader within the application. Simply upload your <code>data_dump.csv</code> file.</li>
        <li><strong>Generate and Download:</strong> The application will process your data, generate the metrics report, and provide a convenient button to download the report as an Excel file.</li>
    </ol>

    <h2>📊 Detailed Metrics Breakdown</h2>
    <p>Here's a closer look at the valuable insights you'll gain:</p>

    <h3>Chat Metrics:</h3>
    <ul>
        <li><strong>Incoming Chats:</strong> The total number of chat conversations initiated.</li>
        <li><strong>Unique Users:</strong> The count of distinct users who engaged in chat.</li>
        <li><strong>Closed by Bot:</strong> The number of chats successfully resolved by automated bots.</li>
        <li><strong>Bot Deflection Percentage:</strong> The proportion of chats handled by bots versus the total number of incoming chats, indicating bot effectiveness.
            <p class="metric-formula">Bot Deflection Percentage = (Number of Chats Closed by Bot / Total Incoming Chats) × 100%</p>
        </li>
        <li><strong>Closed by Agents:</strong> The number of chats that required human agent intervention and were resolved by them.</li>
    </ul>

    <h3>Agent Metrics:</h3>
    <ul>
        <li><strong>Avg Agent First Response Time (seconds):</strong> The average time taken by an agent to provide the initial response to a user's message.</li>
        <li><strong>Avg Agent Chat Resolution Time (seconds):</strong> The average duration from the start of a chat to its final resolution by an agent.</li>
        <li><strong>Average Agent CSAT Score:</strong> The mean Customer Satisfaction score provided by users after interacting with agents.</li>
        <li><strong>Business Hours CSAT [10AM - 5PM]:</strong> The average CSAT score specifically for interactions occurring between 10:00 AM and 5:00 PM.</li>
        <li><strong>Outside Business Hours CSAT:</strong> The average CSAT score for interactions taking place outside the defined business hours.</li>
    </ul>

    <h3>Miscellaneous Metrics (Bonus Insights):</h3>
    <ul>
        <li><strong>Half-Hourly Chats:</strong> A breakdown of the number of chats initiated within each 30-minute interval throughout the day, revealing peak activity times.</li>
        <li><strong>Agent Activity Analysis:</strong> For each agent, track the total time spent actively engaged in chats, the time they were in a 'free' or available state, and the cumulative total time recorded within the dataset.</li>
    </ul>

</body>
</html>

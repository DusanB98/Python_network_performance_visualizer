# 💻 Python Network Performance Visualizer

**Description:** 
This Python script monitors network performance by reading a report file and processing the data using `pandas`. It extracts host connectivity statistics (Success, Slow, Error counts/percentages) and latency metrics (Avg., Max., Min.) via a complex regular expression `regex`. The processed data is then visualized using `matplotlib` graphs and exported to an Excel report. This provides structured feedback for each host's performance over time.

## ✨ Features
- Reads a list of hosts and their performance data from a file `report.txt`.
- Pings each host and measures latency
    - **Note:** *In this version, the script **reads** pre-measured data, but the functionality focuses on processing latency and count metrics.*
- Evaluates host availability with three statuses based on parsed data:
    - 🟢 **Available (Success)**
    - 🟠 **Slow (Latency above threshold)**
    - 🔴 **Unavailable (Error/Failed)**
- Generates detailed statistics and visualizations in the console and as image files.
- Compatible with Linux, macOS, and Windows systems

## 📊 Report Data Structure
The output Excel Report `Network_data_report.xlsx` contains a table named **data** with the following columns:
- **Host** – hostname or IP address
- **Status Counts** – (Success count / Slow count / Error count)
- **Status Percentages** – (Success % / Slow % / Error %)
- **Latency** – response time metrics in milliseconds
    - **Avg. latency**
    - **Max. latency**
    - **Min. latency**

## 🖼️  Visual Output (Matplotlib)
The script generates three charts for visual analysis:
- `success_percentage_chart.png`: Stacked Bar Chart showing the percentage of Success, Slow, and Error statuses.
- `success_rate_chart.png`: Stacked Bar Chart showing the total count of Success, Slow, and Error scans.
- `latency_chart.png`: Line Plot comparing Average, Maximum, and Minimum latencies across hosts.

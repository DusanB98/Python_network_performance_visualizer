# Python network performance visualizer
# Author: DusanB98

import re
import pandas as pd
import matplotlib.pyplot as plt


report_path = "/home/dusan/Desktop/Github/Python_projects/Network_performance_visualizer/Main_program/report.txt"

def reading_report(report_path):
    try:
        with open (file=report_path, mode="r") as report:
            data_report = report.read()
            regex_pattern = (
                r".*?((?:[\w.-]+\.)\w{2,}):\s+"
                r".*?Success:.*?(\d+)x,.*?(\d+\.\d+).*?%\s+"
                r".*?Slow:.*?(\d+)x,.*?(\d+\.\d+).*?%\s+"
                r".*?Error:.*?(\d+)x,.*?(\d+\.\d+).*?%\s+"
                r".*?Avg\..*?latency:.*?(\d+\.\d+|N/A).*?(?:ms)?\s+"
                r".*?Max\..*?latency:.*?(\d+\.\d+|N/A).*?(?:ms)?\s+"
                r".*?Min\..*?latency:.*?(\d+\.\d+|N/A).*?(?:ms)?"
            )
            # there are differences when you are using () - everything inside will catch, outside of () will ignore
            
            # .*? ignores everything until what you write in ()
            # + (catch at least one occurrence)
            # \. (just dot)
            # . (means any character)
            # {2,} (after dot catch domain with at least two characters e.x. .com, .sk ...)
            # \w contains [a-zA-Z0-9_], if you need to catch dash, and dot then [a-zA-Z0-9._-] or \w.-
            data = re.findall(regex_pattern, data_report)

    except FileNotFoundError:
            print("──────────────────────")
            print("This file wasn't found")
            print("──────────────────────")
            return None
    except PermissionError:
            print("───────────────────────────────────────────")
            print("You don't have permission to read this file")
            print("───────────────────────────────────────────")
            return None
    
    return data

def pandas_DataFrame():
    data = reading_report(report_path) 
    
    panda_table = ["Host", "Success count", "Success %",        #creating names for columns in pandas Dataframe
                           "Slow count", "Slow %",
                           "Error count", "Error %",
                           "Avg. latency", "Max. latency", "Min. latency"]
    data_frame = pd.DataFrame(data, columns=panda_table) # creating pandas Dataframe

    for column in panda_table[1:]:
         data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce") #converts string number (There is also N/A) to number

    return data_frame

def bar_percentage_graph():
    data = pandas_DataFrame()

    plt.figure(figsize=(10,6))
    plt.bar(data['Host'], data['Success %'], color="green")
    plt.bar(data['Host'], data['Slow %'], color="orange")
    plt.bar(data['Host'], data['Error %'], color="red")
    plt.title("Ping Success Rate per Host", fontweight='bold')
    plt.ylabel("Success percentage (%)")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(range(0, 110, 10))
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("success_percentage_chart.png")

def bar_rate_graph():
    data = pandas_DataFrame()

    plt.figure(figsize=(10,6))
    plt.bar(data['Host'], data['Success count'], color="green")
    plt.bar(data['Host'], data['Slow count'], color="orange")
    plt.bar(data['Host'], data['Error count'], color="red")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Number of scans")
    plt.yticks(range(0, 70, 5))
    plt.grid(axis='y', linestyle='--', alpha=0.5) # grid is active for y, style of grid, transparency
    plt.title("Ping Count Success Rate per Host", fontweight='bold')
    plt.tight_layout()
    plt.savefig("success_rate_chart.png")

def latency_graph():
    data = pandas_DataFrame()

    plt.figure(figsize=(10,6))
    plt.plot(data['Host'], data['Avg. latency'], color="blue", label="Avg.", marker="o")
    plt.plot(data['Host'], data['Min. latency'], color="green", label="Min.", marker="o")
    plt.plot(data['Host'], data['Max. latency'], color="orange", label="Max.", marker="o")
    plt.plot([], [], color="red", label="N/A", marker="x") # need to separatly create label for legend, because plt.text can't do it

    for index, value in enumerate(data['Avg. latency']): # thanks to enumerate you will get index and also value
        if value != value: # if value is not number but e.x. NaN, then it is true, or you can use np.isna(value) from numpy or pd.isna(value) from pandas
            plt.text(index, -5.5, "×", color="red", ha="center", va="bottom") # position x, position y, string, **kwargs settings

    plt.xticks(ticks=data['Host'], rotation=45, ha="right") # ticks to add all host even when are there which not contain numbers e.x. NaN
    plt.xlim(-0.5, 9.5) # minimum, maximum
    plt.ylabel("Latency (ms)")
    plt.title("Latency Comparison per Host", fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5) # grid is active for x and y, style of grid, transparency
    plt.legend()
    plt.tight_layout()
    plt.savefig("latency_chart.png")

def main():
    reading_report(report_path)
    data_frame = pandas_DataFrame()
    data_frame.to_excel("Network_data_report.xlsx", index=False) #exporting pandas dataframe to the excel to create a report

    bar_percentage_graph()
    bar_rate_graph()
    latency_graph()
    
    print("Successfully extracted data and created graphs!")

if __name__ == '__main__':
    main()
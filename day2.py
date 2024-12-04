import numpy as np

def read_input(path):
   with open(path) as f:
       data = [np.array([int(i) for i in l.strip().split()]) for l in f.readlines()]
   return data

def check_status(report):
    report_delta = []
    for i, level in enumerate(report[1:]) : 
        report_delta.append(level - report[i])
   
    status = True
    
    if len(set(np.sign(report_delta))) != 1:
        status = False

    for delta in report_delta:
        if abs(delta) > 3 or abs(delta) < 1:
            status = False

    return status


def task1(input):
    reports_status = []
    for report in input: 
        status = check_status(report)
        reports_status.append(status)

    return reports_status.count(True)

def generate_possible_altreport(report):
    alt_reports = []
    for i in range(len(report)):
        alt_report = np.delete(report, i)
        alt_reports.append(alt_report)
    return np.array(alt_reports)

        
def task2(input):
    reports_status = []
    for report in input: 
        alt_reports = generate_possible_altreport(report)
        alt_reports_status = []
        for alt_report in alt_reports:
            status = check_status(alt_report)
            alt_reports_status.append(status)
        if any(alt_reports_status):
            reports_status.append(True)
        else:
            reports_status.append(False)

    return reports_status.count(True)

        
def main():
    input = read_input("data/day2.txt")
    result_task1 = task1(input)
    print("Task 1: ", result_task1)

    result_task2 = task2(input)
    print("Task 2: ", result_task2)

if __name__ == "__main__":
    main()
import decimal
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
file_path = '/Users/pianjiliangcha/Desktop/0715CSCW/02代码检测/数据/output.rttm'

# 阈值（s）

fig = plt.figure(figsize=(13, 7))  # Create a `figure' instance
threshold_value = 500
longest_value = decimal.Decimal(120.000)
current_time = 0
person_dict = {}
pie = {}
mark = 0
count = {}
i = 1
x_data = []
y_data = []
plt.ion()
plt.margins(0,0)

while True:
    with open(file_path, 'r', encoding='utf-8') as f:
        all_content = f.read()
        rows = all_content.split('\n')[:-1]
        for row in rows:
            columns = row.split(' ')[:-1]
            person = columns[7]
            start = decimal.Decimal(columns[3])
            if start < (i - 1) * threshold_value or start > i * threshold_value:
                continue
            continue_time = decimal.Decimal(columns[4])
            end = start + continue_time
            count.setdefault(person, 0)
            count[person] = count[person] + 1
            if person not in person_dict:
                person_dict[person] = {
                    'last_start': start,
                    'last_end': end
                }
                pie[person] = continue_time
            else:
                oldValue = pie[person]
                pie[person] = oldValue + continue_time
            for key, value in person_dict.items():
                if key == person:
                    person_dict[person] = {
                        'last_start': start,
                        'last_end': end
                    }
                else:
                    real_end = value['last_end'] + longest_value
                    last_start = value['last_start']
                    if start >= last_start and start <= real_end:
                        mark += 1

    plt.clf()
    # plt.subplot(2, 2, 3)
    x_data.append(i * threshold_value)
    y_data.append(mark)
    plt.rcParams['axes.facecolor'] = '#192431'
    plt.title("plot 3")
    # x_smooth = np.linspace(x_data.min(), x_data.max(), 300)
    # y_smooth = make_interp_spline(x_data, y_data)(x_smooth)
    plt.plot(x_data, y_data,color='#6001D3')
    plt.grid(color='#293446', linewidth=2)

    x1 = np.array([500, 1000, 1500, 2000, 2500])
    y1 = np.array([370, 390, 520, 280, 340])
    x1_smooth = np.linspace(x1.min(), x1.max(), 300)
    y1_smooth = make_interp_spline(x1, y1)(x1_smooth)
    plt.plot(x1_smooth, y1_smooth, color='#6A729A',linestyle='--', linewidth=1)
    for a, b in zip(x1, y1):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10,color='#6A729A')
    for c, d in zip(x_data, y_data):
        plt.text(c, d, d, ha='center', va='bottom', fontsize=10, color='#6001D3')

    plt.subplot(2, 2, 1)
    plt.title("plot 1")
    plt.bar(count.keys(), count.values())
    plt.grid(color='r', linestyle='--', linewidth=0.5)
    print(count)

    plt.subplot(2, 2, 2)
    plt.pie(pie.values(), labels=pie.keys())
    plt.title("plot 2")
    plt.axis('off')
    time.sleep(threshold_value)
    i += 1
    mark = 0
    count = {}
    plt.pause(0.1)

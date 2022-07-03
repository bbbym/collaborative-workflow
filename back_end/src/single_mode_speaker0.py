import decimal
import time
import matplotlib.pyplot as plt
file_path = '/Users/pianjiliangcha/output.rttm'

# 阈值（s）
fig = plt.figure(figsize=(4, 6))  # Create a `figure' instance
threshold_value = 10 #180
longest_value = decimal.Decimal(30.000)
current_time = 0
person_dict = {}
mark = 0
count = {}
i = 1
speaker = 'speaker0'
pie = {
    speaker: 0,
    'others': 0
}

x_data = []
y_data = []

y_low_data = []
# 低阈值线
subline_low = 5
y_high_data = []
# 高阈值线
subline_high = 10

plt.ion()

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
            if person != speaker:
                pie['others'] += continue_time
            else:
                pie[speaker] += continue_time
            if person not in person_dict:
                person_dict[person] = {
                    'last_start': start,
                    'last_end': end
                }
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
    plt.subplot(2, 1, 2)
    x_data.append(i * threshold_value)
    y_data.append(mark)
    # plt.title("小组对话次数")
    plt.plot(x_data, y_data, 'ro--')
    plt.plot(x_data, y_low_data, 'ro--', color='blue', linestyle='-', linewidth=0.5)
    plt.plot(x_data, y_high_data, 'ro--', color='blue', linestyle='-', linewidth=0.5)

    # plt.subplot(2, 2, 1)
    # plt.title("小组成员发言次数")
    # plt.bar(speaker, count.get(speaker, 0))
    # plt.grid(color='r', linestyle='--', linewidth=0.5)
    # print(count)

    plt.subplot(2, 1, 1)
    plt.pie(pie.values(), labels=pie.keys())
    # plt.title("小组成员发言时长")

    time.sleep(threshold_value)
    i += 1
    mark = 0
    count = {}
    plt.pause(0.1)

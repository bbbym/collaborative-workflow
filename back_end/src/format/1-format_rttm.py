import decimal
import time
import matplotlib.pyplot as plt
file_path = '/Users/pianjiliangcha/2output.rttm'

# 阈值（s）
threshold_value = 10
longest_value = decimal.Decimal(30.000)
person_dict = {}
current_time = 0
mark = 0
i = 1

x_data = []
y_data = []
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

    x_data.append(i * threshold_value)
    y_data.append(mark)
    plt.plot(x_data, y_data, 'ro--')
    plt.pause(0.1)
    i += 1
    mark = 0
    time.sleep(threshold_value)


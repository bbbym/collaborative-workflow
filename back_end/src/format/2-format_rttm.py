import decimal
import time
import matplotlib.pyplot as plt


file_path = '/Users/pianjiliangcha/2output.rttm'


# 阈值（s）
count = {}
i = 1
threshold_value = 10


#plot 1:
x_data = []
y_data = []
plt.ion()

while True:
    with open(file_path, 'r', encoding='utf-8') as f:
        all_content = f.read()
        rows = all_content.split('\n')[:-1]
        for row in rows:
            columns = row.split(' ')[:-1]
            start = decimal.Decimal(columns[3])
            if start < (i - 1) * threshold_value or start > i * threshold_value:
                continue
            # print(start)
            # print(start < (i - 1) * threshold_value or start > i * threshold_value)
            person = columns[7]
            count.setdefault(person, 0)
            count[person] = count[person] + 1
        print(count)

        plt.title("plot 2")
        plt.clf()
        plt.bar(count.keys(), count.values())
        plt.pause(0.1)

        count = {}
        i += 1
        time.sleep(threshold_value)




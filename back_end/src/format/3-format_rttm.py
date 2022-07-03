import decimal
import time
import matplotlib.pyplot as plt
import numpy as np
file_path = '/Users/pianjiliangcha/2output.rttm'

stat={}
count = {}
i = 1
threshold_value = 10

with open(file_path, 'r', encoding='utf-8') as f:
    all_content = f.read()
    rows = all_content.split('\n')[:-1]
    for row in rows:
        columns = row.split(' ')[:-1]
        key = columns[7]
        value = decimal.Decimal(columns[4])
        if (key in stat):
            oldValue = stat[key]
            stat[key] = oldValue + value
        else:
            stat[key] = value

    print(stat)
    y = np.array(stat)
    plt.pie(stat.values(),labels=stat.keys())
    plt.title("Test")
    plt.show()

import matplotlib.pyplot as plt
from functools import reduce
import re

def get_acc(filename):
    num = []
    acc = []
    min_lat = []
    mean_lat = []

    epoch_acc = []
    epoch_lat = []

    with open(filename) as f:
        for st in f:
            if st.find('test_accuracy') != -1:
                num.append(len(num)+1)
                acc.append(float(re.search('0\.\d+', st)[0]))
            if st.find('val_acc=') != -1:
                epoch_acc.append(float(re.search('\d+\.\d+', st)[0]))
            if st.find('latency_sum=') != -1:
                epoch_lat.append(float(re.search('\d+\.\d+', st)[0]))
            if st.find('Here are') != -1 and len(epoch_lat) > 0:
                latency_sum = reduce((lambda x, y: x+y), epoch_lat)
                min_val = 10000
                for it in epoch_lat:
                    if min_val > it:
                        min_val = it
                min_lat.append(min_val)
                epoch_lat = []
                mean_lat.append(latency_sum/10)
        
        latency_sum = reduce((lambda x, y: x+y), epoch_lat)
        mean_lat.append(latency_sum/10)
        min_val = 10000
        for it in epoch_lat:
            if min_val > it:
                min_val = it
        min_lat.append(min_val)
    return num, acc, min_lat, mean_lat

# num_1, acc_1, min_lat_1, mean_lat_1 = get_acc('log_210116.log')
# num_2, acc_2, min_lat_2, mean_lat_2 = get_acc('log_210116_mo.log')

num_1, acc_1, min_lat_1, mean_lat_1 = get_acc('log_210117.log')
num_2, acc_2, min_lat_2, mean_lat_2 = get_acc('log_210117_mo.log')

fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

ax1.plot(num_1, acc_1, "r", num_2, acc_2, "b")
ax2.plot(num_1, min_lat_1, "r", num_2, min_lat_2, "b")
ax3.plot(num_1, mean_lat_1, "r", num_2, mean_lat_2, "b")

ax1.axis([0,300,0.0,1.0])
ax2.axis([0,300,10.0,120.0])
ax3.axis([0,300,80.0,160.0])

plt.show()

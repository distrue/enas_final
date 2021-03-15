import matplotlib.pyplot as plt
import re

look = ['./reload_final_1.log', './reload_final_2.log']
shape = ['r', 'b']

for idx, item in enumerate(look):
    num = []
    acc = []

    print(item)
    with open(item) as f:
        for st in f:
            if st.find('test_accuracy') != -1:
                num.append(len(num)+1)
                acc.append(float(re.search('[0-9]+\.\d+', st)[0]))
                print(acc)

    plt.plot(num,acc,shape[idx])

plt.axis([0,700,0.5,1.0])
plt.show()

"""
B1

[1 3 1 0 2 0 1 0 1 4 1 1 0 1 3 4 0 3 2 0]
[0 2 0 2 0 0 2 3 3 3 1 3 2 1 1 1 2 4 3 1]
val_acc=0.7083
latency_sum=64.0000

[1 4 1 0 2 4 0 0 1 0 2 4 0 1 4 4 4 1 3 3]
[0 4 1 0 2 0 0 1 2 4 2 0 3 2 0 1 1 1 3 4]
val_acc=0.7014
latency_sum=74.0000

B2 

[1 2 1 2 2 3 0 1 3 4 2 0 3 4 1 0 2 0 1 2]
[1 3 1 4 2 1 2 4 0 3 3 4 3 1 1 4 1 3 5 0]
val_acc=0.6458
latency_sum=80.0000

[0 1 0 2 1 4 2 0 2 4 1 2 4 1 1 3 1 2 5 3]
[1 1 1 3 2 4 2 2 3 3 0 0 1 3 4 0 0 3 5 2]
val_acc=0.7361
latency_sum=86.0000

B3

[0 4 1 4 0 1 1 3 3 4 2 3 1 0 3 3 1 0 2 0]
[0 4 1 0 1 3 2 4 0 0 1 0 0 0 3 1 2 4 0 3]
val_acc=0.7292
latency_sum=54.0000

[1 3 0 3 2 4 0 0 0 4 2 4 3 4 2 2 2 0 1 0]
[0 0 0 3 2 4 0 2 0 1 0 0 2 3 3 3 1 0 1 4]
val_acc=0.7292
latency_sum=64.0000

b4

[0 0 0 0 0 0 0 4 0 3 1 0 4 4 0 3 0 3 0 0]
[0 0 1 0 2 3 1 2 0 3 2 0 2 0 2 4 3 3 0 2]
val_acc=0.7431
latency_sum=64.0000

[0 0 1 3 0 3 0 3 1 2 2 3 3 2 3 0 5 4 4 1]
[1 2 1 0 0 2 0 1 3 4 3 1 2 1 4 0 5 3 3 3]
val_acc=0.7083
latency_sum=80.0000
"""
import matplotlib.pyplot as plt
import re

look = ['./log.txt']
shape = ['r']

for idx, item in enumerate(look):
    num = []
    acc = []

    print(item)
    with open(item) as f:
        for st in f:
            if st.find('train_acc') != -1:
                num.append(len(num)+1)
                acc.append(float(re.search('[0-9]+\.\d+', st)[0]))
                print(acc)

    plt.plot(num,acc,shape[idx])

plt.axis([0,250,0.,100.])
plt.show()

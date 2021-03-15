import matplotlib.pyplot as plt
import re

look = ['./mo_final_210208.log', './nmo_final_210208.log']
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

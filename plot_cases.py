import matplotlib.pyplot as plt
import re

look = ['./train_batch_1_210119.log', './train_batch_2_210119.log', './final_0122_1.log', './final_0122_2.log', './final_0122_3.log', './final_0122_4.log']
shape = ['r', 'b+', 'b-', 'b.', 'b+', 'b-']

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

plt.axis([0,314,0.5,1.0])
plt.show()

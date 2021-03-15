import matplotlib.pyplot as plt

acc = [0.9291, 0.9012, 0.8912 ]
lat = [142, 150, 130 ]

acc_2 = [0.8832, 0.8642, 0.8949, 0.8235, 0.8602]
lat_2 = [64, 74, 80, 86, 54]

plt.scatter(lat, acc, color='r')
plt.scatter(lat_2, acc_2, color='b')

plt.axis([60,180,0.8,1.0])

# plt.xscale('log')

plt.show()

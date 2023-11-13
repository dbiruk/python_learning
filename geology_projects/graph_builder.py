import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
raw_material = ""

plt.plot(x,y, color='green', linewidth = 3, marker='o', markerfacecolor='blue', markersize=8)

plt.xticks(np.arange(min(x), max(x)+1, 1))

plt.xlabel('Роки') 
plt.ylabel('тис. т')

file_name = raw_material + '.jpg'
plt.title(raw_material) 
plt.savefig(f"/Users/user/Documents/personal/Eco_Geology/Graphs_Biruk/{file_name}", format='jpg')

#plt.show()
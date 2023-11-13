import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
tk.Tk().withdraw() # part of the import if you are not using other tkinter functions    

def get_info():
    exel_loc = askopenfilename()
    histo_loc = askdirectory()

    dataframe = pd.read_excel(exel_loc)
    raw_data = dataframe.replace([np.nan, -np.inf], 0).values.tolist()
    years = [int(i) for i in raw_data[0] if i != 0]
    materials_tons = []
    materials_names = []
    for x in raw_data:
        if x[0] != 0:
            materials_tons.append(x[1:])
            materials_names.append(x[0])

    return materials_tons, years, materials_names, histo_loc

def build_graph():
    x, y, raw_material, histo_loc = get_info()
    for idx, value in enumerate(x):
        col = []
        for num, val in enumerate(value):
            if val == max(value):
                col.append('red')
            elif num % 2 == 0:
                col.append('blue')
            else:
                col.append('green')
        plt.bar(y, value, width = 1, tick_label = y, edgecolor='black', linewidth=1, color = col)
        mat_name = raw_material[idx].replace(', тис. т', '')
        file_name = mat_name + '.jpg'
        plt.title(mat_name) 
        plt.xlabel('Роки') 
        plt.ylabel('тис. т')
        plt.savefig(f"{histo_loc}/{file_name}", format='jpg', dpi = 300)
        plt.close()

def main():

    build_graph()

if __name__ == '__main__':
    main()
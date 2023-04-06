import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA = pd.read_csv('company_sales_data.csv')


def exercise1():
    plt.plot(DATA['month_number'], DATA['total_profit'])
    plt.xlabel('Month Number')
    plt.ylabel('Total profit')
    plt.xticks(DATA['month_number'])
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.title('Company profit per month')
    plt.show()


def exercise3():
    data = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
    labels = ['Face cream Sales Data', 'Face Wash Sales Data', 'ToothPaste Sales Data',
              'ToothPaste Sales Data', 'ToothPaste Sales Data', 'ToothPaste Sales Data']
    for data, label in zip(data, labels):
        plt.plot(DATA['month_number'], DATA[data], label=label, marker='o', linewidth=3)
    plt.xticks(DATA['month_number'])
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.title('Sales data')
    plt.show()


def exercise5():
    plt.bar(DATA['month_number'] - 0.125, DATA['facecream'],
            label='Face Cream sales data', width=0.25)
    plt.bar(DATA['month_number'] + 0.125, DATA['facewash'],
            label='Face Wash sales data', width=0.25)
    plt.xticks(DATA['month_number'])
    plt.yticks(np.arange(500, 4000, 500))
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.grid(True, linestyle='--')
    plt.title('Facewash and facecream sales data')
    plt.show()


def exercise7():
    x_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
    plt.hist(DATA['total_profit'], x_range, label='Profit data')
    plt.xlabel('profit range in dollar')
    plt.ylabel('Actual Profit in dollar')
    plt.xticks(x_range)
    plt.title('Profit data')
    plt.legend(loc='upper left')
    plt.show()


def exercise9():
    plt.subplot(211)
    plt.plot(DATA['month_number'], DATA['bathingsoap'], color='k', marker='o', linewidth=3)
    plt.yticks(np.arange(7500, 15000, 2500))
    plt.xticks(DATA['month_number'])
    plt.title('Sales data of a Bathingsoap')
    plt.subplot(212)
    plt.plot(DATA['month_number'], DATA['facewash'], color='r', marker='o', linewidth=3)
    plt.yticks([1500, 2000])
    plt.xticks(DATA['month_number'])
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.title('Sales data of a facewash')
    plt.show()


if __name__ == '__main__':
    exercise1()
    exercise3()
    exercise5()
    exercise7()
    exercise9()

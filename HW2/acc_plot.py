
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    t = data['time']
    ax = data['acc_x']
    ay = data['acc_y']
    az = data['acc_z']

    plt.cla()

    plt.plot(t, ax, label='acc_x')
    # plt.plot(t, ay, label='acc_y')
    plt.plot(t, az, label='acc_z')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()
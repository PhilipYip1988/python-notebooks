#%% imports
import math
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#%% set style
sns.set_style('whitegrid')

#%% Figure1
def plot1():
    tau = 2 * np.pi
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, tau/8)
    r2 = (0, 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='red')
    
    xticks = ax.xaxis.get_ticklocs()
    xticklabels = [r'$\frac{' + f'{num}' + '}{8}$' + r'$\tau$' for num in range(8)]
    ax.xaxis.set_ticks(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    
    return fig

#%% Figure2
def plot2():
    tau = 2 * np.pi
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, tau/8)
    r2 = (0, 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='red')
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    return fig
# %% Figure 3
def factorial(factor):
    result = 1
    for num in range(2, factor+1):
        result *= num
    return result

def euler_series(factor):
    total = 1.0
    for num in range(1, factor + 1):
        total += 1.0 / factorial(num)
    return total

def plot3():
    x = np.arange(100)
    y = map(euler_series, x)
    y = np.array(list(y))
    fig, ax = plt.subplots()
    ax.plot(x, y, color='royalblue')
    ax.set_xlabel('factorial')
    ax.set_ylabel('euler_series(factorial)')
    return fig
# %% Figure 4
def plot4():
    x1 = list(range(0, 6))
    y1 = list(map(math.factorial, x1))

    x2 = (np.arange(1, 6.1, 0.1)).tolist()
    y2 = list(map(math.gamma, x2)) 
    x2 = np.arange(1, 6.1, 0.1) - 1

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color='tomato', label='n!')
    ax.plot(x2, y2, color='royalblue', label=r'$\Gamma$(n+1)')
    ax.set_label('n')
    ax.legend()
    return fig
# %% Figure 5
def plot5():
    x1 = list(range(0, 11))
    y1 = list(map(math.factorial, x1))

    x2 = (np.arange(1, 11.1, 0.1)).tolist()
    y2 = list(map(math.gamma, x2)) 
    x2 = np.arange(1, 11.1, 0.1) - 1

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color='tomato', label='n!')
    ax.plot(x2, y2, color='royalblue', label=r'$\Gamma$(n+1)')
    ax.set_label('n')
    ax.legend()
    return fig
# %% Figure 6
def plot6():
    x1 = list(range(0, 11))
    y1 = list(map(math.factorial, x1))

    x2 = (np.arange(1, 11.1, 0.1)).tolist()
    y2 = list(map(math.gamma, x2)) 
    x2 = np.arange(1, 11.1, 0.1) - 1

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color='tomato', label='n!')
    ax.plot(x2, y2, color='royalblue', label=r'$\Gamma$(n+1)')
    ax.set_label('n')
    ax.legend()
    ax.set_yscale('log')
    return fig

# %% Figure 7
def plot7():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    ax.set_xlim(left=0, right=6)
    ax.set_ylim(bottom=0, top=6)
    x1 = (1, 1)
    y1 = (1, 5)
    x2 = (1, 4)
    y2 = (1, 1)
    x3 = (4, 1)
    y3 = (1, 5)
    ax.plot(x1, y1, color='mediumpurple', lw=2, ls=':')
    ax.plot(x2, y2, color='darkorange', lw=2, ls=':')
    ax.plot(x3, y3, color='seagreen', lw=2, ls=':')
    return fig
# %% Figure 8
def plot8():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    ax.set_xlim(left=0, right=6)
    ax.set_ylim(bottom=0, top=6)
    x1 = (4, 1)
    y1 = (1, 5)
    x2 = (1, 4)
    y2 = (5, 1)
    ax.plot(x1, y1, color='seagreen', lw=2, ls=':')
    ax.scatter(x2, y2, color='tomato', s=5)
    return fig
# %% Figure 9
def plot9():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    ax.set_xlim(left=0, right=6)
    ax.set_ylim(bottom=0, top=6)
    x1 = (1, 1)
    y1 = (1, 5)
    x2 = (1, 4)
    y2 = (1, 1)
    x3 = (4, 1)
    y3 = (1, 5)
    x4 = (1, 4)
    y4 = (5, 1)
    ax.plot(x1, y1, color='mediumpurple', lw=2, ls=':')
    ax.plot(x2, y2, color='darkorange', lw=2, ls=':')
    ax.plot(x3, y3, color='seagreen', lw=2, ls=':')
    ax.scatter(x4, y4, color='tomato', s=5)
    return fig

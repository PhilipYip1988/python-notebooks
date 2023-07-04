#%% Imports
import math
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#%% Set Style
sns.set_style('whitegrid')
#%% Constants
tau = 2 * math.pi

#%% Figure1
def plot1():
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
#%% Figure 10
def plot10():
    fig, ax = plt.subplots(subplot_kw={'projection':'3d', 'aspect':'equal'})
    x1 = (3,)
    y1 = (4,)
    z1 = (7,)
    x2 = (1, 3)
    y2 = (1, 1)
    z2 = (1, 1)
    x3 = (1, 1)
    y3 = (1, 4)
    z3 = (1, 1)
    x4 = (1, 1)
    y4 = (1, 1)
    z4 = (1, 7)
    x5 = (1, 3)
    y5 = (1, 4)
    z5 = (1, 7)
    ax.scatter3D(x1, y1, z1, s=50, color='tomato')
    ax.plot3D(x2, y2, z2, color='darkorange', lw=2, ls=':')
    ax.plot3D(x3, y3, z3, color='mediumpurple', lw=2, ls=':')
    ax.plot3D(x4, y4, z4, color='cyan', lw=2, ls=':')
    ax.plot3D(x5, y5, z5, color='seagreen', lw=2, ls='-')
    ax.set_xlim(left=0, right=7)
    ax.set_ylim(bottom=0, top=7)
    ax.set_zlim(bottom=0, top=7)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    return fig
#%% Figure 11
def plot11():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    r = 1
    theta = np.arange(-tau, tau, 0.1)
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, color='tomato')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(left=-1.5, right=1.5)
    ax.set_ylim(bottom=-1.5, top=1.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    return fig
#%% Figure12
def plot12():
    angle = 2*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='tomato') 
    ax.scatter(theta3, r3, s=50, color='tomato')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax.annotate('adjacent',
                xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
                xytext=(0.1, math.cos(angle)/2-0.02),
                color='magenta')
    ax.annotate('opposite',
                xy=(angle-0.5, math.cos(angle)-0.02),  # theta, radius
                xytext=(angle-0.5, math.cos(angle)-0.02),
                color='cyan', rotation=90)
    ax.annotate('hypotenuse',
            xy=(angle-0.1, math.cos(angle)/2-0.01),  # theta, radius
            xytext=(angle-0.1, math.cos(angle)/2-0.01),
            color='red', rotation=45)
    ax.annotate(r'$\theta$',
                xy=(0.3, 0.1),  # theta, radius
                xytext=(0.3, 0.1),
                color='black')
#%% Figure13
def plot13():
    angle = 0*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    #ax.plot(theta2, r2, color='tomato') 
    #ax.scatter(theta3, r3, s=50, color='tomato')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    #ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    return fig
#%% Figure14
def plot14():
    angle = 1*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='tomato') 
    ax.scatter(theta3, r3, s=50, color='tomato')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax.annotate('adjacent',
                xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
                xytext=(0.1, math.cos(angle)/2-0.02),
                color='magenta')
    ax.annotate('opposite',
                xy=(angle-0.26, math.cos(angle)-0.06),  # theta, radius
                xytext=(angle-0.26, math.cos(angle)-0.06),
                color='cyan', rotation=90)
    ax.annotate('hypotenuse',
            xy=(angle-0.1, math.cos(angle)/2-0.01),  # theta, radius
            xytext=(angle-0.1, math.cos(angle)/2-0.01),
            color='red', rotation=22.5)
    ax.annotate(r'$\theta$',
                xy=(0.1, 0.1),  # theta, radius
                xytext=(0.1, 0.1),
                color='black')
    return fig
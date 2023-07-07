#%% Data Science library Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%% Numpy Arrays
x = np.array((1, 2, 3, 4, 5))
y = np.array((2, 4, 6, 8, 10))
#%% DataFrames
df = pd.DataFrame(data={'x': x, 'y': y})
#%% Plot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show();
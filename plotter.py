

import numpy as np
import matplotlib.pyplot as plt

# describe the function below

t_ax = [1]
sig = [1]
i=1
while i<10:
    t_ax.append(i)
    sig.append(0)
    i=i+1

# plot the generated signal
plt.stem(sig)
plt.show()

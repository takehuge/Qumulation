from numpy import arange
import matplotlib.pyplot as plt

err_gate = 3.9e-3
err_threshold = 1e-2 # 1%

d = arange(0, 100, 1)
err_logical = (err_gate/err_threshold)**((d+1)/2)
plt.plot(d, err_logical, '.b')
plt.yscale('log')
plt.xlabel('Depth')
plt.ylabel('Logical Error rate')
plt.show()

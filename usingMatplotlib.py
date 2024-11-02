from matplotlib import pyplot as plt
import numpy as np

# generate 100 random data points along 3 dimensions.
x, y, scale = np.random.randn(3, 100)
print(x)
print(y)
print(scale)
fig, ax = plt.subplots()

# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale) * 500)
ax.set(title="Some Random Data created with Jupyter Test")
plt.show()

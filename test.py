from matplotlib.pyplot import plot, scatter, show
from scipy.interpolate import make_interp_spline
import numpy as np

x = np.array([0, 1, 2, 3, 4,  5, 6])
y = np.array([0, 0, 5, 0, 0, -5, 0])

scatter(x, y)

# B-Spline is not very good in this case
smoothed_x = np.linspace(x.min(), x.max(), 1000)
smoothed_y = make_interp_spline(x, y, k=3, t=x)(smoothed_x)
plot(smoothed_x, smoothed_y)
show()

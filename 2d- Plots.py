
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Contour-Plots-and-Beyond" data-toc-modified-id="Contour-Plots-and-Beyond-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Contour Plots and Beyond</a></div><div class="lev2 toc-item"><a href="#2d-Histograms" data-toc-modified-id="2d-Histograms-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>2d Histograms</a></div>

# # Contour Plots and Beyond

# In[8]:

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().magic('matplotlib inline')

# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 

# Display the resulting image with pcolor()
plt.pcolor(X, Y, Z)
plt.colorbar()
plt.axis('tight')
plt.show()


# In[11]:

plt.contourf(X, Y, Z, 30, cmap = "viridis")
plt.colorbar()
plt.show()


# ## 2d Histograms

# In[14]:

hp = np.random.normal(size = 100)
mpg = np.random.normal(loc = 1, scale = 0.5, size = 100)
plt.hist2d(hp, mpg, bins=(13, 13), range=((-3, 3), (-2, 2)), cmap = 'viridis')

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()


# In[ ]:




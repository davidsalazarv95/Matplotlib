
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Many-plots" data-toc-modified-id="Many-plots-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Many plots</a></div><div class="lev2 toc-item"><a href="#Same-axis" data-toc-modified-id="Same-axis-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Same axis</a></div><div class="lev2 toc-item"><a href="#Different-axis" data-toc-modified-id="Different-axis-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Different axis</a></div>

# In[1]:

import matplotlib.pylab as plt
import pandas as pd
import numpy as np
get_ipython().magic('matplotlib inline')


# # Many plots

# ## Same axis

# In[10]:

temperature = np.random.rand(10)
dewey = np.random.rand(10)
x = np.linspace(0, 10, num = 10)
plt.plot(x, temperature, 'red')
plt.plot(x, dewey, 'blue') # Same axis
plt.xlabel('Days Elapsed')
plt.title('Temperature and Dewey')
plt.show()


# ## Different axis

# In[13]:

plt.subplot(2, 1, 1) # nrows, ncols, subplot starting from top left
plt.plot(x, temperature, 'red')
plt.title('Temperature')
plt.subplot(2, 1, 2)
plt.plot(x, dewey, 'blue')
plt.title('Dewey')
plt.xlabel('Days Elapsed')
plt.tight_layout()
plt.show()


# In[ ]:




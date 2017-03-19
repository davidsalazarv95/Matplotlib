
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Many-plots" data-toc-modified-id="Many-plots-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Many plots</a></div><div class="lev2 toc-item"><a href="#Same-axis" data-toc-modified-id="Same-axis-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Same axis</a></div><div class="lev2 toc-item"><a href="#Different-axis" data-toc-modified-id="Different-axis-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Different axis</a></div><div class="lev2 toc-item"><a href="#Axis" data-toc-modified-id="Axis-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Axis</a></div><div class="lev2 toc-item"><a href="#Saving" data-toc-modified-id="Saving-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Saving</a></div><div class="lev2 toc-item"><a href="#Legends" data-toc-modified-id="Legends-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Legends</a></div><div class="lev2 toc-item"><a href="#Annotations" data-toc-modified-id="Annotations-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Annotations</a></div>

# In[14]:

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')


# # Many plots

# ## Same axis

# In[24]:

temperature = np.random.rand(10)
dewey = np.random.rand(10)
x = np.linspace(0, 10, num = 10)
plt.plot(x, temperature, 'red')
plt.plot(x, dewey, 'blue') # Same axis
plt.xlabel('Days Elapsed')
plt.title('Temperature and Dewey')
plt.show()


# ## Different axis

# In[25]:

plt.subplot(2, 1, 1) # nrows, ncols, subplot starting from top left
plt.plot(x, temperature, 'red')
plt.title('Temperature')
plt.subplot(2, 1, 2)
plt.plot(x, dewey, 'blue')
plt.title('Dewey')
plt.xlabel('Days Elapsed')
plt.tight_layout()
plt.show()


# ## Axis

# In[26]:

plt.plot(x, temperature)
plt.axis([0, 8, 0.3, 0.9]) #xinf, xsup, yinf, ysup


# In[27]:

plt.plot(x, temperature)
plt.xlim(0, 8)
plt.ylim(0.3, 0.9)


# ## Saving

# In[17]:

plt.savefig('ss.png')


# ## Legends
# 
# The relevant data are created using specific line colors or markers in various plot commands. Using the keyword argument label in the plotting function associates a string to use in a legend. Request a legend with ```plt.legend```

# In[28]:

plt.plot(x, temperature, color = 'red', label = 'Temperature')
plt.plot(x, dewey, color = 'blue', label = 'Dewey') # Same axis
plt.xlabel('Days Elapsed')
plt.title('Temperature and Dewey')
plt.legend(loc = 0) ## Location of the legend
plt.show()


# ## Annotations

# In[32]:

max_temp = temperature.max()
day_max = x[temperature.argmax()]
plt.plot(x, temperature, color = 'red', label = 'Temperature')
plt.plot(x, dewey, color = 'blue', label = 'Dewey') # Same axis
plt.xlabel('Days Elapsed')
plt.title('Temperature and Dewey')
plt.legend(loc = 0) ## Location of the legend
plt.annotate('Maximum Temperature', (day_max, max_temp), (day_max + 0.1, max_temp + 0.1), 
    arrowprops=dict(facecolor='black'))
plt.show()


# In[ ]:




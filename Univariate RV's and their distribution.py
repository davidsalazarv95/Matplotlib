
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Distributions" data-toc-modified-id="Distributions-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Distributions</a></div><div class="lev2 toc-item"><a href="#Histograms" data-toc-modified-id="Histograms-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Histograms</a></div><div class="lev2 toc-item"><a href="#Strip-plots" data-toc-modified-id="Strip-plots-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Strip-plots</a></div><div class="lev3 toc-item"><a href="#Swarm-Plots:-Strartyfing-according-to-values" data-toc-modified-id="Swarm-Plots:-Strartyfing-according-to-values-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Swarm Plots: Strartyfing according to values</a></div><div class="lev2 toc-item"><a href="#Boxplots-and-Violin-Plots" data-toc-modified-id="Boxplots-and-Violin-Plots-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Boxplots and Violin Plots</a></div>

# # Distributions

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10.0, 8.0)


# In[2]:

tips = sns.load_dataset('tips')
tips.head()


# ## Histograms

# In[3]:

alpha = 0.5
plt.hist(tips.ix[tips['smoker'] == 'Yes' ,'total_bill'], label = 'Smokers', alpha = alpha)
plt.hist(tips.ix[tips['smoker'] == 'No' ,'total_bill'], label = 'Non-Smokers', alpha = alpha)
plt.xlabel('total_bill')
plt.legend()
plt.show()


# An alternative is to use the magic of seaborn sns.FacetGrid function: you tell which hue you need and then by which matplotlib basic function you want. Workflow: you divide the data into pieces, with FacetGrid, you pass on arguments, hue, row, col, to divide the data, and then you use map to apply to each of the pieces a particular function:

# In[13]:

plot = sns.FacetGrid(data= tips, hue= 'smoker', size = 10)
plot.map(plt.hist, 'total_bill', alpha = 0.5).add_legend()
plot.ax.set(ylabel = 'Count', title = 'Do you smoke?')
plt.show()


# ## Strip-plots

# In[10]:

sns.stripplot(x = 'day', y = 'total_bill', data = tips)
plt.show()


# In[11]:

sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter= True)
plt.show()


# ### Swarm Plots: Strartyfing according to values

# In[12]:

sns.swarmplot(x = 'day', y = 'total_bill', data = tips)
plt.show()


# Some other functions have already incorporated the ability to divide the plot into groups and perform a plt.function on each of them.

# In[24]:

sns.swarmplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex')
plt.show()


# In[27]:

sns.swarmplot(y = 'day', x = 'tip', data = tips, hue = 'sex', orient = 'h')
plt.show()


# ## Boxplots and Violin Plots

# In[30]:

sns.boxplot(x = 'day', y = 'tip', data = tips)
plt.show()


# In[31]:

sns.violinplot(x = 'day', y = 'tip', data = tips)
plt.show()


# In[32]:

sns.violinplot(x = 'day', y = 'tip', inner=None, data = tips, color = 'lightgray')
sns.swarmplot(x = 'day', y = 'tip', data = tips)
plt.show()


# Instructor's note: overlaying Histograms may not give you all you need. For small to mid-size datasets, use strip-plots and swarm-plots. For large datasets, use boxplots or violinplots. 

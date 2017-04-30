
# coding: utf-8

# # Visualizing Regression

# In[7]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')


# In[8]:

tips = sns.load_dataset('tips')
tips.head()


# ## lmplot

# In[9]:

sns.lmplot(x = 'total_bill', y = 'tip', data = tips)


# In[10]:

sns.lmplot(x = 'total_bill', y = 'tip', data = tips, ci = None)


# ## Hue, col, row

# In[12]:

sns.lmplot(x = 'total_bill', y = 'tip', hue = 'sex',data = tips)


# In[13]:

sns.lmplot(x = 'total_bill', y = 'tip', hue = 'sex',data = tips, col = 'smoker')


# In[14]:

sns.lmplot(x = 'total_bill', y = 'tip', hue = 'sex',data = tips, col = 'smoker', row = 'day')


# ## Residuals

# In[16]:

sns.residplot(x = 'total_bill', y = 'tip', data = tips)


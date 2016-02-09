@@ -0,0 +1,460 @@

# coding: utf-8

# In[9]:

import pandas as pd
get_ipython().magic(u'pylab inline')


# In[4]:

df = pd.read_csv("train.csv")


# In[5]:

df


# ###Titanic EDA
# 
# EDA - Exploratory Data Analysis.
# 
# For Each Variable :
# <li> Is the variable categorical or continuous
# <li> Are there missing values?
# <li> Min, Max, Mean, and Standard Deviation of the continuous variables
# <li> Histograms describing the distribution of the variable.
# 
# 
# 

# In[12]:

df.Sex.value_counts().plot(kind='bar')


# In[148]:

df[df.Sex=='female'].Survived.value_counts().plot(kind='bar')


# In[150]:

df[df.Sex=='male'].Survived.value_counts().plot(kind='bar')


# In[27]:

df[df.Sex=='female']


# In[151]:

df[df.Sex=='male'].Survived.value_counts()


# In[152]:

df[df.Sex=='female'].Survived.value_counts()


# In[153]:

df.describe()


# In[28]:

df[df.Sex.isnull()]


# ###EDA of Fare

# In[29]:

df.Fare.value_counts()


# In[30]:

df.describe()


# In[34]:

df.Fare.hist()


# In[35]:

df.Fare.hist(bins=5)


# ###EDA for PassengerID

# In[44]:

df.PassengerId.value_counts()


# In[45]:

df[df.PassengerId.isnull()]


# In[47]:

df.describe()


# In[48]:

df.PassengerId.hist()


# ###EDA of Survived :

# In[49]:

df.Survived.value_counts().plot(kind='bar')


# In[136]:

df[df.Sex=='male'].Survived.value_counts().plot(kind='barh')


# In[137]:

df[df.Sex=='female'].Survived.value_counts().plot(kind='barh')


# In[55]:

df.Survived.value_counts()


# In[56]:

df[df.Survived.isnull()]


# In[59]:

df.describe()


# In[60]:

df.Survived.hist()


# ###EDA of Pclass :

# In[61]:

df.Pclass.value_counts().plot(kind='bar')


# In[62]:

df.Pclass.value_counts()


# In[63]:

df[df.Pclass.isnull()]


# In[64]:

df.describe()


# In[65]:

df.Pclass.hist()


# ###EDA of Sex

# In[67]:

df[df.Sex=='male'].Pclass.value_counts().plot(kind='barh')


# In[68]:

df[df.Sex=='female'].Pclass.value_counts().plot(kind='barh')


# ###EDA of Sex

# In[69]:

df.Sex.value_counts().plot(kind='bar')


# In[71]:

df[df.Sex=='female']


# In[72]:

df[df.Sex=='male']


# In[73]:

df[df.Sex=='male'].Survived.value_counts().plot(kind='barh')


# In[74]:

df[df.Sex=='female'].Survived.value_counts().plot(kind='barh')


# In[75]:

df[df.Sex=='male'].Age.value_counts().plot(kind='barh')


# In[76]:

df[df.Sex=='female'].Age.value_counts().plot(kind='barh')


# In[77]:

df.Sex.value_counts()


# In[154]:

df[df.Sex.isnull()]


# In[78]:

df.describe()


# ###EDA of Age

# In[83]:

df[df.Sex=='male'].Age.value_counts().plot(kind='barh')


# In[84]:

df[df.Sex=='female'].Age.value_counts().plot(kind='barh')


# In[85]:

df.Age.value_counts().plot(kind='bar')


# In[86]:

df.Age.value_counts()


# In[87]:

df[df.Age.isnull()]


# In[155]:

avgAge = df.Age.mean()


# In[156]:

df.Age = df.Age.fillna(value=avgAge)


# In[157]:

df[df.Age.isnull()]


# In[158]:

df


# In[88]:

df.describe()


# ###EDA of SibSp

# In[90]:

df.SibSp.value_counts().plot(kind='bar')


# In[91]:

df[df.Sex=='male'].SibSp.value_counts().plot(kind='barh')


# In[92]:

df[df.Sex=='female'].SibSp.value_counts().plot(kind='barh')


# In[93]:

df.SibSp.value_counts()


# In[94]:

df[df.SibSp.isnull()]


# In[95]:

df.describe()


# In[96]:

df.SibSp.hist()


# In[98]:

df.SibSp.hist(bins=5)


# ###EDA of Parch

# In[99]:

df.Parch.value_counts().plot(kind='bar')


# In[100]:

df.Parch.value_counts()


# In[101]:

df[df.Sex=='female'].Parch.value_counts().plot(kind='barh')


# In[102]:

df[df.Sex=='female'].Parch.value_counts()


# In[103]:

df[df.Sex=='male'].Parch.value_counts().plot(kind='barh')


# In[104]:

df[df.Sex=='male'].Parch.value_counts()


# In[105]:

df[df.Parch.isnull()]


# In[106]:

df.describe()


# In[107]:

df.Parch.hist()


# In[108]:

df.SibSp.hist(bins=7)


# ###EDA of Ticket

# In[110]:

df.Ticket.value_counts()


# In[119]:

df[df.Ticket.isnull()]


# In[118]:

df.describe()


# ###EDA of Cabin

# In[122]:

df.Cabin.value_counts()


# In[131]:

df[df.Ticket.isnull()]


# In[132]:

df.describe()


# ###EDA of Embarked

# In[143]:

df.Embarked.value_counts().plot(kind='bar')


# In[138]:

df.Embarked.value_counts()


# In[140]:

df[df.Embarked=='S'].Survived.value_counts().plot(kind='barh')


# In[141]:

df[df.Embarked=='C'].Survived.value_counts().plot(kind='barh')


# In[142]:

df[df.Embarked=='Q'].Survived.value_counts().plot(kind='barh')


# In[144]:

df[df.Embarked.isnull()]


# In[145]:

df.describe()

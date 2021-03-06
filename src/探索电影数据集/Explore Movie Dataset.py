#!/usr/bin/env python
# coding: utf-8

# ## 探索电影数据集
# 
# 在这个项目中，你将尝试使用所学的知识，使用 `NumPy`、`Pandas`、`matplotlib`、`seaborn` 库中的函数，来对电影数据集进行探索。
# 
# 下载数据集：
# [TMDb电影数据](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/explore+dataset/tmdb-movies.csv)
# 

# 
# 数据集各列名称的含义：
# <table>
# <thead><tr><th>列名称</th><th>id</th><th>imdb_id</th><th>popularity</th><th>budget</th><th>revenue</th><th>original_title</th><th>cast</th><th>homepage</th><th>director</th><th>tagline</th><th>keywords</th><th>overview</th><th>runtime</th><th>genres</th><th>production_companies</th><th>release_date</th><th>vote_count</th><th>vote_average</th><th>release_year</th><th>budget_adj</th><th>revenue_adj</th></tr></thead><tbody>
#  <tr><td>含义</td><td>编号</td><td>IMDB 编号</td><td>知名度</td><td>预算</td><td>票房</td><td>名称</td><td>主演</td><td>网站</td><td>导演</td><td>宣传词</td><td>关键词</td><td>简介</td><td>时常</td><td>类别</td><td>发行公司</td><td>发行日期</td><td>投票总数</td><td>投票均值</td><td>发行年份</td><td>预算（调整后）</td><td>票房（调整后）</td></tr>
# </tbody></table>
# 

# **请注意，你需要提交该报告导出的 `.html`、`.ipynb` 以及 `.py` 文件。**

# 
# 
# ---
# 
# ---
# 
# ## 第一节 数据的导入与处理
# 
# 在这一部分，你需要编写代码，使用 Pandas 读取数据，并进行预处理。

# 
# **任务1.1：** 导入库以及数据
# 
# 1. 载入需要的库 `NumPy`、`Pandas`、`matplotlib`、`seaborn`。
# 2. 利用 `Pandas` 库，读取 `tmdb-movies.csv` 中的数据，保存为 `movie_data`。
# 
# 提示：记得使用 notebook 中的魔法指令 `%matplotlib inline`，否则会导致你接下来无法打印出图像。

# In[66]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

movie_data = pd.read_csv('tmdb-movies.csv', index_col=['id'])
movie_data.head()


# ---
# 
# **任务1.2: ** 了解数据
# 
# 你会接触到各种各样的数据表，因此在读取之后，我们有必要通过一些简单的方法，来了解我们数据表是什么样子的。
# 
# 1. 获取数据表的行列，并打印。
# 2. 使用 `.head()`、`.tail()`、`.sample()` 方法，观察、了解数据表的情况。
# 3. 使用 `.dtypes` 属性，来查看各列数据的数据类型。
# 4. 使用 `isnull()` 配合 `.any()` 等方法，来查看各列是否存在空值。
# 5. 使用 `.describe()` 方法，看看数据表中数值型的数据是怎么分布的。
# 
# 

# In[67]:


#获取数据表的行列
movie_data.shape


# In[199]:


#使用head()
movie_data.head(10)


# In[200]:


# 使用tail
movie_data.tail(2)


# In[201]:


# 使用sample
movie_data.sample(5)


# In[71]:


# 使用dtypes
movie_data.dtypes


# In[72]:


#判断是否是空值
movie_data.isnull().any()


# In[73]:


# 使用describe 方法
movie_data.describe()


# ---
# 
# **任务1.3: ** 清理数据
# 
# 在真实的工作场景中，数据处理往往是最为费时费力的环节。但是幸运的是，我们提供给大家的 tmdb 数据集非常的「干净」，不需要大家做特别多的数据清洗以及处理工作。在这一步中，你的核心的工作主要是对数据表中的空值进行处理。你可以使用 `.fillna()` 来填补空值，当然也可以使用 `.dropna()` 来丢弃数据表中包含空值的某些行或者列。
# 
# 任务：使用适当的方法来清理空值，并将得到的数据保存。

# In[74]:


#查看空值
movie_data.info()


# In[75]:


# 删除一些无关紧要 又带空值的列
movie_data.drop( ['homepage', 'tagline','keywords'],axis = 1,inplace = True)


# In[84]:


#删除没有id的行
movie_data = movie_data.dropna(axis=0,subset = ["imdb_id"])


# In[90]:


movie_data.fillna('无', inplace=True)


# In[91]:


movie_data.info()


# ---
# 
# ---
# 
# ## 第二节 根据指定要求读取数据
# 
# 
# 相比 Excel 等数据分析软件，Pandas 的一大特长在于，能够轻松地基于复杂的逻辑选择合适的数据。因此，如何根据指定的要求，从数据表当获取适当的数据，是使用 Pandas 中非常重要的技能，也是本节重点考察大家的内容。
# 
# 

# In[ ]:





# ---
# 
# **任务2.1: ** 简单读取
# 
# 1. 读取数据表中名为 `id`、`popularity`、`budget`、`runtime`、`vote_average` 列的数据。
# 2. 读取数据表中前1～20行以及48、49行的数据。
# 3. 读取数据表中第50～60行的 `popularity` 那一列的数据。
# 
# 要求：每一个语句只能用一行代码实现。

# In[ ]:





# In[93]:


#1. 读取数据表中名为 `id`、`popularity`、`budget`、`runtime`、`vote_average` 列的数据。
movie_data[['imdb_id', 'popularity','budget', 'runtime', 'vote_average']]


# In[202]:


#2. 读取数据表中前1～20行以及48、49行的数据。
# movie_data.iloc[0:20].append(movie_data.iloc[[47,48]])
movie_data.iloc[np.r_[0:20,47:49]]


# In[104]:


#3. 读取数据表中第50～60行的 `popularity` 那一列的数据。
movie_data.iloc[49:60].loc[:, ['popularity']]


# ---
# 
# **任务2.2: **逻辑读取（Logical Indexing）
# 
# 1. 读取数据表中 **`popularity` 大于5** 的所有数据。
# 2. 读取数据表中 **`popularity` 大于5** 的所有数据且**发行年份在1996年之后**的所有数据。
# 
# 提示：Pandas 中的逻辑运算符如 `&`、`|`，分别代表`且`以及`或`。
# 
# 要求：请使用 Logical Indexing实现。

# In[105]:


#读取数据表中 popularity 大于5 的所有数据。
movie_data[movie_data['popularity'] > 5]


# In[107]:


#读取数据表中 popularity 大于5 的所有数据且发行年份在1996年之后的所有数据。
movie_data[(movie_data['popularity'] > 5) & (movie_data['release_year'] > 1996)]


# ---
# 
# **任务2.3: **分组读取
# 
# 1. 对 `release_year` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `revenue` 的均值。
# 2. 对 `director` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `popularity` 的均值，从高到低排列。
# 
# 要求：使用 `Groupby` 命令实现。

# In[117]:


#对 release_year 进行分组，使用 .agg 获得 revenue 的均值。
movie_data.groupby('release_year')['revenue_adj'].agg(['mean'])


# In[121]:


#对 director 进行分组，使用 .agg 获得 popularity 的均值，从高到低排列。
movie_data.groupby('director')['popularity'].agg(['mean']).sort_values(by='mean', ascending=False)


# ---
# 
# ---
# 
# ## 第三节 绘图与可视化
# 
# 接着你要尝试对你的数据进行图像的绘制以及可视化。这一节最重要的是，你能够选择合适的图像，对特定的可视化目标进行可视化。所谓可视化的目标，是你希望从可视化的过程中，观察到怎样的信息以及变化。例如，观察票房随着时间的变化、哪个导演最受欢迎等。
# 
# <table>
# <thead><tr><th>可视化的目标</th><th>可以使用的图像</th></tr></thead><tbody>
#  <tr><td>表示某一属性数据的分布</td><td>饼图、直方图、散点图</td></tr>
#  <tr><td>表示某一属性数据随着某一个变量变化</td><td>条形图、折线图、热力图</td></tr>
#  <tr><td>比较多个属性的数据之间的关系</td><td>散点图、小提琴图、堆积条形图、堆积折线图</td></tr>
# </tbody></table>
# 
# 在这个部分，你需要根据题目中问题，选择适当的可视化图像进行绘制，并进行相应的分析。对于选做题，他们具有一定的难度，你可以尝试挑战一下～

# **任务3.1：**对 `popularity` 最高的20名电影绘制其 `popularity` 值。

# In[196]:


# data = movie_data.sort_values(by='popularity', ascending=False).iloc[0:20]
# plt.figure(figsize=(20,15))
# plt.bar(data['original_title'], data['popularity'])
# plt.title('Top 20 Polularity')
# plt.xlabel('Moive Name')
# plt.xticks(rotation=90) 
# plt.ylabel('Polularity',rotation=0)
movie_data.sort_values('popularity', ascending=False).head(20).  plot(kind='barh', y='popularity', x='original_title', legend=False)
plt.xlabel('popularity')


# ---
# **任务3.2：**分析电影净利润（票房-成本）随着年份变化的情况，并简单进行分析。

# In[211]:


data = movie_data.groupby('release_year')['revenue_adj','budget_adj'].mean()
data_std = movie_data.groupby('release_year')['revenue_adj','budget_adj'].std()
plt.figure(figsize=(20,15))
plt.errorbar(data.index ,data['revenue_adj'] - data['budget_adj'], yerr=data_std['revenue_adj'] - data_std['budget_adj'],fmt='o',ecolor='r',color='b',elinewidth=2,capsize=4)
plt.title('Profit Show By Year')
plt.xlabel('Year')
plt.xticks(rotation=90) 
plt.ylabel('Profit',rotation=0)


# ---
# 
# **[选做]任务3.3：**选择最多产的10位导演（电影数量最多的），绘制他们排行前3的三部电影的票房情况，并简要进行分析。

# In[229]:


def func_top3(df):
    return df['revenue_adj'].sort_values(ascending=False).iloc[0:3].sum()

df = movie_data[movie_data['director'] != '无']
top10directors = df.director.value_counts()[:10]
print('最多产的 10 位导演是:')
print(top10directors)

# 最多产的 10 位导演的全部电影
df = df.loc[df.director.isin(top10directors.keys())]
# print(df.shape)
# 最多产的 10 位导演每人票房排行前三的电影
df = df.sort_values('revenue', ascending = False).groupby('director').head(3)
# df[['director','revenue']].plot(kind='bar', stacked=True)
sns.barplot(y=df.director, x=df.revenue)
# data = movie_data.groupby('director')["imdb_id"].count().sort_values(ascending=False).iloc[0:10]
# data1 = movie_data.groupby('director').apply(func_top3)
# data = pd.concat([data, data1], axis=1, join='inner')
# data.columns = ['imdb_id','revenue']
# # data.info()
# data = data.sort_values(by='revenue', ascending=False)
# plt.figure(figsize=(20,15))
# plt.bar(data.index, data['revenue'])
# plt.title('Top 10 Director Revenue')
# plt.xlabel('Director Name')
# plt.xticks(rotation=90) 
# plt.ylabel('Revenue',rotation=0)


# ---
# 
# **[选做]任务3.4：**分析1968年~2015年六月电影的数量的变化。

# In[212]:


movie_data['release_date'] = (pd.to_datetime(movie_data['release_date']))
data = movie_data[(movie_data.release_year >= 1968) & (movie_data.release_year <=2015) & (movie_data['release_date'].dt.month == 6)].groupby('release_year').imdb_id.count()
plt.figure(figsize=(20,15))
plt.plot(data.index ,data)
plt.title('Movie Number By Year')
plt.xlabel('Year')
plt.xticks(rotation=90) 
plt.ylabel('Number',rotation=0)


# ---
# 
# **[选做]任务3.5：**分析1968年~2015年六月电影 `Comedy` 和 `Drama` 两类电影的数量的变化。

# In[228]:


data_comedy = movie_data[(movie_data.release_year >= 1968) & (movie_data.release_year <=2015) &(movie_data.genres.str.contains('Comedy')) & (movie_data['release_date'].dt.month == 6)].groupby('release_year').imdb_id.count()
data_drama = movie_data[(movie_data.release_year >= 1968) & (movie_data.release_year <=2015) &(movie_data.genres.str.contains('Drama')) & (movie_data['release_date'].dt.month == 6)].groupby('release_year').imdb_id.count()


plt.figure(figsize=(15,15))
l1, = plt.plot(data_comedy.index ,data_comedy,"b");
l2, = plt.plot(data_drama.index ,data_drama, "r");


plt.title('Comedy And Drama Number')
plt.xlabel('Year')
plt.xticks(rotation=90) 
plt.ylabel('Number',rotation=0)

plt.legend([l1,l2],['Comedy','Drama'],loc='upper left')


# > 注意: 当你写完了所有的代码，并且回答了所有的问题。你就可以把你的 iPython Notebook 导出成 HTML 文件。你可以在菜单栏，这样导出**File -> Download as -> HTML (.html)、Python (.py)** 把导出的 HTML、python文件 和这个 iPython notebook 一起提交给审阅者。

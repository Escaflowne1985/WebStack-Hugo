#!/usr/bin/env python
# coding: utf-8

# In[8]:


import yaml
import pandas as pd


# In[76]:


df = pd.read_excel("data.xlsx")
df = df[df["is_use"]==1]
df.reset_index(drop=True,inplace=True)


# In[77]:


# 构建一级菜单
taxonomy_list = df["taxonomy"].unique()
# 构建taxonomy对应的icon字典
taxonomy_icon_dict = df.set_index("taxonomy")["icon"].to_dict()


# In[78]:


taxonomy_icon_dict


# In[79]:


all_list = []
for key_ in taxonomy_list:
    dict_each_one = {}
    for i in range(len(df)):
        dict_each_one["taxonomy"]=key_
        dict_each_one["icon"]=taxonomy_icon_dict[key_]
        dict_each_one["list"]=[]
    all_list.append(dict_each_one)


# In[80]:


# 构建二级菜单
term_list = df["term"].unique()
# 构建taxonomy对应的icon字典
term_taxonomy_dict = df.set_index("term")["taxonomy"].to_dict()


# In[97]:


term_list_all = []
for term_ in term_list:
    dict_each_one = {}
    # 先构建list中的term
    dict_each_one["term"]=term_
    links_list = []
    for i in range(len(df)):
        dict_each_one_temp = {}
        if df["term"][i] == term_:
#             print(df["term"][i])
            dict_each_one_temp["title"] = df["title"][i]
            dict_each_one_temp["logo"] = df["logo"][i]
            dict_each_one_temp["url"] = df["url"][i]
            dict_each_one_temp["description"] = df["description"][i]
        links_list.append(dict_each_one_temp) 
        links_list = [i for i in links_list if i !={}]
    dict_each_one["links"]=links_list
    term_list_all.append(dict_each_one)


# In[111]:


# 将二级菜单合并到1级中
for i in all_list:
    for j in term_list_all:
        term_name = j["term"]
        if i["taxonomy"] == term_taxonomy_dict[term_name]:
            i["list"].append(j)


# In[40]:


d = [
    {
    "taxonomy": "科研办公",
    "icon": "fas fa-flask fa-lg",
    "list": [
        {
            "term": "生物信息",
            "links":[
                {
                    "title": "NCBI",
                    "logo": "ncbi.jpg",
                    "url": "https://www.ncbi.nlm.nih.gov/",
                    "description": "National Center for Biotechnology Information. "
                },
                {
                    "title": "Bioconda",
                    "logo": "bioconda.jpg",
                    "url": "https://anaconda.org/bioconda/",
                    "description": "Bioconda :: Anaconda.org."
                }
            ]
        }
    ]
    }
]


# In[114]:


with open("webstack.yml", 'w',encoding="utf8") as f:
    yaml.dump(all_list,f,allow_unicode=True, default_flow_style=False,sort_keys=False)


# In[ ]:





# In[ ]:





# In[ ]:





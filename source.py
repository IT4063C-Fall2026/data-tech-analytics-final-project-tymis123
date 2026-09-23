#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# Analyzing Technology Careers and the IT Job Market:                                                                                                   I want to look at the technology job market and the opportunities available for new graduates. Technology is always changing, so it can be hard for students to know which careers and skills are in demand. For this project, I want to look at IT jobs, salaries, job growth, and skills to better understand the job market.
# 

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# Which IT careers are growing the most, and how do they compare based on salary, job growth, and skills needed?

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# I think the results will show that some IT careers are growing faster and paying more than others. I also think skills like SQL, Python, and working with data will show up often in growing IT careers. I could use charts to compare salary and job growth between different careers.

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 1. BLS Employment Projections - File/XLSX: Gives employment projections and job growth information by occupation. BLS provides occupational projection tables as downloadable files.
# 2. BLS occupational wage/employment data - File/data tables: We can use this for salary and employment information.
# 3. O*NET Web Services - API: Gives occupation skills information, including skills and in-demand technology skills. It is a REST API and returns JSON.                                                                                                                                                  
# I plan to use three data sources for this project. I will use BLS employment data for job and salary information, BLS employment projections for job growth, and the O*NET API for skills needed for different IT careers. These datasets can be related using occupation names and occupation codes. Together, they will help me compare IT careers based on salary, growth, and skills.

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# I will compare the data from the three sources to look at salary, job growth, and skills for different IT careers. I will use occupation names and codes to connect the datasets. Then I can use charts to compare the careers and look for patterns in the data.

# In[7]:


import pandas as pd

bls_projections = pd.read_excel("occupation.xlsx", sheet_name="Table 1.2")
bls_projections.head()


# In[8]:


bls_wages = pd.read_excel("wages.xlsx")
bls_wages.head()


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[10]:


import requests

url = "https://data.usajobs.gov/api/codelist/occupationalseries?"

response = requests.get(url)

usajobs_data = response.json()
usajobs_data


# In[ ]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')


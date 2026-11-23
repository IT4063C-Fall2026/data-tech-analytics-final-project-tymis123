#!/usr/bin/env python
# coding: utf-8

# Analyzing Technology Careers and the IT Job Market
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
# 3. USAJOBS Occupational Series - API/JSON: Gives occupational information and codes for different careers.                                                                                                                                                 
# I plan to use three data sources for this project. I will use BLS employment data for job and salary information, BLS employment projections for job growth, and the O*NET API for skills needed for different IT careers. These datasets can be related using occupation names and occupation codes. Together, they will help me compare IT careers based on salary, growth, and skills.

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# I will compare the data from the three sources to look at salary, job growth, and skills for different IT careers. I will use occupation names and codes to connect the datasets. Then I can use charts to compare the careers and look for patterns in the data.

# In[2]:


import pandas as pd

bls_projections = pd.read_excel("occupation.xlsx", sheet_name="Table 1.2")
bls_projections.head()


# In[ ]:


bls_wages = pd.read_excel("wages.xlsx")
bls_wages.head()


# ## Resources and References
# *What resources and references have you used for this project?*
# Bureau of Labor Statistics (BLS) – Employment Projections data
# Bureau of Labor Statistics (BLS) – Occupational Employment and Wage Statistics data
# USAJOBS – Occupational Series API

# In[ ]:


import requests

url = "https://data.usajobs.gov/api/codelist/occupationalseries"

response = requests.get(url)

usajobs_data = response.json()
usajobs_data


# # Checkpoint 2: Exploratory Data Analysis & Visualization
# 
# ## 1. Exploratory Data Analysis (EDA)
# 
# In this section, I will explore the IT job market data to compare salaries, job growth, and employment trends. I will also check for missing values, duplicates, and other issues in the datasets.

# # Checkpoint 2: Exploratory Data Analysis & Visualization
# 
# ## 1. Exploratory Data Analysis (EDA)
# 
# In this section, I will explore the IT job market data to compare salaries, job growth, and employment trends.
# I will also check for missing values, duplicates, and other issues in the datasets.

# In[16]:


get_ipython().run_line_magic('pip', 'install pandas openpyxl matplotlib seaborn')


# In[21]:


import pandas as pd

# Load the employment and salary datasets
employment_df = pd.read_excel("occupation.xlsx", sheet_name="Table 1.2", header=1)
wages_df = pd.read_excel("wages.xlsx")

# Check the columns and first five rows
print("Employment Data:")
display(employment_df.head())
print(employment_df.columns.tolist())

print("Wage Data:")
display(wages_df.head())
print(wages_df.columns.tolist())


# In[22]:


# Statistical summary of employment data
print("Employment Data Summary:")
display(employment_df.describe())

# Statistical summary of salary data
print("Salary Data Summary:")
display(wages_df.describe())


# Statistical Summary Findings
# 
# The employment dataset shows that job growth varies across different occupations. Some careers are expected to grow, while others may decline between 2025 and 2035.
# 
# The salary dataset also shows differences in employment levels across occupations. These results will help me compare IT careers and understand which jobs may offer better opportunities.

# In[23]:


# Check for missing values
print("Employment Missing Values:")
print(employment_df.isnull().sum())

print("Salary Missing Values:")
print(wages_df.isnull().sum())

# Check for duplicates
print("Employment Duplicates:", employment_df.duplicated().sum())
print("Salary Duplicates:", wages_df.duplicated().sum())


# ### Missing Values and Duplicates
# 
# Both datasets contain missing values. The employment data has missing information in job experience and training requirements. The salary data also has missing information in some columns.
# 
# Neither dataset has duplicate rows. I will review the missing values and only remove information that is not useful for my analysis.

# In[24]:


print("Employment Data Types:")
print(employment_df.dtypes)

print("Salary Data Types:")
print(wages_df.dtypes)


# ### Data Types
# 
# Most columns have the correct data types. However, some salary and percentage columns are stored as text instead of numbers. I will convert the columns needed for my analysis so I can compare salaries and job growth correctly.

# In[25]:


# Convert employment data columns to numbers
employment_df["Median annual wage, dollars, 2025"] = pd.to_numeric(
    employment_df["Median annual wage, dollars, 2025"], errors="coerce"
)

employment_df["Percent self-employed, 2025"] = pd.to_numeric(
    employment_df["Percent self-employed, 2025"], errors="coerce"
)

# Check the updated data types
print(employment_df[[
    "Median annual wage, dollars, 2025",
    "Percent self-employed, 2025"
]].dtypes)


# In[26]:


# Check the relationship between salary and job growth
correlation = employment_df[
    ["Median annual wage, dollars, 2025",
     "Employment change, percent, 2025–35"]
].corr()

display(correlation)


# Correlation Findings
# 
# The correlation between salary and job growth is 0.21. This shows a weak positive relationship. Higher-paying jobs may have slightly higher growth, but salary alone does not strongly predict job growth.

# In[27]:


import matplotlib.pyplot as plt

# Show the distribution of annual salaries
plt.hist(employment_df["Median annual wage, dollars, 2025"].dropna())

plt.title("Annual Salary Distribution")
plt.xlabel("Annual Salary ($)")
plt.ylabel("Number of Occupations")

plt.show()


# Visualization 1: Annual Salary Distribution
# 
# I used a histogram to show how annual salaries are distributed across occupations. Most jobs fall within the lower salary ranges, while fewer jobs have very high salaries. This shows that higher-paying occupations are less common in the dataset.

# In[28]:


# Show the distribution of job growth
plt.hist(employment_df["Employment change, percent, 2025–35"].dropna())

plt.title("Job Growth Distribution (2025–2035)")
plt.xlabel("Employment Growth (%)")
plt.ylabel("Number of Occupations")

plt.show()


# Visualization 2: Job Growth Distribution
# 
# I used a histogram to show the expected job growth between 2025 and 2035. Most occupations are expected to have small to moderate growth. Some jobs are expected to decline, while a few have much higher growth rates.

# In[29]:


# Compare salary and job growth
plt.scatter(
    employment_df["Median annual wage, dollars, 2025"],
    employment_df["Employment change, percent, 2025–35"],
    alpha=0.5
)

plt.title("Salary vs. Job Growth")
plt.xlabel("Annual Salary ($)")
plt.ylabel("Job Growth (%)")

plt.show()


# Visualization 3: Salary vs. Job Growth
# 
# I used a scatterplot to compare annual salaries and job growth. 
# The chart shows that higher salaries do not always mean higher job growth. 
# Most jobs are grouped in the lower salary ranges, with different growth rates.

# In[30]:


import seaborn as sns

# Select computer and IT occupations
it_jobs = employment_df[
    employment_df["2025 National Employment Matrix code"].str.startswith("15-", na=False)
].copy()

# Keep individual occupations
it_jobs = it_jobs[it_jobs["Occupation type"] == "Line item"]

# Show the 10 fastest-growing IT occupations
top_it_jobs = it_jobs.sort_values(
    "Employment change, percent, 2025–35",
    ascending=False
).head(10)

sns.barplot(
    data=top_it_jobs,
    x="Employment change, percent, 2025–35",
    y="2025 National Employment Matrix title"
)


# Visualization 4: Fastest-Growing Careers
# 
# This bar chart compares the projected job growth of 10 careers from 2025 to 2035. Data scientists have the highest growth, followed by computer and information research scientists and information security analysts. This shows that careers related to data and technology are expected to grow.

# ## 2. Data Cleaning and Transformation
# 
# In this section, I will clean the datasets by checking missing values, duplicates, outliers, and data types. This will help make the data more accurate for my analysis.

# In[31]:


# Check missing values in both datasets
print("Employment Missing Values:")
print(employment_df.isnull().sum())

print("Salary Missing Values:")
print(wages_df.isnull().sum())


# In[32]:


# Remove rows missing salary or job growth data
employment_df = employment_df.dropna(
    subset=[
        "Median annual wage, dollars, 2025",
        "Employment change, percent, 2025–35"
    ]
)

# Check the remaining missing values
print(employment_df.isnull().sum())


# Missing Values
# 
# I found missing values in both datasets. I removed rows from the employment data that were missing salary or job growth information because those values are important for my project. I kept other missing values that do not affect my current analysis.

# In[33]:


# Check for duplicates
print("Employment Duplicates:", employment_df.duplicated().sum())
print("Salary Duplicates:", wages_df.duplicated().sum())

# Remove duplicates if there are any
employment_df = employment_df.drop_duplicates()
wages_df = wages_df.drop_duplicates()


# Duplicate Values
# 
# I checked both datasets for duplicate rows. I used Python to remove any duplicates so the same information would not be counted twice.

# In[34]:


# Check the highest and lowest salaries
print("Highest Salary:")
print(employment_df["Median annual wage, dollars, 2025"].max())

print("Lowest Salary:")
print(employment_df["Median annual wage, dollars, 2025"].min())

# Check the highest and lowest job growth
print("Highest Job Growth:")
print(employment_df["Employment change, percent, 2025–35"].max())

print("Lowest Job Growth:")
print(employment_df["Employment change, percent, 2025–35"].min())


# Outliers
# 
# I checked the highest and lowest salaries and job growth rates. The results showed some large differences between occupations. I decided to keep these values for now because they may represent real changes in the job market. Removing them could leave out useful information.

# Data Types
# 
# I checked the data types in both datasets. Some salary and percentage values were stored as text instead of numbers. I converted the columns needed for my analysis into numeric values so I could compare salaries and job growth correctly.

# 3. Machine Learning Plan
# 
# Type of Machine Learning
# 
# I plan to use supervised learning with regression to predict job growth based on salary and employment data. This could help me understand which IT careers may grow in the future.
# 
# Possible Challenges
# 
# One challenge is that some information is missing from the datasets. Another challenge is that job growth can change depending on the economy and technology.
# 
# How I Will Address These Challenges
# 
# I will continue cleaning the data and focus on the information that is available. I will also compare the model's predictions with the actual data to see how accurate they are.

# 4. Prior Feedback and Updates
# 
# Prior Feedback
# 
# I reviewed my project from Checkpoint 1 and continued working on my original research question about IT careers, salaries, and job growth.
# 
# Project Updates
# 
# For Checkpoint 2, I added statistical summaries, checked the data for missing values and duplicates, and created four visualizations. I also cleaned the data and added a machine learning plan.
# 
# These updates helped me better understand the IT job market and prepare for the next part of my project.

# In[35]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')


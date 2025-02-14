---
layout: post
title: "Credit Risk prediction and Analaysis"
date: 2024-02-10
categories: finance machine-learning
---
## **Credit risk prediction using machine learning methods**

## 🚀 **Overview**
- This project explores the burrowers credit risk in loans and application of machine learning methods to predict credit risk of a loan applicant based on demographic and other characteristics.The technological advancements in machine learning has paved the way to utilise it in many areas of businesses. When credit lenders such as financial institutions lend money it essential to ensure the risk associate with the credit is minimized. Though there are solutions based on classical statistical models such as Logistic regression. This project aims to find a solution based on machine learning approaches. Machine learning models, Decision Tree and Random Forest Regression were used with logistic regression model to compare and analyse the accuracy of each model to classify the risk of default.
## **Data loading and Preprocessing**
- A public dataset found in Kaggle was used, please click the link to download the data set.📁[Dataset link](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) The size of the data set is approximately 32000 and comprised of 11 features.Data preprocessing methods used to handle missing values,duplicates and outlier handling. The outliers were visualised using boxplots for further analysis.
![outliers](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Images/credit_outliers.png)

## **Exploratory analysis**
- The cleaned and prepocessed data was explored to analyse and identify relationships among data. Insights and interconnections among data was explored further to understand the features effectively.
![correlation](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Images/credit_corr.png)
- Further analysis was done using Power BI to enhance the understandability of the credit dataset.
##### 📌Key Insights
- Shorter credit histories correlate with higher default rates.
- Higher loan percentage relative to income leads to increased default risk.
- Renters and 'Other' homeownership types show the highest default rates.
- Higher interest rates are linked to lower loan grades, indicating riskier borrowers.

##### 📊 Dashboard Preview
![Dashboard Screenshot1](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Images/Loandefaultstrends.png)
![Dashboard Screenshot2](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Images/Burrowersriskpatterns.png)
![Dashboard Screenshot3](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Images/Loancharacteristics.png)
[Download Dashboard here](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Projects/CreditRiskAnalysisFinal.pbix)

## **Models used**
##### Logistic Regression
- A classification machine learning algorithm which can be used to predict a given class or not, by estimating the probality of event occuring. It uses the logistic funtion to transform the inputs into values ranging between 0 and
1 probability.
##### Decision Tree
- A machine learning algorithm which is used for classification and regression tasks to make prediction based on a tree like structure. It includes a Root node the starting point of the problem,Branches the flow of the decisions, Internal nodes represents the decisions due to features in the model and Leaf nodes are the ends of the tree which are considered
as the final prediction of the model.
##### Random Forest 
- A machine learning algorithm is model based on the Decision tree which combines a collection of decision trees to make prediction for classification and regression tasks. It is based on enesemble learning method where two or more machine learning models used to make accurate predictions. Randomly selected parts of the dataset is used to train each tree and use the averaged combine result to make predictions.
 
## **Evaluation and Results**
  



## 🔬 **Prediction app Preview** 
![App Screenshot](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Images/streamlitcredpredapp.png)



### 📌 Key Components
- [prediction model using python and sci-kit learn](https://github.com/SachiD123/MyPortfolio.github.io/blob/main/Projects/CreditRiskPrediction1.1.ipynb)



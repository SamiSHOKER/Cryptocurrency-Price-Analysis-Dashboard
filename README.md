# Cryptocurrency-Price-Analysis-Dashboard
It's a dashboard that analysis different cryptocurrencies prices along with fitting  LSTM models and evaluating their performance.

The aim of this project is to create an interactive dashboard using Dash Library in python to analyse and predict 10 different cryptocurrency prices.

This dashboard contains 2 interactive tabs where this first tab provides some financial analysis of 10 different cryptocurrency prices such as historical closing price, daily trading volume and daily returns. The Second tab is a demonstration of the performance of the Deep Learning Algorithm LSTM by prviding and interactive visualization of the predicted values of actual values for each cryptocurrency in additon to performance metrics such a R squared  and Root Mean Squared Errors.

The process to create this project was fistly by importing the data from yahoo finance. The file of data imporation codes is data_importation in "data" folder and the data imported where saved in this file. Secondly, in a seperated Jupyter Notebook file, I applied the LSTM algorithm (LSTM-Prediction.ipynb) and saved the results in 'data' folder.

After having my data and evaluation results ready, I built the elements for my dashabord in 'apps' and 'utils' folder.

The file 'requirements.txt' containts the libraries required for this project.

In case you want to replicated to results you would need to change the file directory in .py and .ipynb files.


Below you'll find screeshots of my dashborad final form : 

![image](https://user-images.githubusercontent.com/58007219/177529824-5cd7f6af-ac12-4734-b94a-d5bcfee77ec4.png)

![image](https://user-images.githubusercontent.com/58007219/177530075-e17d79db-4368-4a6e-bf76-7d450ac8388a.png)

![image](https://user-images.githubusercontent.com/58007219/177530223-3563e0d8-ddca-40c3-8728-c2fbfc99167e.png)


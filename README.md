# WiDS
This repository contains all codefiles and reports related to the WiDS project on movie recommendation system which was done by me in Dec 2024 - Jan 2025.


The main code for the recommendation system is in the collaborative.ipynb jupyter notebook which uses item-based and user-based collaborative filtering to recommend movies which users will like.

The dataset is a subset of **Movielens dataset** which is uploaded in the repository as "movies.dat" and "ratings.dat". This code can be run on any device by creating a virtual environment with required libraries installed.

The model is evaluated using RMSE method with **70-30 train-test split** to get an RMSE value of **1.77** of a particular user. The average for all users can be calculated similarly.
This project also uses **scikit-learn** library for calculating **cosine similarity** in user-item interaction matrix and it also uses Pandas extensively for all data analysis.

The **report** attached has details about the duration/timeline of the project and the collabuser.py codefile is for testing user based collaboration before implementing in the mainfile (this was a weekly task).

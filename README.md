NAME: MERCY CHEPKURUI
PROJECT TITLE: PYTHON MACHINE LEARNING 
DESCRIPTION FOR SUPERVISED ML:
# Supervised Machine Learning: Exam Score Predictor
# Description
This project demonstrates a foundational application of **Supervised Machine Learning** using a **Linear Regression** model to predict a student's examination score based on the number of hours they studied. The application is built using Python and the `scikit-learn` library, showcasing data preparation, model training, and interactive user predictions.

DESCRIPTION FOR UNSUPERVISED ML:
# Customer Segmentation using K-Means Clustering
This project implements an **Unsupervised Machine Learning** pipeline using the K-Means algorithm to segment customers based on their behavior metrics (Spending and Visits). The script handles data preprocessing, feature scaling, model training, and results display.
## Project Structure
* `unsupervised_ml.py` — The main Python script containing the machine learning code.
INSTRUCTIONS FOR SUPERVISED LEARNING PROJECT:
## Features
* **Linear Regression Model**: Utilizes `sklearn.linear_model.LinearRegression` to find the linear relationship between study time and performance.
* **Interactive CLI**: Allows users to input custom study hours dynamically via the command line to get instant predictions.
* **Formatted Outputs**: Automatically handles prediction estimation and formats the output to two decimal places.

## Core Technical Steps
1. **Data Preparation**: Prepares a dataset utilizing native Python lists for features and targets.
2. **Feature Separation**: Splits data into independent input features (`X`) and dependent target values (`y`).
3. **Model Training**: Initializes the regression model and fits it to the dataset using the `.fit()` method.
4. **Prediction**: Takes user input via `input()` and uses `.predict()` to evaluate the estimated score.
## Dataset Overview
The model is trained on a structured dataset mapping student dedication directly to performance metrics:
* **Hours Studied**: The independent feature representing the total time spent preparing.
* **Exam Score**: The dependent target value representing the final test marks achieved.

INSTRUCTIONS FOR UNSUPERVISED LEARNING PROJECT:
## How the Script Works
The script executes the following machine learning steps sequentially:
1. **Data Collection:** Prepares a structured dataset containing customer behavior features (`Spending` and `Visits`).
2. **Feature Scaling:** Uses `StandardScaler` from `scikit-learn` to normalize the features, ensuring the K-Means algorithm isn't biased by different measurement scales.
3. **Model Initialization:** Configurations are optimized for stability:
   * `n_clusters=3`: Groups the customers into 3 distinct behavioral segments.
   * `random_state=42`: Seeds the random number generator to guarantee **reproducible results** across runs.
   * `n_init=10`: Runs the algorithm 10 independent times with different random centroid placements to prevent getting stuck in local minima, selecting the most accurate overall clustering strategy.
4. **Model Training:** Fits the K-Means model to the scaled customer data.
5. **Output Generation:** Displays the exact cluster assignment for each customer alongside the total aggregate count of customers within each cluster.

## Setup and Requirements

### Prerequisites
Ensure you have Python installed on your machine. You will also need the following dependencies:
* `numpy`
* `scikit-learn`

### Installation
Install the required packages using pip:
```bash
pip install scikit-learn numpy
```

What is supervised machine learning? It is a type of artificial intelligence where model is traned using labeled data,
What is unsupervised machine learning? It is a type of artificial intelligence where data is not labeled, it learns the pattern by grouping related data.
Explain the difference between supervised and unsupervised learning. The main difference between supervised and unsupervised machine learning is that supervised machine leaning uses labeled data while unsupervised machine learning uses raw unlabed data.
Why is Linear Regression considered supervised learning? Because it trains on labeled data.
Why is K-Means considered unsupervised learning? Because it operates on unlabeled data without any external guidance, target variable or pre defined categories.
What is the difference between fit() and predict()? fit() is in the trainig phase while predict() is in the inference stage, fit() teaches the model by learning patterns, weights and parameters from the training data while predict() uses the knowledge and learned parameters from fit() to generate outputs for new unseen data.
Give two real-world applications of supervised learning and two of unsupervised learning. Supervised learning is used the financial sector for froud detection and also used for weather forecasting. Unsupervised learning is used for customer segmentation and anomaly detection

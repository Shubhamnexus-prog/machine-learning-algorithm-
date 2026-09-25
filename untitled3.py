# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:21:45 2026

@author: SHUBHAM
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ============================================================
# 1. LOAD DATASET
# ============================================================

dataset = pd.read_csv(
    r'C:\Users\SHUBHAM\Downloads\Restaurant_Reviews.tsv',
    delimiter='\t',
    quoting=3
)

print(dataset.head())
print(dataset.shape)


# ============================================================
# 2. TEXT PREPROCESSING
# ============================================================

corpus = []

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

for i in range(0, 1000):

    # Remove special characters
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])

    # Lowercase
    review = review.lower()

    # Split words
    review = review.split()

    # Stemming + Stopword removal
    review = [
        ps.stem(word)
        for word in review
        if word not in stop_words
    ]

    # Join words
    review = ' '.join(review)

    corpus.append(review)


print("\nPreprocessing completed!")
print(corpus[:5])


# ============================================================
# 3. BAG OF WORDS
# ============================================================

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1500)

x = cv.fit_transform(corpus).toarray()

y = dataset.iloc[:, 1].values

print("\nX Shape:", x.shape)
print("Y Shape:", y.shape)


# ============================================================
# 4. TRAIN TEST SPLIT
# ============================================================

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=0
)

print("\nTraining data:", x_train.shape)
print("Testing data:", x_test.shape)


# ============================================================
# 5. LOGISTIC REGRESSION
# ============================================================

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(max_iter=1000)

lr.fit(x_train, y_train)

y_pred_lr = lr.predict(x_test)


# ============================================================
# 6. NAIVE BAYES
# ============================================================

from sklearn.naive_bayes import MultinomialNB

nb = MultinomialNB()

nb.fit(x_train, y_train)

y_pred_nb = nb.predict(x_test)


# ============================================================
# 7. DECISION TREE
# ============================================================

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(
    random_state=0
)

dt.fit(x_train, y_train)

y_pred_dt = dt.predict(x_test)


# ============================================================
# 8. RANDOM FOREST
# ============================================================

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=0
)

rf.fit(x_train, y_train)

y_pred_rf = rf.predict(x_test)


# ============================================================
# 9. SVM
# ============================================================

from sklearn.svm import SVC

svm = SVC(
    kernel='linear',
    random_state=0
)

svm.fit(x_train, y_train)

y_pred_svm = svm.predict(x_test)


# ============================================================
# 10. KNN
# ============================================================

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(
    n_neighbors=5
)

knn.fit(x_train, y_train)

y_pred_knn = knn.predict(x_test)


# ============================================================
# 11. MODEL ACCURACY
# ============================================================

from sklearn.metrics import accuracy_score

accuracy_lr = accuracy_score(y_test, y_pred_lr)
accuracy_nb = accuracy_score(y_test, y_pred_nb)
accuracy_dt = accuracy_score(y_test, y_pred_dt)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
accuracy_knn = accuracy_score(y_test, y_pred_knn)


print("\n======================================")
print("MODEL ACCURACY")
print("======================================")

print("Logistic Regression :", accuracy_lr)
print("Naive Bayes         :", accuracy_nb)
print("Decision Tree       :", accuracy_dt)
print("Random Forest       :", accuracy_rf)
print("SVM                 :", accuracy_svm)
print("KNN                 :", accuracy_knn)


# ============================================================
# 12. MODEL COMPARISON
# ============================================================

models = [
    'Logistic Regression',
    'Naive Bayes',
    'Decision Tree',
    'Random Forest',
    'SVM',
    'KNN'
]

accuracies = [
    accuracy_lr,
    accuracy_nb,
    accuracy_dt,
    accuracy_rf,
    accuracy_svm,
    accuracy_knn
]

results = pd.DataFrame({
    'Model': models,
    'Accuracy': accuracies
})

results = results.sort_values(
    by='Accuracy',
    ascending=False
)

print("\n======================================")
print("MODEL COMPARISON")
print("======================================")

print(results)


# ============================================================
# 13. CONFUSION MATRIX - BEST MODEL
# ============================================================

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Find best model
best_model_name = results.iloc[0]['Model']

print("\nBest Model:", best_model_name)


if best_model_name == 'Logistic Regression':
    best_prediction = y_pred_lr

elif best_model_name == 'Naive Bayes':
    best_prediction = y_pred_nb

elif best_model_name == 'Decision Tree':
    best_prediction = y_pred_dt

elif best_model_name == 'Random Forest':
    best_prediction = y_pred_rf

elif best_model_name == 'SVM':
    best_prediction = y_pred_svm

else:
    best_prediction = y_pred_knn


cm = confusion_matrix(
    y_test,
    best_prediction
)

print("\nConfusion Matrix:")
print(cm)


# ============================================================
# 14. CLASSIFICATION REPORT
# ============================================================

print("\n======================================")
print("CLASSIFICATION REPORT")
print("======================================")

print(
    classification_report(
        y_test,
        best_prediction
    )
)


# ============================================================
# 15. CONFUSION MATRIX PLOT
# ============================================================

plt.figure(figsize=(6, 5))

plt.imshow(cm)

plt.title(
    f'Confusion Matrix - {best_model_name}'
)

plt.xlabel('Predicted')
plt.ylabel('Actual')

plt.colorbar()

plt.xticks(
    [0, 1],
    ['Negative', 'Positive']
)

plt.yticks(
    [0, 1],
    ['Negative', 'Positive']
)

for i in range(2):
    for j in range(2):
        plt.text(
            j,
            i,
            cm[i, j],
            ha='center',
            va='center'
        )

plt.show()


# ============================================================
# 16. ACCURACY COMPARISON GRAPH
# ============================================================

plt.figure(figsize=(10, 5))

plt.bar(
    results['Model'],
    results['Accuracy']
)

plt.title('ML Model Accuracy Comparison')

plt.xlabel('Machine Learning Model')

plt.ylabel('Accuracy')

plt.xticks(
    rotation=45,
    ha='right'
)

plt.ylim(0, 1)

plt.tight_layout()

plt.show()
    
    
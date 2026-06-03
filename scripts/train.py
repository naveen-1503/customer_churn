import mlflow

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

print("1. Bibliotek installert")

mlflow.set_tracking_uri(uri="http://host.docker.internal:5001")
mlflow.set_experiment("MLflow Quickstart")

print("2. Startet mlflow")
# Enable autologging for scikit-learn
mlflow.sklearn.autolog()

df = pd.read_excel('data/Telco_customer_churn.xlsx', engine='openpyxl')
print("3. Lastet ned dataen")

# Fjerner mellomrom i alle kolonnenavn og gjør dem lettere å jobbe med
df.columns = [c.replace(' ', '') for c in df.columns]

y = df['ChurnLabel'].apply(lambda x: 1 if x == 'Yes' else 0)

# 2. Definer X (Features) - dropp ID og selve målet
drop_cols = ['CustomerID', 'Count', 'Country', 'State', 'City', 'ZipCode', 
             'LatLong', 'Latitude', 'Longitude', 'ChurnLabel', 'ChurnValue', 
             'ChurnScore', 'CLTV', 'ChurnReason']

X = df.drop(columns=drop_cols)

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("4. Delt opp dataen")
with mlflow.start_run():
    classifier = RandomForestClassifier(class_weight='balanced', random_state=42)
    classifier.fit(X_train, y_train.values)
    y_pred = classifier.predict(X_test)

    test_accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("test_accuracy", test_accuracy)

    print(f'Test Accuracy {test_accuracy}')



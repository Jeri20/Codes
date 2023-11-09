import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score
import requests

# Function to load the dataset from a URL
def load_data_from_url(url):
    response = requests.get(url)
    data = pd.read_csv(pd.compat.StringIO(response.text))
    return data

# Replace 'your_url' with the actual URL to fetch the dataset
data = load_data_from_url('your_url')
# Split the dataset into features (X) and target (y)
X = data.drop('completed_course', axis=1)
y = data['completed_course']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = NearestNeighbors(n_neighbors=3)
model.fit(X_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Use the trained model to make course recommendations for a new user
new_user = pd.DataFrame({'user_id': ['new_user'], 'course_id': ['math_course']})
recommendations = model.kneighbors(new_user, n_neighbors=3, return_distance=False)
print(f"Recommended courses for new user: {recommendations}")

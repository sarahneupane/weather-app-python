import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Page Configuration
st.set_page_config(
    page_title="Iris Flower Predictor",
    page_icon="🌸",
    layout="wide"
)

# Title
st.title("🌸 Iris Flower Prediction App")
st.write("Predict the species of an Iris flower using Machine Learning.")

# Load Dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Sidebar
st.sidebar.header("Flower Measurements")

sepal_length = st.sidebar.slider(
    "Sepal Length (cm)",
    float(X["sepal length (cm)"].min()),
    float(X["sepal length (cm)"].max()),
    5.8
)

sepal_width = st.sidebar.slider(
    "Sepal Width (cm)",
    float(X["sepal width (cm)"].min()),
    float(X["sepal width (cm)"].max()),
    3.0
)

petal_length = st.sidebar.slider(
    "Petal Length (cm)",
    float(X["petal length (cm)"].min()),
    float(X["petal length (cm)"].max()),
    4.3
)

petal_width = st.sidebar.slider(
    "Petal Width (cm)",
    float(X["petal width (cm)"].min()),
    float(X["petal width (cm)"].max()),
    1.3
)

# Input Data
input_data = pd.DataFrame({
    "sepal length (cm)": [sepal_length],
    "sepal width (cm)": [sepal_width],
    "petal length (cm)": [petal_length],
    "petal width (cm)": [petal_width]
})

# Prediction
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

species = iris.target_names[prediction[0]]

# Display Input
st.subheader("Input Measurements")
st.dataframe(input_data)

# Prediction Result
st.subheader("Predicted Flower Species")

if species == "setosa":
    st.success("🌼 Iris Setosa")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
        width=300
    )

elif species == "versicolor":
    st.success("🌺 Iris Versicolor")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
        width=300
    )

else:
    st.success("🌷 Iris Virginica")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
        width=300
    )

# Probability Table
st.subheader("Prediction Probability")

prob_df = pd.DataFrame(
    prediction_proba,
    columns=iris.target_names
)

st.dataframe(prob_df)

# Dataset Preview
st.subheader("Iris Dataset Preview")
st.dataframe(X.head())

# Dataset Statistics
st.subheader("Dataset Statistics")
st.write(X.describe())

# Model Accuracy
accuracy = model.score(X, y)

st.subheader("Model Accuracy")
st.metric("Accuracy", f"{accuracy*100:.2f}%")

# Scatter Plot
st.subheader("Sepal Length vs Petal Length")

fig, ax = plt.subplots()

ax.scatter(
    X["sepal length (cm)"],
    X["petal length (cm)"]
)

ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Petal Length (cm)")
ax.set_title("Iris Dataset Scatter Plot")

st.pyplot(fig)

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit, Scikit-Learn and Iris Dataset")
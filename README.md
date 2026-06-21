# 🎓 GRE Admission Prediction using ANN

A Deep Learning Regression project that predicts a student's probability of admission to graduate school using academic and profile-related features such as GRE Score, TOEFL Score, CGPA, SOP, LOR, University Rating, and Research Experience.

The model is built using TensorFlow/Keras and deployed using Streamlit.

---

## 🚀 Project Overview

Graduate admissions depend on multiple factors. This project uses an Artificial Neural Network (ANN) to estimate the probability of admission based on a student's academic profile.

The model learns patterns from historical admission data and predicts the admission probability for new applicants.

---

## 📊 Dataset Features

The model uses the following inputs:

* GRE Score
* TOEFL Score
* University Rating
* SOP Strength
* LOR Strength
* CGPA
* Research Experience

### Target Variable

* Chance of Admit

---

## 🧠 Model Architecture

```text
Input Layer (7 Features)
        ↓
Dense Layer (7 Neurons, ReLU)
        ↓
Output Layer (1 Neuron, Linear)
```

### Training Configuration

* Optimizer: Adam
* Loss Function: Mean Squared Error (MSE)
* Epochs: 100
* Validation Split: 20%

---

## ⚙️ Data Preprocessing

* Removed unnecessary columns
* Feature scaling using StandardScaler
* Train-Test Split
* ANN training using TensorFlow/Keras

---

## 📈 Evaluation

The model is evaluated using:

* Mean Squared Error (MSE)
* R² Score

The ANN successfully learns the relationship between applicant profiles and admission probability.

---

## 🎨 Streamlit Application

The application allows users to:

* Enter academic details
* Predict admission probability
* Receive instant results

---

## 🖥️ Run Locally

```bash
git clone https://github.com/Rajeevydvv/GRE-Admission-ANN.git

cd GRE-Admission-ANN

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* Pandas
* NumPy
* Scikit-Learn
* Streamlit

---

## 📚 Learning Outcomes

* Artificial Neural Networks
* Deep Learning for Regression
* Data Preprocessing
* Feature Scaling
* TensorFlow/Keras Workflow
* Model Deployment with Streamlit

---

## 👨‍💻 Author

Rajeev Yadav

GitHub: https://github.com/Rajeevydvv

⭐ If you found this project useful, consider giving the repository a star.

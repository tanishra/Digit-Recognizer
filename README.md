#  Digit Recognizer using Decision Tree Classifier

This project is a machine learning-based digit recognizer that classifies hand-drawn digits (0–9) using a **Decision Tree Classifier**. The model is trained on grayscale images from the famous MNIST dataset and deployed via an interactive **Streamlit UI**.

---

## 📊 Dataset

- **Source**: [Kaggle - Digit Recognizer](https://www.kaggle.com/c/digit-recognizer/data)
- The dataset consists of 28x28 grayscale images flattened into 784 pixel columns. The training file (`train.csv`) contains:
- 785 columns: `label` (digit) + 784 pixel values (`pixel0` to `pixel783`)
- Labels are integers from `0` to `9`.

The test file (`test.csv`) contains:
- 784 pixel columns (no labels)

---

## ⚙️ Features

- Cleaned and preprocessed dataset.
- Built and trained a classification model (e.g., Logistic Regression, Random Forest, etc.).
- Evaluated model performance using accuracy, precision, recall, and F1-score.
- Streamlit-based UI for easy prediction.
- Simple and clean interface to input user health data and get predictions instantly.

---

## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/diabetic-predictor.git
cd diabetic-predictor
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3. Install dependencies
```bash
pip install -r streamlit_app/requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

---

# 🧠 Machine Learning Model

- **Model Used:** Logistic Regression
- **Testing Accuracy:** 78.57%

---

# 🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.



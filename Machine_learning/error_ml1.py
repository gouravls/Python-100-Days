import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from scipy.stats import ttest_ind

# Title
st.title("Understanding Type I and Type II Errors with Hypothesis Testing")

# Introduction
st.markdown("""
### 🔍 What are Type I and Type II Errors?

These concepts come from **hypothesis testing** and are closely related to **binary classification** problems.

Examples:
- True vs. False
- Spam vs. Not Spam
- Fraud vs. Legitimate

Let’s understand with a simple example:

Suppose you're a teacher trying to detect cheating in an exam.

- **H₀ (Null Hypothesis):** Nobody cheated  
- **H₁ (Alternative Hypothesis):** Somebody cheated

Now you make a decision:
- If you say someone cheated but they didn't → **Type I Error** (False Positive)
- If you say nobody cheated but someone actually did → **Type II Error** (False Negative)
""")

# Binary classification analogy
st.markdown("""
### 🤖 In Machine Learning Terms

| Reality \\ Prediction | Predicted Yes | Predicted No |
|----------------------|---------------|--------------|
| **Actually Yes**     | ✅ True Positive | ❌ False Negative (Type II) |
| **Actually No**      | ❌ False Positive (Type I) | ✅ True Negative |

We can now simulate this with a real-world dataset!
""")

# Hypothesis testing overview
st.subheader("🧪 Steps in Hypothesis Testing")
st.markdown("""
1. **State Hypotheses:**
   - H₀: Nothing is happening  
   - H₁: Something is happening
2. **Collect Data**
3. **Calculate Test Statistic (t-score or z-score)**
4. **Set Significance Level (α)**: Commonly 0.05
5. **Decision:**
   - If p-value ≤ α → Reject H₀  
   - If p-value > α → Fail to reject H₀
""")

# File upload
st.subheader("📂 Upload CSV File")
uploaded_file = st.file_uploader("Upload a CSV file with 'Score' and 'Method' columns", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    if 'Method' in data.columns and 'Score' in data.columns:
        st.success("✅ File uploaded successfully!")
        st.dataframe(data.head())

        # Extract scores
        old_score = data[data['Method'].str.lower() == 'old']['Score']
        new_score = data[data['Method'].str.lower() == 'new']['Score']

        # Perform t-test
        t_stat, p_value = ttest_ind(new_score, old_score, equal_var=False)
        alpha = 0.05

        # Display results
        st.subheader("📊 Hypothesis Test Results")
        st.write(f"**Average score (Old method):** {old_score.mean():.2f}")
        st.write(f"**Average score (New method):** {new_score.mean():.2f}")
        st.write(f"**T-statistic:** {t_stat:.2f}")
        st.write(f"**P-value:** {p_value:.4f}")

        # Interpretation
        if p_value < alpha:
            st.success("✅ Reject H₀: The new method **significantly improved** scores.")
        else:
            st.warning("❌ Fail to reject H₀: No strong evidence that the new method is better.")

        # Plotting the score distribution
        st.subheader("📈 Score Distribution by Method")
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=data, x='Method', y='Score', palette='Set2')
        st.pyplot(plt)
    else:
        st.error("❗ Columns 'Method' and 'Score' are required in the uploaded file.")
else:
    st.info("Please upload a dataset to continue.")


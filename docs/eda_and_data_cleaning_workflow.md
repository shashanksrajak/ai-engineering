# EDA, Data Cleaning, and Transformation: A Practical Workflow

This document addresses the critical questions of *when* to perform data cleaning and transformation in a machine learning project, and *how* to handle the training and test sets correctly to prevent data leakage.

## The Golden Rule: Fit on Train, Transform on Train & Test

The most important principle is to **never learn anything from your test set**. The test set should be a true simulation of new, unseen data. Therefore, any data transformation that *learns* parameters from the data (like the mean for imputation, or the min/max for scaling) must be learned **only** from the training data.

Here is a reliable, step-by-step workflow.

### Step 1: Initial, "Safe" Cleaning (Before EDA and Splitting)

You can and should perform a small amount of cleaning on the **entire dataset** *before* splitting it. These are "safe" operations because they don't learn from the data's distribution.

**What to do here:**

*   **Drop Truly Irrelevant Columns:** This is exactly where you would delete columns like `ID`, `customer_id`, or other unique identifiers that have no predictive value.
*   **Fix Obvious Data Entry Errors:** This includes things like stripping leading/trailing whitespace from string columns or correcting manually identified typos in categorical features (e.g., changing "N.Y." to "New York").
*   **Correct Data Types:** Ensure columns are in the correct format (e.g., converting a column of numbers stored as strings to a numeric type).

**Why is this safe?** These actions are based on the metadata and common sense, not on statistical properties (like mean, variance) of the data itself.

### Step 2: Exploratory Data Analysis (EDA)

Now, with your slightly cleaner dataset, you perform EDA on the **entire dataset**.

The goal here is **to understand and to plan, not to transform**. You are like a detective gathering clues. You should identify:

*   The extent and nature of **missing values**.
*   The presence and impact of **outliers**.
*   The distribution of your variables (e.g., are they skewed?).
*   The relationships between variables.

Based on this analysis, you will form a **plan of action** for the data wrangling and transformations you will perform in Step 4.

### Step 3: Split Your Data (Train/Test Split)

This is the most critical step. **Before you do any data wrangling that involves learning, you must split your data.**

```python
from sklearn.model_selection import train_test_split

# X contains your features, y is your target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

From this point forward, you will largely be working with `X_train` and `y_train`.

### Step 4: Preprocessing and Transformation (On the Training Set)

This is where you execute the plan you made during EDA. You will **fit** your preprocessing objects **only on the training data (`X_train`)**.

**What to do here:**

1.  **Imputation:** If you decide to fill missing values with the mean, that mean must be calculated **from the training set only**.
    ```python
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy='mean')
    X_train_imputed = imputer.fit_transform(X_train) # fit_transform here
    ```
2.  **Scaling:** If you scale your data, the scaler must learn its parameters (like min/max or mean/std) **from the training set only**.
    ```python
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_imputed) # fit_transform here
    ```
3.  **Outlier Handling:** If you remove outliers based on a statistical rule (e.g., values outside 1.5 * IQR), the IQR and quartiles must be calculated **from the training set only**.
4.  **Encoding:** For categorical variables, the encoder learns the categories **from the training set only**.

### Step 5: Applying the SAME Transformations to the Test Set

Now it's time to prepare your test set. You will apply the **exact same transformations** you did in Step 4, but you will **not** refit your preprocessing objects. You only use the `.transform()` method.

**What to do here:**

1.  **Imputation:** Use the *same imputer* (which learned the mean from the training data).
    ```python
    X_test_imputed = imputer.transform(X_test) # Note: .transform() ONLY
    ```
2.  **Scaling:** Use the *same scaler* (which learned the mean and std from the training data).
    ```python
    X_test_scaled = scaler.transform(X_test_imputed) # Note: .transform() ONLY
    ```

**Why this way?** Your test set represents new data your model will see in the future. You won't have the mean or standard deviation of future data. By fitting only on the training set, you are ensuring your entire model pipeline (including preprocessing) is tested on data it has genuinely never seen.

## Summary Workflow

| Phase | Action | On Which Data? | Purpose |
|---|---|---|---|
| **1. Initial Cleaning** | Drop ID cols, fix obvious errors | Entire Dataset | Basic hygiene, no "learning" |
| **2. EDA** | Analyze, visualize, plan transformations | Entire Dataset | Understand data, decide on strategy |
| **3. Split** | `train_test_split` | Entire Dataset | Create training and validation sets |
| **4. Preprocessing** | `fit_transform` (Impute, Scale, Encode) | **Training Set Only** | Learn transformation parameters |
| **5. Testing** | `transform` (using objects from Step 4) | **Test Set Only** | Apply learned transformations to unseen data |

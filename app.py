from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split


st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #f8fbff 0%, #ffffff 100%);
    }
    .title-block {
        padding: 1.2rem 1.4rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: white;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.18);
        margin-bottom: 1rem;
    }
    .small-note {
        color: #475569;
        font-size: 0.95rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = next(
    (path for path in [BASE_DIR / "titani.csv", BASE_DIR / "titanic.csv"] if path.exists()),
    None,
)
FEATURES = ["pclass", "sex", "age", "fare", "familysize", "embarked"]


@st.cache_data
def load_data(data_path: Path) -> pd.DataFrame:
    df = pd.read_csv(data_path)
    df.columns = df.columns.str.lower()
    df["age"] = df["age"].fillna(df["age"].median())
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
    df["fare"] = df["fare"].fillna(df["fare"].median())
    df = df.copy()
    df["familysize"] = df["sibsp"] + df["parch"] + 1
    df["sex"] = df["sex"].map({"female": 0, "male": 1})
    df["embarked"] = df["embarked"].map({"C": 0, "Q": 1, "S": 2})
    return df


@st.cache_resource
def train_model(df: pd.DataFrame):
    model_df = df[["pclass", "sex", "age", "fare", "familysize", "embarked", "survived"]].dropna()
    X = model_df[FEATURES]
    y = model_df["survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return model, accuracy, cm


if DATA_PATH is None:
    st.error("Could not find titani.csv or titanic.csv in this folder.")
    st.stop()


df = load_data(DATA_PATH)
model, accuracy, cm = train_model(df)

st.markdown(
    """
    <div class="title-block">
        <h1 style="margin:0; font-size: 2.3rem;">Titanic Survival Predictor</h1>
        <p style="margin:0.45rem 0 0 0; font-size: 1rem; opacity: 0.95;">
            Enter passenger details on the left, then click Predict to see the result on this webpage.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.05, 1.4], gap="large")

with left:
    st.subheader("Passenger Input")
    st.write("Choose the passenger details from the form below.")

    with st.form("prediction_form"):
        pclass = st.selectbox("Passenger Class", [1, 2, 3], index=2)
        sex = st.selectbox("Sex", ["female", "male"], index=0)
        age = st.number_input("Age", min_value=0.0, max_value=100.0, value=29.0, step=0.5)
        sibsp = st.number_input("Siblings / Spouses Aboard", min_value=0, max_value=10, value=0, step=1)
        parch = st.number_input("Parents / Children Aboard", min_value=0, max_value=10, value=0, step=1)
        fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0, step=0.5)
        embarked = st.selectbox("Embarked From", ["S", "C", "Q"], index=0)
        submitted = st.form_submit_button("Predict Survival")

    st.caption("The model uses these features: passenger class, sex, age, fare, family size, and embarkation point.")

    st.markdown("### What to enter")
    st.markdown(
        """
        - Passenger Class: 1, 2, or 3
        - Sex: female or male
        - Age: passenger age in years
        - Siblings/Spouses Aboard: number traveling with the passenger
        - Parents/Children Aboard: number traveling with the passenger
        - Fare: ticket price paid
        - Embarked From: S, C, or Q
        """
    )

with right:
    metric_left, metric_right = st.columns(2)
    metric_left.metric("Model Accuracy", f"{accuracy * 100:.2f}%")
    metric_right.metric("Passengers in Dataset", f"{len(df):,}")

    st.subheader("Data Preview")
    st.dataframe(df.head(), width="stretch")

    fig1, ax1 = plt.subplots(figsize=(6.5, 4))
    sns.countplot(x="survived", hue="survived", data=df, palette=["#ef4444", "#22c55e"], legend=False, ax=ax1)
    ax1.set_title("Survival Count")
    ax1.set_xlabel("Survived")
    ax1.set_ylabel("Count")
    st.pyplot(fig1, width="stretch")
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(6.5, 4))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Did Not Survive", "Survived"],
        yticklabels=["Did Not Survive", "Survived"],
        ax=ax2,
    )
    ax2.set_title("Confusion Matrix")
    ax2.set_xlabel("Predicted")
    ax2.set_ylabel("Actual")
    st.pyplot(fig2, width="stretch")
    plt.close(fig2)

if submitted:
    family_size = sibsp + parch + 1
    input_row = pd.DataFrame(
        [
            {
                "pclass": pclass,
                "sex": 0 if sex == "female" else 1,
                "age": age,
                "fare": fare,
                "familysize": family_size,
                "embarked": {"C": 0, "Q": 1, "S": 2}[embarked],
            }
        ]
    )

    prediction = int(model.predict(input_row)[0])
    probability = float(model.predict_proba(input_row)[0][1])

    st.markdown("---")
    st.subheader("Prediction Result")
    if prediction == 1:
        st.success(f"Predicted outcome: Survived")
    else:
        st.error(f"Predicted outcome: Did Not Survive")

    st.metric("Survival Probability", f"{probability * 100:.1f}%")
    st.write(f"Family size used by the model: {family_size}")
    st.caption("This is a machine learning prediction for learning purposes, not a real-life guarantee.")

st.markdown("---")
st.markdown(
    "<p class='small-note'>Run this app with Streamlit to open it in your browser.</p>",
    unsafe_allow_html=True,
)

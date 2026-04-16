# Titanic Survival Prediction

This project analyzes the Titanic dataset and builds a machine learning model to predict whether a passenger survived.

It includes:
- A complete Python data science pipeline (cleaning, EDA, feature engineering, model training, evaluation)
- A modern web dashboard built with Next.js for interactive prediction and visualization

## Project Objective

Understand and apply an end-to-end data science workflow on a real dataset:
- Data cleaning and preprocessing
- Data visualization
- Feature engineering
- Model building
- Evaluation using accuracy and confusion matrix

## Learning Outcomes and Skills

- Data cleaning and preprocessing with NumPy and Pandas
- Data visualization with Matplotlib and Seaborn
- Feature engineering
- Classification model building with Logistic Regression
- Model evaluation using Accuracy and Confusion Matrix

## Workflow Followed

1. Data collection: loaded Titanic dataset.
2. Data cleaning: handled missing values and removed unnecessary columns.
3. Data visualization: generated bar plots, histograms, and heatmaps.
4. Feature engineering: created familysize feature.
5. Model building: trained Logistic Regression.
6. Evaluation: measured accuracy and visualized confusion matrix.

## Features Used in Model

- pclass
- sex
- age
- fare
- familysize
- embarked

## Model and Result

- Model: Logistic Regression
- Typical accuracy: around 75% to 85% depending on split and preprocessing
- Evaluation: confusion matrix and classification report

## Repository Structure

```text
app/
  globals.css
  layout.tsx
  page.tsx
lib/
  titanic-model.ts
app.py
titanic_project.py
titani.csv
Titanic_Data_Science_Project_Report.docx
README.md
```

## How to Run (Python Pipeline)

1. Create and activate virtual environment.
2. Install dependencies from requirements.txt.
3. Run:

```bash
python titanic_project.py
```

This runs cleaning, feature engineering, visualizations, training, and evaluation.

## How to Run (Web App)

```bash
npm install
npm run dev
```

Then open:
- http://localhost:3000

## Submission Checklist

- Dataset used: present (titani.csv)
- Python code for preprocessing, visualization, and model building: present (titanic_project.py)
- Final report in Word format: present (Titanic_Data_Science_Project_Report.docx)
- Screenshots of graphs and confusion matrix: generate and include before final submission

## Notes

- The web dashboard is deployment-ready for Vercel.
- A repository-level vercel.json is included so Vercel uses Next.js build settings.

## License

MIT License

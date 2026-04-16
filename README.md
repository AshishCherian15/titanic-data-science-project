# Titanic Survival Prediction Dashboard

An end-to-end Data Science project built on the Titanic dataset, covering data cleaning, visualization, feature engineering, machine learning, and interactive prediction.

This repository contains two deliverables:
- Python ML pipeline for training and evaluation
- Next.js dashboard for interactive prediction and analytics-style visualization

## Overview

The goal of this project is to understand the full data science workflow using a real-world dataset and to present the results through both analysis code and a web interface.

## Key Features

- End-to-end Titanic preprocessing pipeline in Python
- Data visualization with bar charts, histograms, and correlation heatmaps
- Feature engineering with `familysize`
- Logistic Regression model for survival classification
- Evaluation using accuracy, classification report, and confusion matrix
- Web dashboard with interactive passenger input and survival prediction
- Vercel-ready project setup

## Tech Stack

### Data Science
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn

### Web Dashboard
- Next.js 15
- React 19
- TypeScript
- CSS

## Project Structure

```text
Titanic Project/
├── app/
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── lib/
│   └── titanic-model.ts
├── app.py
├── titanic_project.py
├── titani.csv
├── Titanic_Data_Science_Project_Report.docx
├── package.json
├── requirements.txt
├── vercel.json
└── README.md
```

## Data Science Workflow

1. Data Collection
2. Data Cleaning and Missing Value Handling
3. Exploratory Data Analysis and Visualization
4. Feature Engineering (`familysize`)
5. Model Training (Logistic Regression)
6. Model Evaluation (Accuracy + Confusion Matrix)

## Features Used for Prediction

- `pclass`
- `sex`
- `age`
- `fare`
- `familysize`
- `embarked`

## Model Performance

- Model: Logistic Regression
- Typical Accuracy: ~75% to ~85%
- Evaluation Metrics:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report

## Local Setup

### 1) Python Pipeline

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python titanic_project.py
```

### 2) Next.js Dashboard

```bash
npm install
npm run dev
```

Open:
- http://localhost:3000

## Submission Readiness

Required items and status:
- Dataset used: available ([titani.csv](titani.csv))
- Python preprocessing/model code: available ([titanic_project.py](titanic_project.py))
- Final report (Word): available ([Titanic_Data_Science_Project_Report.docx](Titanic_Data_Science_Project_Report.docx))
- Screenshots of graphs and confusion matrix: to be added before final submission

## Deployment

This project is configured for Vercel deployment.

```bash
npm run build
```

The repository includes [vercel.json](vercel.json) for framework build configuration.

## Author

Ashish Cherian

GitHub: https://github.com/AshishCherian15

## License

MIT License

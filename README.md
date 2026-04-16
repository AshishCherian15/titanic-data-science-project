<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1d4ed8,100:06b6d4&height=230&section=header&text=Titanic%20Survival%20Prediction&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Data%20Science%20Project%20%7C%20ML%20%2B%20Visualization%20%2B%20Web%20Dashboard&descAlignY=58)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&pause=1000&color=22D3EE&center=true&vCenter=true&width=900&lines=Machine+Learning+on+Titanic+Dataset;Data+Cleaning+%2B+Visualization+%2B+Prediction;Logistic+Regression+%7C+Confusion+Matrix+%7C+Dashboard)](https://git.io/typing-svg)

![Status](https://img.shields.io/badge/Project-Submission%20Ready-16a34a?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15-000000?style=for-the-badge&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=111827)
![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployment-Vercel-black?style=for-the-badge&logo=vercel)

</div>

---

## Overview

Welcome aboard the Titanic data journey. This project demonstrates an end-to-end data science workflow and a modern interactive web dashboard.

- Python pipeline for preprocessing, feature engineering, model training, and evaluation
- Next.js dashboard for interactive passenger-level survival prediction
- Visual analysis with multiple charts and confusion matrix interpretation

## Project Objective

Apply core data science concepts to a real-world dataset and produce meaningful predictive insights.

## What This Project Covers

- Data cleaning and preprocessing using NumPy and Pandas
- Data visualization using Matplotlib and Seaborn
- Feature engineering (`familysize`)
- Logistic Regression model development
- Model evaluation with accuracy, confusion matrix, and classification report
- Interactive web-based predictor UI

## Feature Highlights

- End-to-end Titanic ML workflow in Python
- Survival analysis charts (count, class, gender, age, fare)
- Correlation heatmap and confusion matrix
- Modern dashboard UI with rich styling and charts
- Vercel-ready deployment setup

## Tech Stack

### Data Science
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn

### Frontend Dashboard
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

## Model Inputs

- `pclass`
- `sex`
- `age`
- `fare`
- `familysize`
- `embarked`

## Model Performance

- Model: Logistic Regression
- Typical accuracy range: `~75% to ~85%`
- Evaluation metrics:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report

## Local Setup

### 1) Run Python Pipeline

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python titanic_project.py
```

### 2) Run Next.js Dashboard

```bash
npm install
npm run dev
```

Open in browser:
- http://localhost:3000

## Submission Checklist

- Dataset: available ([titani.csv](titani.csv))
- Python preprocessing + modeling code: available ([titanic_project.py](titanic_project.py))
- Final report (Word): available ([Titanic_Data_Science_Project_Report.docx](Titanic_Data_Science_Project_Report.docx))
- Graph/confusion-matrix screenshots: add before final submission

## Deployment

Build command:

```bash
npm run build
```

This repository includes [vercel.json](vercel.json) for Vercel framework configuration.

## Author

Ashish Cherian  
GitHub: https://github.com/AshishCherian15

## License

MIT License

---

<div align="center">

### Thanks for visiting this project 🚢

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:06b6d4,50:1d4ed8,100:0f172a&height=130&section=footer)

</div>

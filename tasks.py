                    AI-Powered Student Performance Prediction System
                                        │
                                        ▼
                           Student Performance Dataset
                               (student-mat.csv)
                                        │
                                        ▼
                          1. Data Preprocessing
        ┌──────────────────────────────────────────────────────┐
        │ • Load dataset                                       │
        │ • Inspect data                                       │
        │ • Check missing values & duplicates                  │
        │ • Remove G1 and G2 (avoid data leakage)              │
        │ • One-Hot Encode categorical features                │
        │ • Train-Test Split (80:20)                           │
        └──────────────────────────────────────────────────────┘
                                        │
                                        ▼
                   Processed Training & Testing Data
                                        │
                    ┌───────────────────┴───────────────────┐
                    ▼                                       ▼
          2. Exploratory Data Analysis             3. Model Training
        ┌─────────────────────────────┐      ┌────────────────────────────┐
        │ • Grade distribution        │      │ • Linear Regression        │
        │ • Study Time vs Grade       │      │ • Decision Tree            │
        │ • Failures vs Grade         │      │ • Random Forest            │
        │ • Absences vs Grade         │      │                            │
        │ • Parent Education vs Grade │      │ Compare using:             │
        │ • Correlation Heatmap       │      │ • MAE                      │
        └─────────────────────────────┘      │ • RMSE                     │
                    │                        │ • R² Score                 │
                    │                        ┴────────────────────────────┘
                    │                                       │
                    └──────────────┬────────────────────────┘
                                   │
                                   ▼
                         Select Best Performing Model
                                   │
                                   ▼
                    Feature Importance Analysis
        ┌──────────────────────────────────────────────────────┐
        │ • Extract feature importances (Random Forest)        │
        │ • Rank features                                      │
        │ • Plot Top 10 influential factors                    │
        └──────────────────────────────────────────────────────┘
                                   │
                                   ▼
                     Identify Factors Affecting
                         Academic Success
                                   │
                                   ▼
                      Save Best Model (best_model.pkl)
                                   │
                                   ▼
                        4. Prediction on New Student
        ┌──────────────────────────────────────────────────────┐
        │ Input New Student Information                        │
        │            │                                         │
        │            ▼                                         │
        │     Best Trained Model                               │
        │            │                                         │
        │            ▼                                         │
        │  Predicted Final Grade (G3)                          │
        └──────────────────────────────────────────────────────┘

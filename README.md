
# Student Performance Prediction

## Project Overview
This project aims to predict student performance in competitive exams based on key factors such as attendance, study hours, previous grades, extracurricular activities, and parental support. The prediction model can be used by educators to identify students who may require additional support or interventions, enabling a more personalized learning experience.

## Data and Features
The dataset used for this project contains the following features:

- **StudentID**: A unique identifier for each student.
- **AttendanceRate**: The percentage of classes attended by the student.
- **StudyHoursPerWeek**: The number of hours the student spends on studying each week.
- **PreviousGrade**: The student's previous performance or grade.
- **ExtracurricularActivities**: The level of involvement in extracurricular activities (on a scale of 0 to 10).
- **ParentalSupport**: Whether the student has parental support (Yes/No).

## Models Used
This project employs several machine learning models to predict student performance:

1. **Linear Regression**: A simple approach to model the relationship between the features and the final grade.
2. **Lasso Regression**: A regression technique with L1 regularization to prevent overfitting.
3. **Ridge Regression**: Similar to Lasso, but with L2 regularization.
4. **K-Neighbors Regressor**: A non-parametric model that makes predictions based on the k-nearest neighbors.
5. **Decision Tree Regressor**: A model that uses decision rules to predict the final grade.
6. **Random Forest Regressor**: An ensemble method that combines multiple decision trees for better performance.
7. **XGBRegressor**: A gradient boosting method that enhances predictive accuracy.
8. **AdaBoost Regressor**: A boosting method that improves weak learners' predictions by combining them.

## Streamlit Application
The project includes a Streamlit application that allows users to upload student data in CSV format for prediction. The app predicts the final grade based on the input features and displays the results.

### **How to Use**
1. **Upload CSV for Bulk Prediction**: Users can upload a CSV file containing student data, and the app will return predicted final grades for each student.
2. **Single Student Prediction**: Users can input individual student data, and the app will predict the final grade for that student

### Output Display
![Output Image 1](https://github.com/PankajDevikar/Student-Performance-Prediction/blob/main/img1.png)
![Output Image 1](https://github.com/PankajDevikar/Student-Performance-Prediction/blob/main/img2.png)  
![Output Image 1](https://github.com/PankajDevikar/Student-Performance-Prediction/blob/main/img3.png)
![Output Image 1](https://github.com/PankajDevikar/Student-Performance-Prediction/blob/main/img4.png)
![Output Image 1](https://github.com/PankajDevikar/Student-Performance-Prediction/blob/main/img5.png)

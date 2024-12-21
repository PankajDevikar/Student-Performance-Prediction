import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder

# Define the model file path (update with correct path)
MODEL_FILE = r'model\student_performance_model.pkl'  # Update with your correct model path

# Load the trained model
def load_model():
    try:
        model = joblib.load(MODEL_FILE)
        return model
    except FileNotFoundError:
        st.error(f"Model file '{MODEL_FILE}' not found. Please train and save the model.")
        return None

# Load the model when the app starts
model = load_model()

# Streamlit app interface
st.title("🎓 Student Performance Prediction App")
st.write("Predict student final grades based on attendance, study hours, previous grades, extracurricular activities, and parental support.")

# Function to preprocess the input data
def preprocess_data(data, model=None):
    # Handle 'ParentalSupport' (assuming one-hot encoding in the model)
    parental_support_dummies = pd.get_dummies(data['ParentalSupport'], prefix='ParentalSupport', drop_first=True)
    data = pd.concat([data, parental_support_dummies], axis=1)
    data = data.drop(columns=['ParentalSupport'])  # Drop the original column
    
    # Handle 'Gender' (assuming one-hot encoding in the model)
    gender_dummies = pd.get_dummies(data['Gender'], prefix='Gender', drop_first=True)
    data = pd.concat([data, gender_dummies], axis=1)
    data = data.drop(columns=['Gender'])
    
    # Ensure the columns match the model's training columns
    if model:
        model_columns = model.feature_names_in_  # Get the columns that the model expects
        missing_cols = [col for col in model_columns if col not in data.columns]
        for col in missing_cols:
            data[col] = 0  # Add missing columns with 0s (assuming they are all zeros for missing categories)

        # Ensure the order of columns is the same as the model's expected order
        data = data[model_columns]
    
    return data

# Sidebar navigation
menu = st.sidebar.radio("Choose an option:", ["Upload CSV for Bulk Prediction", "Predict for a Single Student"])

# Bulk Prediction
if menu == "Upload CSV for Bulk Prediction":
    st.header("📁 Upload CSV File")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load and display the uploaded data
        data = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data Preview:")
        st.dataframe(data)

        # Check for required columns
        required_columns = ['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade', 
                            'ExtracurricularActivities', 'ParentalSupport', 'Gender']
        if not all(col in data.columns for col in required_columns):
            st.error(f"The dataset must contain the following columns: {', '.join(required_columns)}.")
        else:
            # Preprocess the data to match the training data format
            input_data = data[required_columns].copy()

            # Apply preprocessing
            input_data = preprocess_data(input_data, model=model)

            # Ensure the model is loaded
            if model:
                try:
                    predictions = model.predict(input_data)
                    data['Predicted Final Grade'] = predictions
                    st.write("### Prediction Results:")
                    st.dataframe(data[['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade', 
                                       'ExtracurricularActivities', 'ParentalSupport', 'Gender', 'Predicted Final Grade']])
                except Exception as e:
                    st.error(f"Error during prediction: {e}")

# Single Student Prediction
elif menu == "Predict for a Single Student":
    st.header("🎓 Predict for a Single Student")

    # Input fields for student data
    attendance_rate = st.number_input("Attendance Rate (%)", min_value=0, max_value=100, step=1)
    study_hours = st.number_input("Study Hours Per Week", min_value=0, max_value=168, step=1)
    previous_grade = st.number_input("Previous Grade (%)", min_value=0, max_value=100, step=1)
    extracurricular_activities = st.slider("Extracurricular Activities (0 to 10)", min_value=0, max_value=10, step=1)
    parental_support = st.selectbox("Parental Support", ["Yes", "No"])
    gender = st.selectbox("Gender", ["Male", "Female"])  # Assuming gender is required

    # Create input DataFrame
    input_data = pd.DataFrame({
        'AttendanceRate': [attendance_rate],
        'StudyHoursPerWeek': [study_hours],
        'PreviousGrade': [previous_grade],
        'ExtracurricularActivities': [extracurricular_activities],
        'ParentalSupport': [parental_support],
        'Gender': [gender]
    })

    # Preprocess the input data to match the training data format
    input_data = preprocess_data(input_data, model=model)

    # Predict button
    if st.button("Predict Final Grade"):
        if model:
            try:
                # Make prediction
                prediction = model.predict(input_data)
                st.success(f"The predicted final grade is: {prediction[0]:.2f}")
            except Exception as e:
                st.error(f"Error during prediction: {e}")

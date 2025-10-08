import streamlit as st
import pandas as pd
import pickle
import os

PICKLE_FILE = r'C:\Users\nikhi\OneDrive\Desktop\IICET\Employee Salary Prediction Regression\employee_salary.pkl'

# Create and save default employee dataset
def create_default_dataset():
    data = {
        'EmployeeID': [101, 102, 103, 104],
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing'],
        'Salary': [50000, 60000, 55000, 52000]
    }
    df = pd.DataFrame(data)
    save_data(df)
    return df

# Load employee data from pickle
def load_data():
    if not os.path.exists(PICKLE_FILE):
        return create_default_dataset()
    with open(r'C:\Users\nikhi\OneDrive\Desktop\IICET\Employee Salary Prediction Regression\employee_salary.pkl', 'rb') as f:
        df = pickle.load(f)
    return df

# Save employee data to pickle
def save_data(df):
    with open(r'C:\Users\nikhi\OneDrive\Desktop\IICET\Employee Salary Prediction Regression\employee_salary.pkl', 'wb') as f:
        pickle.dump(df, f)

# Streamlit UI
def main():
    st.set_page_config(page_title="Employee Salary App")
    st.title("👨‍💼 Employee Salary Management")

    df = load_data()

    # Show employee data
    st.subheader("📊 Employee Data")
    st.dataframe(df)

    # Form to add a new employee
    st.subheader("➕ Add New Employee")
    with st.form("add_employee_form"):
        emp_id = st.number_input("Employee ID", min_value=1, step=1)
        name = st.text_input("Name")
        department = st.selectbox("Department", ['HR', 'IT', 'Finance', 'Marketing', 'Engineering'])
        salary = st.number_input("Salary", min_value=0, step=1000)
        submitted = st.form_submit_button("Add Employee")

        if submitted:
            new_emp = {
                "EmployeeID": emp_id,
                "Name": name,
                "Department": department,
                "Salary": salary
            }

            # Check if ID already exists
            if emp_id in df['EmployeeID'].values:
                st.warning("⚠️ Employee ID already exists. Please use a unique ID.")
            else:
                df = pd.concat([df, pd.DataFrame([new_emp])], ignore_index=True)
                save_data(df)
                st.success("✅ Employee added successfully!")
                st.rerun() # Refresh to show new data

if __name__ == "__main__":
    main()

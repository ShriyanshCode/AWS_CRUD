import streamlit as st
import requests
import pandas as pd
    
base_url = "<PLACE YOUR INVOKE URL HERE AFTER THE LAST STEP>"

def fetch_all_employees():
    response = requests.get(f"{base_url}employees")
    if response.status_code == 200:
        employees = response.json().get('employees', [])
        return employees
    else:
        st.error("Failed to fetch employees.")
        return []

def display_employee_table(employees):
    if employees:
        df = pd.DataFrame(employees)
        if {'employee_id', 'full_name', 'movie', 'age'}.issubset(df.columns):
            st.table(df[['employee_id', 'full_name', 'movie', 'age']])
        else:
            st.error("The expected columns are not in the API response.")
    else:
        st.write("No employees found.")

st.title("Employee Movie System")

# Fetch all employees to make a table
employees_data = fetch_all_employees()

# CRUD Operations
option = st.sidebar.selectbox("Select Operation", ("Create", "Read", "Update", "Delete"))

# Create an Employee 
if option == "Create":
    st.header("Add a New Employee")
    employee_id = st.text_input("Employee ID")
    full_name = st.text_input("Full Name")
    movie = st.text_input("Favorite Movie")
    age = st.number_input("Age", min_value=0)
    
    if st.button("Add Employee"):
        data = {
            "employee_id": employee_id,
            "full_name": full_name,
            "movie": movie,
            "age": age
        }
        response = requests.post(f"{base_url}employee", json=data)
        if response.status_code == 200:
            st.success("Employee added successfully!")
            employees_data = fetch_all_employees()  
        else:
            st.error("Failed to add employee.")

# Read an Employee
elif option == "Read":
    st.header("Get Employee Details")
    employee_id = st.text_input("Employee ID to Retrieve")
    
    if st.button("Get Employee"):
        response = requests.get(f"{base_url}employee", params={"employee_id": employee_id})
        if response.status_code == 200:
            employee = response.json()
            full_name = employee.get("full_name", "Unknown")
            movie = employee.get("movie", "Unknown")
            age = employee.get("age", "Unknown")

            # GET call but to put in a sentence
            st.write(f"The employee with ID {employee_id} is {full_name}, who loves the movie '{movie}', and is {age} years old.")
        else:
            st.error("Employee not found.")

# Update an Employee
elif option == "Update":
    st.header("Update Employee Information")
    employee_id = st.text_input("Employee ID to Update")
    update_key_select = st.selectbox("Field to Update", ("Full Name", "Movie", "Age"))
    update_key_mapping = {
        "Full Name": "full_name",
        "Movie": "movie",
        "Age": "age"
    }
    update_key = update_key_mapping[update_key_select]
    update_value = st.text_input(f"New {update_key_select}")
    
    if st.button("Update Employee"):
        data = {
            "employee_id": employee_id,
            "updateKey": update_key,
            "updateValue": update_value
        }
        response = requests.patch(f"{base_url}employee", json=data)
        if response.status_code == 200:
            st.success("Employee updated successfully!")
            employees_data = fetch_all_employees()  
        else:
            st.error("Failed to update employee.")

# Delete an Employee 
elif option == "Delete":
    st.header("Delete an Employee")
    employee_id = st.text_input("Employee ID to Delete")
    
    if st.button("Delete Employee"):
        data = {"employee_id": employee_id}
        response = requests.delete(f"{base_url}employee", json=data)
        if response.status_code == 200:
            st.success("Employee deleted successfully!")
            employees_data = fetch_all_employees()  
        else:
            st.error("Failed to delete employee.")

# Display All Employees
st.header("All Employees")
if employees_data:
    display_employee_table(employees_data)
else:
    st.write("No employees to display.")

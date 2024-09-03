import streamlit as st
import pandas as pd
from pathlib import Path

# Define the path to the tasks file
TASKS_DIR = Path("data")
TASKS_FILE = TASKS_DIR / "tasks.csv"

def save_task(task):
    # Ensure the directory exists
    if not TASKS_DIR.exists():
        TASKS_DIR.mkdir(parents=True, exist_ok=True)

    # Check if the tasks file exists
    if TASKS_FILE.exists():
        tasks_df = pd.read_csv(TASKS_FILE)
    else:
        
        tasks_df = pd.DataFrame(columns=["Title", "Description", "Date", "Time"])

    # Convert the task dictionary to a DataFrame and concatenate it with the existing tasks
    task_df = pd.DataFrame([task])
    tasks_df = pd.concat([tasks_df, task_df], ignore_index=True)

    # Save the updated tasks DataFrame back to the CSV file
    tasks_df.to_csv(TASKS_FILE, index=False)

def show_post_task_page():
    st.title("Post a Task")
    
    # Task input form
    with st.form(key='task_form'):
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Task Description")
        task_date = st.date_input("Preferred Date")
        task_time = st.time_input("Preferred Time")
        submit_button = st.form_submit_button(label='Post Task')
    
    # On form submission
    if submit_button:
        new_task = {
            "Title": task_title,
            "Description": task_description,
            "Date": task_date,
            "Time": task_time
        }
        save_task(new_task)

        st.success("Task posted successfully!")

if __name__ == "__main__":
    show_post_task_page()

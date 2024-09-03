import streamlit as st
import pandas as pd
from pathlib import Path

# Define paths to the CSV files
TASKS_FILE = Path("data/tasks.csv")
WRITE_FILE = Path("data/Time_to_Complete_Task.csv")

def show():
    st.title("Volunteer for a Task")
    
    if TASKS_FILE.exists():
        tasks_df = pd.read_csv(TASKS_FILE)
        
        if tasks_df.empty:
            st.write("No tasks available at the moment. Check back later!")
            return

        for index, task in tasks_df.iterrows():
            st.subheader(task['Title'])
            st.write(f"**Description:** {task['Description']}")
            st.write(f"**Date:** {task['Date']}")
            st.write(f"**Time:** {task['Time']}")
            
            hours_completed = st.text_input("Hours Completed", key=f"hours_{index}")
            task_volunter_name = st.text_input("Volunteer Name")
            if st.button(f"Volunteer for {task['Title']}", key=index):

                st.success(f"You have volunteered for {task['Title']}!")
                
                # Update tasks.csv by removing the volunteered task
                tasks_df.drop(index, inplace=True)
                tasks_df.to_csv(TASKS_FILE, index=False)
                
                # Record the hours completed in Time_to_Complete_Task.csv
                volunteer_record = pd.DataFrame({
                    'Title': [task['Title']],
                    'Volunteer': [task_volunter_name],  # Add a Volunteer field if needed
                    'Hours_Completed': [hours_completed],
                    'Date': [task['Date']],
                    'Time': [task['Time']]
                    
                })
                
                if WRITE_FILE.exists():
                    volunteer_record.to_csv(WRITE_FILE, mode='a', header=False, index=False)
                else:
                    volunteer_record.to_csv(WRITE_FILE, mode='w', header=True, index=False)
                    
    else:
        st.write("No tasks available at the moment. Check back later!")

show()

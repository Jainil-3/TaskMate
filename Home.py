import streamlit as st
from pages import *  # Import all page modules
import  pandas as pd
from pathlib import Path
from PIL import Image


completedTFile = Path("data/Time_to_Complete_Task.csv")

#To-Do 
def loadCompletedTasks():
    if completedTFile.exists():
        return pd.read_csv(completedTFile)
    
def calculate_completed_tasks(tasks_df):
    return len(tasks_df)


def calc_total_hours(task_df):
    return task_df['Hours_Completed'].sum()

def show():
    

    # App Configuration
    st.set_page_config(page_title="Neighborhood Helper", page_icon=":house:", layout="wide")


    # Load the banner image from your computer
    banner_image = Image.open("/Users/apple/Downloads/banner.jpg")

    # Resize the image to a specific height while maintaining the aspect ratio
    desired_height = 300  # Set the desired height for your banner
    aspect_ratio = banner_image.width / banner_image.height
    new_width = int(desired_height * aspect_ratio)
    banner_image = banner_image.resize((new_width, desired_height))
    # Display the banner-style image
    st.image(banner_image, caption='Welcome to Our Store', use_column_width=True)

    # Sidebar Navigation
    #st.title("Neighborhood Helper")
    st.title("Welcome to Neighborhood Helper")
    st.write("""
        **Neighborhood Helper** connects local residents who need help with tasks to volunteers in their area.
        Whether you need assistance or want to offer help, you're in the right place!
    """)
    tasks_df = loadCompletedTasks()
    total_comp_tasks = calculate_completed_tasks(tasks_df)
    volunteers = tasks_df['Volunteer']
    total_hours = calc_total_hours(tasks_df)
    st.metric(label="Completed Tasks", value=total_comp_tasks)
    st.metric(label="Total Hours Contributed", value=total_hours)
    st.subheader("Most Worked Volunteers")
    st.bar_chart(tasks_df['Volunteer'].value_counts().sort_index())

    # Optionally add a progress bar or other visuals
    st.progress(total_comp_tasks / len(tasks_df) if len(tasks_df) > 0 else 0)
    

if __name__ == "__main__":
    show()

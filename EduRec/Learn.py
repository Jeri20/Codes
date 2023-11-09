import streamlit as st
import pandas as pd

# API endpoint to fetch course data
COURSE_API = "https://your-api-url-here/courses"

# API endpoint to fetch user's completed courses
USER_API = "https://your-api-url-here/user/completed_courses"


@st.cache(allow_output_mutation=True)
def get_data(url):
    try:
        data = pd.read_json(url)
        return data
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()


def fetch_recommended_courses(user_id):
    # Fetch the list of user's completed courses
    completed_courses = get_data(f"{USER_API}/{user_id}")

    # Fetch all available courses
    all_courses = get_data(COURSE_API)

    # Remove the completed courses from the list of all courses
    recommended_courses = all_courses[~all_courses['id'].isin(completed_courses['id'])]

    return recommended_courses


st.title("Course Recommendation System")

# Replace 'your_user_id' with the actual user ID or obtain it through user authentication
user_id = 'your_user_id'
recommended_courses = fetch_recommended_courses(user_id)

if not recommended_courses.empty:
    st.subheader("Recommended Courses")
    for _, course in recommended_courses.iterrows():
        st.write(f"{course['name']} - Level

import streamlit as st

def main():
    st.title("Deployed Gemini Projects")

    # Brief details about the tech stack and app overview
    st.markdown(
        """
        **Tech Stack:**
        - Streamlit: Used for building interactive web applications with Python.
        - Google Gemini Pro: Leveraged for various functionalities like text-to-SQL, image analysis, etc.

        **Overview:**
        This Streamlit app showcases three projects developed using Google Gemini Pro. Each project has its unique features and functionalities, ranging from Applicant Tracking System (ATS) to image analysis and text-to-SQL conversion for student data analysis.
        """
    )

    # Project selection buttons
    selected_project = st.button("Smart ATS")
    if selected_project:
        show_smart_ats()

    selected_project = st.button("Calories Advisor App")
    if selected_project:
        show_calories_advisor_app()

    selected_project = st.button("Student Data Analyzer")
    if selected_project:
        show_student_data_analyzer()

    # Acknowledgments and "Hire Me" button
    st.text("Acknowledgments: Thanks to Krish Naik for his guidance and Streamlit for deployment.")

    # Blue-colored container for your information
    with st.container():
        st.markdown(
            """
            **Author Information:**
            - Author: M Sanjay Kumar Reddy
            - Email: sanjaykumarreddymanyam@gmail.com
            - Mobile: +61 7601003069
            
            **Copyright Notice:**
            © 2024 M Sanjay Kumar Reddy. All rights reserved.
            """
        )

        # "Hire Me" button
        if st.button("Click here to Hire me ❤️"):
            st.success("Thank you for considering me! Feel free to reach out at sanjaykumarreddymanyam@gmail.com")

def show_smart_ats():
    st.header("1. Smart ATS")
    st.subheader("Description:")
    st.write("Smart ATS is an Applicant Tracking System that collects job descriptions (JD) and resumes. It evaluates profile alignment, provides detailed analysis, ATS tracking, and percentage match.")
    st.subheader("GitHub Link:")
    st.markdown("[Smart ATS - GitHub](https://github.com/ManyamSanjayKumarReddy/Resume-ATS-using-Google-Gemini-Pro-)")
    st.subheader("Deployed Link:")
    st.markdown("[Smart ATS - Deployed](https://ats-tracker-sanjay.streamlit.app/)")
    st.subheader("Features:")
    st.write("- Profile Alignment Evaluation")
    st.write("- Detailed Analysis of Resumes")
    st.write("- ATS Tracking and Percentage Match Calculation")

def show_calories_advisor_app():
    st.header("2. Calories Advisor App")
    st.subheader("Description:")
    st.write("Calories Advisor App uses Google Gemini Pro Vision to analyze images and provide advice based on the content. It helps users understand the calories and ratio in the given image.")
    st.subheader("GitHub Link:")
    st.markdown("[Calories Advisor App - GitHub](https://github.com/ManyamSanjayKumarReddy/Health-Advisor-App-using-Google-Gemini-Pro-Vision)")
    st.subheader("Deployed Link:")
    st.markdown("[Calories Advisor App - Deployed](https://health-advisor-app-sanjay.streamlit.app/)")
    st.subheader("Features:")
    st.write("- Image Analysis for Calorie Estimation")
    st.write("- Advice Based on Image Content")

def show_student_data_analyzer():
    st.header("3. Student Data Analyzer Application")
    st.subheader("Description:")
    st.write("Student Data Analyzer Application uses Google Gemini Pro to convert user input into an SQL query. It retrieves data from the database and provides a proper output, making it easy to analyze student data.")
    st.subheader("GitHub Link:")
    st.markdown("[Student Data Analyzer - GitHub](https://github.com/ManyamSanjayKumarReddy/Google-Gemini-Pro-Text-to-SQL-LLM-Project)")
    st.subheader("Deployed Link:")
    st.markdown("[Student Data Analyzer - Deployed](https://gemini-data-analyzer-sanjay.streamlit.app/)")
    st.subheader("Features:")
    st.write("- Text to SQL Query Conversion")
    st.write("- Database Data Retrieval")
    st.write("- User Input Analysis")

if __name__ == "__main__":
    main()

import streamlit as st
import json
import os
import re

FILE_NAME = "students.json"


# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="StudentSphere 3D",
    page_icon="🌐",
    layout="wide"
)


# ==============================
# 3D STYLE DESIGN
# ==============================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at 20% 20%, #172554, transparent 30%),
    radial-gradient(circle at 80% 10%, #312e81, transparent 30%),
    linear-gradient(135deg, #020617, #0f172a, #111827);
}

/* Main 3D Header */

.hero {
    padding: 35px;
    text-align: center;
    border-radius: 30px;

    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.15),
        rgba(255,255,255,0.03)
    );

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 25px 60px rgba(0,0,0,0.5),
        inset 0 1px rgba(255,255,255,0.15);

    margin-bottom: 30px;
}

/* 3D Globe */

.globe {
    width: 120px;
    height: 120px;

    margin: auto;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #67e8f9,
            #2563eb 45%,
            #172554 75%,
            #020617
        );

    box-shadow:
        inset -20px -15px 30px rgba(0,0,0,0.6),
        0 0 35px rgba(59,130,246,0.6);

    animation: float 4s ease-in-out infinite;
}

@keyframes float {

    0%,100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-12px);
    }

}

/* Cards */

.card {

    padding: 25px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.12),
            rgba(255,255,255,0.03)
        );

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 18px 40px rgba(0,0,0,0.4),
        inset 0 1px rgba(255,255,255,0.1);

    text-align: center;

    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow:
        0 25px 50px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)


# ==============================
# FILE FUNCTIONS
# ==============================

def load_students():

    try:

        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:

        st.error("⚠️ Student data file is corrupted.")
        return []

    except Exception as e:

        st.error(f"⚠️ Error reading file: {e}")
        return []


def save_students(students):

    try:

        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

        return True

    except Exception as e:

        st.error(f"⚠️ Error saving data: {e}")
        return False


# ==============================
# EMAIL REGEX
# ==============================

def validate_email(email):

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.fullmatch(pattern, email) is not None


# ==============================
# HEADER
# ==============================

st.markdown("""
<div class="hero">

<div class="globe"></div>

<h1>🌐 StudentSphere 3D</h1>

<h3>Student Record Manager</h3>

<p>
A modern Python-based student management system
</p>

</div>
""", unsafe_allow_html=True)


students = load_students()


# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("🌐 StudentSphere")

menu = st.sidebar.radio(
    "Select Operation",
    [
        "🏠 Dashboard",
        "➕ Add Student",
        "📚 View Students",
        "🔍 Search Student",
        "🗑️ Delete Student"
    ]
)


# ==============================
# DASHBOARD
# ==============================

if menu == "🏠 Dashboard":

    st.title("📊 Student Dashboard")

    total_students = len(students)

    courses = set()

    for student in students:
        courses.add(student.get("course", ""))

    total_courses = len(courses)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="card">
            <h1>👨‍🎓</h1>
            <h2>{total_students}</h2>
            <p>Total Students</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="card">
            <h1>📚</h1>
            <h2>{total_courses}</h2>
            <p>Total Courses</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="card">
            <h1>🔐</h1>
            <h2>Secure</h2>
            <p>Validated Records</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("✨ Project Features")

    st.write("📧 Email Validation using Regex")
    st.write("💾 Student Data File Storage")
    st.write("📖 Read Student Records")
    st.write("🔍 Search Student")
    st.write("🗑️ Delete Student")
    st.write("⚠️ Exception Handling")


# ==============================
# ADD STUDENT
# ==============================

elif menu == "➕ Add Student":

    st.title("➕ Add New Student")

    with st.form("student_form"):

        student_id = st.text_input(
            "🆔 Student ID"
        )

        name = st.text_input(
            "👤 Student Name"

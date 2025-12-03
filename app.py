import streamlit as st
from db import (
    add_program,
    add_student,
    add_employer,
    add_internship,
    add_job,
    init_db,
)

# Initialize database on startup
init_db()

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="ESB Alumni & Student Journey", layout="wide")

# ---------- GLOBAL STYLES ----------
st.markdown(
    """
    <style>
    /* Bely Display Font */
    @font-face {
        font-family: 'belydisplayw00regular';
        src: url('belydisplayw00regulare.woff2') format('woff2'),
             url('belydisplayw00regulare.woff') format('woff'),
             url('belydisplayw00regulare.ttf') format('truetype'),
             url('belydisplayw00regulare.otf') format('opentype');
        font-weight: normal;
        font-style: normal;
    }

    /* GLOBAL COLORS
       Navy Blue: #001F3F
       Orange:    #FF6600
       Black:     #000000
       White:     #FFFFFF
    */

    body {
        background: #001F3F;
        color: #FFFFFF;              /* default text on navy */
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
        padding: 0;
    }
    .main {
        background: #001F3F;
        padding: 0;
    }

    /* Pacific Header */
    .pacific-header {
        background: #001F3F;
        color: #FFFFFF;
        padding: 12px 0;
        width: 100%;
        position: sticky;
        top: 0;
        z-index: 1000;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        border-bottom: 2px solid #FF6600;
    }
    .pacific-header-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .pacific-logo {
        font-size: 40px;
        font-weight: 400;
        letter-spacing: 0.15em;
        color: #FFFFFF;   /* white text on navy */
        font-family: 'belydisplayw00regular', Arial, Helvetica, sans-serif;
        text-transform: uppercase;
        line-height: 1.5;
    }
    .pacific-logo-img {
        max-height: 60px;
        width: auto;
        margin: 5px 15px 5px 0;
    }

    /* Center content area still on navy */
    .center-container {
        max-width: 980px;
        margin: 0 auto;
        padding: 20px;
        background: #001F3F;
    }

    /* Cards stay white with dark text */
    .card {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 30px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        color: #000000;
        border: 2px solid #FF6600;
    }
    .card h2, .card h3 {
        color: #FF6600;  /* orange headings on white card */
        font-family: 'belydisplayw00regular', Arial, Helvetica, sans-serif;
        font-weight: 700;
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 28px;
        line-height: 1.3;
    }
    .card h2.survey-title {
        font-family: 'belydisplayw00regular', Arial, Helvetica, sans-serif;
        font-weight: 700;
        font-size: 28px;
        color: #FF6600;
    }

    .subtitle {
        color: #000000;
        font-size: 14px;
        font-family: Arial, Helvetica, sans-serif;
        line-height: 1.5;
        margin-bottom: 15px;
    }

    /* Step chips row sits on navy background; chips themselves are white/colored */
    .step-chip-row {
        display: flex;
        gap: 0.5rem;
        margin-top: 0.75rem;
        flex-wrap: wrap;
    }
    .step-chip {
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 13px;
        border: 1px solid #001F3F;   /* navy border */
        color: #001F3F;              /* navy text */
        background: #FFFFFF;         /* white chip when inactive */
        font-family: Arial, Helvetica, sans-serif;
        font-weight: 400;
    }
    .step-chip.active {
        border-color: #FF6600;
        color: #FFFFFF;              /* white text on orange */
        background: #FF6600;
        font-weight: 500;
    }

    .section-title {
        font-size: 16px;
        font-weight: 600;
        text-transform: none;
        letter-spacing: 0;
        color: #FF6600;
        margin-bottom: 10px;
        font-family: Arial, Helvetica, sans-serif;
    }
    .hint {
        font-size: 13px;
        color: #333333;
        margin-bottom: 15px;
        font-family: Arial, Helvetica, sans-serif;
        line-height: 1.5;
    }

    /* Creator badge stays white/orange so it pops on navy */
    .creator-badge {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999;
        background: #FFFFFF;
        border: 2px solid #FF6600;
        border-radius: 8px;
        padding: 12px 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        gap: 12px;
        max-width: 250px;
    }
    .creator-photo {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #FF6600;
    }
    .creator-info {
        display: flex;
        flex-direction: column;
    }
    .creator-label {
        font-size: 11px;
        color: #666666;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-family: Arial, Helvetica, sans-serif;
    }
    .creator-name {
        font-size: 13px;
        color: #FF6600;
        font-weight: 600;
        margin-top: 2px;
        font-family: Arial, Helvetica, sans-serif;
    }

    /* Streamlit form elements */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        background-color: #FFFFFF;
        color: #000000;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 14px;
        border: 1px solid #FF6600;
        border-radius: 4px;
    }

    .stButton > button {
        background-color: #FF6600;
        color: #FFFFFF;
        border: none;
        border-radius: 4px;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 14px;
        font-weight: 500;
        padding: 10px 24px;
    }
    .stButton > button:hover {
        background-color: #FF8533;
    }

    label {
        color: #000000;
        font-weight: 500;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 14px;
    }
    .stRadio > label,
    .stCheckbox > label {
        color: #000000;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 14px;
    }

    body {
        background-color: #001F3F !important;
    }

    .stApp {
        background-color: #001F3F !important;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #001F3F !important;
    }

    [data-testid="stAppViewContainer"] > .main {
        background-color: #001F3F !important;
    }

    [data-testid="stSidebar"] {
        background-color: #001F3F !important;
    }

    /* ---------------------------
       1. TEXT ON NAVY BLUE = WHITE
       --------------------------- */
    .center-container,
    .center-container * {
        color: #FFFFFF !important;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] * {
        color: #FFFFFF !important;
    }

    .pacific-header,
    .pacific-header * {
        color: #FFFFFF !important;
    }

    /* ---------------------------
       2. CARD TEXT = BLACK
       --------------------------- */
    .card,
    .card * {
        color: #000000 !important;
    }

    /* Keep card headers orange */
    .card h1, .card h2, .card h3, .card h4 {
        color: #FF6600 !important;
    }
</style>
    """,
    unsafe_allow_html=True,
)

# ---------- STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 1

if "student" not in st.session_state:
    st.session_state.student = {}
if "internship" not in st.session_state:
    st.session_state.internship = None
if "has_internship" not in st.session_state:
    st.session_state.has_internship = "No"
if "job" not in st.session_state:
    st.session_state.job = None
if "has_job" not in st.session_state:
    st.session_state.has_job = "No"

step = st.session_state.step

# ---------- PACIFIC HEADER ----------
def render_pacific_header():
    """Render University of the Pacific header at the top with Bely font or logo image"""
    import os
    import base64
    
    # Check for uploaded logo in session state first
    logo_data = None
    logo_ext = "png"
    
    if "pacific_logo" in st.session_state and st.session_state.pacific_logo is not None:
        logo_data = st.session_state.pacific_logo
        # Try to determine extension from the uploaded file
        if hasattr(st.session_state.pacific_logo, 'type'):
            if 'png' in st.session_state.pacific_logo.type:
                logo_ext = "png"
            elif 'jpeg' in st.session_state.pacific_logo.type or 'jpg' in st.session_state.pacific_logo.type:
                logo_ext = "jpeg"
    
    # If no uploaded logo, check for logo image file (including seal/emblem variations)
    if logo_data is None:
        logo_paths = [
            "pacific_logo.png", "pacific_logo.jpg", 
            "logo.png", "logo.jpg", 
            "university_logo.png", "university_logo.jpg",
            "pacific_seal.png", "pacific_seal.jpg",
            "seal.png", "seal.jpg",
            "uop_logo.png", "uop_logo.jpg",
            "pacific_emblem.png", "pacific_emblem.jpg"
        ]
        logo_path = None
        
        for path in logo_paths:
            if os.path.exists(path):
                logo_path = path
                break
        
        if logo_path:
            try:
                with open(logo_path, "rb") as img_file:
                    logo_data = img_file.read()
                    logo_ext = os.path.splitext(logo_path)[1][1:].lower()
                    if logo_ext == "jpg":
                        logo_ext = "jpeg"
            except Exception:
                logo_data = None
    
    # Display the logo and text together
    logo_html = ""
    if logo_data:
        try:
            if isinstance(logo_data, bytes):
                img_base64 = base64.b64encode(logo_data).decode()
            else:
                # If it's a file-like object, read it
                logo_data.seek(0)
                img_base64 = base64.b64encode(logo_data.read()).decode()
            
            img_base64 = f"data:image/{logo_ext};base64,{img_base64}"
            logo_html = f'<img src="{img_base64}" class="pacific-logo-img" alt="University of the Pacific">'
        except Exception:
            pass
    
    # Always show text, with logo if available
    st.markdown(
        f"""
        <div class="pacific-header">
            <div class="pacific-header-content">
                {logo_html}
                <div class="pacific-logo">UNIVERSITY OF THE PACIFIC</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- HEADER ----------
def render_header():
    st.markdown(
        """
        <div class="center-container">
          <div class="card" style="margin-top: 18px;">
            <h2 class="survey-title">🎓 ESB Alumni & Student Journey Survey</h2>
            <p class="subtitle">
                A simple 3-step form to capture <b>student profile</b>, <b>internships</b>, and <b>first jobs</b>
                for the Eberhardt School of Business.
            </p>
            <div class="step-chip-row">
        """,
        unsafe_allow_html=True,
    )

    chips = [
        ("Step 1 · Student Info", 1),
        ("Step 2 · Internship", 2),
        ("Step 3 · Job Outcome", 3),
    ]
    chip_html = ""
    for label, num in chips:
        cls = "step-chip active" if num == st.session_state.step else "step-chip"
        chip_html += f'<div class="{cls}">{label}</div>'

    st.markdown(chip_html, unsafe_allow_html=True)

    st.markdown(
        """
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


render_pacific_header()
render_header()

# ---------- LOGO UPLOADER (in main content) ----------
def render_logo_uploader():
    """Display logo uploader in the main content area"""
    import os
    
    # Check if logo already exists
    logo_exists = False
    logo_paths = ["pacific_logo.png", "pacific_logo.jpg", "logo.png", "logo.jpg"]
    for path in logo_paths:
        if os.path.exists(path):
            logo_exists = True
            break
    
    # Also check session state
    if "pacific_logo" in st.session_state and st.session_state.pacific_logo is not None:
        logo_exists = True
    
    if not logo_exists:
        st.markdown('<div class="center-container">', unsafe_allow_html=True)
        with st.container():
            st.markdown("### 🏛️ Upload University of the Pacific Logo")
            st.markdown("Upload the University seal/logo to display it in the header.")
            logo_uploaded = st.file_uploader(
                "Choose a logo file (PNG, JPG, or JPEG)",
                type=['jpg', 'jpeg', 'png'],
                key="logo_uploader_main"
            )
            if logo_uploaded is not None:
                # Save to session state
                st.session_state.pacific_logo = logo_uploaded
                # Also save to disk for persistence
                try:
                    file_ext = logo_uploaded.name.split('.')[-1].lower()
                    filename = f"pacific_logo.{file_ext}"
                    with open(filename, "wb") as f:
                        f.write(logo_uploaded.getbuffer())
                    st.success("✅ Logo uploaded successfully! The page will refresh to show it in the header.")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error saving logo: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

render_logo_uploader()

# ---------- CREATOR BADGE ----------
def render_creator_badge():
    """Display creator photo and name in bottom right corner"""
    import os
    import base64
    
    # Your name
    creator_name = "Abhishek Jitendra Sonawane"
    
    # Check for uploaded photo in session state first
    photo_data = None
    photo_ext = "jpg"
    
    if "creator_photo" in st.session_state and st.session_state.creator_photo is not None:
        photo_data = st.session_state.creator_photo
        # Try to determine extension from the uploaded file
        if hasattr(st.session_state.creator_photo, 'type'):
            if 'png' in st.session_state.creator_photo.type:
                photo_ext = "png"
            elif 'jpeg' in st.session_state.creator_photo.type or 'jpg' in st.session_state.creator_photo.type:
                photo_ext = "jpeg"
    
    # If no uploaded photo, check for photo file in directory
    if photo_data is None:
        photo_paths = ["creator_photo.jpg", "creator_photo.png", "creator_photo.jpeg", "photo.jpg", "photo.png", "my_photo.jpg", "my_photo.png", "abhishek.jpg", "abhishek.png"]
        photo_path = None
        
        for path in photo_paths:
            if os.path.exists(path):
                photo_path = path
                break
        
        if photo_path:
            try:
                with open(photo_path, "rb") as img_file:
                    photo_data = img_file.read()
                    photo_ext = os.path.splitext(photo_path)[1][1:].lower()
                    if photo_ext == "jpg":
                        photo_ext = "jpeg"
            except Exception:
                photo_data = None
    
    # Display the badge with photo if available
    if photo_data:
        try:
            if isinstance(photo_data, bytes):
                img_base64 = base64.b64encode(photo_data).decode()
            else:
                # If it's a file-like object, read it
                photo_data.seek(0)
                img_base64 = base64.b64encode(photo_data.read()).decode()
            
            img_base64 = f"data:image/{photo_ext};base64,{img_base64}"
            
            st.markdown(
                f"""
                <div class="creator-badge">
                    <img src="{img_base64}" class="creator-photo" alt="Creator">
                    <div class="creator-info">
                        <div class="creator-label">Created by</div>
                        <div class="creator-name">{creator_name}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        except Exception as e:
            # Fallback if image can't be loaded
            st.markdown(
                f"""
                <div class="creator-badge">
                    <div class="creator-info">
                        <div class="creator-label">Created by</div>
                        <div class="creator-name">{creator_name}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        # Show uploader in main content area
        st.markdown('<div class="center-container">', unsafe_allow_html=True)
        with st.container():
            st.markdown("### 📸 Upload Your Photo")
            st.markdown("Upload your photo to display it in the creator badge (bottom right corner).")
            uploaded_file = st.file_uploader(
                "Choose a photo file (PNG, JPG, or JPEG)",
                type=['jpg', 'jpeg', 'png'],
                key="photo_uploader_main"
            )
            if uploaded_file is not None:
                # Save to session state
                st.session_state.creator_photo = uploaded_file
                # Also save to disk for persistence
                try:
                    with open("creator_photo.jpg", "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    st.success("✅ Photo uploaded successfully! The page will refresh to show it in the badge.")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error saving photo: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Fallback if photo doesn't exist - just show text
        st.markdown(
            f"""
            <div class="creator-badge">
                <div class="creator-info">
                    <div class="creator-label">Created by</div>
                    <div class="creator-name">{creator_name}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

render_creator_badge()

st.markdown('<div class="center-container">', unsafe_allow_html=True)

# =========================================================
# STEP 1 – STUDENT INFO
# =========================================================
if step == 1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Step 1 · About you</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hint">Select your current status and fill basic details. '
        'This will be your main identifier in the database.</p>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        status_type = st.radio(
            "Current status",
            ["Still studying (current student)", "Graduated (alumni)"],
        )
    with col2:
        student_id = st.text_input("University Student ID")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
    with col3:
        program_id = st.text_input("Program ID", placeholder="e.g., MSBA, MBA")
        program_name = st.text_input("Program Name", placeholder="MS in Business Analytics")
        entry_term = st.text_input("Entry Term", placeholder="e.g., Fall 2024")

    col4, col5 = st.columns(2)
    with col4:
        grad_term = st.text_input("Graduation Term (if graduated)", placeholder="e.g., Spring 2026")
        citizenship = st.text_input("Citizenship Country")
    with col5:
        email = st.text_input("Email (Pacific / personal)")
        linkedin = st.text_input("LinkedIn URL (optional)")

    status_value = "Current" if "Still" in status_type else "Alumni"

    st.markdown("</div>", unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        next_clicked = st.button("Next ➜")

    if next_clicked:
        errors = []
        if not student_id.strip():
            errors.append("Student ID is required.")
        if not first_name.strip():
            errors.append("First name is required.")
        if not last_name.strip():
            errors.append("Last name is required.")
        if not program_id.strip():
            errors.append("Program ID is required.")
        if not program_name.strip():
            errors.append("Program name is required.")

        if errors:
            st.error("Please fix the following before continuing:")
            for e in errors:
                st.write(f"• {e}")
        else:
            st.session_state.student = {
                "status_type": status_type,
                "status_value": status_value,
                "student_id": student_id.strip(),
                "first_name": first_name.strip(),
                "last_name": last_name.strip(),
                "program_id": program_id.strip(),
                "program_name": program_name.strip(),
                "entry_term": entry_term.strip(),
                "grad_term": grad_term.strip(),
                "citizenship": citizenship.strip(),
                "email": email.strip(),
                "linkedin": linkedin.strip(),
            }
            st.session_state.step = 2
            st.rerun()

# =========================================================
# STEP 2 – INTERNSHIP
# =========================================================
elif step == 2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Step 2 · Internship experience</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hint">If you did an internship during the program, select <b>Yes</b> and the form will open. '
        'If not, choose <b>No</b> and continue to the next step.</p>',
        unsafe_allow_html=True,
    )

    has_internship = st.radio(
        "Did you complete at least one internship during your program?",
        ["No", "Yes"],
        horizontal=True,
        index=0 if st.session_state.has_internship == "No" else 1,
    )

    internship_data = None
    if has_internship == "Yes":
        st.write("✅ You selected **Yes** – please fill your main internship details below.")

        ic1, ic2, ic3 = st.columns(3)
        with ic1:
            internship_id = st.text_input("Internship ID", placeholder="INT001")
            internship_title = st.text_input("Internship Title", placeholder="Data Analyst Intern")
        with ic2:
            internship_employer_id = st.text_input("Internship Employer ID", placeholder="EMP001")
            internship_employer_name = st.text_input("Internship Employer Name", placeholder="Company name")
            internship_mode = st.selectbox("Internship Mode", ["Virtual", "In-Person", "Hybrid"])
        with ic3:
            internship_city = st.text_input("City")
            internship_state = st.text_input("State")
            internship_country = st.text_input("Country")

        ic4, ic5, ic6 = st.columns(3)
        with ic4:
            internship_start = st.text_input("Start Date (YYYY-MM-DD)")
        with ic5:
            internship_end = st.text_input("End Date (YYYY-MM-DD)")
        with ic6:
            internship_related = st.checkbox("Related to your program of study?", value=True)

        internship_industry = st.text_input("Employer Industry (optional)", placeholder="e.g., Tech, Finance")
        internship_website = st.text_input("Employer Website (optional)")

        internship_data = {
            "internship_id": internship_id.strip(),
            "title": internship_title.strip(),
            "employer_id": internship_employer_id.strip(),
            "employer_name": internship_employer_name.strip(),
            "mode": internship_mode,
            "city": internship_city.strip(),
            "state": internship_state.strip(),
            "country": internship_country.strip(),
            "start_date": internship_start.strip(),
            "end_date": internship_end.strip(),
            "is_related": internship_related,
            "industry": internship_industry.strip(),
            "website": internship_website.strip(),
        }
    else:
        st.info("If you did **not** do an internship, leave this as No and click Next.")

    st.markdown("</div>", unsafe_allow_html=True)

    col_back, col_next = st.columns([1, 1])
    with col_back:
        back_clicked = st.button("⬅ Back", key="back_step2")
    with col_next:
        next_clicked = st.button("Next ➜", key="next_step2")

    if back_clicked:
        st.session_state.step = 1
        st.rerun()

    if next_clicked:
        st.session_state.has_internship = has_internship
        if has_internship == "Yes":
            errors = []
            if not internship_data["internship_id"]:
                errors.append("Internship ID is required.")
            if not internship_data["employer_id"]:
                errors.append("Internship Employer ID is required.")
            if not internship_data["title"]:
                errors.append("Internship Title is required.")

            if errors:
                st.error("Please fix the following before continuing:")
                for e in errors:
                    st.write(f"• {e}")
            else:
                st.session_state.internship = internship_data
                st.session_state.step = 3
                st.rerun()
        else:
            st.session_state.internship = None
            st.session_state.step = 3
            st.rerun()

# =========================================================
# STEP 3 – JOB
# =========================================================
elif step == 3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Step 3 · Job / first destination</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hint">If you already have a job offer or are working, select <b>Yes</b> '
        'and the job form will open. If not, you can submit without a job.</p>',
        unsafe_allow_html=True,
    )

    has_job = st.radio(
        "Do you currently have (or did you get) a job after this program?",
        ["No", "Yes"],
        horizontal=True,
        index=0 if st.session_state.has_job == "No" else 1,
    )

    job_data = None
    source_internship_id = None

    if has_job == "Yes":
        st.write("✅ You selected **Yes** – please enter your job details below.")

        jc1, jc2, jc3 = st.columns(3)
        with jc1:
            job_id = st.text_input("Job ID", placeholder="JOB001")
            job_title = st.text_input("Job Title", placeholder="Data Analyst")
        with jc2:
            job_employer_id = st.text_input("Job Employer ID", placeholder="EMP002 or same as internship")
            job_employer_name = st.text_input("Job Employer Name")
            job_level = st.text_input("Job Level", placeholder="Intern, Entry-Level, etc.")
        with jc3:
            job_type = st.text_input("Job Type / Role", placeholder="Business Analyst, Data Scientist, etc.")
            employment_status = st.text_input("Employment Status", value="Employed")

        jc4, jc5, jc6 = st.columns(3)
        with jc4:
            job_city = st.text_input("Job City")
        with jc5:
            job_state = st.text_input("Job State")
        with jc6:
            job_country = st.text_input("Job Country")

        jc7, jc8, jc9 = st.columns(3)
        with jc7:
            job_start = st.text_input("Job Start Date (YYYY-MM-DD)")
        with jc8:
            job_end = st.text_input("Job End Date (YYYY-MM-DD, blank if current)")
        with jc9:
            job_sequence = st.number_input(
                "Job Sequence (1 = first job)", min_value=1, value=1, step=1
            )

        if st.session_state.has_internship == "Yes" and st.session_state.internship:
            came_from_internship = st.checkbox("Did this job come from your internship?", value=False)
            if came_from_internship:
                default_int_id = st.session_state.internship["internship_id"]
                source_internship_id = st.text_input(
                    "Which internship ID does it come from?",
                    value=default_int_id,
                )
        else:
            source_internship_id = None

        job_industry = st.text_input("Job Employer Industry (optional)")
        job_website = st.text_input("Job Employer Website (optional)")

        job_data = {
            "job_id": job_id.strip(),
            "title": job_title.strip(),
            "employer_id": job_employer_id.strip(),
            "employer_name": job_employer_name.strip(),
            "job_level": job_level.strip(),
            "job_type": job_type.strip(),
            "employment_status": employment_status.strip(),
            "city": job_city.strip(),
            "state": job_state.strip(),
            "country": job_country.strip(),
            "start_date": job_start.strip(),
            "end_date": job_end.strip(),
            "sequence": int(job_sequence),
            "source_internship_id": source_internship_id.strip() if source_internship_id else None,
            "industry": job_industry.strip(),
            "website": job_website.strip(),
        }

    else:
        st.info("If you don’t have a job yet, keep this as No and submit your record.")

    st.markdown("</div>", unsafe_allow_html=True)

    col_back, col_submit = st.columns([1, 2])
    with col_back:
        back_clicked = st.button("⬅ Back", key="back_step3")
    with col_submit:
        submit_clicked = st.button("✅ Submit to ESB Database", key="submit_step3")

    if back_clicked:
        st.session_state.step = 2
        st.rerun()

    if submit_clicked:
        st.session_state.has_job = has_job
        st.session_state.job = job_data if has_job == "Yes" else None

        student = st.session_state.student
        internship = st.session_state.internship
        job = st.session_state.job

        errors = []

        required_student_fields = [
            "student_id", "first_name", "last_name", "program_id", "program_name"
        ]
        for f in required_student_fields:
            if not student.get(f):
                errors.append(f"Missing student field: {f} (go back to Step 1).")

        if st.session_state.has_internship == "Yes":
            if not internship:
                errors.append("Internship data missing (Step 2).")
            else:
                if not internship["internship_id"]:
                    errors.append("Internship ID is required.")
                if not internship["employer_id"]:
                    errors.append("Internship Employer ID is required.")
                if not internship["title"]:
                    errors.append("Internship Title is required.")

        if st.session_state.has_job == "Yes":
            if not job:
                errors.append("Job data missing (Step 3).")
            else:
                if not job["job_id"]:
                    errors.append("Job ID is required.")
                if not job["employer_id"]:
                    errors.append("Job Employer ID is required.")
                if not job["title"]:
                    errors.append("Job Title is required.")

        if errors:
            st.error("Please fix the following before we can save to the database:")
            for e in errors:
                st.write(f"• {e}")
        else:
            try:
                # 1) Program
                add_program(
                    student["program_id"],
                    student["program_name"],
                    None,
                    "Eberhardt School of Business",
                )

                # 2) Student
                add_student(
                    student["student_id"],
                    student["program_id"],
                    student["first_name"],
                    student["last_name"],
                    student["email"],
                    student["entry_term"],
                    student["grad_term"],
                    student["status_value"],
                    student["citizenship"],
                    student["linkedin"],
                )

                # 3) Internship (optional)
                if st.session_state.has_internship == "Yes" and internship:
                    add_employer(
                        internship["employer_id"],
                        internship["employer_name"],
                        internship["industry"],
                        internship["city"],
                        internship["state"],
                        internship["country"],
                        internship["website"],
                    )

                    add_internship(
                        internship["internship_id"],
                        student["student_id"],
                        internship["employer_id"],
                        internship["title"],
                        internship["mode"],
                        internship["city"],
                        internship["state"],
                        internship["country"],
                        internship["start_date"],
                        internship["end_date"],
                        internship["is_related"],
                    )

                # 4) Job (optional)
                if st.session_state.has_job == "Yes" and job:
                    add_employer(
                        job["employer_id"],
                        job["employer_name"],
                        job["industry"],
                        job["city"],
                        job["state"],
                        job["country"],
                        job["website"],
                    )

                    add_job(
                        job["job_id"],
                        student["student_id"],
                        job["employer_id"],
                        job["title"],
                        job["job_level"],
                        job["job_type"],
                        job["employment_status"],
                        job["city"],
                        job["state"],
                        job["country"],
                        job["start_date"],
                        job["end_date"] or None,
                        job["sequence"],
                        job["source_internship_id"],
                    )

                st.success("✅ Record saved to ESB database. Thank you for submitting your journey!")

                # Reset for a new entry
                st.session_state.step = 1
                st.session_state.student = {}
                st.session_state.internship = None
                st.session_state.has_internship = "No"
                st.session_state.job = None
                st.session_state.has_job = "No"

            except Exception as e:
                st.error(f"Something went wrong while saving: {e}")

st.markdown("</div>", unsafe_allow_html=True)

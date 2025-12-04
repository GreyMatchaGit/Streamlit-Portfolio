import streamlit as st
from streamlit_folium import st_folium
import folium

# --- 🎨 WARM THEME SETTINGS ---
# Terra Cotta & Gold Palette
HIGHLIGHT_COLOR = "#E07A5F"  # Terra Cotta (Used for Name, Emphasis)
MUTED_COLOR = "#F2CC8F"      # Warm Gold (Used for Tagline)
BORDER_COLOR = "#815355"     # Darker Brick (Used for Image Border)
TEXT_COLOR = "#b2b2b2"       # Standard Gray text
# ------------------------------

# Page Config
st.set_page_config(page_title="Karl Phoenix Portfolio")

# Custom CSS
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {{
        font-family: 'Inter', sans-serif;
    }}
</style>
""", unsafe_allow_html=True)

# Layout
col1, col_spacer, col2 = st.columns([1, 0.2, 3])

with col1:
    st.write("##")
    try:
        st.image("./assets/img/profile.jpg", width=600)
    except:
        st.warning("Image not found")
    try:
        with open("./assets/Cornilla_Karl_Phoenix_Resume.pdf", "rb") as resume_file:
            resume_data = resume_file.read()
    except:
        st.warning("Resume file not found")

    st.divider()

    st.link_button("GitHub", url="https://github.com/GreyMatchaGit", use_container_width=True)
    st.link_button("LinkedIn", url="https://www.linkedin.com/in/karl-phoenix/", use_container_width=True)

    st.divider()
    st.download_button(
      "Download Resume",
      data=resume_data,
      file_name="Cornilla_Karl_Phoenix_Resume.pdf",
      use_container_width=True,
      mime="application/pdf"
    )

with col2:
    # 1. Intro
    st.markdown(
        """<h3 style='text-align: left; margin-bottom: -15px; opacity: 0.8;'>Hi, my name is</h3>""",
        unsafe_allow_html=True
    )

    # 2. Name
    st.markdown(
        f"""<h1 style='text-align: left; color: {HIGHLIGHT_COLOR}; font-size: 3.5rem; font-weight: 800;'>Karl Phoenix.</h1>""",
        unsafe_allow_html=True
    )

    # 3. Tagline
    st.markdown(
        f"""<h1 style='text-align: left; color: {MUTED_COLOR}; font-size: 1.8rem; margin-top: -10px;'>I build software solutions to real-world problems.</h1>""",
        unsafe_allow_html=True
    )

    # 4. Bio
    st.markdown(
        f"""
        <h5 style='text-align: left; color: {TEXT_COLOR}; line-height: 1.6; margin-top: 20px;'>
            I am currently studying <span style='color: {HIGHLIGHT_COLOR}; font-weight: bold;'>Computer Science</span>
            at <span style='color: {HIGHLIGHT_COLOR}; font-weight: bold;'>Cebu Institute of Technology — University</span>.
            With a passion for coding and problem-solving, I aspire to create
            <span style='color: #ffffff; text-decoration: underline; text-decoration-color: {MUTED_COLOR};'>impactful software solutions</span>
            that address real-world challenges.
        </h5>
        """,
        unsafe_allow_html=True
    )

    # 5. Map
    CITU_Coords = [10.294540710724048, 123.88128577402682]
    CITU_CENTER = [10.29552627941116, 123.88028529422941]

    m = folium.Map(location=CITU_Coords, zoom_start=16, zoom_control=False, tiles="CartoDB Dark Matter")

    folium.Marker(
        location=CITU_CENTER,
        popup="Cebu Institute of Technology - University",
        icon=folium.Icon(color="white", prefix="fa", icon="university", icon_color=HIGHLIGHT_COLOR)
    ).add_to(m)

    folium.Circle(
        location=CITU_CENTER,
        radius=150,
        color=HIGHLIGHT_COLOR,
        fill=True,
        fill_color=MUTED_COLOR,
        fill_opacity=0.4,
        popup="CIT-U"
    ).add_to(m)

    st_folium(m, height=350, width="100%", returned_objects=[])

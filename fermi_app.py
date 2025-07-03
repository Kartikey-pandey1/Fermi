import streamlit as st

# Set page configuration
st.set_page_config(page_title="Fermi Semiconductors", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Digital Design", "Analog Design", "ASIC Design", "Projects", "Contact"])

# ---------------------- Homepage ----------------------
if page == "Home":
    st.title("Fermi Semiconductors")
    st.subheader("Designing the Future of Semiconductor Chips")

    st.markdown("""
    Welcome to **Fermi Semiconductors**, a chip design startup focused on building a AI Agent for digital VLSI design especially from layout to GDSII file generation using open-source tools involves integrating multiple components of the physical design flow and possibly layering AI/ML or LLM-based assistance on top. 

    🔹 We enable end-to-end chip design using open-source tools  
    🔹 Covering everything from RTL to GDSII  
    🔹 Supporting simulation, synthesis, layout, and verification  
    🔹 Built for VLSI Designers, students, and researchers in VLSI

    Explore our design flows using the sidebar menu!
    """)

# ---------------------- Digital Design ----------------------
elif page == "Digital Design":
    st.title("Digital Design Flow")
    st.markdown("Work in Progress: Upload Verilog, Simulate, Synthesize and Generate Layout.")

# ---------------------- Analog Design ----------------------
elif page == "Analog Design":
    st.title("Analog Design Flow")
    st.markdown("Work in Progress: Upload SPICE netlist, Simulate, Layout and Run DRC/LVS.")

# ---------------------- ASIC Design ----------------------
elif page == "ASIC Design":
    st.title("ASIC Design Flow")
    st.markdown("Work in Progress: Floorplan, Power Plan, Place & Route, Sign-Off.")

# ---------------------- Projects ----------------------
elif page == "Projects":
    st.title("Project Showcase")
    st.markdown("Add your completed chip projects, demo layouts, and GitHub links here.")

# ---------------------- Contact ----------------------
elif page == "Contact":
    st.title("Contact Us")
    st.markdown("""
    **Founder**: Kartikey Pandey  
    **Email**: [kartikeypandey8115@gmail.com](mailto:kartikeypandey8115@gmail.com)  
    **LinkedIn**: [fermi-semiconductors](https://www.linkedin.com/)  
    """)

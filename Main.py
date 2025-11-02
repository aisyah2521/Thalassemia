import streamlit as st

st.set_page_config(
    page_title="Student Survey"
)

visualise = st.Page('objective 1.py', title='Pencapaian Akademik', icon=":material/school:")

home = st.Page('objective 2.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
    {
        "Menu": ['Objective 1', 'Objective 2']
    }
)

pg.run()   

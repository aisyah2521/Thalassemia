import streamlit as st

st.set_page_config(
    page_title="Student Survey"
)

objective1 = st.Page('objective 1.py', title='Objective 1', icon=":material/school:")

objective2 = st.Page('objective 2.py', title='objective 2', default=True, icon=":material/home:")

objective3 = st.Page('objective 3.py', title='objective 3', icon=":material/home:")

pg = st.navigation(
    {
        "Menu": [objective1, objective2, objective3]
    }
)

pg.run()   

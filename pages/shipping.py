import streamlit as st
from streamlit_modal import Modal

import streamlit.components.v1 as components


modal = Modal(key="Demo Modal" ,title="")
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():

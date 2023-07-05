import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
import streamlit as st
import streamlit_modal as Modal
import streamlit.components.v1 as components
from google.cloud import firestore


orderan = Modal("Orderan")
open_modal = st.button("Input Orderan")
if open_modal:
    orderan.open()
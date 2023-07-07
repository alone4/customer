import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from streamlit_modal import Modal
from google.cloud import firestore
from input_order import *
st.set_page_config(initial_sidebar_state="collapsed") 
st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )
order = Modal(key="order modal", title="input order")
open_modal = st.button("Open")
if open_modal:
    order.open()
placeholder = st.empty()
if order.is_open():
    input_pertama()
st.title("Selamat datang apa yang anda perlukan hari ini?")
st.write("click di bawah untuk memilih memasukkan orderan")

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")
eks_choice = ["SAP","JNE"]
metode_choice = ["COD","TRANSFER"]
status_choice = ["Belum bayar (TF)", "Dikirim nanti", "Sudah bayar (tf)", "Pending", "Proses", "Cancel"]
cs_by = ["salma","alya","salsa","intan"]
# Create a reference to the Google post.
# Let's see what we got!
cs,shipping,admin = st.tabs(["cs","shipping","admin"])
with cs:
        orderan,wa_masuk,fu,ro,barang= st.tabs(["Orderan","WA masuk", "FU","RO","Barang"])
        with orderan:
            with st.container():
                col1,col2,col3,col4 = st.columns(4)
                with col1:
                    st.write("")
                with col2:
                    st.write("")
                with col3:
                    st.write("")
                with col4:
                    min_date = datetime.datetime(2023,7,5)
                    max_date = datetime.date(2023,12,31)

                    a_date = st.date_input("Pilih tanggal", (min_date, max_date))
            with st.container():
                col1,col2,col3 = st.columns(3)
                with col1:
                    st.subheader("Jumlah Orderan")
                    c1,c2,c3 = st.columns(3)
                    with c1:
                       st.write("")
                    with c2:
                        st.write("8")
                    with c3:
                        st.write("")
                with col2:
                    st.subheader("Belum Transfer")
                    c1,c2,c3 = st.columns(3)
                    with c1:
                       st.write("")
                    with c2:
                        st.write("8")
                    with c3:
                        st.write("")
                with col3:
                    st.subheader("Orderan Pending")
                    c1,c2,c3 = st.columns(3)
                    with c1:
                       st.write("")
                    with c2:
                        st.write("8")
                    with c3:
                        st.write("")
                 
                with st.container():
                    col1,col2,col3,col4 = st.columns(4)
                    with col1:
                        st.write("")
                    with col2:
                        st.write("")
                    with col3:
                        st.write("")
                    with col4:
                        min_date = datetime.datetime(2023,7,5)
                        max_date = datetime.date(2023,12,31)

                if st.button("masukkan orderan"):       
                    switch_page('input_order')
import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from google.cloud import firestore
def hides_side_page():
    st.set_page_config(initial_sidebar_state="collapsed") 
    st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )

hides_side_page()

st.title("masukkan orderan")
db = firestore.Client.from_service_account_json("firestore-key.json")
eks_choice = ["SAP","JNE"]
metode_choice = ["COD","TRANSFER"]
status_orderan_choice = [ "Pending", "Proses", "Cancel"]
status_pembayaran_choice = ["Belum bayar (TF)", "Sudah bayar (tf)"]
jenis_order_choice = ["fu tiktok","fu facebook","ro","fu cs"]
cs_by = ["salma","alya","salsa","intan"]

with st.form("Masukkan orderan"):
                                check = st.radio("apakah user sudah pernah membeli?", ("belum","sudah"))
                                if check == "belum":
                                    col1,col2= st.columns(2)
                                    with col1:
                                        nama = st.text_input("nama customer")
                                        nama_wa = st.text_input("nama wa customer")
                                        no_hp = st.number_input("no hp")
                                    with col2:
                                        alamat = st.text_area("alamat")
                                        kota = st.text_input("kota")
                                        metode_pem = st.selectbox("pilih pembayaran", metode_choice)
                                    if st.form_submit_button("submit"):
                                        doc_input = db.collection("customer").document(nama_wa)
                                        doc_input.set({
                                                "nama": nama,
                                                "no_telp": no_hp,
                                                "alamat": alamat,
                                                "kota": kota
                                            })
                                        switch_page('input_order_barang')
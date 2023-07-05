import pandas as pd
import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components
from google.cloud import firestore
import datetime

db = firestore.Client.from_service_account_json("firestore-key.json")
eks_choice = ["SAP","JNE"]
metode_choice = ["COD","TRANSFER"]
status_choice = ["Belum bayar (TF)", "Dikirim nanti", "Sudah bayar (tf)", "Pending", "Proses", "Cancel"]
cs_by = ["salma","alya","salsa","intan"]


st.title("Selamat datang apa yang anda perlukan hari ini?")

st.write("click di bawah untuk memilih memasukkan orderan")

modal = Modal(key="Demo Modal", title="")



open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
            with st.form("Masukkan orderan"):
                    check = st.radio("apakah customer sudah pernah membeli?", ("belum","sudah"))
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

                              
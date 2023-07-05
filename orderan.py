import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_modal import Modal
import streamlit.components.v1 as components
import datetime
st.title("Selamat datang apa yang anda perlukan hari ini?")

st.write("click di bawah untuk memilih memasukkan orderan")

import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

eks_choice = ["SAP","JNE"]
metode_choice = ["COD","TRANSFER"]
status_choice = ["belum bayar (TF)", "dikirim nanti", "sudah bayar (tf)", "pending"]
cs_by = ["salma","alya","salsa","intan"]
# Create a reference to the Google post.
# Let's see what we got!
modal = Modal(key="Demo Modal", title="")
open_modal = st.button("Open")
if open_modal:
    modal.open()



if modal.is_open():
    with modal.container():
            check = st.radio("apakah user sudah pernah membeli?", ("belum","sudah"))
            if check == "belum":
                col1,col2= st.columns(2)
                while True:
                    with col1:
                        nama = st.text_input("nama customer", key="nama")
                        nama_wa = st.text_input("nama wa customer", key="nama1")
                        no_hp = st.number_input("no hp", key="nama2")
                        barang = st.text_input("nama barang", key="nama3")
                        jumlah_barang = st.number_input("jumlah barang", key="nama4")
                    with col2:
                        alamat = st.text_area("alamat", key="nama5")
                        kota = st.text_input("kota", key="nama6")
                        ekspedisi = st.selectbox("pilih ekspedisi", eks_choice, key="nama7")
                        metode_pem = st.selectbox("pilih pembayaran", metode_choice, key="nama8")
                        status = st.selectbox("status orderan", status_choice, key="nama9")
                if status == "dikirim nanti":
                        harga_barang = st.number_input("harga barang awal", key="nama11")
                        diskon = st.number_input("jumlah diskon", key="nama12")
                        ongkir = st.number_input("biaya ongkir", key="nama13")
                        update_harga = harga_barang+ongkir-diskon
                        harga_akhir = st.number_input("harga akhir", key="nama14")
                        closing_by = st.selectbox("closing by", cs_by, key="nama15")
                        tanggal = datetime.datetime.now()
                elif status == "dikirim nanti":
                        harga_barang = st.number_input("harga barang awal")
                        diskon = st.number_input("jumlah diskon")
                        ongkir = st.number_input("biaya ongkir")
                        update_harga = harga_barang+ongkir-diskon
                        harga_akhir = st.number_input("harga akhir")
                        closing_by = st.selectbox("closing by", cs_by)
                if st.button("submit"):
                    doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                    doc_input.set({
                            "nama": nama,
                            "no_telp": no_hp,
                            "alamat": alamat,
                            "kota": kota,
                            "barang": barang,
                            "jumlah_barang": jumlah_barang,
                            "ekspedisi": ekspedisi,
                            "metode pembayaran": metode_pem,
                            "status": status,
                            "harga_barang": harga_barang,
                            "diskon": diskon,
                            "ongkir": ongkir,
                            "harga_akhir": harga_akhir,
                            "closing_by": closing_by
                })

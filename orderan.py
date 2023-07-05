import pandas as pd
import streamlit as st
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
status_choice = ["Belum bayar (TF)", "Dikirim nanti", "Sudah bayar (tf)", "Pending", "Proses", "Cancel"]
cs_by = ["salma","alya","salsa","intan"]
# Create a reference to the Google post.
# Let's see what we got!
modal = Modal(key="Demo Modal", title="")
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
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
                        peng = st.selectbox("apakah dikirim nanti?", ["ya","tidak"])
                        if metode_pem == "TRANSFER" and peng == "ya":
                            with modal.container():
                                with st.form("Masukkan orderan"):
                                    status = st.selectbox("status orderan", status_choice[0,1,2])
                                    ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                    barang = st.text_input("nama barang")
                                    jumlah_barang = st.number_input("jumlah barang")
                                    status = st.selectbox("status orderan", status_choice)
                                    harga_barang = st.number_input("harga barang awal")
                                    diskon = st.number_input("jumlah diskon")
                                    ongkir = st.number_input("biaya ongkir")
                                    update_harga = harga_barang+ongkir-diskon
                                    harga_akhir = st.number_input("harga akhir")
                                    closing_by = st.selectbox("closing by", cs_by)
                                    tanggal = datetime.datetime.now()

                if st.form_submit_button("submit"):
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
                    doc_input = db.collection("customer").document(nama_wa)
                    doc_input.set({
                            "nama": nama,
                            "no_telp": no_hp,
                            "alamat": alamat,
                            "kota": kota
                })

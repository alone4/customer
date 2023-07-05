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
            st.write("Masukkan orderan")
            check = st.radio("apakah user sudah pernah membeli?", ("belum","sudah"))
            if check == "belum":
                nama = st.text_input("nama customer")
                nama_wa = st.text_input("nama wa customer")
                no_hp = st.number_input("no hp")
                alamat = st.text_area("alamat")
                kota = st.text_input("kota")
                barang = st.text_input("nama barang")
                ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                metode_pem = st.selectbox("pilih pembayaran", metode_choice)
                status = st.selectbox("status orderan", status_choice)
                harga_barang = st.number_input("harga barang awal")
                diskon = st.number_input("jumlah diskon")
                ongkir = st.number_input("biaya ongkir")
                update_harga = harga_barang+ongkir-diskon
                harga_akhir = st.number_input("harga akhir")
                closing_by = st.selectbox("closing by", cs_by)
                tanggal = datetime.datetime.now()
                doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                doc_input.set({
                        "nama": nama,
                        "no_telp": no_hp,
                        "alamat": alamat,
                        "kota": kota,
                        "barang": barang,
                        "ekspedisi": ekspedisi,
                        "metode pembayaran": metode_pem,
                        "status": status,
                        "harga_barang": harga_barang,
                        "diskon": diskon,
                        "ongkir": ongkir,
                        "harga_akhir": harga_akhir,
                        "closing_by": closing_by
                })
            else:
                pilih = st.selectbox('pilih nama orang', l.get('data'))
                for x,y in p.get(pilih).items():
                    if y == p.get(pilih)["nama"]:
                        nama = st.text_input("nama customer", value=y, disabled=True)
                    if y == p.get(pilih)["no"]:
                        now = st.text_input("no hp", value=y, disabled=True)
                option = st.selectbox("Barang", l1)

            if st.button("Submit"):
                p["data3"] = {'nama': nama,'no': now, 'barang': option}
            st.write(p)
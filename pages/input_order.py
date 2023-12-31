import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from google.cloud import firestore


st.set_page_config(initial_sidebar_state="collapsed") 
st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )




st.title("masukkan orderan")
db = firestore.Client.from_service_account_json("firestore-key.json")
eks_choice = ["SAP","JNE"]
metode_choice = ["COD","TRANSFER"]
status_orderan_choice = [ "Pending", "Proses", "Cancel"]
status_pembayaran_choice = ["Belum bayar (TF)", "Sudah bayar (tf)"]
jenis_order_choice = ["fu tiktok","fu facebook","ro","fu cs"]
cs_by = ["salma","alya","salsa","intan"]

def input_pertama():
    global nama,nama_wa,metode_pem,kota,alamat,no_hp,pengiriman,placeholder
    placeholder = st.empty()
    with placeholder.container():
                                    
                                    check = st.radio("apakah user sudah pernah membeli?", ("belum","sudah"))
                                    if check == "belum":
                                        col1,col2= st.columns(2)
                                        with col1:
                                            nama = st.text_input("nama customer")
                                            nama_wa = st.text_input("nama wa customer")
                                            no_hp = st.number_input("no hp")
                                            pengiriman = st.selectbox("apakah pengiriman nanti?", ['ya','tidak'])
                                        with col2:
                                            alamat = st.text_area("alamat")
                                            kota = st.text_input("kota")
                                            metode_pem = st.selectbox("pilih pembayaran", metode_choice)
                                        if st.button(key="submit", label="submit") and no_hp != "":
                                            doc_input = db.collection("customer").document(nama_wa)
                                            doc_input.set({
                                                    "nama": nama,
                                                    "no_telp": no_hp,
                                                    "alamat": alamat,
                                                    "kota": kota
                                                })
                                            placeholder.empty()
def harga_b(x,z,y):
        return x-z-y
                                     
def input_kedua():                             

    if metode_pem == "TRANSFER" and pengiriman == "tidak":                                 
                                                                            col1,col2 = st.columns(2)
                                                                            with col1:
                                                                                jenis_order = st.selectbox(key=("asjldhajkfhajkfhakjdfshhjkladfshjkzdbfhjksr"),label="Jenis orderan", options=jenis_order_choice)
                                                                                status_orderan = "pending"
                                                                                status_pembayaran = st.selectbox("Apakah sudah membayar?", status_pembayaran_choice)
                                                                                closing_by = st.selectbox("closing by", cs_by)
                                                                            with col2:
                                                                                barang = st.text_input("nama barang")
                                                                                jumlah_barang = st.number_input("jumlah barang")
                                                                                harga_barang = st.number_input("harga barang awal")
                                                                            ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                                            diskon = st.number_input("jumlah diskon")
                                                                            ongkir = st.number_input("biaya ongkir")
                                                                            tanggal = datetime.datetime.now()
                                                                            if st.button(key="TRANSFER Later",label="submit")  :
                                                                                doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                                                                                doc_input.set({
                                                                                        "nama": nama,
                                                                                        "no_telp": no_hp,
                                                                                        "alamat": alamat,
                                                                                        "kota": kota,
                                                                                        "metode pembayaran": metode_pem,
                                                                                        "jenis_order": jenis_order,
                                                                                        "barang": barang,
                                                                                        "jumlah_barang": jumlah_barang,
                                                                                        "ekspedisi": ekspedisi,
                                                                                        "status_orderan": status_orderan,
                                                                                        "status_pembayaran": status_pembayaran,
                                                                                        "harga_barang": harga_barang,
                                                                                        "diskon": diskon,
                                                                                        "ongkir": ongkir,
                                                                                        "harga_akhir": harga_barang-diskon-ongkir,
                                                                                        "closing_by": closing_by
                                                                            })
                                                                            st.success("data berhasil di masukkan")
    elif metode_pem== "TRANSFER" and pengiriman == "ya":
                                                                        
                                                                            col1,col2 = st.columns(2)
                                                                            

                                                                            with col1:
                                                                                jenis_order = st.selectbox(key=("asjldhajkfhajkfhakjdfshhjkladfshjkzdbfhjksr"),label="Jenis orderan", options=jenis_order_choice)
                                                                                status_orderan = "pending"
                                                                                status_pembayaran = st.selectbox("Apakah sudah membayar?", status_pembayaran_choice)
                                                                                tanggal_pengiriman = st.date_input("kapan tanggal pengiriman", datetime.datetime.now())
                                                                                closing_by = st.selectbox("closing by", cs_by)
                                                                            with col2:
                                                                                barang = st.text_input("nama barang")
                                                                                jumlah_barang = st.number_input("jumlah barang")
                                                                                ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                                                harga_barang = st.number_input("harga barang awal")
                                                                            diskon = st.number_input("jumlah diskon")
                                                                            ongkir = st.number_input("biaya ongkir")
                                                                            tanggal = datetime.datetime.now()
                                                                            if st.button(key="TRANSFER NOW",label="submit")  :
                                                                                doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                                                                                doc_input.set({
                                                                                        "nama": nama,
                                                                                        "no_telp": no_hp,
                                                                                        "alamat": alamat,
                                                                                        "kota": kota,
                                                                                        "metode pembayaran": metode_pem,
                                                                                        "jenis_order": jenis_order,
                                                                                        "tanggal_pengiriman": f"{tanggal_pengiriman}",
                                                                                        "barang": barang,
                                                                                        "jumlah_barang": jumlah_barang,
                                                                                        "ekspedisi": ekspedisi,
                                                                                        "status_orderan": status_orderan,
                                                                                        "status_pembayaran": status_pembayaran,
                                                                                        "harga_barang": harga_barang,
                                                                                        "diskon": diskon,
                                                                                        "ongkir": ongkir,
                                                                                        "harga_akhir": harga_barang+ongkir-diskon,
                                                                                        "closing_by": closing_by
                                                                            })
                                                                                st.success("data berhasil di masukkan")
                                                                                switch_page("orderan")
    elif metode_pem== "COD" and pengiriman == "tidak":
                                                                    
                                                                            col1,col2 = st.columns(2)
                                                                            with col1:
                                                                                jenis_order = st.selectbox(key=("asjldhajkfhajkfhladfshjkzdbfhjksr"),label="Jenis orderan", options=jenis_order_choice)
                                                                                status_orderan = "pending"
                                                                                closing_by = st.selectbox("closing by", cs_by)
                                                                            with col2:
                                                                                barang = st.text_input("nama barang")
                                                                                jumlah_barang = st.number_input("jumlah barang")
                                                                                harga_barang = st.number_input("harga barang awal")
                                                                            ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                                            diskon = st.number_input("jumlah diskon")
                                                                            ongkir = st.number_input("biaya ongkir")
                                                                            tanggal = datetime.datetime.now()
                                                                            if st.button(key="COD NOW",label="submit")  :
                                                                                doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                                                                                doc_input.set({
                                                                                        "nama": nama,
                                                                                        "no_telp": no_hp,
                                                                                        "alamat": alamat,
                                                                                        "kota": kota,
                                                                                        "metode pembayaran": metode_pem,
                                                                                        "jenis_order": jenis_order,
                                                                                        "barang": barang,
                                                                                        "jumlah_barang": jumlah_barang,
                                                                                        "ekspedisi": ekspedisi,
                                                                                        "status_orderan": status_orderan,
                                                                                        "harga_barang": harga_barang,
                                                                                        "diskon": diskon,
                                                                                        "ongkir": ongkir,
                                                                                        "harga_akhir": harga_barang+ongkir-diskon,
                                                                                        "closing_by": closing_by
                                                                            })
                                                                                st.success("data berhasil di masukkan")
                                                                                switch_page("orderan")
    elif metode_pem== "COD" and pengiriman == "ya":
                                                                            col1,col2 = st.columns(2)
                                                                            with col1:
                                                                                jenis_order = st.selectbox(key=("streamlit kkontolllllllllllllll"),label="Jenis orderan", options=jenis_order_choice)
                                                                                status_orderan = "pending"
                                                                                tanggal_pengiriman = st.date_input("kapan tanggal pengiriman", datetime.datetime.now())
                                                                                closing_by = st.selectbox("closing by", cs_by)
                                                                            with col2:
                                                                                barang = st.text_input("nama barang")
                                                                                jumlah_barang = st.number_input("jumlah barang")
                                                                                harga_barang = st.number_input("harga barang awal")
                                                                            ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                                            diskon = st.number_input("jumlah diskon")
                                                                            ongkir = st.number_input("biaya ongkir")
                                                                            tanggal = datetime.datetime.now()
                                                                            if st.button(key="COD Later",label="submit")  :
                                                                                doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                                                                                doc_input.set({
                                                                                        "nama": nama,
                                                                                        "no_telp": no_hp,
                                                                                        "alamat": alamat,
                                                                                        "kota": kota,
                                                                                        "metode pembayaran": metode_pem,
                                                                                        "jenis_order": jenis_order,
                                                                                        "status_orderan": status_orderan,
                                                                                        "tanggal_pengiriman": f"{tanggal_pengiriman}",
                                                                                        "barang": barang,
                                                                                        "jumlah_barang": jumlah_barang,
                                                                                        "ekspedisi": ekspedisi,
                                                                                        "harga_barang": harga_barang,
                                                                                        "diskon": diskon,
                                                                                        "ongkir": ongkir,
                                                                                        "harga_akhir": harga_barang+ongkir-diskon,
                                                                                        "closing_by": closing_by
                                                                            })
                                                                                st.success("data berhasil di masukkan")
                                                                                switch_page("orderan")

input_pertama()

input_kedua()
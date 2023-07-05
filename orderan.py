import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components
from google.cloud import firestore

st.title("Selamat datang apa yang anda perlukan hari ini?")
st.write("click di bawah untuk memilih memasukkan orderan")
components.html("""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
  </body>
</html>""")
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


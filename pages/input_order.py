import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
import streamlit.components.v1 as components
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


def input_pertama():
        placeholder = st.empty()
        with placeholder.container():
            with st.form("Masukkan orderan"):
                                    global nama,nama_wa,no_hp,alamat,kota,metode_pem,peng
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
                                        peng = st.radio("apakah barang dikirim nanti?", ["ya","tidak"])
                                        if st.form_submit_button("submit"):
                                            doc_input = db.collection("customer").document(nama_wa)
                                            doc_input.set({
                                                    "nama": nama,
                                                    "no_telp": no_hp,
                                                    "alamat": alamat,
                                                    "kota": kota
                                                })
                                            placeholder.empty()

                                            input_kedua(metode_pem, peng)
                                            
def input_kedua(x,y):
                                            if x == "TRANSFER" and y == "tidak":
                                                            col1,col2 = st.columns(2)
                                                            with col1:
                                                                jenis_order = st.selectbox("Jenis orderan", jenis_order_choice)
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
                                                            harga_akhir = harga_barang+ongkir-diskon
                                                            tanggal = datetime.datetime.now()
                                                            if st.button("submit"):
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
                                                                        "harga_akhir": harga_akhir,
                                                                        "closing_by": closing_by
                                                            })
                                                                st.success("data berhasil di masukkan")
                                            elif x == "TRANSFER" and y == "ya":
                                                            col1,col2 = st.columns(2)
                                                            op = nama
                                                            with col1:
                                                                jenis_order = st.selectbox("Jenis orderan", jenis_order_choice)
                                                                status_orderan = "pending"
                                                                status_pembayaran = st.selectbox("Apakah sudah membayar?", status_pembayaran_choice)
                                                                tanggal_pengiriman = st.date_input("kapan tanggal pengiriman", datetime)
                                                                closing_by = st.selectbox("closing by", cs_by)
                                                            with col2:
                                                                barang = st.text_input("nama barang")
                                                                jumlah_barang = st.number_input("jumlah barang")
                                                                ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                                harga_barang = st.number_input("harga barang awal")
                                                            diskon = st.number_input("jumlah diskon")
                                                            ongkir = st.number_input("biaya ongkir")
                                                            harga_akhir = harga_barang+ongkir-diskon
                                                            tanggal = datetime.datetime.now()
                                                            if st.button("submit"):
                                                                doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                                                                doc_input.set({
                                                                        "nama": nama,
                                                                        "no_telp": no_hp,
                                                                        "alamat": alamat,
                                                                        "kota": kota,
                                                                        "metode pembayaran": metode_pem,
                                                                        "jenis_order": jenis_order,
                                                                        "tanggal_pengiriman": tanggal_pengiriman,
                                                                        "barang": barang,
                                                                        "jumlah_barang": jumlah_barang,
                                                                        "ekspedisi": ekspedisi,
                                                                        "status_orderan": status_orderan,
                                                                        "status_pembayaran": status_pembayaran,
                                                                        "harga_barang": harga_barang,
                                                                        "diskon": diskon,
                                                                        "ongkir": ongkir,
                                                                        "harga_akhir": harga_akhir,
                                                                        "closing_by": closing_by
                                                            })
                                                                st.success("data berhasil di masukkan")
                                            elif x == "COD" and y == "tidak":
                                                            col1,col2 = st.columns(2)
                                                            with col1:
                                                                jenis_order = st.selectbox("Jenis orderan", jenis_order_choice)
                                                                status_orderan = "pending"
                                                                closing_by = st.selectbox("closing by", cs_by)
                                                            with col2:
                                                                barang = st.text_input("nama barang")
                                                                jumlah_barang = st.number_input("jumlah barang")
                                                                harga_barang = st.number_input("harga barang awal")
                                                            ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                            diskon = st.number_input("jumlah diskon")
                                                            ongkir = st.number_input("biaya ongkir")
                                                            harga_akhir = harga_barang+ongkir-diskon
                                                            tanggal = datetime.datetime.now()
                                                            if st.button("submit"):
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
                                                                        "harga_akhir": harga_akhir,
                                                                        "closing_by": closing_by
                                                            })
                                                                st.success("data berhasil di masukkan")
                                            elif x == "COD" and y == "ya":
                                                            col1,col2 = st.columns(2)
                                                            op = nama
                                                            with col1:
                                                                jenis_order = st.selectbox("Jenis orderan", jenis_order_choice)
                                                                tanggal_pengiriman = st.date_input("kapan tanggal pengiriman", datetime)
                                                                status_orderan = "pending"
                                                                closing_by = st.selectbox("closing by", cs_by)
                                                            with col2:
                                                                barang = st.text_input("nama barang")
                                                                jumlah_barang = st.number_input("jumlah barang")
                                                                harga_barang = st.number_input("harga barang awal")
                                                            ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                            diskon = st.number_input("jumlah diskon")
                                                            ongkir = st.number_input("biaya ongkir")
                                                            harga_akhir = harga_barang+ongkir-diskon
                                                            tanggal = datetime.datetime.now()
                                                            if st.button("submit"):
                                                                doc_input = db.collection("customer").document(nama_wa).collection("orderan").document(f"{tanggal}")
                                                                doc_input.set({
                                                                        "nama": nama,
                                                                        "no_telp": no_hp,
                                                                        "alamat": alamat,
                                                                        "kota": kota,
                                                                        "metode pembayaran": metode_pem,
                                                                        "jenis_order": jenis_order,
                                                                        "status_orderan": status_orderan,
                                                                        "tanggal_pengiriman": tanggal_pengiriman,
                                                                        "barang": barang,
                                                                        "jumlah_barang": jumlah_barang,
                                                                        "ekspedisi": ekspedisi,
                                                                        "harga_barang": harga_barang,
                                                                        "diskon": diskon,
                                                                        "ongkir": ongkir,
                                                                        "harga_akhir": harga_akhir,
                                                                        "closing_by": closing_by
                                                            })
                                                                st.success("data berhasil di masukkan")
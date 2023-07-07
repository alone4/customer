import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
import streamlit.components.v1 as components
from streamlit_modal import Modal
from streamlit_extras.switch_page_button import switch_page
from google.cloud import firestore
def hides_side_page():
    st.set_page_config(initial_sidebar_state="collapsed") 
    st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )

hides_side_page()

modal = Modal(key="Demo Modal", title="order")
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")

        html_string = '''
        <h1>HTML string in RED</h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
        </script>
        '''
        components.html(html_string)

        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")

st.title("masukkan orderan")
db = firestore.Client.from_service_account_json("firestore-key.json")
eks_choice = ["SAP","JNE"]
metode_choice = ["COD","TRANSFER"]
status_orderan_choice = [ "Pending", "Proses", "Cancel"]
status_pembayaran_choice = ["Belum bayar (TF)", "Sudah bayar (tf)"]
jenis_order_choice = ["fu tiktok","fu facebook","ro","fu cs"]
cs_by = ["salma","alya","salsa","intan"]
placeholder = st.empty()
with placeholder.container():
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
                                        placeholder.empty()

peng = st.radio("apakah barang dikirim nanti?", ["ya","tidak"])
if metode_pem == "TRANSFER" and peng == "tidak":
                                                        col1,col2 = st.columns(2)
                                                        op = nama
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
                                                            switch_page("orderan")
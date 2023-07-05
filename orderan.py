import bootstrap4 as bs
import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import datetime
import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components
from google.cloud import firestore

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
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
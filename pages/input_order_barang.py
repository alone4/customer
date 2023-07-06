
import pandas as pd
import streamlit as st
from streamlit.web import bootstrap
import sys
import datetime
import streamlit.components.v1 as components
from google.cloud import firestore
from input_order import *
import os

hides_side_page()

peng = st.radio("apakah barang dikirim nanti?", ["ya","tidak"])
if metode_pem == "TRANSFER" and peng == "tidak":
                                                        op = nama
                                                        jenis_order = st.selectbox("Jenis orderan", jenis_order_choice)
                                                        barang = st.text_input("nama barang")
                                                        jumlah_barang = st.number_input("jumlah barang")
                                                        status_orderan = "pending"
                                                        status_pembayaran = st.selectbox("Apakah sudah membayar?", status_pembayaran_choice)
                                                        ekspedisi = st.selectbox("pilih ekspedisi", eks_choice)
                                                        harga_barang = st.number_input("harga barang awal")
                                                        diskon = st.number_input("jumlah diskon")
                                                        ongkir = st.number_input("biaya ongkir")
                                                        update_harga = harga_barang+ongkir-diskon
                                                        harga_akhir = st.number_input("harga akhir", value=update_harga)
                                                        closing_by = st.selectbox("closing by", cs_by)
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
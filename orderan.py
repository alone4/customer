import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_modal import Modal
import streamlit.components.v1 as components
import urllib3
st.title("Selamat datang apa yang anda perlukan hari ini?")

st.write("click di bawah untuk memilih memasukkan orderan")

import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

# Create a reference to the Google post.
doc_ref = db.collection("meina").document("customer")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
st.write(type(doc.to_dict()))
modal = Modal(key="Demo Modal", title="")
l1 = ["a","b","c"]
nama = ['endang','sukijem','larry']
no = ['00','01','02']
p = {}
l = {}
p2 = {}
o = 0
for x,y in zip(nama,no) :
    p[f"data{o}"]= {'nama': x,'no': y}
    o += 1
    l['data'] = p

open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
            st.write("Inside the form")
            check = st.radio("apakah user sudah pernah membeli?", ("belum","sudah"))
            if check == "belum":
                nama = st.text_input("nama customer")
                no_hp = st.text_input("no hp")
                option = st.selectbox("Barang", l1)
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
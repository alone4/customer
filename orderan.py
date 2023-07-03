import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_modal import Modal
import streamlit.components.v1 as components

st.title("Selamat datang apa yang anda perlukan hari ini?")

st.write("click di bawah untuk memilih memasukkan orderan")

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
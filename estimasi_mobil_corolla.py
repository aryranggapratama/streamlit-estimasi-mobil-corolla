import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_corolla.sav', 'rb'))

st.title('estimasi harga mobil corolla')

Age = st.number_input('input tahun mobil')
KM = st.number_input('input jarak tempuh atau kilometer mobil')
HP = st.number_input('input horse power atau tenaga mobil')
CC = st.number_input('input cc mobil')
Quarterly_Tax = st.number_input('input pajak mobil')
Weight = st.number_input('input berat mobil')

predict = ''

if st.button('estimasi harga'):
    predict = model.predict(
        [[Age,KM,HP,CC,Quarterly_Tax,Weight]]
    )
    st.write ('estimasi harga mobil corolla dalam dolar ($) : ', predict)
    st.write ('estimasi harga mobil corolla dalam IDR (Rp) :',predict*14673)
import streamlit as st
import joblib
import pandas as pd

# Fungsi untuk memuat model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Fungsi untuk melakukan prediksi
def predict_kelulusan(model, data):
    prediction = model.predict(data)
    return prediction

# Judul aplikasi
st.title("Prediksi Kelulusan Mahasiswa")

# Input dari pengguna
st.header("Masukkan Data Mahasiswa")

nama = st.text_input("Nama Mahasiswa")
nim = st.text_input("NIM Mahasiswa")

ip1 = st.number_input("IP Semester 1", min_value=0.0, max_value=4.0, step=0.01)
ip2 = st.number_input("IP Semester 2", min_value=0.0, max_value=4.0, step=0.01)
ip3 = st.number_input("IP Semester 3", min_value=0.0, max_value=4.0, step=0.01)
ip4 = st.number_input("IP Semester 4", min_value=0.0, max_value=4.0, step=0.01)
ip5 = st.number_input("IP Semester 5", min_value=0.0, max_value=4.0, step=0.01)
ip6 = st.number_input("IP Semester 6", min_value=0.0, max_value=4.0, step=0.01)
ipk = st.number_input("IPK", min_value=0.0, max_value=4.0, step=0.01)

# Tombol untuk prediksi
if st.button("Prediksi Kelulusan"):
    # Membuat DataFrame dari input pengguna
    input_data = pd.DataFrame([[ip1, ip2, ip3, ip4, ip5, ip6, ipk]],
                              columns=['IP Semester 1', 'IP Semester 2', 'IP Semester 3', 'IP Semester 4',
                                       'IP Semester 5', 'IP Semester 6', 'IPK'])
    
    # Memuat kembali model
    model_path = 'model3.pkl'
    model = load_model(model_path)
    
    # Melakukan prediksi
    prediction = predict_kelulusan(model, input_data)
    kelulusan = "tepat waktu" if prediction[0] == 0 else "tidak tepat waktu"
    
    # Menampilkan hasil prediksi
    st.success(f"Prediksi: {kelulusan}")

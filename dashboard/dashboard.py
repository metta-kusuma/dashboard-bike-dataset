import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# 1. Pengaturan Halaman & Judul
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
st.title('Dashboard Analisis Bike Sharing (2011-2012)')

# 2. Load Data
# Pastikan file main_data.csv berada di dalam folder 'dashboard'
df = pd.read_csv("dashboard/main_data.csv")

# Urutkan kategori waktu agar rapi di grafik
orderwaktu = ['Pagi', 'Siang', 'Sore', 'Malam']
df['katewaktu'] = pd.Categorical(df['katewaktu'], categories=orderwaktu, ordered=True)

# 3. Sidebar untuk Filter Interaktif
st.sidebar.header("Filter Eksplorasi")
tipe_hari = st.sidebar.selectbox(
    "Pilih Tipe Hari:", 
    ("Semua", "Working Day", "Weekend")
)

# Terapkan filter jika user tidak memilih "Semua"
if tipe_hari != "Semua":
    df = df[df['workingday_label'] == tipe_hari]

# 4. Menampilkan Metrik Angka
st.subheader("Ringkasan Data")
col1, col2 = st.columns(2)

with col1:
    total_pinjam = df['cnt'].sum()
    st.metric("Total Peminjaman Sepeda", value=f"{total_pinjam:,}")

with col2:
    rata_rata = round(df['cnt'].mean()) if not df.empty else 0
    st.metric("Rata-rata Peminjaman (per jam)", value=f"{rata_rata:,}")

st.markdown("---")

# 5. Visualisasi 1: Berdasarkan Musim (Menjawab Pertanyaan 1)
st.subheader('1. Total Penyewaan Berdasarkan Musim')
musimdf = df.groupby('season_label')['cnt'].sum().reset_index()

# Mengurutkan dari total penyewaan tertinggi ke terendah
musimdf = musimdf.sort_values(by='cnt', ascending=False)

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="season_label", 
    y="cnt", 
    hue="season_label", 
    data=musimdf, 
    palette="viridis",
    dodge=False,
    ax=ax1
)
if ax1.get_legend() is not None:
    ax1.get_legend().remove()
    
ax1.set_xlabel("Musim")
ax1.set_ylabel("Total Penyewaan")
st.pyplot(fig1)

# 6. Visualisasi 2: Berdasarkan Waktu/Clustering (Menjawab Pertanyaan 2)
st.subheader('2. Rata-rata Penyewaan Berdasarkan Waktu')
waktudf = df.groupby(['katewaktu', 'workingday_label'], observed=False)['cnt'].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x='katewaktu', 
    y='cnt', 
    hue='workingday_label', 
    data=waktudf, 
    palette="Set2", 
    ax=ax2
)
ax2.set_xlabel("Kategori Waktu (Clustering)")
ax2.set_ylabel("Rata-rata Penyewaan per Jam")
st.pyplot(fig2)
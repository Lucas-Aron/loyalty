import streamlit as st

class LoyaltyProgram:
    def __init__(self):
        self.customers = {}

    def register_customer(self, customer_id, name):
        if customer_id in self.customers:
            return f"Pelanggan dengan ID {customer_id} sudah terdaftar."
        else:
            self.customers[customer_id] = {"name": name, "points": 0}
            return f"Pelanggan {name} berhasil terdaftar."

    def add_points(self, customer_id, amount):
        if customer_id in self.customers:
            points_earned = int(amount // 10)  # Setiap 10 unit mata uang mendapatkan 1 poin
            self.customers[customer_id]["points"] += points_earned
            return f"{points_earned} poin telah ditambahkan ke pelanggan {self.customers[customer_id]['name']}."
        else:
            return "Pelanggan tidak ditemukan."

    def redeem_points(self, customer_id, points):
        if customer_id in self.customers:
            if self.customers[customer_id]["points"] >= points:
                self.customers[customer_id]["points"] -= points
                return f"{points} poin berhasil ditukarkan oleh {self.customers[customer_id]['name']}."
            else:
                return "Poin tidak mencukupi untuk ditukarkan."
        else:
            return "Pelanggan tidak ditemukan."

    def view_customer(self, customer_id):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            return f"Pelanggan: {customer['name']}, Poin: {customer['points']}"
        else:
            return "Pelanggan tidak ditemukan."

# Inisialisasi program
program = LoyaltyProgram()

# Antarmuka Streamlit
st.title("Sistem Loyalitas Pelanggan")

menu = st.sidebar.selectbox("Menu", ["Daftar Pelanggan", "Tambah Poin", "Tukarkan Poin", "Lihat Detail Pelanggan"])

if menu == "Daftar Pelanggan":
    st.header("Daftar Pelanggan Baru")
    customer_id = st.text_input("Masukkan ID Pelanggan:")
    name = st.text_input("Masukkan Nama Pelanggan:")
    if st.button("Daftar"):
        if customer_id and name:
            result = program.register_customer(customer_id, name)
            st.success(result)
        else:
            st.error("Harap masukkan ID dan nama pelanggan.")

elif menu == "Tambah Poin":
    st.header("Tambah Poin ke Pelanggan")
    customer_id = st.text_input("Masukkan ID Pelanggan:")
    amount = st.number_input("Masukkan Jumlah Pembelian:", min_value=0.0, step=0.1)
    if st.button("Tambah Poin"):
        if customer_id:
            result = program.add_points(customer_id, amount)
            st.success(result)
        else:
            st.error("Harap masukkan ID pelanggan.")

elif menu == "Tukarkan Poin":
    st.header("Tukarkan Poin")
    customer_id = st.text_input("Masukkan ID Pelanggan:")
    points = st.number_input("Masukkan Jumlah Poin untuk Ditukarkan:", min_value=0, step=1)
    if st.button("Tukarkan"):
        if customer_id:
            result = program.redeem_points(customer_id, points)
            st.success(result)
        else:
            st.error("Harap masukkan ID pelanggan.")

elif menu == "Lihat Detail Pelanggan":
    st.header("Lihat Detail Pelanggan")
    customer_id = st.text_input("Masukkan ID Pelanggan:")
    if st.button("Lihat"):
        if customer_id:
            result = program.view_customer(customer_id)
            st.info(result)
        else:
            st.error("Harap masukkan ID pelanggan.")

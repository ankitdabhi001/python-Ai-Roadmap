import streamlit as st
import base64

# Helper functions for encoding/decoding passwords
def encrypt_password(password):
    return base64.b64encode(password.encode()).decode()

def decrypt_password(encoded):
    return base64.b64decode(encoded.encode()).decode()

# Initial demo vault (dictionary of tuples)
vault = {
    "gmail": ("ankit@gmail.com", encrypt_password("mysecure123")),
    "github": ("ankitGH", encrypt_password("gitpass456"))
}

st.title("🔐 Password Vault v1.0")

# Lookup credentials
st.subheader("🔍 Get Stored Credentials")
platform = st.text_input("Enter platform name (e.g., gmail)")
if st.button("Get Credentials"):
    if platform in vault:
        username, enc_password = vault[platform]
        password = decrypt_password(enc_password)
        st.success(f"Username: {username}\nPassword: {password}")
    else:
        st.error("Platform not found in vault.")

st.markdown("---")

# Add new credentials
st.subheader("➕ Add New Credentials")
new_platform = st.text_input("New Platform", key="p1")
new_username = st.text_input("Username", key="u1")
new_password = st.text_input("Password", type="password", key="pw1")

if st.button("Add Credentials"):
    if new_platform and new_username and new_password:
        vault[new_platform] = (new_username, encrypt_password(new_password))
        st.success(f"Credentials added for {new_platform}!")
    else:
        st.error("Please fill in all fields.")

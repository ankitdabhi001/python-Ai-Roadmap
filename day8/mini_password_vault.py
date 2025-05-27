import streamlit as st

# Using session state to persist vault data across interactions
if "vault" not in st.session_state:
    st.session_state.vault = {
        "gmail": ("ankit@gmail.com", "mysecure123"),
        "github": ("ankitGH", "gitpass456")
    }

st.title("🔐 Password Vault (Demo)")

# Section: Retrieve credentials
st.subheader("Get Credentials")
platform = st.text_input("Enter platform name to retrieve")
if st.button("Get Credentials"):
    if platform in st.session_state.vault:
        username, password = st.session_state.vault[platform]
        st.success(f"Username: {username}\nPassword: {password}")
    else:
        st.error("Platform not found in vault.")

st.markdown("---")

# Section: Add new credentials
st.subheader("Add New Credentials")
new_platform = st.text_input("Platform name (e.g., twitter)", key="new_platform")
new_username = st.text_input("Username", key="new_username")
new_password = st.text_input("Password", type="password", key="new_password")

if st.button("Add Credentials"):
    if new_platform and new_username and new_password:
        st.session_state.vault[new_platform] = (new_username, new_password)
        st.success(f"Credentials added for {new_platform}!")
        # Clear inputs after adding
        st.experimental_rerun()
    else:
        st.error("Please fill in all fields to add credentials.")

import streamlit as st
from PIL import Image
PAGE_CONFIG={"page_title":"Colab APP", "page_icon":":smiley:", "layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)

def main():
  st.title("Streamlit app")
  st.subheader("Colab")

  menu=["Home", "About"]
  choice = st.sidebar.selectbox("Menu",menu)
  if choice == "Home":
    st.subheader("st for colab")

if __name__ == "__main__":
  main()
from dataclasses import dataclass
import streamlit as st
from db.models import Product, conn
from PIL import Image
from models.predictions import prediction, post_api, preprocessing


@dataclass 
class Page:
    config = st.set_page_config(layout="wide")
    side_selection = ""
    selling_page_title = "Vos produits"
    col0, col1, col2 = st.columns([0.1,3,6])
    sess = conn()

    def sidebar_options(self):
        st.sidebar.subheader('Welcom to your account')
        self.side_selection = st.sidebar.selectbox('What do you want to do', ['Sell products', 'Your products'])

    def display_page(self):
        if self.side_selection == "Sell products":
            st.markdown("<h1 style='text-align: center; color: yellow;'> Sell your products </h1>", unsafe_allow_html=True)
            name = st.text_input('Product name')
            description = st.text_input('Product description')
            image = st.file_uploader("Product image")
            clic_sell = st.button("Send your product")
            if clic_sell:
                img = Image.open(image)
                img_path = f"upload_image/{image.name}"
                img.save(img_path, format="JPEG")
                with st.spinner('Wait for it...'):
                    # description_process, image_process = preprocessing(description, image)
                    # category = post_api(description_process, image_process)
                    category = prediction(description, image )
                    Product(name=name, description=description, image=image.name, category=category).save_to_db()
                st.success('Done! Product sent successfully')
                
        if self.side_selection == "Your products":
            products = self.sess.query(Product).all()[::-1]
            self.col1.markdown("<h1 style='text-align: center; color: yellow; padding-bottom:100px; '>Product name </h1>", unsafe_allow_html=True)
            self.col2.markdown("<h1 style='text-align: center; color: yellow; padding-bottom:100px; '>Product description </h1>", unsafe_allow_html=True)
            for product in products:
                with self.col1:
                    st.markdown(f"<h3 style='text-align: left; color: yellow; padding-bottom: 30px; padding-top: 25px;'> {product.name} </h3>", unsafe_allow_html=True)
                    st.image(f'./models/Images/{product.image}', width=250, caption=f"{product.category}")
                    # st.write('------------------------')
                with self.col2:
                    st.markdown(f"<p style='text-align: left; color: red; padding-top:100px; '> {product.description} </p>", unsafe_allow_html=True)
                    st.markdown("<h1 style='text-align: center; color: yellow; height:250px; '> </h1>", unsafe_allow_html=True)
                    # st.write('------------------------')

    def run_page(self):
        self.sidebar_options()
        self.display_page()

page = Page()
page.run_page()
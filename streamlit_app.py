import streamlit as st
from datetime import datetime
import pandas as pd
import google.generativeai as genai
#import pathlib
import textwrap
#from typing import Dict

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "cart" not in st.session_state:
    st.session_state.cart = []
if "payment_mode" not in st.session_state:
    st.session_state.payment_mode = None
# Fortune session state
for k in ["fortune_teller", "fortune_type", "date", "time"]:
    if k not in st.session_state:
        st.session_state[k] = ""

# --- Navigation Function ---
def go_to(page, payment_mode=None):
    st.session_state.page = page
    if payment_mode:
        st.session_state.payment_mode = payment_mode

# --- Sidebar Menu ---
with st.sidebar:
    st.title("🔮 PryPround")
    st.markdown("**เพราะทุกวันควรมีพลังเสริมดวง ✨**")
    st.button("🏠 หน้าแรก", on_click=go_to, args=("home",))
    st.button("🔮 เริ่มดูดวง", on_click=go_to, args=("booking",))
    st.button("🛍️ สินค้าเสริมดวง", on_click=go_to, args=("products",))
    st.button("🛒 ตะกร้าสินค้า", on_click=go_to, args=("cart",))

# --- AI ----
key = st.secrets['gemini_api_key']
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name='gemini-2.0-flash-lite' ,
                                         system_instruction='You are an expert in fashion and astrology')
def to_markdown(text):
  text = text.replace('•', '*')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# ----------- Data -----------
user_focus = "love"
sign = "Capricorn"

import pandas as pd

# Create product data
data = [
    {"Product ID": "V001", "Name": "Structured Blazer", "Description": "Tailored blazer with sharp lines, ideal for work meetings and presentations", "Color": "Beige, Navy"},
    {"Product ID": "V002", "Name": "Minimalist Analog Watch", "Description": "Sleek gold/silver watch to add a touch of professionalism", "Color": "Gold, Silver"},
    {"Product ID": "V003", "Name": "Earth-Tone Leather Tote", "Description": "Spacious, structured tote that fits laptops and work essentials", "Color": "Camel, Olive"},
    {"Product ID": "V004", "Name": "Nude Comfort Loafers", "Description": "Comfortable yet polished loafers for long workdays", "Color": "Nude, Taupe"},
    {"Product ID": "V005", "Name": "Crisp White Shirt", "Description": "Classic button-up with a clean silhouette, easy to layer under blazers", "Color": "White"},
    {"Product ID": "V006", "Name": "High-Waisted Tailored Trousers", "Description": "Formal pants that elongate the silhouette and provide a perfect fit", "Color": "Taupe, Charcoal"},
    {"Product ID": "V007", "Name": "Silk Camisole", "Description": "Light innerwear with a refined sheen – perfect for layering", "Color": "White, Ivory"},
    {"Product ID": "V008", "Name": "Pencil Skirt", "Description": "A timeless workwear staple with a clean, fitted cut", "Color": "Black, Navy"},
    {"Product ID": "V009", "Name": "Pearl Stud Earrings", "Description": "Small, elegant pearls to subtly elevate your professional look", "Color": "White Pearl"},
    {"Product ID": "V010", "Name": "Leather Crossbody Bag", "Description": "Compact yet structured for everyday use without losing polish", "Color": "Black, Brown"},
]
# Create DataFrame
products = pd.DataFrame(data)

df_name = products
prod_name = products['Name']
prod_cl = products['Color']
prod_desc = products['Description']

user_focus = "love"
sign = "Capricorn"
username = "AAAA"


# --- Page Functions ---
def homepage():
    st.set_page_config("🔮 PryPround", layout="centered")
    st.title("Pry in your stars - Proud of your style")
    st.title("🏠 Lucky Style of the Day")
    st.image("https://images.unsplash.com/photo-1587049352844-96ec023f16f6", width=500)
    st.info(f"{username}")
    st.info(f"Zodiac Sign: {sign}")
    st.info(f"Current Focus: {user_focus}")

    prompt_rec = f"""
    You are a helpful stylist who recommends outfits and products in the store that align with the user’s current focus.
    Your goal is to recommend outfits based on the zodiac sign,
    and recommend products in the store based on the focus from the horoscope (e.g., career, love, finance).

    Here's the context:
    **Focus from Horoscope:**
    {user_focus}
    **Zodiac Sign:**
    {sign}
    **Product Name:**
    {prod_name}
    **Product Color:**
    {prod_cl}
    **Product Describtion:**
    {prod_desc}

    **Instructions:**
    1. You will first identify the user’s focus based on their horoscope from {user_focus}, such as their Career, Love, or Finance.
        This will guide the selection of products that match the user’s needs.
    2. You will then look at the user’s Zodiac Sign {sign} to determine the core style principles, key style elements (such as fabrics, silhouettes, and accessories),
        and which colors best promote the user’s focus area (e.g., colors for success in career, love, or finance). You’ll also consider which colors may not be beneficial for them (e.g., inauspicious colors for the zodiac).
    3. Finally, you will use the product description {prod_desc} and the color {prod_cl} to filter and recommend three products {prod_name} from the store that are aligned with the user's current focus and their zodiac characteristics.
    The products selected should enhance the user's goals and style.

    **Format:**
    The generated answer should provide: Core Style Principles, Key Style Elements to Consider, 3 Outfit Ideas – Mix & Match to Create Your Own,
    and recommend products from the store, based on the user's zodiac style and their current focus from the horoscope (e.g., career, love, finance)

    A clear list of recommended products from the store
    """

    bot_response_rec = model.generate_content(prompt_rec)
    #to_markdown(bot_response.text)
    st.markdown(bot_response_rec.text)

    st.info("💖 วันนี้แนะนำ: Mystic Rose Gold – เสริมเสน่ห์และการเจรจา")


def booking_page():
    st.title("🔮 จองดูดวง")
    st.session_state.fortune_type = st.selectbox("ประเภท:", ["Tarot", "Western Astrology", "Thai Astrology"])
    st.session_state.fortune_teller = st.selectbox("หมอดู:", ["หมอเมษา", "อ.นที", "แม่หมอลิลลี่"])
    st.session_state.date = st.date_input("วัน:", value=datetime.today())
    st.session_state.time = st.time_input("เวลา:")
    if st.button("📌 ยืนยัน"):
        go_to("payment", "booking")

def products_page():
    st.title("🛍️ สินค้าเสริมดวง")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1614281082180-b6f93bdf7ee7", width=250)
        if st.button("➕ เพิ่ม Rose Quartz Charm"):
            st.session_state.cart.append("Rose Quartz Charm")
    with col2:
        st.image("https://images.unsplash.com/photo-1619941803101-774d2fd7f4cd", width=250)
        if st.button("➕ เพิ่ม Mystic Perfume"):
            st.session_state.cart.append("Mystic Perfume")

def cart_page():
    st.title("🛒 ตะกร้าสินค้า")
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"✅ {item}")
        if st.button("💳 ดำเนินการชำระเงิน"):
            go_to("payment", "product")
    else:
        st.info("ยังไม่มีสินค้าในตะกร้า")

def payments_page():
    st.title("💳 ยืนยันการชำระเงิน")
    if st.session_state.payment_mode == "booking":
        st.write(f"จองกับ: `{st.session_state.fortune_teller}`")
        st.write(f"📅 {st.session_state.date}, 🕒 {st.session_state.time}")
        st.success("✅ ยืนยันการจองเรียบร้อย")
    elif st.session_state.payment_mode == "product":
        st.write("สินค้าในตะกร้า:")
        for item in st.session_state.cart:
            st.markdown(f"🧧 {item}")
        st.success("✅ การสั่งซื้อสำเร็จ")
        st.session_state.cart.clear()

# --- Page Dispatcher ---
page = st.session_state.page
if page == "home":
    homepage()
elif page == "booking":
    booking_page()
elif page == "products":
    products_page()
elif page == "cart":
    cart_page()
elif page == "payment":
    payments_page()

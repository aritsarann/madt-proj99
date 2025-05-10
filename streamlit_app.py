import streamlit as st
from datetime import datetime

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

# --- Page Functions ---
def homepage():
    st.title("🏠 Lucky Style of the Day")
    st.image("https://images.unsplash.com/photo-1587049352844-96ec023f16f6", width=500)
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

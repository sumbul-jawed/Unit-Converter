import streamlit as st
import datetime

# Custom CSS Stylish Sidebar & Buttons
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #2193b0, #6dd5ed, #24243e);
            color: #ffffff;
        }
        .main {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 10px;
            color: red;
            border: 2px solid #FFD700;
        }
        .stButton>button {
            background: linear-gradient(to right, #02AAB0, #E4E5E6);
            color: black;
            border-radius: 8px;
            padding: 12px 24px;
            font-weight: bold;
            border: none;
            transition: 0.3s ease-in-out;
            font-size: 18px;
        }
        .stButton>button:hover {
            background: linear-gradient(to right, #1FA2FF , #E4E5E6);
            transform: scale(1.05);
        }
        .sidebar .sidebar-content h1, .sidebar .sidebar-content h2 {
            color: #0a192f !important;
        }
        .sidebar .sidebar-content a {
            color: #FFD700;
            font-weight: bold;
        }
        .sidebar .sidebar-content ul {
            color: #0a192f !important;
            font-weight: bold;
        }
        .currency-card {
            background-color: red;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(255, 215, 0, 0.2);
        }
        .currency-text {
            color: black; 
            font-weight: bold;
        }
        
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown('<h2 style="color: blue;">🚀 Navigation</h2>', unsafe_allow_html=True)
option = st.sidebar.radio("📌 Choose a Conversion:", ("📏 Length", "⚖️ Weight", "🌡️ Temperature", "💱 Currency"))

st.sidebar.markdown("""
    <style>
        ul {
            list-style-type: disc; 
        }
        li::marker {
            color: black; /* Change bullet points to black */
            font-size: 18px; /* Increase size if needed */
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<h2 style="color: blue;">🌟 Connect with me:</h2>', unsafe_allow_html=True)
st.sidebar.markdown(""" 
- 🏆 [GitHub](https://github.com/sumbul-jawed)  
- 💼 [LinkedIn](https://www.linkedin.com/in/sumbul-jawed-b9a5231b5/)  
- 🌍 [Portfolio](https://portfolio-sj-lp8m.vercel.app/)  
""", unsafe_allow_html=True)


# Unit Conversion Functions
def length_converter(value, from_unit, to_unit):
    conversion_factors = {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Inch": 39.3701, "Foot": 3.28084}
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274}
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

def usd_to_pkr_converter(amount, direction="to_pkr"):
    c = CurrencyRates()
    try:
        if direction == "to_pkr":
            rate = c.get_rate("USD", "PKR")
            return amount * rate
        else:
            rate = c.get_rate("PKR", "USD")
            return amount * rate
    except Exception:
        fallback_rates = {"USD_PKR": 278.50, "PKR_USD": 0.00359}
        return amount * fallback_rates["USD_PKR"] if direction == "to_pkr" else amount * fallback_rates["PKR_USD"]

# UI for Conversions
st.title("🔢 Unit Converter")

if option == "📏 Length":
    st.subheader("📐 Length Conversion")
    value = st.number_input("🔢 Enter Value", min_value=0.0)
    from_unit = st.selectbox("📤 From", ["Meter", "Kilometer", "Centimeter", "Inch", "Foot"])
    to_unit = st.selectbox("📥 To", ["Meter", "Kilometer", "Centimeter", "Inch", "Foot"])
    if st.button("🔄 Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif option == "⚖️ Weight":
    st.subheader("⚖️ Weight Conversion")
    value = st.number_input("🔢 Enter Value", min_value=0.0)
    from_unit = st.selectbox("📤 From", ["Kilogram", "Gram", "Pound", "Ounce"])
    to_unit = st.selectbox("📥 To", ["Kilogram", "Gram", "Pound", "Ounce"])
    if st.button("🔄 Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif option == "🌡️ Temperature":
    st.subheader("🌡️ Temperature Conversion")
    value = st.number_input("🔢 Enter Value", min_value=-273.15)
    from_unit = st.selectbox("📤 From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("📥 To", ["Celsius", "Fahrenheit"])
    if st.button("🔄 Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"✅ {value}° {from_unit} = {result:.2f}° {to_unit}")

elif option == "💱 Currency":
    st.subheader("💰 USD ↔ PKR Conversion")
    st.markdown("🇵🇰 💱 🇺🇸")

    try:
        c = CurrencyRates()
        current_rate = c.get_rate("USD", "PKR")
        st.info(f"📈 1 USD = {current_rate:.2f} PKR (as of {datetime.datetime.now().strftime('%Y-%m-%d')})")
    except Exception:
        st.info(f"📉 1 USD ≈ 278.50 PKR (Fallback rate)")

    conversion_direction = st.radio("🔄 Select Conversion", ["USD to PKR", "PKR to USD"])

    if conversion_direction == "USD to PKR":
        amount = st.number_input("💵 Enter USD Amount", min_value=0.0, value=1.0)
        if st.button("🔄 Convert to PKR"):
            result = usd_to_pkr_converter(amount, "to_pkr")
            st.success(f"✅ {amount:.2f} USD = {result:.2f} PKR")
    else:
        amount = st.number_input("💴 Enter PKR Amount", min_value=0.0, value=1000.0)
        if st.button("🔄 Convert to USD"):
            result = usd_to_pkr_converter(amount, "to_usd")
            st.success(f"✅ {amount:.2f} PKR = {result:.4f} USD")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 10px; background-color: #26a0da; border-radius: 5px;">
    <p>© 2025 Unit Converter App | Created By Sumbul Jawed 🚀</p>
</div>
""", unsafe_allow_html=True)

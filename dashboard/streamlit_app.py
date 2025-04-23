import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Crypto Pulse Dashboard", layout="centered")

st.title("📊 Crypto Pulse - Real-time BTC/USDT Prices")
st.markdown("Powered by Binance WebSocket → Kafka → MongoDB")

# MongoDB connection
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["crypto_db"]
    collection = db["prices"]

    # Fetch recent prices
    data_cursor = collection.find({"symbol": "BTCUSDT"}).sort("timestamp", -1).limit(50)
    data = list(data_cursor)

    if not data:
        st.warning("⚠️ No price data found in MongoDB.")
    else:
        # Convert to DataFrame
        df = pd.DataFrame(data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

        # Display latest price
        latest = df.iloc[-1]
        st.metric(label="📈 Latest BTC Price (USDT)", value=f"${latest['price']:,.2f}", delta=None)

        # Line chart
        st.line_chart(df.set_index("timestamp")["price"], use_container_width=True)

        # Optional: raw data table
        with st.expander("📋 View Raw Data"):
            st.dataframe(df[["timestamp", "price"]].tail(10), use_container_width=True)

except Exception as e:
    st.error(f"❌ Database connection failed: {e}")

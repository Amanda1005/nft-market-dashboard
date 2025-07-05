import streamlit as st
import pandas as pd
import os
import sys

# Dynamically add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from utils.reservoir_api import get_top_collections


# ----------------- Page Header -----------------
st.title("📊 NFT Market Dashboard")
st.markdown("Explore the most popular NFT collections: total trading volume, floor prices, and distribution analysis")

# -----------------  Load Data資料 -----------------
@st.cache_data
def load_data():
    data = get_top_collections(limit=20)
    df = pd.DataFrame(data)
    df["total_volume"] = df["volume"].apply(lambda v: v.get("allTime", 0) if isinstance(v, dict) else 0)
    
    def extract_floor_price(item):
        try:
            return item["floorAsk"]["price"]["amount"]["decimal"]
        except (TypeError, KeyError):
            return None
    
    df["floor_price"] = df.apply(extract_floor_price, axis=1)
    return df[["name", "total_volume", "floor_price"]]

df = load_data()

# ----------------- Top List -----------------
st.subheader("🏆 Top 10 NFT Collections")

#  Add Sorting Menu
sort_option = st.selectbox(
    "Sort by：",
    ("total_volume", "floor_price"),
    index=0,
    format_func=lambda x: "Total Trading Volume (ETH)" if x == "total_volume" else "Floor Price (ETH)"
)

# Sort data by selection
top10 = df.sort_values(by=sort_option, ascending=False).head(10)

# Show Table
st.dataframe(top10.reset_index(drop=True))


# ----------------- Floor Price Distribution-----------------
st.subheader("💰 Floor Price Distribution")
df_clean = df.dropna(subset=["floor_price"])
st.bar_chart(df_clean["floor_price"])

st.subheader("🥇 Top 3 Featured NFT Collections")

top3 = df.sort_values(by="total_volume", ascending=False).head(3)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label=top3.iloc[0]["name"],
        value=f'{top3.iloc[0]["floor_price"]:.2f} ETH',
        delta=f'{top3.iloc[0]["total_volume"]:.0f} ETH'
    )

with col2:
    st.metric(
        label=top3.iloc[1]["name"],
        value=f'{top3.iloc[1]["floor_price"]:.2f} ETH',
        delta=f'{top3.iloc[1]["total_volume"]:.0f} ETH'
    )

with col3:
    st.metric(
        label=top3.iloc[2]["name"],
        value=f'{top3.iloc[2]["floor_price"]:.2f} ETH',
        delta=f'{top3.iloc[2]["total_volume"]:.0f} ETH'
    )

st.subheader("📥 Download Data")

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇️ Download CSV File",
    data=csv,
    file_name='nft_collections.csv',
    mime='text/csv',
)
st.subheader("🧠 My opinion")

st.markdown("""
- 💡 High trading volume doesn’t necessarily mean a high floor price — for example, the difference between Bored Ape and CryptoPunks.
- 📉 Some collections maintain active trading despite low floor prices, indicating strong community engagement.
- ⏱️ Further analysis could explore the relationship between floor price and sales frequency.

""")

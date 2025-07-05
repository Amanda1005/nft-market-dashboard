# NFT Market Analysis Dashboard

📊 Analyze real-time NFT market trends, visualize trading volume, and uncover insights using Python, Streamlit, and Reservoir API.

---

## 🔍 Project Overview
This dashboard explores the top NFT collections by analyzing:
- Total trading volume
- Floor price distribution
- Top collections ranking
- Sales dynamics and market insights

Built with:
- 📦 Python (pandas, matplotlib, seaborn)
- 📈 Streamlit for interactive visualization
- 🌐 Reservoir API for real-time NFT data

---

## 💡 Key Features
- ✅ Real-time NFT collection ranking (by volume / floor price)
- 🎯 Interactive dashboard with sort & filter
- 📊 Floor price distribution histogram
- 🧠 Business insights based on data patterns
- 📥 Downloadable CSV data

---

## 📸 Dashboard Screenshot

![NFT Dashboard](streamlit_app/screenshots/dashboard.png)


---

## 🧠 Insights
> Some key observations from the data:

- **High trading volume ≠ high floor price**  
  > e.g., Bored Ape vs CryptoPunks
- **Strong community = sustained activity**  
  > Some low-price projects still trade frequently
- **More analysis needed**  
  > Correlation between price and sales frequency is worth exploring

---

## 🛠️ How to Run
```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py

📎 Data Source  
- [Reservoir API](https://docs.reservoir.tools/)

👩‍💻 Author  
Amanda Weng
Data Analyst | Web3 Enthusiast  
[LinkedIn](https://www.linkedin.com/in/nianya-weng-41517b331/)  
[Portfolio](https://ludicrous-decade-ba2.notion.site/Azuki-NFT-Trading-Analysis-Web3-Product-Data-Case-Study-225e65a7b35080f58c7de64db0b08f80)
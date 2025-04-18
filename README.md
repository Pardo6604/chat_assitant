# 🏢 Apartment Listing Assistant (LangChain + Ollama + Chroma)

This is a conversational AI assistant designed to help users find apartment rentals based on listing data. It uses natural language processing and vector search to return the most relevant results from a dataset of listings.

---

## 🔧 Tech Stack

- [LangChain](https://python.langchain.com/) – Framework for LLM-powered apps
- [Ollama](https://ollama.com/) – Local LLM and embedding model host
- [Chroma](https://www.trychroma.com/) – Vector database for storing and searching embeddings
- `pandas` – For data processing
- JSON – Source data format

---

## 🚀 Features

- Embeds apartment listings using `mxbai-embed-large` via Ollama
- Stores and retrieves vectors using Chroma
- Uses `llama3.2` (via Ollama) to answer questions about listings
- Command-line interface for chatting with the assistant
- Retrieves top 5 most relevant listings for each user query

---

## 📂 Project Structure
```
project-root/
├── db/
│   └── chroma_langchain_db/       # Vector DB files
├── train.json                 # Listing data
├── main.py
├── vector.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. Loads apartment listings from `train.json`
2. Converts listings to documents with metadata
3. Embeds each document and stores them in a Chroma vector DB
4. Uses a retriever to find the top 5 most relevant listings for any question
5. Sends retrieved info and question to the LLM to generate a helpful answer

---

## ✅ Setup Instructions

### 1. Install dependencies


Make sure you have Python 3.9+ and create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Install & run Ollama


Download and run Ollama locally, then pull the models:

```bash
ollama pull llama3
ollama pull mxbai-embed-large
```

### 3. Run the assistant


```bash
python main.py
```
Type your questions! To exit, just type quit.

💡 Example Questions:

"What's the best 2-bedroom apartment under $3000?"

"Do any listings have laundry in the building?"

"Which apartments have private decks?"

⚠️ Notes
On first run, embeddings will be generated and saved to chroma_langchain_db/. This can take time!

The assistant uses only the info in the listings dataset — no internet access.

📌 To Do
Add filters (price, neighborhood, etc.)

Web interface with Streamlit or Flask

Improve prompt for more accurate LLM responses

Add better error handling/logging

## 🧑‍💻 Author
Built by Santiago Velasco

## 📚 Dataset
This project uses data from the Two Sigma Connect: Rental Listing Inquiries Kaggle competition.

Citation:

Meg Risdal, Thandar, Wendy Kan.
Two Sigma Connect: Rental Listing Inquiries. Kaggle, 2017.
https://kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries

<details> <summary>BibTeX Citation</summary>
@misc{two-sigma-connect-rental-listing-inquiries,
    author = {Meg Risdal and Thandar and Wendy Kan},
    title = {Two Sigma Connect: Rental Listing Inquiries},
    year = {2017},
    howpublished = {\url{https://kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries}},
    note = {Kaggle}
}
</details>


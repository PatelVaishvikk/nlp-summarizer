An advanced NLP-powered app to summarize and paraphrase text instantly (CPU-friendly).

Demo (Example screenshot)

🚀 Features
Text Summarization (Extractive + Abstractive using T5-small)

Text Paraphrasing (Pegasus model)

Simple UI built with Streamlit

Runs on CPU (No GPU required)

⚙️ Installation
Clone the repo:

bash
Copy
git clone [https://github.com/yourusername/nlp-summarizer.git](https://github.com/PatelVaishvikk/nlp-summarizer.git
)
cd nlp-summarizer
Set up a virtual environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # Windows: `venv\Scripts\activate`
Install dependencies:

bash
Copy
pip install torch transformers sentencepiece streamlit
🖥️ Usage
Run the app:

bash
Copy
streamlit run app.py
Open http://localhost:8501 in your browser.

Enter text and click Summarize or Paraphrase!

📂 Project Structure
Copy
nlp-summarizer/
├── app.py           # Streamlit UI
├── model.py         # NLP models (Summarizer + Paraphraser)
├── requirements.txt # Dependencies
└── README.md
🔧 Dependencies
Python 3.8+

PyTorch (pip install torch)

Transformers (pip install transformers)

Streamlit (pip install streamlit)

📜 License
MIT License - Free for personal and commercial use.

📌 Notes
For faster CPU performance, see Optimization Guide (optional).

Models are cached locally after first run.

Enjoy summarizing and paraphrasing! 🎉

Want to Contribute?
Fork the repo.

Add features (e.g., PDF/URL input, multilingual support).

Submit a PR!

Let me know if you'd like any modifications! 😊

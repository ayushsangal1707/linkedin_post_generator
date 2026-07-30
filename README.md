# 🚀 LinkedIn Post Generator

An AI-powered LinkedIn Post Generator that creates engaging, professional, and ready-to-post LinkedIn content using Large Language Models (LLMs). Users can generate posts based on topic, language, and desired post length through an intuitive Streamlit interface.

## 🌐 Live Demo

**Live Demo:** https://linkedin-post-generator-ayush-sangal.streamlit.app/

## ✨ Features

- 🤖 AI-powered LinkedIn post generation using Groq LLM
- 🌍 Supports English and Hinglish
- 📏 Generate Short, Medium, or Long posts
- 🏷️ Topic-based content generation
- 🎯 Few-shot prompting for more natural and realistic posts
- 🖥️ Interactive Streamlit web interface
- ⚡ Fast response using Groq's Llama 3.3 70B model

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Pandas
- JSON
- python-dotenv

## 📂 Project Structure

```
linkedin_post_generator/
│── data/
│   ├── processed_posts.json
│   └── raw_posts.json
│
│── main.py
│── few_shot.py
│── post_generator.py
│── llm_helper.py
│── preprocess.py
│── requirements.txt
│── .gitignore
│── README.md
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/ayushsangal1707/linkedin_post_generator.git
cd linkedin_post_generator
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

### Run the application

```bash
streamlit run main.py
```

## 🚀 How It Works

1. Select a topic.
2. Choose the desired post length.
3. Select the language (English or Hinglish).
4. The application retrieves similar few-shot examples.
5. Groq Llama 3.3 generates a high-quality LinkedIn post.
6. The generated post is displayed instantly.

## 📸 Screenshots

_Add screenshots of your application here._

## 👨‍💻 Author

**Ayush Sangal**

- GitHub: https://github.com/ayushsangal1707
- LinkedIn: https://www.linkedin.com/in/ayush-sangal-218b9a214/

---

⭐ If you found this project useful, consider giving it a star on GitHub!

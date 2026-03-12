# ✍️ GenAI Powered Writing Assistant

This is a small project I built where you just give a topic, select which platform you want to write for — like LinkedIn, Twitter, Email, Instagram, etc. — and it will generate a proper write-up for you using OpenAI's GPT-3.5 and LangChain.

---

## 🤔 What does it do exactly?

Simple. You type something like *"I just got a new job"* and select LinkedIn — and it will write a nice, professional post for you. Select Twitter and it gives a short punchy tweet. Select Email and you get a full proper email. That's it!

Platforms supported:
- 📧 Email
- 💼 LinkedIn
- 🐦 Twitter
- 📘 Facebook
- 📸 Instagram
- 📝 Blog

---

## 🛠️ How to set it up on your system

Don't worry, it's not that complicated. Just follow these steps one by one.

### Step 1 — Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/GenAI_Powered_Writing_Assistant.git
cd GenAI_Powered_Writing_Assistant
```

### Step 2 — Install all the required libraries
```bash
pip install -r requirements.txt
```
This will install everything. Just wait for it to finish.

### Step 3 — Add your API Keys (Important! Don't skip this)

This is the step most people mess up so read carefully.

Create a file called `.env` in the same folder as `app.py`:
```bash
touch .env
```

Now open that `.env` file and paste this inside:
```
OPENAI_API_KEY=paste_your_openai_key_here
LANGCHAIN_API_KEY=paste_your_langchain_key_here
```

**Where to get these keys?**
- OpenAI key → go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys), sign in and create a key
- LangChain key → go to [smith.langchain.com](https://smith.langchain.com/), sign in and get your API key from settings

> ⚠️ Please don't share this `.env` file with anyone or push it to GitHub. It has your secret keys. The `.gitignore` file will make sure it doesn't get uploaded by mistake, but still be careful yaar.

### Step 4 — Run the app
```bash
streamlit run app.py
```

Once you run this, it will automatically open in your browser at:
```
http://localhost:8501
```

If it doesn't open automatically, just copy that link and paste it in your browser. Done!

---

## 📁 What's inside the project

```
├── app.py               # The main code file
├── requirements.txt     # All libraries needed
├── .env                 # Your API keys (don't share this!)
├── .gitignore           # Makes sure .env doesn't go to GitHub
└── README.md            # This file you're reading right now
```

---

## 🔑 API Keys — Quick Reference

| Key | Where to get |
|-----|--------------|
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com/api-keys) |
| `LANGCHAIN_API_KEY` | [smith.langchain.com](https://smith.langchain.com/) |

---

## 🧰 Tech Stack used

- [Streamlit](https://streamlit.io/) — for the UI
- [LangChain](https://www.langchain.com/) — for chaining the AI pipeline
- [OpenAI GPT-3.5](https://platform.openai.com/) — the actual AI model
- [python-dotenv](https://pypi.org/project/python-dotenv/) — to load the API keys safely

---

## 📄 License

Open source. Use it, modify it, learn from it — whatever you want!

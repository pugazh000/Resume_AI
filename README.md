---
t: gradio
license: mit
title: Resume_AI
sdk: gradio
---
# 🚀 ResumeGenius AI - Smart Resume Builder & Matcher

**Empower your career with AI!**
ResumeGenius AI is an all-in-one intelligent assistant that helps users **generate**, **match**, and **enhance** resumes with ease. Built using Gradio, Python, and machine learning from scratch — no pre-trained models, just pure talent 💼✨

---

## ✨ Features

🔹 **Generate Resume**
Craft a polished resume from scratch with a guided form — just enter your info and get a formatted resume instantly.

🔹 **Match Resume to Job**
Upload your resume and a job description to get **Top 3 matching career roles** with real-time relevance scoring using TF-IDF + Cosine Similarity.

🔹 **Enhance Resume**
Get smart suggestions based on your job category to boost your resume and align with industry standards.

---

## 🧠 Tech Stack

* **Frontend:** Gradio (UI for resume builder & bot)
* **Backend:** Python
* **NLP & ML:**

  * Custom Tokenizer
  * TF-IDF Featurizer
  * Logistic Regression (built from scratch)
  * Cosine Similarity Matching
* **PDF Parsing:** PyMuPDF (`fitz`)
* **Data:** Resume dataset from Kaggle (2000+ labeled resumes)

---

## 📁 Project Structure

```
resumeproject/
|
├── data/
|   └── processed/
|       ├── model_weights.npz
|       ├── tokenizer.pkl
|       └── label_encoder.pkl
|
├── src/
|   ├── app.py               ← Main Gradio app
|   ├── resume_generator.py  ← Resume builder logic
|   ├── job_matcher.py       ← Job description matcher
|   ├── enhancer.py          ← Resume improver
|   ├── tokenizer.py         ← Tokenizer for ML model
|   ├── featurizer.py        ← TF-IDF logic
|   ├── model.py             ← Logistic Regression from scratch
|   └── predict.py           ← CLI or demo prediction
|
├── requirements.txt
└── README.md
```

---

## 💻 How to Use

### ▶️ Online Demo

Deployed via Hugging Face Spaces — [Click Here to Try It Now!](https://huggingface.co/spaces/PoPz007/resume_AI)

### 🛠️ Run Locally

```bash
git clone https://huggingface.co/spaces/PoPz007/resume_AI
cd resume_AI
pip install -r requirements.txt
python src/app.py
```

---

## 🧪 Sample Use Cases

* ✔️ Students creating their **first resume**
* ✔️ Professionals matching their resume to **a job post**
* ✔️ Job seekers improving their **resume alignment & impact**
* ✔️ HR teams showcasing **resume matching AI** in action


---

## 🏆 Credits

Made with 💻, ☕, and 🚀 by **[PoPz007](https://huggingface.co/PoPz007)**
Guided by ChatGPT and powered by open-source innovation.

---

## 📜 License

This project is licensed for educational and demonstration purposes. Commercial use requires permission.

---

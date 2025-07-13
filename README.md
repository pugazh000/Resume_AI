# 🤖 ResumeGenius AI - Smart Resume Builder & Job Matcher

ResumeGenius AI is a web-based application that empowers users to effortlessly generate professional resumes, match their resumes with job descriptions, get enhancement suggestions, and find relevant job postings using AI-powered features.

---

## 🌟 Features

* **📝 Resume Generation**

  * Input your personal details, skills, education, certifications, and more.
  * Get a clean, professional resume format instantly.

* **🔍 Job Match Scoring**

  * Upload your resume and a job description.
  * The app uses a fuzzy string similarity algorithm to score how well your resume matches the job.

* **💡 Resume Enhancement Suggestions**

  * Select your job category and upload your resume.
  * The app suggests improvements based on common job-specific keywords and role expectations.

* **🌐 Smart Job Finder**

  * Extracts relevant keywords from your resume.
  * Automatically opens job search links on Naukri and LinkedIn based on your skillset.

---

## 🗂️ Dataset Used

We used the **Resume Dataset** from Kaggle which contains structured resumes categorized into job domains along with sample resumes in `.pdf` format:

🔗 [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset?select=data)

---

## 🛠️ Tech Stack

* **Frontend:** Gradio (Python-based UI library)
* **Backend:** Python (NLP + Resume Parsing + Regex)
* **Libraries:**

  * `fuzzywuzzy` for job-resume match scoring
  * `re` for keyword extraction via regex
  * `PyMuPDF (fitz)` for PDF parsing
  * `Gradio` for building the UI

---

## ⚙️ How It Works

```
User selects a feature mode:
    1. Resume Generator
    2. Resume Matcher
    3. Resume Enhancer

▶ Resume Generator:
   - User fills in details
   - App formats data into a professional resume layout

▶ Resume Matcher:
   - Resume & job description are parsed
   - Uses fuzzy match to score similarity
   - Shows Top 3 matching job categories
   - Opens job links on Naukri & LinkedIn

▶ Resume Enhancer:
   - Resume + selected job category
   - Suggests missing keywords / improvements
```

---

## 🚀 Deployment

This app is deployed on [Hugging Face Spaces](https://huggingface.co/spaces/PoPz007/resume_AI) using Gradio.

---

## 🧠 AI Techniques

* **Fuzzy String Matching:**

  * Helps compare the similarity between resume content and job descriptions.

* **Regex-based Keyword Extraction:**

  * Extracts job titles and technical terms for job search redirection.

---

## 📁 Directory Structure

```
resumeproject/
│
├── app.py                 # Main Gradio app interface
├── resume_generator.py   # Resume formatting logic
├── job_matcher.py        # Fuzzy matching logic
├── enhancer.py           # Suggests keyword enhancements
├── job_recommender.py    # Extracts skills & opens job search
├── data/                 # Resumes grouped by categories
├── resume.csv            # Metadata from Kaggle dataset
└── README.md             # Project documentation
```

---

## 💬 Feedback

If you liked the project or want to suggest improvements, feel free to open an issue or fork it and enhance it further!

---


Thank you for exploring ResumeGenius AI! 💼✨

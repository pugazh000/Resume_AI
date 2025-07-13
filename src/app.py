# Gradio-based ResumeBot Pro UI (For Google Colab)

import gradio as gr
from resume_generator import generate_resume
from job_matcher import match_resume_to_job
from enhancer import suggest_enhancements
from job_recommender import recommend_jobs  # Now returns links as string
import fitz

job_categories = [
    "ACCOUNTANT", "ADVOCATE", "AGRICULTURE", "APPAREL", "ARTS", "AUTOMATION", "AVIATION", 
    "BANKING", "BPO", "BUSINESS DEVELOPMENT", "CHEMICAL", "CONSTRUCTION", "CONSULTANT", 
    "CONTENT WRITING", "DATA ANALYST", "DATA ENTRY", "DATA SCIENCE", "DIGITAL MARKETING", 
    "ENGINEERING", "FINANCE", "FITNESS", "GRAPHIC DESIGNER", "HR", "INFORMATION TECHNOLOGY", 
    "INSURANCE", "INTERNET", "IT", "LEGAL", "LOGISTICS", "MANUFACTURING", "MARKETING", 
    "MECHANICAL", "MEDICAL", "MERCHANDISING", "NETWORKING", "NON PROFIT", "PHARMA", 
    "PUBLIC RELATIONS", "REAL ESTATE", "RESEARCH", "SALES", "SCIENCE", "SECURITY SERVICES", 
    "SOFTWARE", "SPORTS", "TEACHER", "TECHNICAL SUPPORT", "TRAINING", "WEB DESIGNER"
]

def load_file(file):
    if file is None:
        return ""
    if file.name.endswith(".pdf"):
        doc = fitz.open(file.name)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    return file.read().decode("utf-8")

def top_category_predictions(resume_text, job_desc):
    sample_titles = ["IT", "DATA SCIENCE", "AI", "TEACHER", "HR"]
    predictions = [(title, match_resume_to_job(resume_text, job_desc, title)) for title in sample_titles]
    top3 = sorted(predictions, key=lambda x: x[1], reverse=True)[:3]
    return "\n".join([f"{title}: {round(score * 100)}% match" for title, score in top3])

def chatbot_handler(mode, resume, job_desc, name, title, exp, skills, soft_skills, edu, certs, projects, awards, interests, category):
    if mode == "Generate Resume":
        return generate_resume(name, title, exp, skills, edu, certs, projects, awards, soft_skills, interests)

    elif mode == "Match Resume":
        summary = top_category_predictions(resume, job_desc)
        job_links = recommend_jobs(resume)
        return f"🔍 Top 3 Match Predictions:\n{summary}\n\n{job_links}"

    elif mode == "Enhance Resume":
        suggestions = suggest_enhancements(resume, category)
        return "\n".join(suggestions) if suggestions else "✅ Your resume looks great!"

    else:
        return "❌ Invalid choice."

with gr.Blocks() as demo:
    gr.Markdown(" <div style='text-align: center; font-size: 24px;'>🚀 ResumeGenius AI - Smart Resume Builder & Matcher</div>")
    mode = gr.Radio(["Generate Resume", "Match Resume", "Enhance Resume"], label="Choose Mode")

    with gr.Column(visible=False) as gen_ui:
        gr.Markdown("### ✍️ Resume Generator")
        name = gr.Textbox(label="Full Name", placeholder="e.g., John Marston")
        title = gr.Textbox(label="Target Job Title", placeholder="e.g., Software Engineer")
        exp = gr.Textbox(label="Experience", placeholder="e.g., Fresher, 6 months internship, 2 years full-time")
        skills = gr.Textbox(label="Technical Skills", placeholder="e.g., Python, AWS, React, Git, Java")
        soft_skills = gr.Textbox(label="Soft Skills", placeholder="e.g., Problem-solving, Time management, Communication")
        edu = gr.Textbox(label="Education", placeholder="e.g., B.Tech Department, Year, University")
        certs = gr.Textbox(label="Certifications", placeholder="e.g., Udemy, Google IT Support, Nptel, coursera")
        projects = gr.Textbox(label="Projects", placeholder="e.g., In college and Events")
        awards = gr.Textbox(label="Achievements / Publications", placeholder="e.g., Patent , publication")
        interests = gr.Textbox(label="Interests / Hobbies", placeholder="e.g., Open-source projects, Tech blogging, Cloud labs, Ethical hacking, Data storytelling, Reading non-fiction")

    with gr.Column(visible=False) as match_ui:
        gr.Markdown("### 🔍 Match Resume to Job Description")
        resume_file = gr.File(label="Upload Resume File (.txt or .pdf)")
        resume = gr.Textbox(label="Resume Text", lines=10, interactive=True)
        job_desc = gr.Textbox(
            label="Job Description",
            lines=10,
            placeholder="e.g., We are hiring a motivated and detail-oriented Software Engineer to join our engineering team..."
        )
        job_title = gr.Textbox(label="Job Title (optional, for keyword scoring)")
        resume_file.change(fn=load_file, inputs=resume_file, outputs=resume)

    with gr.Column(visible=False) as enhance_ui:
        gr.Markdown("### 💡 Resume Enhancer")
        enh_resume_file = gr.File(label="Upload Resume File (.txt or .pdf)")
        enh_resume = gr.Textbox(label="Resume Text", lines=10, interactive=True)
        category = gr.Dropdown(choices=job_categories, label="Select Job Category")
        enh_resume_file.change(fn=load_file, inputs=enh_resume_file, outputs=enh_resume)

    btn = gr.Button("Run ResumeBot Pro")
    output = gr.Markdown()

    def toggle_ui(choice):
        return {
            gen_ui: gr.update(visible=choice == "Generate Resume"),
            match_ui: gr.update(visible=choice == "Match Resume"),
            enhance_ui: gr.update(visible=choice == "Enhance Resume")
        }

    mode.change(fn=toggle_ui, inputs=mode, outputs=[gen_ui, match_ui, enhance_ui])
    btn.click(
        fn=chatbot_handler,
        inputs=[mode, resume, job_desc, name, title, exp, skills, soft_skills, edu, certs, projects, awards, interests, category],
        outputs=output
    )

demo.launch(share=True)

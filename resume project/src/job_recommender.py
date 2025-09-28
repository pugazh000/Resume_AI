# src/job_recommender.py
import re

def extract_keywords(resume_text):
    resume_text = resume_text.lower()
    title_match = re.search(r'(job title|role|position)[:\- ]*(.+)', resume_text)
    skills_match = re.findall(r'\b(python|java|sql|aws|cloud|excel|rpa|automation|data|analysis|django|react|git|linux)\b', resume_text)

    job_title = title_match.group(2).strip() if title_match else "software developer"
    skills = "+".join(set(skills_match)) if skills_match else "python+developer"

    return job_title.replace(" ", "-"), skills

def recommend_jobs(resume_text):
    job_title, skills = extract_keywords(resume_text)

    naukri_url = f"https://www.naukri.com/{job_title}-jobs?k={skills}"
    linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={skills}"

    return f"🌐 **Job Search Links:**\n- [Naukri Jobs]({naukri_url})\n- [LinkedIn Jobs]({linkedin_url})"

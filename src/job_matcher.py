import re
import string
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Skill bank for fallback keyword scoring
keyword_bank = {
    'ACCOUNTANT': ["Financial reporting", "Bookkeeping", "Accounts payable", "Budget forecasting", "Tax compliance"],
    'ADVOCATE': ["Legal research", "Litigation", "Client counseling", "Case documentation", "Court procedures"],
    'AGRICULTURE': ["Soil science", "Crop rotation", "Irrigation systems", "Farm machinery", "Pest management"],
    'APPAREL': ["Fabric selection", "Pattern making", "Fashion trends", "Sewing techniques", "Quality control"],
    'ARTS': ["Creativity", "Design thinking", "Sketching", "Art history", "Exhibition planning"],
    'AUTOMOBILE': ["Vehicle diagnostics", "Engine repair", "Brake systems", "Automotive electronics", "Workshop safety"],
    'AVIATION': ["Flight operations", "Aircraft maintenance", "Navigation systems", "Aviation safety", "ATC communication"],
    'BANKING': ["Financial services", "Risk assessment", "Loan processing", "Credit analysis", "Banking regulations"],
    'BPO': ["Customer service", "Voice process", "CRM", "Email handling", "Escalation management"],
    'BUSINESS DEVELOPMENT': ["Market research", "Lead generation", "Pitch presentations", "Client relationship", "Sales strategy"],
    'CHEF': ["Recipe creation", "Food safety", "Kitchen management", "Menu planning", "Culinary techniques"],
    'CONSTRUCTION': ["Blueprint reading", "Site management", "Safety compliance", "Project scheduling", "Concrete work"],
    'CONSULTANT': ["Problem solving", "Client presentations", "Industry analysis", "Strategic planning", "Process optimization"],
    'DESIGNER': ["User experience (UX)", "Wireframing", "Adobe Creative Suite", "Typography", "Visual storytelling"],
    'DIGITAL MEDIA': ["Content creation", "Social media marketing", "SEO", "Analytics tools", "Video editing"],
    'ENGINEERING': ["CAD software", "Project design", "Thermodynamics", "Electrical systems", "Problem solving"],
    'FINANCE': ["Financial modeling", "Valuation", "Investment analysis", "Portfolio management", "Excel reporting"],
    'FITNESS': ["Workout planning", "Diet coaching", "Client assessment", "Strength training", "Injury prevention"],
    'HEALTHCARE': ["Patient care", "Medical records", "Health screening", "CPR", "EMR systems"],
    'HR': ["Recruitment", "Communication", "Employee relations", "Onboarding", "Payroll systems"],
    'IT': ["Python", "SQL", "Git", "Cloud computing", "System administration"],
    'PUBLIC RELATION': ["Press release writing", "Media relations", "Crisis communication", "Event planning", "Brand management"],
    'SALES': ["Lead generation", "Negotiation", "CRM", "Sales strategy", "Customer retention"],
    'TEACHER': ["Lesson planning", "Classroom management", "Curriculum development", "Student assessment", "Parent communication"]
}

def clean_unicode(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

def preprocess(text):
    text = clean_unicode(text)
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def extract_relevant_resume_sections(resume_text):
    start_keywords = ["summary", "skills", "certifications"]
    lines = resume_text.lower().split('\n')
    relevant = []

    for i, line in enumerate(lines):
        if any(k in line for k in start_keywords):
            for j in range(i+1, min(i+6, len(lines))):
                relevant.append(lines[j])

    result = " ".join(relevant)
    return result if len(result) > 50 else resume_text

def keyword_match_score(resume_text, job_title):
    expected_skills = keyword_bank.get(job_title.upper(), [])
    found = sum(1 for skill in expected_skills if skill.lower() in resume_text.lower())
    return round(found / len(expected_skills), 2) if expected_skills else 0.0

def match_resume_to_job(resume_text, job_description, job_title=""):
    focused_resume = extract_relevant_resume_sections(resume_text)

    resume_clean = preprocess(focused_resume)
    job_clean = preprocess(job_description)

    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume_clean, job_clean])
    tfidf_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    # Optional fallback keyword score (only if job_title provided)
    keyword_score = keyword_match_score(resume_clean, job_title) if job_title else 0.0

    # Hybrid score: weighted average
    hybrid_score = round((tfidf_score * 0.7 + keyword_score * 0.3), 2) if job_title else round(tfidf_score, 2)

    return hybrid_score

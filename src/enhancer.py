# resumeproject/src/enhancer.py

suggestion_bank = {
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

def suggest_enhancements(resume_text, predicted_category):
    suggestions = []
    expected_skills = suggestion_bank.get(predicted_category.upper(), [])
    for skill in expected_skills:
        if skill.lower() not in resume_text.lower():
            suggestions.append(f"✅ Consider adding '{skill}' to enhance your {predicted_category} resume.")
    return suggestions
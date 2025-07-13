# resumeproject/src/chatbot.py
from resume_generator import generate_resume
from job_matcher import match_resume_to_job
from enhancer import suggest_enhancements

print("🤖 Welcome to ResumeBot! Type 'exit' to quit.\n")

while True:
    print("What would you like to do?")
    print("1. Generate a resume")
    print("2. Match resume to a job description")
    print("3. Suggest improvements for a resume")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice.lower() == 'exit':
        print("👋 Goodbye!")
        break

    elif choice == '1':
        name = input("Full Name: ")
        title = input("Target Job Title: ")
        experience = input("Total Experience (e.g., 2 years, Fresher): ")
        skills = input("List your core technical skills (comma-separated): ")
        soft_skills = input("List your soft skills (comma-separated): ")
        education = input("Education (degree, university, year): ")
        certifications = input("Certifications (if any): ")
        achievements = input("Key achievements or awards: ")
        projects = input("Mention 1-2 significant projects: ")
        interests = input("Your interests or hobbies: ")

        print("\n📝 Generated Resume:\n")
        print(generate_resume(name, title, experience, skills, education,
                              certifications, projects, achievements, soft_skills, interests))

    elif choice == '2':
        resume = input("Paste your resume text: ")
        job_desc = input("Paste the job description: ")
        score = match_resume_to_job(resume, job_desc)
        print(f"\n🔍 Match Score: {score}")

    elif choice == '3':
        resume = input("Paste your resume text: ")
        category = input("Enter the predicted job category (e.g., BPO, HR, IT): ")
        suggestions = suggest_enhancements(resume, category)
        if suggestions:
            print("\n💡 Suggestions:")
            for s in suggestions:
                print(s)
        else:
            print("✅ Your resume looks great!")
    elif choice == '4':
        resume = input("Paste your resume text: ")
        recommend_jobs(resume)
    else:
        print("❗ Invalid option. Please enter 1, 2, or 3.")

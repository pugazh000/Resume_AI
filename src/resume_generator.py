# resumeproject/src/resume_generator.py

def generate_resume(name, title, experience, skills, education, certifications, projects, achievements, soft_skills, interests):
    resume = f"""
{name.upper()}
{title.title()}

Experience:
{experience}

Professional Summary:
Seeking a {title.lower()} role in a dynamic, growth-oriented organization. Skilled in {skills}. Passionate about solving real-world problems through technology, with a strong focus on performance, security, and user experience.

Skills:
- Technical: {skills}
- Soft: {soft_skills}

Education:
{education}

Certifications:
{certifications}

Projects:
{projects}

Achievements:
{achievements}

Interests:
{interests}

References:
Available upon request.
"""
    return resume.strip()



def ask_user_for_resume_info():
    print("📝 Let's generate your resume. Please answer the following prompts:")
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

    print("\n✅ Resume generated successfully!\n")
    return generate_resume(name, title, experience, skills, education, certifications, projects, achievements, soft_skills, interests)


# Example usage:
if __name__ == "__main__":
    final_resume = ask_user_for_resume_info()
    print(final_resume)

    # Optionally save to file
    with open("generated_resume.txt", "w", encoding="utf-8") as f:
        f.write(final_resume)
        print("\n💾 Resume saved to 'generated_resume.txt'")

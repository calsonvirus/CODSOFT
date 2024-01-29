def get_course_info(course):
    assignments = {"stats101": "Statistics project", "NMAT701": "Calculus assignment, Calculas project 1", "DSC101": "Data Scienece 1A"}
    exams = {"stats101": "Final exam in July", "NMAT701": "Final Exam in December", "DSC101": "Final Exam in July"}
    lecturers= {"stats101": "Dr. Whata", "NMAT701": "Dr. Shozi", "DSC101": "Dr. Tumo"}
    office= {"stats101": "Office 124 NAS Building","NMAT701": "Office 138 NAS Building ","DSC101": "Office 120 NAS Building"}
    contact={"stats101":"dr_whats_stats@varsity.com","NMAT701": "dr_shozi_pass@varsity.com","DSC101":"dr_tumo_A@varsity.com"}

    return f"""For {course.upper()}: Your Assignments are - {assignments.get(course, 'No assignments')},
      Exams - {exams.get(course, 'No exams')},
      Lecturer - {lecturers.get(course,"No Lecturere")},
      Consultation Office - {office.get(course,"No Office")},
      Contact Details of Lecturer - {contact.get(course,"No Contact Details")}"""

def get_general_tips():
    return """Make sure to attend lectures, complete assignments on time, and seek help when needed. Remember that time management is key!
     Take Calsons advices they are the best too. """

def first_year_assistant(user_input):
    #I have added atleast one greeting for all the official languages of the Northern Cape province for convience 
    greetings = ["hi", "hey", "hello","dumela","hy","gooday","goeie dag","dumela"]
    courses = ["stats101", "NMAT701", "DSC101"]
    resources = ["library", "tutoring center", "career services", "counseling"]
    study_tips_keywords = ["study tips", "how to study", "tips for exams","pass","module help","help","study"]

    user_input_lower = user_input.lower()

    # Check for greetings
    if any(greet in user_input_lower for greet in greetings):
        return "Hi! I am your First-Year Assistant. How can I help you?"

    # Check for course-related queries
    for course in courses:
        if course in user_input_lower:
            return get_course_info(course)

    # Check for information about campus resources
    #Take note that complex responsess would require complex logic which is not covered in this code.
    if any(resource in user_input_lower for resource in resources):
        return f"Sure, let me provide information about the {user_input}. (Note: For more information about {user_input} please contact you academic mentor for advice.)"

    # Provide general tips for studying 
    if any(keyword in user_input_lower for keyword in study_tips_keywords):
        return get_general_tips()

    return "I'm sorry, I didn't understand your query. Please ask about a specific course, campus resource, or study tips."

if __name__ == "__main__":
    print("First-Year Assistant: Hi! I am your First-Year Assistant. How can I help you?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("First-Year Assistant: Goodbye! Be sure to come again if you need assistance.")
            break
        response = first_year_assistant(user_input)
        print("First-Year Assistant:", response)

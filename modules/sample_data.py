class InstitutionalSampleData:
    """
    Centralized mock data repository providing realistic institutional records 
    for students, faculty, courses, and department audits across PragyanAI.
    """
    
    STUDENTS = [
        {"roll": "ECE2026_01", "name": "Aarav Sharma", "dept": "ECE", "term": "Sem 5", "attendance": "92.0%", "status": "Optimal"},
        {"roll": "ECE2026_02", "name": "Priya Patel", "dept": "ECE", "term": "Sem 5", "attendance": "84.0%", "status": "Good"},
        {"roll": "ECE2026_03", "name": "Rohan Verma", "dept": "ECE", "term": "Sem 5", "attendance": "68.0%", "status": "At-Risk"},
        {"roll": "ECE2026_04", "name": "Sateesh Ambesange", "dept": "ECE", "term": "Sem 5", "attendance": "84.7%", "status": "Safe"},
        {"roll": "ECE2026_05", "name": "Sneha Rao", "dept": "ECE", "term": "Sem 5", "attendance": "96.0%", "status": "Optimal"}
    ]

    FACULTY = [
        {"id": "FAC_01", "name": "Dr. Smitha Rao", "dept": "ECE", "course": "VLSI Design", "compliance": "100%"},
        {"id": "FAC_02", "name": "Prof. Anand Kumar", "dept": "ECE", "course": "Digital Systems", "compliance": "96.6%"},
        {"id": "FAC_03", "name": "Dr. Rajeshwari", "dept": "ECE", "course": "Signals & Theory", "compliance": "96.4%"},
        {"id": "FAC_04", "name": "Prof. Suresh Hegde", "dept": "ECE", "course": "Microprocessors", "compliance": "100%"}
    ]

    DEPARTMENTS = [
        {"name": "Computer Science & Engineering (CSE)", "students": 650, "turnout": "91.2%", "status": "Optimal"},
        {"name": "AI & Data Science (AIDS)", "students": 500, "turnout": "92.0%", "status": "Optimal"},
        {"name": "Electronics & Communication (ECE)", "students": 420, "turnout": "87.4%", "status": "Good"},
        {"name": "Mechanical Engineering (ME)", "students": 480, "turnout": "84.5%", "status": "Monitor"},
        {"name": "Civil Engineering (CE)", "students": 400, "turnout": "83.9%", "status": "Monitor"}
    ]

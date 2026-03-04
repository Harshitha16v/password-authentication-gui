def generate_ml_ideas():
    ml_projects = {
        "College": {
            "Problem": "Predict student performance",
            "Input": "Attendance, Study Hours, Assignment Scores",
            "Output": "Predicted Marks / Grade"
        },
        "Healthcare": {
            "Problem": "Disease risk prediction",
            "Input": "Age, BMI, Blood Pressure, Sugar Level",
            "Output": "Risk level (Low / Medium / High)"
        },
        "Shopping": {
            "Problem": "Product recommendation system",
            "Input": "Customer purchase history, browsing history",
            "Output": "Recommended products"
        }
    }
    print("\n🔹 Machine Learning Idea Generator\n")
    for domain, details in ml_projects.items():
        print("Domain:", domain)
        print("Problem:", details["Problem"])
        print("Input →", details["Input"])
        print("Output →", details["Output"])
        print("-" * 40)
generate_ml_ideas()
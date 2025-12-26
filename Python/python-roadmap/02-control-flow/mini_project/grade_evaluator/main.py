print("=== GRADE EVALUATOR ===")

score_input = input("Enter your exam score (0-100): ")

score = int(score_input)

if score < 0 or score > 100:
    print("Invalid score. Please enter a value between 0 and 100.")
elif score >= 90:
    print("Your grade is: A")
elif score >= 80:
    print("Your grade is: B")
elif score >= 70:
    print("Your grade is: C")
elif score >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

percentage = float(input("Enter the percentage: "))

if percentage < 25:
    grade = "D"

elif percentage >= 25 and percentage <= 45 :
    grade = "C"

elif percentage > 45 and percentage <= 50:
    grade = "B"

elif percentage >= 50 and percentage < 60 :
    grade = "B+"

elif percentage > 60 and percentage <= 80 :
    grade = "A"

elif percentage > 80 and percentage <= 100:
    grade = "A+"
    
print(f"Percentage: {percentage}%\nGrade: {grade}")

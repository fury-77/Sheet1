percentage = float(input("Enter the percentage: "))

if percentage > 90:
    grade = "A"

elif percentage > 80 and percentage <= 90:
    grade = "B"

elif percentage >= 60 and percentage <= 80:
    grade = "C"

elif percentage < 60 :
    grade = "D"
    
print(f"Percentage: {percentage}%\nGrade: {grade}")

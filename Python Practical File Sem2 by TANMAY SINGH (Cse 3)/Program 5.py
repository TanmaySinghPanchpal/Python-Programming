# Python Program to Grade a Score
score = float(input("Enter score between 0.0 and 1.0: "))

if 0.0 <= score <= 1.0:
    if score >= 0.9:
        print("Grade: A")
    elif score >= 0.8:
        print("Grade: B")
    elif score >= 0.7:
        print("Grade: C")
    elif score >= 0.6:
        print("Grade: D")
    else:
        print("Grade: E")
else:
    print("Error : Score is out of range!")

# function to calculate average
def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average

# function to determine grade
def get_grade(average):
    if average >= 90:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

# main program
try:
    marks = list(map(int, input("Enter marks for 5 subjects: ").split()))
    if len(marks) != 5:
        print("Please enter exactly 5 marks.")
    else:
        for m in marks:
            if m < 0 or m > 100:
                print("Marks must be between 0 and 100")
                exit()

        avg = calculate_average(marks)
        grade = get_grade(avg)

        print("Average Marks:", avg)
        print("Grade:", grade)

except ValueError:
    print("Please enter valid numbers.")











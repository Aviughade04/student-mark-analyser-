def calculate_grades(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    print(f"Average Marks: {average}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")

marks = [78, 85, 62, 90, 74]
calculate_grades(marks)

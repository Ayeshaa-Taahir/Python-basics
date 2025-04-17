# Each course has 50 marks
max_marks_per_course = 50
total_max_marks = max_marks_per_course * 5  

# Taking marks input from the user
course1 = float(input("Enter marks for Course 1 (out of 50): "))
course2 = float(input("Enter marks for Course 2 (out of 50): "))
course3 = float(input("Enter marks for Course 3 (out of 50): "))
course4 = float(input("Enter marks for Course 4 (out of 50): "))
course5 = float(input("Enter marks for Course 5 (out of 50): "))

# Calculate total, average, and percentage
total_marks = course1 + course2 + course3 + course4 + course5
average = total_marks / 5
percentage = (total_marks * 100) / total_max_marks

# Display the results
print("\n----- Result -----")
print("Total Marks:", total_marks, "/", total_max_marks)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
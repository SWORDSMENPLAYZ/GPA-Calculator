def calculate_gpa(grades):
      grade_lookup = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "F": 1.0,
      } 
      total_grade_points = 0
      total_credits = 0.0
      for i in range(grades):
          grade = input(f"Enter the grade for class {i+1}: ")
          credit = float(input(f"Enter the credit for class {i+1}: "))
          course_type = input(f"Enter the course type for class {i+1} (AP/Honors/Regular/IB): ")
          if grade.isnumeric():
            grade = int(grade)
            if grade >= 89.45 and grade <= 100:
              grade_value = 4.0
            if grade >= 79.45 and grade <= 89.44:
              grade_value= 3.0
            if grade >= 69.45 and grade <= 79.45:
              grade_value = 2.0
            if grade < 69.45:
              grade_value = 1.0
            if grade > 100 or grade < 0.1:
              print("Invalid Grade")
              break 
          else: 
            if grade in grade_lookup:
              grade_value = grade_lookup[grade]
            else:
              grade_value = 0
          if course_type == 'AP' or course_type == 'IB':
              grade_value += 1.0
          elif course_type == 'Honors': 
              grade_value += 0.0
          total_grade_points += grade_value * credit
          total_credits += credit
      if total_credits == 0:
          return "N/A"
      else:
          return total_grade_points / total_credits

while True:
  num_classes = int(input("How many classes are you taking? "))
  gpa = calculate_gpa(num_classes)
  rounded_gpa = round(gpa,1) #rounds gpa to nearest 10th
  print(f"Your GPA is: {rounded_gpa}")
  choice = input("Do you want to calculate another GPA? (y/n)")
  if choice.lower() == 'n':
      break

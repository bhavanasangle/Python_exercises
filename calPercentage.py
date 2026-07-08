#Write a Python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
#Percentage >= 90% : Grade A Percentage >= 80% : Grade B Percentage >= 70% : Grade C Percentage >= 60% : Grade D Percentage >= 40% : Grade E Percentage < 40% : Grade F

'''physics = float(input('Enter your physics marks '))
chemistry = float(input('Enter your physics marks '))
biology = float(input('Enter your physics marks '))
maths = float(input('Enter your physics marks '))
computer = float(input('Enter your physics marks '))'''

def studentsMarks(physics: int,chemistry: int,biology: int,maths: int,computer: int) -> int:
  totalMArks = physics + chemistry + biology + maths + computer
  return totalMArks

def calculate_grade(per):
  if(per >= 90):
    return 'A'
  elif per >= 80:
    return 'B'
  elif per >= 70:
    return 'C'
  elif per >= 60:
    return 'D'
  elif per >= 50:
    return 'E'
  elif per >= 40:
    return 'F'
  else:
    return 'fail'


percentage = studentsMarks(90,67,49,68,80) / 500 * 100
grade = calculate_grade(percentage)

print('Your persentage is', percentage)
print('Your grade is',grade)

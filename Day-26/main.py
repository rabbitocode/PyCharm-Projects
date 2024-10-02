import random


numbers = [1,2,3,4,5]

new_list = [n + 1 for n in numbers]
range_list = [n * 2 for n in range(1,5)]


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]
all_caps = [name.upper() for name in names if len(name) >= 5]

students_score = {student: random.randint(1,100) for student in names}


passed_students = {student: score for (student, score) in students_score.items() if score >= 60}

print(passed_students)




import pandas



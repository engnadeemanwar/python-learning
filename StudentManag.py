students = []
student_ids = {}

student_id = 1
while True:
   
    name = input(f"Please enter the student's name (or type 'stop' to finish): ")
    
   
    if name.lower() == 'stop':
        break
    
   
    if name in student_ids:
        print("This name is already in the list.")
    else:
        
        students.append((student_id, name))
        student_ids[name] = student_id
        student_id += 1


print("\nComplete List of Students (Tuples):")
print(students)


print("\nList of Students with IDs:")
for student in students:
    print(f"ID: {student[0]}, Name: {student[1]}")


total_students = len(students)
print(f"\nTotal number of students: {total_students}")


total_name_length = sum(len(student[1]) for student in students)
print(f"Total length of all student names combined: {total_name_length}")


longest_name_student = max(students, key=lambda x: len(x[1]))
print(f"The student with the longest name is: {longest_name_student[1]}")


shortest_name_student = min(students, key=lambda x: len(x[1]))
print(f"The student with the shortest name is: {shortest_name_student[1]}")

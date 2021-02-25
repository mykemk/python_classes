students = [
    {'name':'Kezia', 'age':10, 'course':'growing'},
    {'name':'John', 'age':20, 'course':'Writing'},
    {'name':'Cherono', 'age':70, 'course':'Programming'}
]

def show_details(students):
    for student in students:
        comment = 'lucky'
        
        if student['age'] < 15:
            comment = 'too young'
        else:
            comment = 'too old'
            
        print(f"{student['name']} is {comment} to study {student['course']} at the age of {student['age']}")
        
show_details(students)


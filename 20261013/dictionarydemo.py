grades = {'Agus':'B', 'Budi':'A','Chandra':'B+',
          'Dave':'A'}
print(grades)
grades['Edward']='B'
print(grades['Edward'])
print(grades)
del(grades['Agus'])
print(grades)

student01 = {
    "NRP":"C11260001",
    "Nama":"Jasen",
    "Umur":"18"
}

student02 = {
    "NRP":"C11260002",
    "Nama":"Jocelyn",
    "Umur":"18"
}

students = [student01,student02]

print(students[0]["Nama"])
print(students[0].get("NRP"))
print(students[1]["Nama"])
print(student02["Nama"])
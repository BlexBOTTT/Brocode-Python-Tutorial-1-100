# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Blex", 19, "male")

print(student.count("Blex"))
print(student.index("male"))

for i in student:
    print(i, end=" ")

print()
if "Blex" in student:
    print("Blex is here")

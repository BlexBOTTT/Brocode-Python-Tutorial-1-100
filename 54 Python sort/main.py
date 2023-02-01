# sort() method = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 30),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

age = lambda ages: ages[2]              # [] index number

# Only for Lists with tuple inside
#students.sort(key=age)                  # can reverse by adding iterable reverse=True

# Only for Tuple of tuples
sorted_students = sorted(students, key=age) # can reverse by adding iterable reverse=True

for i in sorted_students:
    print(i)

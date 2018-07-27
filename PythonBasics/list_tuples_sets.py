my_variable = "hello"

grades = [77,80,90] # List, elements can be added/removed
tuple_grades = (77,80,90,) #This is a tuple, tuples are immutible - They cannot be changed
#print((grade_one + grade_two + grade_tree) / 3)
set_grades = {77,80,90,100,100} #Sets must be unique and are unordered
print(set_grades)

#print(sum(grades) / len(grades))

grades.append(100)

print(grades)

#tuple_grades = tuple_grades + (100,) #comma required to show its a tuple
grades[0] =60
print(grades)


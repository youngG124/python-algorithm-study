korean = 92
english = 49
mathematics = 86
science = 81

# if (korean>=50 and english>=50 and mathematics >=50 and science >= 50) :
#     print(True)
# else :
#     print(False)

grade = [korean, english, mathematics, science]

result = True
for i in grade:
    if i < 50:
        result = False
print(result)
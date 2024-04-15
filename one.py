message = "hello python world///"
print(message)

name = "wang aib"
print(name.upper())
print(name.lower())
print(name.title())

first_name = "wang"
last_name  = "aid"
full_name =f"{first_name} {last_name}"
print(f"hello {full_name.title()}")

names = ['wang','cheng','liu']
print(names)
names.append('peng')
print(names)
names.insert(1,'zhang')
print(names)
del names[1]
print(names)

popped_names = names.pop()
print(names)
print(popped_names)

names.remove('cheng')
print(names)

lovers = ['about','know','please','no']
lovers.sort()
print(lovers)
lovers.sort(reverse=True)
print(lovers)
print(sorted(lovers))
print(lovers)
print(lovers[-1])

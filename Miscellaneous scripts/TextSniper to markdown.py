arraynew = []

k = print("Paste textsniper script")
while True:
    try:
        line = input()
    except EOFError:
        break
    arraynew.append(line)

array = []
print(arraynew)

for i in arraynew:
    if i != "":
        print("- [] " + i)
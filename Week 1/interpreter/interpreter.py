xyz = input("Expression: ").strip()

x = float(xyz[0])
z = float(xyz[4])

if xyz[2] == "+" :
    print(x+z)
elif xyz[2] == "-" :
    print(x-z)
elif xyz[2] == "*" :
    print(x*z)
elif xyz[2] == "/" :
    print(x/z)

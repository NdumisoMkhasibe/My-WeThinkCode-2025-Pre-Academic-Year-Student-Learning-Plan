def main():
    camel = input("camelCase: ").strip()
    output = snake(camel)
    print("snake_case:"+ output)

def snake(text):
    new_text = ""
    for char in text:
        if char.isupper():
            char = char.lower()
            new_text = new_text + "_" + char
        else:
            char = char.lower()
            new_text = new_text + char

    return new_text

main()

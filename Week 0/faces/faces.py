def main():
    text = input("Enter text with emoticons: ")
    text = convert(text)
    print(text)

def convert(message):
    message = message.replace(":)","🙂")
    message = message.replace(":(","🙁")
    return message

main()

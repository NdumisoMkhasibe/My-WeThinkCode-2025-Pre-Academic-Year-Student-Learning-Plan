
def main():
    text = input("Input: ").strip()
    final = omitter(text)
    print("Output: "+ final)

def omitter(msg):
    new_msg = ""
    for char in msg:
        if char in "aeiouAEIOU":
            pass
        else:
            new_msg = new_msg + char
    return new_msg

if __name__ == "__main__":
    main()

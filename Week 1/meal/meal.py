def main():
    clock = input("What time is it?: ").strip()
    clock = convert(clock)
    if 7.00 <= clock <= 8.00 :
        print("breakfast time")
    elif 12.00 <= clock <= 13.00 :
        print("lunch time")
    elif 18.00 <= clock <= 19.00 :
        print("dinner time")

def convert(time):
    if len(time) == 4:
        hrs = float(time[0])
        mins = (float(time[2:4])) / 60
        hrmin = round((hrs + mins),2)
        return (hrmin)
    else:
        hrs = float(time[0:2])
        mins = (float(time[3:5])) / 60
        hrmin = round((hrs + mins),2)
        return (hrmin)

if __name__ == "__main__":
    main()

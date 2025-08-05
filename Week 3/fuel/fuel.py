def main():
    answer = decifer()
    if answer <= 1 :
        print("E")
    elif answer >= 99 :
        print("F")
    else:
        print(f"{answer}%")

def decifer():
    while True :
        try :
            xy = input("Fraction: ").strip()
            x,y = xy.split("/")
            x = int(x)
            y = int(y)
            if x == 0:
                return 0
            elif x > y :
                pass
            else:
                ans = (x/y)*100
                ans = round(ans)
                return ans
        except ValueError:
            pass
        except ZeroDivisionError :
            pass

main()

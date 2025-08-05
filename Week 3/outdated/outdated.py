import re
while True :
    try:
        date = input("Date: ").strip()
        MM,DD,YY = date.split("/")
        if not MM.isdigit():
            continue
        if (1 <= int(MM) <= 12) and (1 <= int(DD) <= 30) :
            if len(MM) == 1:
                MM = "0"+ MM
            if len(DD) == 1 :
                DD = "0" + DD
            print(f"{YY}-{MM}-{DD}")
            break
        else:
            continue
    except ValueError :
        calender = {
        "January": "01" ,
        "February" : "02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12"
        }
        date = date.title()
        if "," not in date :
            continue
        YMD = re.split(r'\W+', date)
        M = YMD[0]
        D = YMD[1]
        if len(D) == 1:
            DD = "0" + D
        Y = YMD[2]
        if calender.get(M) is None:
            continue
        else:
            MM = calender.get(M)
            if (1 <= int(MM) <= 12) and (1 <= int(D) <= 31) :
                print(f"{Y}-{MM}-{DD}")
                break
            else:
                continue
    except IndexError :
        continue
    except EOFError :
        print()
        break

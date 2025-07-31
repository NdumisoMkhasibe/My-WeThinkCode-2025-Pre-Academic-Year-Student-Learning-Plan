def main():
    plate = (input("Plate: ").upper())
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #check lenght is between 2 and 6 characters
   if  not ( 2 <= len(s) <= 6 ) :
        return False

   #check first two characters are letters
   if  not (s[0].isalpha() and s[1].isalpha() ) :
        return False

   #Check for punctuation
   if  not s.isalnum():
       return False
     
   #Check all last digits and not equal to zero
   for i in range(len(s)):
       if s[i].isdigit():
           if s[i] == "0":
               return False
           if not s[i:].isdigit() :
               return False
           break
   return True

main()

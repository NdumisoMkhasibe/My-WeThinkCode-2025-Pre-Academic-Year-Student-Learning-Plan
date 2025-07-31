def main():
    fruit = input("Item: ").strip().title()
    answer = nutri_val(fruit)
    if answer is None :
        pass
    else:
        print("Calories:",answer)

def nutri_val(s):
    table = {
    "Apple":"130",
    "Avocado":"50",
    "Banana":"110",
    "Cantaloupe":"50",
    "Grapefruit":"60",
    "Grapes":"90",
    "Honeydew Melon":"50",
    "Kiwifruit":"90",
    "Lemon":"15",
    "Lime":"20",
    "Orange":"80",
    "Peach":"60",
    "Pear":"100",
    "Pineapple":"50",
    "Plums":"70",
    "Strawberries":"50",
    "Sweet Cherries":"100",
    "Tangerine":"50",
    "Watermelon":"80"
    }
    return table.get(s)

main()

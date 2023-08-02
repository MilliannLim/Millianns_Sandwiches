def get_string(m):
    user_input = input(m).strip()
    return user_input


def get_option(m):
    user_input = input(m).strip().upper()
    return user_input


def get_integer(m):
    user_input = int(input(m))
    return user_input


def view_menu(L):
    for i in range(0, len(L)):
        output = "{:<3} : {:10} --- ${:}".format(i, L[i][0], L[i][1])
        print(output)


def add_to_order(L, O):
    # show the sandwich menu to the user
    view_menu(L)
    sandwich = get_integer("What number sandwich would you like to add to your order?")
    if sandwich <= 5:
        sandwich_name = L[sandwich][0]
        price = L[sandwich][1]
        amount = get_integer("How many would you like?")
        if amount >= 6:
            print("Sorry, you have ordered too many sandwiches, the maximum amount of one sandwich is 5")
            return None  # the maxi is 5
        else:
            temp = [sandwich_name, price, amount]
            O.append(temp)
            output = ("{} {} has been added to your order".format(amount, sandwich_name))
            print(output)
    else:
        print("Sorry, this is not an option")
        return None


def review_order(O):
    if len(O) != 0:
        for i in range(0, len(O)):
            item_total = O[i][2]*O[i][1]
            output = "{:<3} : {} {:10} --- ${:} = ${}".format(i, O[i][2], O[i][0], O[i][1], item_total)
            print(output)
    else:
        print("Sorry, you haven't ordered anything yet")
        return None


def full_review(O, C, delivery_charge=3):
    total = 0
    if len(O) != 0:
        for i in range(0, len(O)):
            item_total = O[i][2]*O[i][1]
            total += item_total
            output = "{:<3} : {} {:10} --- ${:} = ${}".format("", O[i][2], O[i][0], O[i][1], item_total)
            print(output)
        if "Delivery" in C:
            total += delivery_charge
            output = "{:<3} : {} {:10} --- ${:} = ${}".format("", "", "Delivery Charge", 3, 3)
            print(output)
        # print total cost
        output = "Your total is: ${}".format(total)
        print(output)
    else:
        print("Sorry, you haven't ordered anything yet")
        return None
    if len(C) != 0:
        print("Your current details:")
        for i in range(0,len(C)-1, 2):
            output = "{}:  {}".format(C[i], C[i+1])
            print(output)
    else:
        print("You don't have any details yet")
        return None


def take_away_from_order(L, O):
    if len(O) != 0:
        view_menu(L)
        print("." * 100)
        print("You order is:")
        review_order(O)
        sandwich = get_integer("What number sandwich would you like to change the quantity for?")
        amount = get_integer("How many would you like to add/take away?")
        sandwich_name = O[sandwich][0]
        O[sandwich][2] -= amount
        if O[sandwich][2] <= 0:
            O.pop(sandwich)
            # take out of list
            output = "{} has been removed from your order".format(sandwich_name)
            print(output)
        else:
            output = ("You now have {} of {}".format(O[sandwich][2], O[sandwich][0]))
            print(output)
    else:
        print("Sorry, you haven't ordered anything yet")


def d_or_p(C):  # need to add a delivery fee, (would need to add to the total)
    # check if C is empty or not
    if len(C) != 0:
        choice = get_option("You already have Delivery/Pickup details, do you want to change them? Yes (Y) or No (N)")
        if choice == "Y":
            C.clear()
        else:
            print("Ok!")
            return None
    # starting fresh
    choice = get_option("Would you like your order delivered (D) or would you like to pick it up (P)?")
    if choice == "D":
        name = get_string("What's your name?")
        address = get_string("What's your address?")
        phone_number = get_integer("What's your phone number?")
        output = ("Hi {}, your order will be delivered to {}. We will call {} if a problem occurs".format(name, address, phone_number))
        print(output)
        C.append("Type")
        C.append("Delivery")
        C.append("Name")
        C.append(name)
        C.append("Address")
        C.append(address)
        C.append("Phone Number")
        C.append(phone_number)
    if choice == "P":
        name = get_string("What's your name?")
        import random
        num = random.randint(0, 100)
        output = ("Hi, {}, come to the counter when we call your number. Your number is {}".format(name, num))
        print(output)
        C.append("Type")
        C.append("Pick up")
        C.append("Name")
        C.append(name)
        C.append("Pick Up Number")
        C.append(num)


def start_over(O):   # clear_order
    review_order(O)
    if len(O) != 0:
        choice = get_option("Do you want to clear your order? Yes (Y) or No (N)")
        if choice == "Y":
            O.clear()
        if choice == "N":
            print("Ok!")
        return None


def main():
    menu_list = [
        ["Cheesy Meatball Sub", 20],
        ["Roast Beef and Onion Sandwich", 24],
        ["Grilled Pastrami Sandwich", 18.50],
        ["Chicken Cranberry Panini", 18],
        ["Vegan Pulled-Jackfruit Slider", 25],
        ["Tomato mozzarella and pesto Baguette", 20]
            ]
    order_list = []
    customer_list = []

    menu = """
    V: View menu
    A: Add new sandwich
    F: Full review
    E: Edit current sandwiches
    D: Delivery or Pickup
    S: Start over order
    Q: Quit
    
    """
    run = True
    print("Hi there! Welcome to Milliann's Sandwiches, How can I help you today?")
    while run is True:
        print(menu)
        choice = get_option("Please select your option: ->")
        print("." * 100)
        if choice == "V":
            view_menu(menu_list)
        if choice == "Q":
            print("Thank you for visiting Milliann's Sandwiches!")
            run = False
        if choice == "A":
            add_to_order(menu_list, order_list)
        if choice == "F":
            full_review(order_list, customer_list)
        if choice == "E":
            take_away_from_order(menu_list, order_list)
        if choice == "D":
            d_or_p(customer_list)
        if choice == "S":
            start_over(order_list)


main()

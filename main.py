def get_string(m):
    """Request string from user.

       :param m: string (string)
       :return: string
       """
    user_input = input(m).strip()  # this is so that if user puts a lower case, or accidentally add a space, the code won't throw an error and will just run normally
    return user_input


def get_yes_no(L):
    """Get Y or N from user.

    :param L: string
    :return: integer
    """
    run = True
    while run is True:  # while the code is running
        my_string = input(L).upper()
        if my_string == "Y":  # if user enters y
            return my_string
        elif my_string == "N":  # if user enters n
            return my_string
        else:
            print("Sorry, please try again")  # if user enters not y or n


def get_option(m):
    """Get option from user

    :param m: option (option)
    :return: option
    """
    user_input = input(m).strip().upper()  # So even if someone were to put a lower case or uppercase, the code would still run
    return user_input


def get_integer(m):
    """Request integer from user.

    :param m: string
    :return: integer
    """
    while True:
        try:
            user_input = int(input(m))
            return user_input
        except ValueError:  # if user enters something that's not a number, instead of throwing an error, it loops to give the user another chance to enter a number
            print("Sorry, please enter a number")


def get_letter(O):
    """Request letter from a list from user.

    :param O: list
    :return: None
    """
    run = True
    while run is True:
        user_choice = input("Please choose an option:").upper().strip()
        for i in range(0, len(O)):
            if user_choice == O[i][0]:
                return user_choice
        print("Oops, invalid entry, please try again")  # this is if the user enters something that isn't on the list, it won't throw an error and it will say "Oops invalid entry" instead


def view_menu(L):
    """View menu

    :param L: List
    :return:
    """
    for i in range(0, len(L)):
        if len(L[i]) != 2:
            print("Sublist is not the correct length")  # if it's wrong
            return None
        output = "{:<3} : {:10} --- ${:}".format(i + 1, L[i][0], L[i][1])  # by doing i + 1, it means that the list's index doesn't start at 0
        print(output)


def validate_integer(message, a, b):
    """Request limited integer from user.

    :param message: string
    :param a: integer
    :param b: integer
    :return: integer
    """
    # must be between a and b
    while True:
        try:
            my_integer = int(input(message))
        except ValueError:  # if user doesn't enter a number
            print("Sorry, invalid entry, please try again")
            continue
        if my_integer < a:  # If the user enters a number that is too small
            print("This number is too small, please try again")
        elif my_integer > b:  # If the user enters a number that is too big
            print("This number is too large, please try again")
        else:
            return my_integer


def validate_string_len(message, a, b):
    """Request limited length string from user.

    :param message: string
    :param a: integer
    :param b: integer
    :return: integer
    """
    # must be between a and b
    run = True
    while run is True:
        m = get_string(message)  # m = message
        m_len = len(str(m))
        if m_len < a:  # if user enters something that's too short (mainly if user doesn't enter anything)
            print("This entry is too short, please try again")
        elif m_len > b:  # if user enters somthing that's too long
            print("This entry is too large, please try again")
        else:
            return m


def find_name_index(L, n):
    """Find name of item from on index number.
    :param L: list
    :param n: string
    :return: integer
    """
    i = 0
    for x in L:
        if x[0] == n:
            return i
        i += 1
    return -1  # this is so that user can find the name of a sandwich from the index number


def add_to_order(L, O):
    """Add sandwiches to the customer's order

    :param L: list (sandwich menu)
    :param O: list (customer order list)
    :return: None
    """
    view_menu(L)  # show the sandwich menu to the user
    sandwich_index = validate_integer("Choose index number "
                                      "of sandwiches to order:", 1, len(L))  # this makes sure that the value the user puts in is valid and so it won't throw an error
    sandwich_index -= 1
    name = L[sandwich_index][0]
    index = find_name_index(O, name)
    if index != -1:  # if the user already ordered a sandwich, this means that their order isn't empty
        output = ("You currently have {} {} in your order, you can order up to {} more".format(O[index][2], name,
                                                                                               5 - O[index][2]))
        print(output)
        old_amount = O[index][2]  # This is what the user has previously ordered
        number = validate_integer("How many more would you like to add?:", 0, 5 - O[index][2])  # since the max is 5, need to do 5 - amount of sandwiches they already added so, they don't order more than the max
        print()
        O[index][2] = old_amount + number  # new amount
        output_message = "You now have {} {}s in your order." \
            .format(O[index][2], O[index][0])
        print(output_message)
    else:
        old_amount = 0  # it is 0 because the user hasn't ordered anything yet
        number = validate_integer("How many would you like to add? "
                                  "(max 5):", 0, 5)  # by showing the user that the max is 5, this gives the user a guide
        print()
        new_amount = old_amount + number
        output_message = "You added {} {}s to your order." \
            .format(new_amount, L[sandwich_index][0])
        print(output_message)
        temp = [L[sandwich_index][0], L[sandwich_index][1], new_amount]  # update list
        if new_amount != 0:
            O.append(temp)  # updates the order list


def review_order(O):
    """Review the customer's order

    :param O: List (customer order list)
    :return: None
    """
    if len(O) != 0:  # so that customer can see what they ordered
        for i in range(0, len(O)):
            item_total = O[i][2] * O[i][1]  # number of sandwiches times the cost is the total
            output = "{:<3} : {} {:10} --- ${:} = ${}".format(i+1, O[i][2], O[i][0], O[i][1], item_total)
            print(output)
    else:
        print("Sorry, you haven't ordered anything yet")  # this is just incase if the user hasn't ordered anything yet because it would come up blank anyway
        return None  # goes back to the menu


def full_review(O, C, delivery_charge=4):
    """Full review of what the customer ordered and their delivery details

    :param O: List (customer order list)
    :param C: List (customer detail list)
    :param delivery_charge: ($4 surcharge for delivery)
    :return: None
    """
    total = 0
    if len(O) != 0:
        for i in range(0, len(O)):
            item_total = O[i][2] * O[i][1]  # cost times number of sandwich
            total += item_total  # Total cost
            output = "{:<3} : {} {:10} --- ${:} = ${}".format("", O[i][2], O[i][0], O[i][1], item_total)
            print(output)
        if "Delivery" in C:
            total += delivery_charge
            output = "{:<3} : {} {:10} --- ${:} = ${}".format("", "", "Delivery Charge", 4, 4)  # $4 extra for delivery
            print(output)  # print total cost
        output = "Your total is: ${}".format(total)
        print(output)
    else:
        print("Sorry, you haven't ordered anything yet")  # just incase if the customer hasn't ordered anything yet
        return None
    if len(C) != 0:
        print("Your current details:")
        for i in range(0, len(C) - 1, 2):  # delivery details
            output = "{}:  {}".format(C[i], C[i + 1])
            print(output)  # This is the full review where it reviews what the customer's order as well as their delivery options
    else:
        print("You don't have any delivery details yet")  # need delivery details to see full review
        return None


def take_away(O):
    """Remove an item from order

    :param O: list (customer order list)
    :return: None
    """
    if len(O) == 0:  # if customer hasn't ordered anything, they can't take away any or else it will go into negatives
        print("You haven't ordered any sandwiches yet")
        return None
    print("In your current order you have:")  # showing the user their current order
    review_order(O)
    sandwich_index = validate_integer("Choose which sandwich you would like to remove:", 1, len(O))  # asking the user which sandwich they want to remove
    sandwich_index -= 1
    print()
    number = validate_integer("How many would would you like to remove? "
                              "(please use numbers):", 0, O[sandwich_index][2])  # asking the user how many sandwiches they want to remove
    O[sandwich_index][2] -= number
    if O[sandwich_index][2] == 0:
        print()
        output = ("You have removed {} from your order".format(O[sandwich_index][0]))
        print(output)
        print()
        O.pop(sandwich_index)  # gets rid of the sandwich from order
        if len(O) == 0:
            print("Your order is now empty")  # sad
        else:
            print("In your order you now have:")
            review_order(O)   # this is if the user made a mistake and wanted to change the order a little
    elif O[sandwich_index][2] != 0:
        print()
        output_message = "Your order is:"
        print(output_message)
        review_order(O)  # shows order


def d_or_p(C):
    """Delivery or Pickup option

    :param C: List (customer detail list)
    :return: None
    """
    if len(C) != 0:   # check if C is empty or not
        choice = get_option("You already have Delivery/Pickup details, do you want to change them? Yes (Y) or No (N)")
        if choice == "Y":
            C.clear()  # gets rid of the previous delivery or pick up details
        elif choice == "N":
            print("Ok!")  # goes back to main menu because the user doesn't want to change the details
            return None
        else:
            print("Sorry this isn't an option")  # wasn't one of the options I gave
            return None
    # starting fresh
    choice = get_option("Would you like your order delivered (D) or would you like to pick it up (P)?")
    if choice == "D":  # delivery
        run = True
        while run is True:
            name = validate_string_len("Please enter your name:", 1, 100) \
                .capitalize()  # punctuation is important
            address = validate_string_len("Please enter your street address "
                                          "and suburb:", 5, 200)
            get_num = True
            while get_num is True:
                phone_number = validate_string_len("Please enter your phone number:", 5, 12).strip().replace(" ", "")
                if phone_number.isdigit():  # NEED TO BE NUMBER
                    get_num = False
                else:
                    print("Sorry, invalid entry, please enter only digits")
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
            return None
    elif choice == "P":
        run = True
        while run is True:
            name = validate_string_len("Please enter your name:", 1, 100) \
                .capitalize()
            import random  # random number for like when restaurants call your number when you pick up from front desk
            num = random.randint(0, 100)  # by giving it a range between 0 and 100, it is more realistic to the real world
            output = ("Hi, {}, come to the counter when we call your number. Your number is {}".format(name, num))
            print(output)
            C.append("Type")
            C.append("Pick up")
            C.append("Name")
            C.append(name)
            C.append("Pick Up Number")
            C.append(num)
            return None
    else:
        print("Sorry this is not an option")
        return None


def start_over(O):
    """Start over order

    :param O: List (customer order list)
    :return: None
    """
    # clear order so if someone wanted to start over, instead of having to delete the sandwiches individually or changing their delivery options, they can just start over
    review_order(O)  # shows order
    if len(O) != 0:
        choice = get_option("Do you want to clear your order? Yes (Y) or No (N)")
        if choice == "Y":
            O.clear()
        if choice == "N":
            print("Ok!")
        else:
            print("Sorry this isn't an option")  # not an option
        return None


def confirm_order(O, C):
    """Confirm order before buying

    :param O: List (customer order list)
    :param C: List (customer detail list)
    :return: None
    """
    if len(O) == 0:   # need to check if they have filled in everything
        print("Sorry you have not ordered anything yet")
        return None
    if len(C) == 0:
        print(
            "Sorry, you have not filled in your delivery details yet")  # can't finish an order without the delivery details!
        return None
    else:
        full_review(O, C, delivery_charge=4)
        choice = get_option("Would you like to confirm this order? Yes (Y) or No (N)")
        if choice == "N":
            print("Ok!")
            return None  # nothing happens
        if choice == "Y":
            print("Thank you for visiting Milliann's Sandwiches, hope you enjoy your meal!")  # need help
            C.clear()  # clears both the lists so the next customer can order
            O.clear()
        else:
            print("Sorry this isn't an option")


def main():
    menu_list = [  # yummy
        ["Cheesy Meatball Sub", 20],
        ["Roast Beef and Onion Sandwich", 24],
        ["Grilled Pastrami Sandwich", 18.50],
        ["Chicken Cranberry Panini", 18],
        ["Vegan Pulled-Jackfruit Slider", 25],
        ["Tomato mozzarella and pesto Baguette", 20],
        ["Plain cheese toastie", 10]
    ]
    order_list = []
    customer_list = []

    menu = """
    V: View menu
    A: Add new sandwich
    F: Full review
    T: Take away sandwiches from order
    D: Delivery or Pickup
    S: Start over order
    C: Confirm order
    Q: Quit
    
    """
    run = True
    print("Hi there! Welcome to Milliann's Sandwiches, How can I help you today?")
    while run is True:
        print(menu)
        choice = get_option("Please select your option: ->")
        print("." * 100)
        if choice == "V":
            print("Sandwich Menu:")
            view_menu(menu_list)
        elif choice == "Q":
            print("Thank you for visiting Milliann's Sandwiches!")
            run = False
        elif choice == "A":
            add_to_order(menu_list, order_list)
        elif choice == "F":
            full_review(order_list, customer_list)
        elif choice == "T":
            take_away(order_list)
        elif choice == "D":
            d_or_p(customer_list)
        elif choice == "S":
            start_over(order_list)
        elif choice == "C":
            confirm_order(order_list, customer_list)
        else:
            print("Sorry, please try again")


main()

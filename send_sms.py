import SMS, getpass

if __name__ == '__main__':
    # email = input("email: ") #'personaldeveloper9@gmail.com'
    # password = getpass.getpass(prompt="password: ") #jadjaq-3toxte-xyNzas
    #
    email = 'personaldeveloper9@gmail.com'
    password = 'jadjaq-3toxte-xyNzas'
    message = "The end is near"


    SMS.send_message(email=email, password=password, message=message)

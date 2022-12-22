# Case Study: Virtual Assistant using Python (Assitant.py)

import speech_recognition as sr
import smtplib
import pyttsx3
import datetime
import pyjokes
import random

class Assistant():

    def __init__(self, name):

        self.name = name
        self.initialize()

    def run(self):

        while True:

            menu_option = "1. Change My Name\n2. Create Schedue\n3. View Schedule\n4. Random Jokes\n5. Send Email\n0. Exit"

            print("\n************************************")
            print("Hello Python, my name is " + self.name + ", how can i help you?")
            print(menu_option)
            print("**************************************")

            menu = input("which one do you want?")

            if menu == "1":
                name = input("input new name: ")
                self.change_name(name)
            elif menu == "2":
                self.create_schedule()
            elif menu == "3":
                self.view_schedule()
            elif menu == "4":
                self.random_jokes()
            elif menu == "5":
                self.send_email()
            elif menu == "0":
                print("Good Bye!")
                break
            else:
                print("please try again")

    def initialize(self):
        print("New Virtual Assitant has been created succesfully")
        input("- Press ENTER -")

    def change_name(self, name):
        self.name = name
        print("\nMy name has been changed.")
        input("- Press ENTER -")

    def create_schedule(self):
        file = open("schedule.txt", "a")
        schedule = input("\nPlease input your agenda: (format : dd/mm/yyyy - agenda_name)\n")
        file.write(schedule + "\n")
        file.close()
        print("\nNew schedule has been created.")
        input("- Press ENTER -")

    def view_schedule(Self):
        print("\nHere is list of your schedule:")
        file = open("schedule.txt", "r")
        print(file.read())
        file.close()

        input("- Press ENTER -")

    def random_jokes(self):
        jokes=[
            "Debuuging is like being the detective in a crime movie where you're also the murderer at the same time.",
            "I visited my friend at this new house. He told me to make myself at home. So i threw him put. I hate having visitors",
            "To whoever stole my copy of microsoft office, i will find you. You have my word!"]

        while True:

            print(random.choice(jokes))
            is_again = input("again [Yes/No]? ")

            if is_again.lower() == "no" or is_again.lower() == "0" : break

    def send_email(self):

        sender = ('herizkiwahyusaputra@gmail.com')
        password = ('...................')
        receiver = ['herizkiwsrvr@gmail']

        file = open("receiver_list.txt", "r")
        for x in file:
            receiver.append(x)

        subject = "Greetings"
        body = "Hello, I hope you have a great day"

        message = "subject: %s\n\n%s\n\nSent from %s." % (subject, body, self.name)

        try:
            #Create SMTP Session
            smtp = smtplib.SMTP('smtp.gmail.com', 587)

            #Use TLS to add security
            smtp.starttls()

            #User Authentication
            smtp.login(sender, password)

            #Sending the Email
            smtp.sendmail(sender, receiver, message)

            #Terminating the session
            smtp.quit()
            print("Email sent succesfully")

        except Exception as e:
            print("Error message:", str(e))

            input("- Press ENTER -")

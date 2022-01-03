import pandas as pd
from bs4 import BeautifulSoup



                #############
                #           #
                # MAIN CODE #
                #           #
                #############



running_variable=1

while running_variable!=0:
    print()
    print("         #################")
    print("         ##             ##")
    print("         ##  MAIN MENU  ##")
    print("         ##             ##")
    print("         #################")

    print()
    print("What would you like to do :")
    print()
    print("1) Inspect index.html")
    print("2) Modify template")
    print("0) Exit.")
    print()
    choose_desire=input("Enter your choice: ")

    if choose_desire=="1":



    elif choose_desire=="2":



    elif choose_desire=="0":
        continue_exit=input("Do you want to exit (y/n)? ")
        if continue_exit=="y":
            running_variable=0

    else:
        print()
        print("Please enter a valid choice.")






                ##########################
                #                        #
                #  CHANGE TEMPLATE MENU  #
                #                        #
                ##########################


def change_template_menu(dataset):

    running_variable=1

    while running_variable!=0:
        print()
        print("         ############################")
        print("         ##                        ##")
        print("         ##  CHANGE TEMPLATE MENU  ##")
        print("         ##                        ##")
        print("         ################~###########")

        print()
        print("What would you like to do :")
        print()
        print("1) Load webpages list")
        print("2) Modify webpages")
        print("0) Exit.")
        print()
        choose_desire=input("Enter your choice: ")

        if choose_desire=="1":



        elif choose_desire=="2":



        elif choose_desire=="0":
            continue_exit=input("Do you want to return (y/n)? ")
            if continue_exit=="y":
                running_variable=0

        else:
            print()
            print("Please enter a valid choice.")




    pages_to_change = pd.read_csv("webpages.csv", sep=";")
    pages_to_change["webpage"]

    for webpage in pages_to_change["webpage"]:
    with open(webpage) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    tag=soup.footer
    tag.string="'\n                miguelmath 2022\n          "
    html = soup.prettify("utf-8")
    with open(webpage, "wb") as file:
        file.write(html)

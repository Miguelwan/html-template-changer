import pandas as pd
from bs4 import BeautifulSoup





def inspect_html(file_to_inspect):

    with open(file_to_inspect) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    tag=""
    modification=""
    order=""
    change_made=0

    running_variable=1

    while running_variable!=0:
        print()
        print("         ##########################")
        print("         ##                      ##")
        print("         ##  INDEX EXPLORE MENU  ##")
        print("         ##                      ##")
        print("         ##########################")

        print()

        print("What would you like to do :")
        print()
        print("1) Print", file_to_inspcet)
        print("2) Select id")
        print("3) Select tag")
        print("4) Select attribute")
        print("5) Show selection")
        print("6) Change content")
        print("8) Reset changes")
        print("9) Reset selection")
        print("0) Return to main menu.")
        print()
        choose_desire=input("Enter your choice: ")


        if choose_desire=="1":
            print(soup)

        elif choose_desire=="2":
            selected_id=input("Enter the id of the tag you want to modify: ")
            order=order+".find(id='"+selected_id+"')"

        elif choose_desire=="3":
            selected_tag=input("Enter the tag of the section you want to modify: ")
            order=order+"."+selected_tag

        elif choose_desire=="4":
            print("If your selection only contains text, then write 'string' as the attribute to modify.")
            selected_attr=input("Enter the attribute of the tag you want to modify: ")
            if selected_attr=="string":
                order=order+".string"

            else:
                order=order+"['"+selected_attr+"']"

        elif choose_desire=="5":
            print()
            print_order="print(soup"+order+")"
            exec(print_order)

        elif choose_desire=="6":
            if change_made==1:
                was_saved=input("Warning: The changes made in 'Inspect html file' are only a preview. Making a new preview will erase the previous one. Would you like to proceed (y/n)?")
                if was_saved=="y":
                    with open(file_to_inspcet) as fp:
                        soup = BeautifulSoup(fp, 'html.parser')
                    tag="soup"+order
                    soup, modification=modify_content(soup, tag)

                elif was_saved=="n":
                    print("check the selection you have made, with option 5. You can reset a mistaken selection with option 9.")

            elif change_made==0:
                change_made=1
                tag="soup"+order
                soup, modification=modify_content(soup, tag)
        
        elif choose_desire=="8":
            reset_changes=input("Would you like to reset the changes made so far (y/n)? ")
            if reset_selection=="y":
                with open(file_to_inspcet) as fp:
                    soup = BeautifulSoup(fp, 'html.parser')
                modification=""
                tag=""

        elif choose_desire=="9":
            reset_selection=input("Your selection is "+order+" would you like to reset this selection (y/n)? ")
            if reset_selection=="y":
                order=""
                tag=""

        elif choose_desire=="0":
            continue_exit=input("Do you want to return (y/n)? ")
            if continue_exit=="y":
                running_variable=0

        else:
            print()
            print("Please enter a valid choice.")

    return(tag, modification)



                ####################
                #                  #
                #  MODIFY CONTENT  #
                #                  #
                ####################


def modify_content(soup, tag):
    modification=""
    confirm_selection=input("Your selection is "+tag+" would yo like to confirm this selection (y/n)? ")
    if confirm_selection=="y":
        modification=input("Please enter the new information: ")
        exec(tag+"=modification")

    return(soup, modification)




                ##########################
                #                        #
                #  CHANGE TEMPLATE MENU  #
                #                        #
                ##########################


def change_template_menu(tag, modification):

    pages_selected=0
    running_variable=1

    while running_variable!=0:
        print()
        print("         ############################")
        print("         ##                        ##")
        print("         ##  CHANGE TEMPLATE MENU  ##")
        print("         ##                        ##")
        print("         ############################")

        print()
        print("What would you like to do :")
        print()
        print("1) Load webpages list")
        print("2) Modify webpages")
        print("0) Return to main menu.")
        print()
        choose_desire=input("Enter your choice: ")

        if choose_desire=="1":
            pages_selected=1
            pages_to_change = pd.read_csv("webpages.csv", sep=";")
            print("Webpages loaded")
            print()


        elif choose_desire=="2":
            if pages_selected==1:
                for webpage in pages_to_change["webpage"]:
                    print("modifying:", webpage)
                    with open(webpage) as fp:
                        soup = BeautifulSoup(fp, 'html.parser')
                    exec(tag+"=modification")
                    html = soup.prettify("utf-8")
                    with open(webpage, "wb") as file:
                        file.write(html)
                        
            else:
                print("No webpages have been loaded.")


        elif choose_desire=="0":
            continue_exit=input("Do you want to return (y/n)? ")
            if continue_exit=="y":
                running_variable=0

        else:
            print()
            print("Please enter a valid choice.")



                #############
                #           #
                # MAIN CODE #
                #           #
                #############


tag=""
modification=""
file_to_inspect="index.html"
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
    print("1) Inspect html file")
    print("2) Modify template")
    print("0) Exit.")
    print()
    choose_desire=input("Enter your choice: ")

    if choose_desire=="1":
        file_to_inspect=input("What is the name of the file that you want to change (include the extension .html)?")
        tag, modification=inspect_html(file_to_inspect)
        print(tag)


    elif choose_desire=="2":
        if tag="" or modification="":
            print("No change or selection has been made, please go to 'Inspect html file'.")
        else:
            change_template_menu(tag, modification)


    elif choose_desire=="0":
        continue_exit=input("Do you want to exit (y/n)? ")
        if continue_exit=="y":
            running_variable=0

    else:
        print()
        print("Please enter a valid choice.")


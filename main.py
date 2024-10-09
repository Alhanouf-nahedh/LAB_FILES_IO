def to_do_list():
    while True:
        new_item = input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no. ')
        if new_item == "y":
            add_new_item = input("type in your new To-Do item ")
            file = open("to_do.txt", "a", encoding="utf-8")
            file.write(add_new_item + "\n")
            file.close()
        elif new_item == "n":
            list_items = input('do you want to list your To-Do items ? answer "y" for yes and "n" for no.')
            if list_items == "y":
                file = open("to_do.txt", "r", encoding="utf-8")
                content = file.readlines()
                print(content)  
                file.close()
                if content:
                    for l in content:
                        print(l)
                else:
                        ("empty")    
            else:
                break
        
to_do_list()

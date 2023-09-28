def adding_definition(definitions, key, definition):
    definitions[key] = definition
    print("Definition added succesfully!")

def find_definition(definitions, key):
    if key in definitions:
        print(definitions[key])
    else:
        print("There is no definition called:", key)    

def delete_definition(definitions, key):
    if key in definitions:
        del definitions[key]
        print("Succesfully removed definition called:", key)
    else:
        print("There is no definition called:", key)


definitions = {}
 
while(True):
    print("1: Add definition")
    print("2: Find definition")
    print("3: Delete definition")
    print("4: End programm")
 
    wybor = input("What you want to do? ")

    if (wybor == "1"):
        key = input("Give a key (word) to be defined: ")
        definition = input("Give definition: ")
        adding_definition(definitions, key, definition)
    elif (wybor == "2"):
        key = input("What are you looking for? ")
        find_definition(definitions, key)
    elif (wybor == "3"):
        key = input("Which definition you want to be deleted? ")
        delete_definition(definitions, key)
    elif (wybor == "4"):
        print("SEE YOU NEXT TIME!")
        break
    else:
        print("You give something out of range")

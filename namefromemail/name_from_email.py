# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter
# email = str(input("elek.viz@exam.com")

def new_function(email):
    name_split = email.split(".")
    first_name = name_split[0]
    name_split2 = name_split[1]
    look_up_last_name = name_split2.split("@")
    last_name = look_up_last_name[0]
    name_from_email = (last_name).title() + " " + (first_name).title()
    print(name_from_email)
new_function("elek.viz@exam.com")
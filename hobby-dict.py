# * Create a dictionary to store the following:
#   * Your name
#   * Your age
#   * A list of a few of your hobbies
#   * A dictionary of a few times you wake up during the week
# * Print out your name, how many hobbies you have and a time you get up during the week.

my_dictionary = {
    "name": "Pablo",
    "age": 29,
    "hobbies": ["hacking", "snacking", "fracking", "tennis"],
    "wake up times": {
        "Sun": "11 AM",
        "Mon": "6 AM",
        "Tue": "6 AM",
        "Wed": "6 AM",
        "Thurs": "6 AM",
        "Fri": "6 AM",
        "Sat": "9 AM",
    },
}

print(
    f'Hello I am {my_dictionary["name"]} and my hobbies are {my_dictionary["hobbies"]}.'
)

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username, password = input("Username: "), input("Password: ")
dash = "-" * 48

if users.get(username) == password:
    print(f"{dash}\nWelcome to the app, {username}\nWe have 3 texts to be analyzed.\n{dash}")
    
    selection = input("Enter a number btw. 1 and 3 to select: ")
    if selection.isdigit() and 1 <= int(selection) <= 3:
        text = TEXTS[int(selection) - 1]
        words = text.split()
        words = [''.join(char for char in word if char.isalnum()) for word in words]

        stats = {
            "total": 0,
            "titlecase": 0,
            "uppercase": 0,
            "lowercase": 0,
            "numeric": 0,
            "sum_numbers": 0
        }

        for word in words:
            stats["total"] += 1
            if word.istitle():
                stats["titlecase"] += 1
            if word.isupper() and word.isalpha():
                stats["uppercase"] += 1
            if word.islower() and word.isalpha():
                stats["lowercase"] += 1
            if word.isnumeric():
                stats["numeric"] += 1
                stats["sum_numbers"] += int(word)

        print(
        f"There are {stats['total']} words in the selected text.",
        f"There are {stats['titlecase']} titlecase words.",
        f"There are {stats['uppercase']} uppercase words.",
        f"There are {stats['lowercase']} lowercase words.",
        f"There are {stats['numeric']} numeric strings.",
        f"The sum of all the numbers is {stats['sum_numbers']}.",
        dash,
        f"{'LEN':>3}|{'OCCURENCES':^20}|{'NR.':>2}",
        dash,
        sep="\n"
        )

        lengths = {len(word): 0 for word in words if word.isalnum()}
        for word in words:
            if word.isalnum():
                lengths[len(word)] += 1

        for length, count in sorted(lengths.items()):
            print(f"{length:>3}|{'*' * count:<20}|{count:>2}")
    else:
        print("Your input was incorrect, terminating the program.")
else:
    print("Unregistered user, terminating the program.")

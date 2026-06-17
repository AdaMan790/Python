Name1 = input("Enter 1st name: ")
Name2 = input("Enter 2nd name: ")
Year = input("Enter year: ")

Name1_splitted = Name1[0]
Year_splitted = Year[-2:]

Username = Name1_splitted + Name2 + Year_splitted

print(Username)
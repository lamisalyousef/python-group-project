# Class List Manager - Group 4
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====
# Written by: Ghala Albedairi (task 2)
def search_name(names, name):
    if name in names:
        return True
    else:
        return False


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    name = input("Enter a name to search: ")
    print("Search result:", search_name(names, name))
    
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))

main()


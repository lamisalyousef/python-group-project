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
# Written by: Raneem Almutiri (task 3)
def sort_names(names):
    return sorted(names)

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    name = input("Enter a name to search: ")
    print("Search result:", search_name(names, name))
    print("Sorted names:", sort_names(names))
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))

main()


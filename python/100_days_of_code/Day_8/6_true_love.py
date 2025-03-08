# # v1
def calculate_love_score(name1, name2):
    t = name1.lower().count('t')
    r = name1.lower().count('r')
    u = name1.lower().count('u')
    e = name1.lower().count('e')
    l = name1.lower().count('l')
    o = name1.lower().count('o')
    v = name1.lower().count('v')
    t2 = name2.lower().count('t')
    r2 = name2.lower().count('r')
    u2 = name2.lower().count('u')
    l2 = name2.lower().count('l')
    o2 = name2.lower().count('o')
    v2 = name2.lower().count('v')
    e2 = name2.lower().count('e')
    print((t+r+u+e+t2+r2+u2+e2), (l+o+v+e+l2+o2+v2+e2), sep="")

first_name = input("Enter First Name: ")
second_name = input("Enter Second Name: ")
calculate_love_score(first_name, second_name)

# v2
# def calculate_love_score(name1, name2):
#     combined_names = (name1 + name2).lower()
    
#     true_count = sum(combined_names.count(char) for char in "true")
#     love_count = sum(combined_names.count(char) for char in "love")
    
#     print(f"{true_count}{love_count}")

# first_name = input("Enter First Name: ")
# second_name = input("Enter Second Name: ")
# calculate_love_score(first_name, second_name)

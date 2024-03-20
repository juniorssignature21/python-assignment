# Capitalize
name = input("what's your name? ").capitalize()

print("hello"+ " " + name)


# Casefold
hubby = input("what's your hubby? ").casefold()

print(f"I love {hubby} too")

# Center
location = input("where do you reside? ").center(4)

print(f"{location}is a nice place to stay")

# count
count = ["john", "favour", "prince", "john"].count("john")

print(count)

# endswith
world = input("write a correct sentence ").endswith(".")

print(world)

# expandtabs
expand = "say h\te\tl\tl\to "

x = expand.expandtabs(4)

print(x)

#  find
hi = "hello, welcome to my world".find("my")

print(hi)

# format
Fruit = input("which fruit do you want to buy? ")

fruit_price = 40

match Fruit.capitalize():
    case "Apple" | "Orange" | "Mango" | "Pineaple" | "Banana" | "cherry":
        print(f"${fruit_price:.2f}")
    case _:
        print("not available!")

# format_map 
sample_string = {'firstname':'Jane','lastname':'Doe'}

print('{firstname} {lastname}'. format_map(sample_string))

# 
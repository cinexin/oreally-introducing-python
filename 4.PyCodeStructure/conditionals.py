disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

color = "puce"
if color == "red":
    print ("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of that colour")

an_empty_list = []
if an_empty_list:
    print ("It seems there's something here")
else:
    print ("Nothing here!")

vowels = "aeiou"
letter = 'o'
if (letter in vowels):
    print("We have a vowel there")
else:
    print("Not a vowel")
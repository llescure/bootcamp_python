from generator import generator

# Test 1

print("\nTest 1\n")
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)

# Test 2

print("\nTest 2\n")
text = 1.0
for word in generator(text, sep=" "):
    print(word)

#Test 3

print("\nTest 3\n")
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)

#Test 4

print("\nTest 4\n")
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)

#Test 5

print("\nTest 5\n")
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

# Test 6

print("\nTest 6\n")
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="bonjour"):
    print(word)

# Test 7

print("\nTest 7\n")
text = "Mes amis, aujourd'hui, est un grand jour. Moi, je, personnellement, \
        pense donc je suis"
for word in generator(text, sep=", "):
    print(word)

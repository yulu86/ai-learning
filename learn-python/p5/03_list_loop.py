letters = ["a", "b", "c", "d"]

#
for letter in enumerate(letters):
    print(letter[0], letter[1])

# unpack
for index, letter in enumerate(letters):
    print(index, letter)


# add
letters.append("e")
letters.insert(0, "-")
print(letters)

# remove
letters.pop()
letters.remove("b")
del letters[0:3]
# letters.clear()
print(letters)

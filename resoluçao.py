letters = {
    "a": "e",
    "b": "f",
    "c": "g"
}

x = raw_input("Reading: ")

for l in letters:
    x = x.replace(l, letters[l])

print x
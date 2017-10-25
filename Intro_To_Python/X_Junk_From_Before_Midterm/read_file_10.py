# read first ten characters
with open('file_example.txt', 'r') as example_file:
    first_ten_chars= example_file.read(10)
    the_rest= example_file.read() # cursor moved to 11thcharacter
print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)

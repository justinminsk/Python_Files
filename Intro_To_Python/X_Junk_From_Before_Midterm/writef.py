def writef():
    file = open('topics.txt', 'w')
    return(file.write('Computer Science 111')) # will return the number of characters written
    file.close()

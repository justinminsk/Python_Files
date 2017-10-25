def backup(writefile):
    newtitle = input('Enter new file name')  # get new title
    newtitle = newtitle + '.bak'
    with open(writefile, 'r') as file:  # read the old file
        with open(newtitle, 'w') as title:  # write the new file
            for text in file:  # read all of the text
                text = text  # save the text as a variable
                title.write(text)  # write the new file


if __name__ == '__main__':  # Run the rewrite
    backup('test.txt')
    # run using test.txt
    # test.txt has:
    # this is a text
    # doc
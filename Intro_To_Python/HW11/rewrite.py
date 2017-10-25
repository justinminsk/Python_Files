import os.path


def rewrite(writefile):
    while os.path.isfile(writefile):  # sees if the file exsits
        overwrite = input('The file exists. Do you want to overwrite it (1), give it a new name (2), or cancel(3).')
        # menu
        if overwrite == '1':
            print('I will overwrite the ' + writefile + ' file.')
            with open(writefile, 'w') as file:  # write over the file
                newtext = input('Enter you new text')  # get new text to put in the file
                file.write(newtext)  # write the new text into file
            break  # end loop
        elif overwrite == '2':
            print('I will now change the name of ' + writefile + ' file')
            newtitle = input('Enter new file name with .txt')  # get new title
            with open(writefile, 'r') as file:  # read the old file
                with open(newtitle, 'w') as title:  # write the new file
                    for text in file:  # read all of the text
                        text = text     # save the text as a variable
                        title.write(text)  # write the new file
            break  # end loop
        elif overwrite == '3':
            return 'Canceling'  # ends the rewrite
        else:
            print('Invalid key pressed')  # print to let user know what they did wrong
            continue  # restart loop


if __name__ == '__main__':  # Run the rewrite
    rewrite('test.txt')  # run using test.txt
    # test.txt has:
    # this is a text
    # doc

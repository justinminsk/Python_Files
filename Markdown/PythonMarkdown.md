# Markdown in a Python Shell
Markdown can be writen in a python shell and the code can be turned into a block with a 4 space indention.
For example:

    python_string = 'Hello World'
    print(python_string)

The problem with doing it in the shell is that while converting to html is easy with the cmd line:

    python -m markdown -x codehilite some_markdown.md > body.html
    
or:
    
    python -m markdown input.md > output.html

It does not run the code like an RMarkdown file does with R and knitr. My previous post call Pokemon shows is done in 
this manner since as I will show with the next post RMarkdown would not work for a full exploratory analysis like my 
Pokemon project, even thou it can run blocks of python.
# This script opens a file, reads the file, and counts the number of times 
# the letter "e" appears (in either upper or lower case).
# The user enters the name of the file to be read on the command line after writing
# the name of the script ("07_numberofes"). 
# The file to be read should ideally be saved within the same directory as the program, to make it easier to
# retrieve the file path when typing the name of the text file on the command line.

# References: 
# https://www.gutenberg.org/files/786/786-0.txt  (source of text file)
# https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
# https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
# https://www.programiz.com/python-programming/methods/string/count


# To read the file from the command line, we need to import and use the sys module.
import sys

# This equates the name of the file to be read to the first argument on the command line
# (that is, the argument following the name of the python script itself)
filename = sys.argv[1]

# This opens the file in text mode and read its contents.
with open(filename, 'rt') as f:
    content = f.read()

# The count method returns the number of times a given substring ("e" or "E" in this case) occurs
# within a given string (in this case, the contents of the text document read in from the command line)
    num_es = content.count("e") + content.count("E")

# This prints out the number of times the letter 'e' appears in the text file.
print(f"The letter 'e' appears in the file '{filename}' {num_es} times." )
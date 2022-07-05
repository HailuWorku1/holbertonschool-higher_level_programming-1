#!/usr/bin/python3
"""read_file function
"""


def read_file(filename=""):
    """Reads a file
    Args:
        filename (str): filename/filepath
    """
    if type(filename) is str:       
        with open(filename, 'r') as reader:
            # Read and print the entire file line by line
            line = reader.readline()
            while line != '':  # The EOF char is an empty string
                print(line, end='')
                line = reader.readline()

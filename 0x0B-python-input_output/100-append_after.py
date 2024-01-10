#!/usr/bin/python3
""" A module that provides the definition for a function
    responsible for inserting content into a text file
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends text following each line that
       contains a specified string within a file
    """
    txt = ""
    with open(filename) as fhandle:
        for line in fhandle:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as wr:
        wr.write(txt)

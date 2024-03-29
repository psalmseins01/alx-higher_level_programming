"""

This module is comprised of a function
that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ This function prints 2 new lines after ".?:" characters

    Args:
        text: input str

    Returns:
        No return value

    Raises:
        TypeError: raise error if text is not a str

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")



from unicodedata import name


def showUserInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

showUserInfo(name="sam", family='azizi')
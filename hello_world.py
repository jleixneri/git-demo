"""Demo Python File"""


def say_something(to_say:str) -> None :
    """print variable to_say"""
    print(to_say)


if __name__=='__main__':
    for say in ['hello world', 'hello DIA', 'hello GIT']:
        say_something(say)

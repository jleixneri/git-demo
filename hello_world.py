"""Demo Python File"""
import os
from dotenv import load_dotenv

def say_something(to_say:str) -> None :
    """print variable to_say"""
    print(to_say)


if __name__=='__main__':
    load_dotenv() # Environment Variablen werden geladen

    for say in ['hello world', 'hello DIA', 'hello GIT']:
        say_something(say)

    if os.environ.get('USER'):
        say_something(os.environ['USER'])
        say_something(os.environ['PWD'])

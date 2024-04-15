"""Demo Python File"""
import os
import logging
from dotenv import load_dotenv


def say_something(to_say:str) -> None :
    """log variable to_say"""
    logging.info(to_say)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO) #Console Loglevel
    load_dotenv() # Environment Variablen werden geladen

    for say in ['hello world', 'hello DIA .:)', 'hello GIT']:
        say_something(say)

    if os.environ.get('USER'):
        say_something(os.environ['USER'])
        say_something(os.environ['PWD'])

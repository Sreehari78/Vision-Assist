import jarvis
from connection import get_query

while True:
    # command = jarvis.listen()
    command = 'what am i looking at'

    if 'jarvis' in command.lower():
        command = command.lower().replace('jarvis', '')
    get_query(command)

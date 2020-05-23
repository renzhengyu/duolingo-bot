"""
Migrate json to SQLite3.

"""
from duolingo.main import Duobot
from duolingo.db import DuoDictionary

mike = Duobot('/lessons/de-ueberraschung')
target = DuoDictionary(mike.story_name)

mike.load_dictionary()
for a in mike.dictionary:
    target.append(a, mike.dictionary[a])

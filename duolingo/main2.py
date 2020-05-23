from .main import Duobot
from .db import DuoDictionary


class DuobotWithDB(Duobot):
    def load_dictionary(self):
        self.dictionary = DuoDictionary(self.story_name)

    def word_in_dict(self, word):
        return self.dictionary.find(word)

    def translate(self, word):
        return self.dictionary.pair(word)

    def commit_words_to_dictionary(self, a, b):
        self.dictionary.append(a, b)

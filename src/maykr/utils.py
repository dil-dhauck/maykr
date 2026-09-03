import random
from wordhoard import Synonyms

class Utils():

    def pick_random(self, items: list) -> str:
        return random.choice(items)

    def get_synonim(self, word: str) -> str:
        synonyms = Synonyms(search_string=word)
        result = synonyms.find_synonyms()
        return self.pick_random(result)

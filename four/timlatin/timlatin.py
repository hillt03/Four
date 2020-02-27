from four.bot.helpers import get_json

class TimlatinTranslator():

    def __init__(self, filepath):
        self.filepath = filepath # filepath to json containing word translations

    def translate_word(self, word):
        """
        Translates a word to Timlatin
        Input: str to be translated
        Output: translated str
        """
        return word.replace("ng", "n").replace("n", "ng").replace("in", "i").replace("i", "in")

    def translate_text(self, input_str):
        timlatin_dictionary = get_json(self.filepath)

        input_str = input_str.lower()

        split = input_str.split()
        for index, word in enumerate(split):
            if word in timlatin_dictionary.keys():
                if isinstance(timlatin_dictionary[word], list):
                    # If the dict value is a list, select a random word from the list to replace it with
                    split[index] = timlatin_dictionary[word][random.randint(0, len(timlatin_dictionary[word]) - 1)]
                else:
                    # Replace the string with its dictionary value
                    split[index] = timlatin_dictionary[word]
            else:
                # If the word isn't in the dict, let's use translate_word()
                if split[index] is not None:
                    split[index] = self.translate_word(word)

        return " ".join(split)

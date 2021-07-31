import itertools
import enchant
from pathlib import Path
from src.infra import YamlHandler
from src.infra import Logger

# Defines
CONFIG_FILENAME = 'config.yaml'


class AnagramGenerator(object):

    def __init__(self, config_file=None):
        config_file = CONFIG_FILENAME if config_file is None else config_file
        self.logger = Logger(module_name=self.__class__.__name__)
        self.yaml_handler = YamlHandler(yaml_file=Path(__file__).parent / config_file)
        self.data = self.yaml_handler.get_data()
        self.requested_word_list = self.data['words_list']
        self.word_checker = enchant.Dict(self.data['language'])
        self.generated_words_buffer = set([])

    def __repr__(self):
        """
        String represent the object
        """
        return "Input words: {}".format(self.requested_word_list)

    def _get_all_permutations(self, word: str) -> list:
        """
        Return all permutation of letters in a word including the letter order
        :param word: word to generate permutation from
        :return: list of permutations
        """
        word = word.replace('-', ' ')  # Remove hyphen
        all_permutations = ["".join(word) for word in itertools.permutations(word)]
        self.logger.debug(f"permutations for {word}: {all_permutations}")
        return all_permutations

    @staticmethod
    def _apply_output_format(output: list) -> list:
        """
        Transcode list to string with addition of a comma and newline
        :param output: list of lists of anagram words
        :return: list of rows of words
        """
        return [', '.join(row) + '\n' for row in output]

    def _get_all_anagrams(self, word: str) -> set:
        """
        Returns all anagram of a single word, if the anagram was not contained on a former word
        :param word: word to generate anagram from
        :return: set of all anagram (to deduct duplications)
        """
        all_anagrams = [word for word in self._get_all_permutations(word) if word not in self.generated_words_buffer]
        # Remove duplications from permutations
        all_anagrams_filtered = set(all_anagrams)
        # Save these words in buffer to prevent repetition of the same word
        [self.generated_words_buffer.add(word) for word in all_anagrams_filtered]
        self.logger.debug(f"all_anagram_filtered: {all_anagrams_filtered}")
        return all_anagrams_filtered

    def _get_all_language_words(self, word: str) -> list:
        """
        Returns list of anagram words only if they appear on the language dictionary
        :param word: anagram word
        :return: list of anagram words
        """
        all_language_words = [word for word in self._get_all_anagrams(word) if self.word_checker.check(word)]
        self.logger.debug(f"all_language_words: {all_language_words}")
        return all_language_words

    def clear_buffer(self):
        self.generated_words_buffer = set([])

    def get_result(self) -> str:
        """
        Final result of the anagram words
        :return: Anagram words in string
        """
        # Get all anagram words excluding repetitions
        output = [self._get_all_language_words(word) for word in self.requested_word_list]
        # Filter the empty lists
        output_filtered = [word_list for word_list in output if word_list]
        result = "".join(self._apply_output_format(output_filtered))
        self.clear_buffer()
        return result

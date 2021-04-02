# -*- coding: utf-8 -*-

import re

class Retriever:
    def __init__(self, filename):
        self.alphabet = u'abcdefghijklmnopqrstuvwxyzåäö'
        self.lang_words = self.__read_vocabulary(filename)

    def __read_vocabulary(self, filename):
        """Returns language vocabulary from a file.

        The file should contain rows (word | frequency like
            hei|215634
            hello|160402
        """
        word_dict = {}
        with open(filename, 'r') as fin:
            lines = fin.readlines()
        for line in lines:
            word, freq = line.strip().split('|')
            word_dict[word] = int(freq)
        return word_dict

    def spell(self, word):
        """Returns the word that is most likely used in the language.

        Check different variations of string, check them in the language
        vocabulary, and return the one with highest word usage.

        Args:
            word: input word string

        Returns:
            A string that is mostly the 'correct' one.
        """
        def edits(word):
            """Returns spelling edits.

            Manipulate the word and generate different variations.

            Args:
                word: Original word string.

            Returns:
                A set containing different word variations.
            """
            partitions = [(word[:i], word[i:]) for i in range(len(word) + 1)]

            # delete the first char of second half
            deletes = [first + second[1:] for first, second in partitions if second]

            # swap the first and second chars of second half
            transposes = [first + second[1] + second[0] + second[2:]
                          for first, second in partitions if len(second) > 1]

            # replace the first char of second half with defined alphabet
            replaces = [first + c + second[1:] for first, second in partitions
                        for c in self.alphabet if second]

            # insert the defined alphabet between first and second halves
            inserts = [first + c + second for first, second in partitions
                       for c in self.alphabet]
            return set(deletes + transposes + replaces + inserts)

        def known_edits(word):
            """Returns spelling edits known by the language.

            Note that input word edit is nested.
            """
            return set(e2 for e1 in edits(word) for e2 in edits(e1) if e2 in self.lang_words)

        def known(words):
            """Returns words known by the language."""
            return set(w for w in words if w in self.lang_words)

        candidates = known([word]) or known(edits(word)) or known_edits(word) or [word]
        return max(candidates, key=self.lang_words.get)

    def correct_question(self, question):
        """Returns corrected question by including spelling edits."""
        words = question.split(' ')
        correct_words = []

        def has_numbers(word_str):
            return bool(re.search(r'\d', word_str))

        for word in words:
            # if the word has numbers, leave as it is
            if has_numbers(word):
                correct_words.append(word)
            else:
                correct_words.append(self.spell(word))

        return ' '.join(correct_words)

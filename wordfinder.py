from random import randint


class WordFinder:
    """
    Word Finder: finds random words from a dictionary.
    """

    def __init__(self, path):
        """
        Constructs WordFinder instance

        >>> words = WordFinder(path='normal_words.txt')
        5 words read
        """

        self.path = path
        self.words = self.read_file_and_append()
        self.print_words_read()

    def __repr__(self):
        return f"path={self.path}, words={self.words}"

    def read_file_and_append(self):
        """
        reads file and appends words to self.words

        >>> words = WordFinder(path='normal_words.txt')
        5 words read

        >>> words.words == ['one', 'two', 'three', 'four', 'five']
        True
        """

        file = open(self.path, "r")
        file_text = file.read()
        split_words = file_text.split("\n")
        return split_words

    def print_words_read(self):
        """
        prints number of words in the read file
        """
        print(f"{len(self.words)} words read")

    def random(self):
        """
        outputs a random word from file path

        >>> words = WordFinder(path='normal_words.txt')
        5 words read

        >>> words.random() in words.words
        True

        """
        rand_index = randint(0, len(self.words))
        return self.words[rand_index]


class RandomWordFinder(WordFinder):
    """
    Word finder that ignores blank lines and lines that start with #
    """

    def __init__(self, path):
        """
        Constructs RandomWordFinder instance

        >>> words = RandomWordFinder(path='words.txt')
        5 words read
        """
        super().__init__(path)

    def read_file_and_append(self):
        """
        Returns a list of words in file from filepath, ignoring lines
        that start with #

        >>> words = RandomWordFinder(path='words.txt')
        5 words read

        >>> words.words == ['one', 'two', 'three', 'four', 'five']
        True
        """
        file = open(self.path, "r")
        file_text = file.read()

        # replace all instances of \n with space
        # make list of words
        # remove words that start with #

        filtered_words = file_text.replace("\n", " ").split(" ")

        return [word for word in filtered_words if word != "" and word[0] != "#"]

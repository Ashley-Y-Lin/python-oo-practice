class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        self.path = path
        self.words = []
        self.read_file_and_append()
        self.print_words_read()

    def read_file_and_append:
        #reads file and appends words to self.words
        file = open(self.path, "r")
        file_text = file.read()

    def print_words_read:
        print(f"{len(self.words)} words read")

    def random:
        #random word from self.words

class Open(object):

    def open_text(self):
        words = {}

        with open('words.txt', 'r') as reader:
            for line in reader:
                line = line.replace("\n", "")
                words[line] = 0

        return words

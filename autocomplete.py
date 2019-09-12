from open_words import Open

class Autocomplete(object):

    def __init__(self, dic = {}):
        self.dic = {}


    def make_dictionary(self):
        p = Open()
        self.dic = op.open_text()


    def auto_complete(self, word):
        for item in self.dic.keys():
            if item.startswith(word):
                print item

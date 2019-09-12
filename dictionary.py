from open_words import Open

try:
    import cPickle as pickle
except:
    import pickle

class Dictionary(object):
    def __init__(self, dictionary_words = {}):
        self.dictionary_words = {}


    def save_dictionary(self):
        fichero = file('data.txt', 'w')
        pickle.dump(self.dictionary_words, fichero)
        fichero.close()


    def print_dictionary_ordered_by_most_call_word(self):
        dic = sorted(self.dictionary_words.items(), key=lambda t: t[1])

        for i, j in reversed(dic):
            if j == 0:
                break

            else:
                print i, j


    def make_dictionary(self): 
        try:
            fichero = file('data.txt')
            self.dictionary_words = pickle.load(fichero)

        except IOError:
            print "data.txt not found, making new data.txt"
            op = Open()
            self.dictionary_words = op.open_text()


    def search_word(self, word):
        if self.dictionary_words.has_key(word):
            self.dictionary_words[word] += 1
            print self.dictionary_words[word]
            print "found"

        else:
            print "not found"

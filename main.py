#!/usr/bin/python
from dictionary import Dictionary
from autocomplete import Autocomplete
from time import time


#start_time = time()
#p = Dictionary()
#p.make_dictionary()
#start_time = time()
#p.search_word("weel")
#p.save_dictionary()
#p.print_dictionary_ordered_by_most_call_word()
a = Autocomplete()
a.make_dictionary()
start_time = time()
a.auto_complete("a")
print time() - start_time

def print_upper_words(list_of_words, must_start_with):
    """Given a list of words, and a set of letters, returns
	   in uppercase, only the words in the list that start 
	   with one of the letters contained in the set
    
    For example:
      print_upper_words(["arglebargle","affluent","gazebo","unguent","unctuous"], {"a","u"})

    Should print: ARGLEBARGLE
    			  AFFLUENT
    			  UNGUENT
    			  UNCTUOUS
    """
    for word in list_of_words:
    	if word[0] in must_start_with:
    		print(word.upper())


print_upper_words(["arglebargle","affluent","gazebo","unguent","unctuous"], {"a","u"})
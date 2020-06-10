def build_word_index(self, words):
    '''
    Build the character tree of all the words in a dictionary
    Parameters: 
        words: a list of words
    Returns: 
        The tree
    '''
    index = {}
    for w in words:
        crnt_index = index
        for ch in w:
            if ch not in crnt_index:
                crnt_index[ch] = {}
            crnt_index = crnt_index[ch]
        crnt_index['is_end'] = True
    return index

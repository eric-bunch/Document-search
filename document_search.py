def answer(document, searchTerms):
    doc = document.split(' ')
    
    """
    The segment of document will begin and end with a word in searchTerms.
    pairs will be a list of pairs of indicies of words in searchTerms 
    between which are all the words in searchTerms.
    """

    length_search_terms = len(searchTerms)
    length_doc = len(doc)
    
    searchCoordsHash = {}
    
    for i in range(0, length_doc):
        if doc[i] in searchTerms:
            searchCoordsHash[i] = 1
        else:
            searchCoordsHash[i] = 0
    
    
    pairs = []
    
    for (i, j) in [(x, y) for x in range(0, length_doc) if searchCoordsHash[x] == 1
                          for y in range(0, length_doc) if searchCoordsHash[y] == 1
                          if y - x >= length_search_terms - 1]:
        if set(doc[i : j + 1]).intersection(set(searchTerms)) == set(searchTerms):
            pairs.append((i, j))
    
    
    shortest_length = min(pair[1] - pair[0] for pair in pairs)

    shortest_pairs = [pair for pair in pairs if pair[1] - pair[0] == shortest_length]
    
    smallest_first_coord = min(pair[0] for pair in shortest_pairs)
    
    first_shortest_pair = [pair for pair in shortest_pairs 
                                if pair[0] == smallest_first_coord][0]
    
    return ' '.join(doc[first_shortest_pair[0] : first_shortest_pair[1] + 1])	
	


# mapping, wrd->{synlsts}
wrdtolsts = {}
# mapping, wrd->{pharses containing this word}
wrdtophrases = {}

# get above data structures
fp = open("synlists.txt","r")
while True:
    lst = fp.readline()
    if not lst:
        break
    lst = lst.strip()
    for term in lst.split(','):
        if wrdtolsts.get(term) is None:
            wrdtolsts[term] = []
        wrdtolsts[term].append(lst)
        if term.find(' ') != -1:
            for wrd in term.split(' '):
                if wrdtophrases.get(wrd) is None:
                    wrdtophrases[wrd] = set()
                wrdtophrases[wrd].add(term)
fp.close()

# get synonym lists for word "w".
def getSynlsts(w):
    if wrdtolsts.get(w) is None:
        return []
    synlsts = []
    for lst in wrdtolsts[w]:
        # "lst" includes the word "w": remove it (every word is presumed
        # synonymous to itself).
        lstPrime = []
        for wx in lst.split(','):
            if wx != w:
                lstPrime.append(wx)
        if len(lstPrime) > 0:
            synlsts.append(','.join(lstPrime))
    return synlsts

# lookup word "w", return synonyms + ref's to related phrases.
def lookup(w):
    info = []
    # show synonyms for word "w"
    synlsts = getSynlsts(w)
    if len(synlsts) == 0:
        info.append('No entry for "%s"' % w)
    elif len(synlsts) == 1:
        info.append(synlsts[0])
    else:
        lstEnum = 1
        for lst in synlsts:
            info.append('%d. %s' % (lstEnum, lst))
            lstEnum += 1
    # show synonyms for phrases containing "w"
    phrases = wrdtophrases.get(w)
    if phrases is not None:
        info.append('\nSee also:')
        phrases = list(phrases)
        phrases.sort()
        info.append(','.join(phrases))
    return info

if __name__== "__main__":
    """ loop on user input, and print info about words """
    while True:
        w = raw_input("Enter word: ")
        w = w.strip()
        if w == 'q':
            exit(1)
        print '\n'.join(lookup(w))
        print ''
        




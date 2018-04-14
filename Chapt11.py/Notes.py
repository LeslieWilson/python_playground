import fname

def main ():

    print ("this program analyzes word frequency in a file")
    print ("and prints a report on the n most frequent words. \n")

    # get sequence of words from the file.

    fname = input("file to analyze:")
    text = open(fname, 'r').read()
    text = string.lower(text)
    for ch in ('!$@%^@&^&$%&#^(*)'):
        text = string.replace (text,ch,'')
    words = string.split(text)

    # construcct a dictionary of word counts.

    counts = {}
    for w in words:
        counts [w] = counts.get(w,0) +1

        # output analysis of n most frequent words
        n = input ("output analysis of n most frwquent words.")
        items = counts.items()
        items.sort(compareItems)
        for i in range (n):
            print ("%-10s%5d") % items [i]

if __name__ == '__main__': main()

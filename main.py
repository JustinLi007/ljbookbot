def main():
    bookBasePath = "books"
    bookPath = f"{bookBasePath}/frankenstein.txt"
    fileContents = getBookContent(bookPath)
    wordCount = countWords(fileContents)
    letterFreq = countLetter(fileContents)
    sortedLetterFreq = sortLetterFreq(letterFreq)
    printReport(wordCount, sortedLetterFreq, bookPath)

def sort_on(dict):
    return dict["num"]

def sortLetterFreq(letterFreq):
    sortedFreqArr = []
    for key in letterFreq:
        sortedFreqArr.append({"char": key, "num": letterFreq[key]})
    sortedFreqArr.sort(reverse=True, key=sort_on)
    return sortedFreqArr

def countLetter(text):
    freq = {}
    for ch in text:
        c = ch.lower()
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def countWords(text):
    if not len(text): return 0
    return len(text.split())

def getBookContent(path):
    with open(path) as f:
        return f.read()

def printReport(wordCount, freqs, path):
    print(f"--- Begin report of {path} ---")
    print(f"{wordCount} words found in the document\n")
    for entry in freqs:
        if entry["char"].isalpha():
            print(f"The '{entry['char']}' character was found {entry['num']} times")
    print("--- End report ---")

main()

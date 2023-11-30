givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer(object):
    def __init__(self, text):
        formattedtext = text.replace('.','').replace('!','').replace(',','').replace('?','')

        formattedtext = formattedtext.lower()

        self.fmtText = formattedtext

    def freqALL(self): #frequency of all unique words
        #Splitting text into words
        wordList = self.fmtText.split(' ')
        #Creating a dictionary
        freqdict = {}

        for word in set(wordList): #removing the duplicates in the list
            freqdict[word] = wordList.count(word)

        return freqdict
    
    def freqOf(self, word): #frequency of specific word
        freqMap = self.freqALL()

        if word in freqMap:
            return freqMap[word]
        else:
            return 0
        
analyzed = TextAnalyzer(givenstring)

print(f"Formatted Text: {analyzed.fmtText}")

freqMap = analyzed.freqALL()
print(freqMap)

word = "Lorem"
frequency = analyzed.freqOf(word)
print(f"The word {word} appears {frequency} times")
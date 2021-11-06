import re
class Solution:
    def countValidWords(self, sentence: str) -> int:
        #for words in sentence.strip().split():
            #print(words)
        cleaned_sentence = sentence.strip().split()
        #print(cleaned_sentence)
        #count =len(re.findall(r'(?<!\S)[a-z]+[-]*[a-z]+(?!\S)[?.!,]$',sentence))
        
        #r = re.compile("[\w\.-]+[-]*[\w\.-]+[.!,]*$") #^[a-z]+
        #pattern = re.compile('(^[a-z]+(-[a-z]+)?)?[,.!]?$')
        r =  re.compile('^[a-z]*([a-z]-[a-z])?[a-z]*[.,!]?$') # failed "!this  1-s b8d!"
        
        #newlist = list(filter(r.match, cleaned_sentence))
        #return len(newlist)
        word_count = 0
        for word in cleaned_sentence:
            if r.match(word):
                print(word)
                word_count += 1
        return word_count
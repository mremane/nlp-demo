# Marco Remane

# coding: utf-8

# In[27]:


class Article:
    def __init__(self, docNo, docID, date, headline, docText):
            self.docNo = docNo
            self.docID = docID
            self.date = date
            self.headline = headline
            self.docText = docText
    def getText(self):
        return self.headline + self.docText;
    def __str__(self):
        return 'doc No:' + self.docNo + 'loaded.'


# In[34]:


import string
from bs4 import BeautifulSoup
from collections import Counter
from collections import deque
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem.porter import *

#read file
inputFile = open("txt-articles.txt", "r") 
contents = inputFile.read()
parser = BeautifulSoup(contents, 'lxml')
#load stop words to be removed from parsed text.
docs = parser.select('doc')
stopWords = stopwords.words('english') 
stopWords.extend(string.punctuation) 
stopWords.append("''") 
stopWords.append("``")
tempDic = {}
#scan each article
for count, doc in enumerate(docs):
    article = Article(doc.select_one('docno').get_text(),
    doc.select_one('docid').get_text(), 
    doc.select_one('date').get_text(), 
    doc.select_one('headline').get_text(), 
    doc.select_one('text').get_text())
    #print(article)
    #tokenize words
    tokens = word_tokenize(article.getText())
    #lowercase tokens
    tokensLower = [w.lower() for w in tokens]
    #remove stop words on tokens
filtered = [w for w in tokensLower if not w in stopWords] #append word count for each doc on array
tempDic[count] = Counter(filtered)
wordCounter = Counter()
for item in tempDic.values(): 
    wordCounter = wordCounter + item

for k,v in wordCounter.most_common(): 
    print([k],':',v)


import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

pdfFileObj = open('JavaBasics-notes.pdf', 'rb')
data=[]
 # Reading the pdf file 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

#calculating the number of pages in the file
num=pdfReader.getNumPages()  

#extracting the text of the file

for i in range(0,num):
    pageObj = pdfReader.getPage(i)
    data.append(pageObj.extractText())
    
data=' '.join(data)

data=data.lower()

#removing stop words from collected data

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(data)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)


# filtered_sentence = ' '.join(filtered_sentence)
# print(filtered_sentence)

keywords=['operator','inheritance','polymorphism','applet','encapsulation','robust','class','abstraction','encapsulation','string','array','overloading','protection','constructor','exception','awt','generic','stream','serialization','threads','multithreading','swing','jdbc']
count=0
keywords_present=[]
for w in filtered_sentence:
    if w in keywords:
        keywords_present.append(w)
        count=count+1
keywords_present.sort()
comparison_list=[]
demo=[]
for i in keywords_present:
    if i not in comparison_list:
        comparison_list.append(i)


for i in comparison_list:
    temp=0
#     print('external loop working',i)
    
    for j in keywords_present:
#         print('internal loop working',j)
        if i==j:
            temp=temp+1
    
    w=i+' '+str(temp)
    demo.append(w)

demo = ','.join(demo)           
demo = demo.split(' ') 
demo = ','.join(demo) 
demo = demo.split(',')
string=[]
numeral=[]
for i in demo:
    value=i.isalpha()
    value1=i.isdigit()
    if(value==True):
        string.append(i)
    
    if(value1==True):
        numeral.append(i)
print(string)
print(numeral)
weights=[]
for i in numeral:
    i =int(i)
    if(i>0 and i<10):
        weights.append(0.2)
    elif(i>10 and i<20):
        weights.append(0.4)
    elif(i>20 and i<26):
        weights.append(0.6)
    elif(i>25 and i<31):
        weights.append(0.7)
    elif(i>30):
        weights.append(0.75)
print(numeral)
print(weights)

    
csv = open('result.csv', 'w') 
columnTitleRow = "Keywords, Weights\n"
csv.write(columnTitleRow)
csv.close()

csv = open('result.csv', 'a')
for i in range(0,len(weights)):
    keyword=string[i]
    weight=weights[i]
    row = keyword + "," + str(weight) + "\n"
    csv.write(row)
csv.close()


# print(demo)       
# print(keywords_present)
# print(comparison_list)
# print(count)
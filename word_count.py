import os
import string
import operator

LIMIT = 10  # The limit we want to place on the number of words printed 
DIR = "text" #The directory the .txt files are located in
words = {}

for file in os.listdir(DIR):# Opens all files in the directoty one by one
   with open(os.path.join(DIR, file), 'r') as text:
      content = text.read()
      new_content = content.translate(str.maketrans('', '', string.punctuation)) #cleans words
      c_list = new_content.split()
      for each in c_list: #tallies the words in the text files
         each = each.lower()
         if each in words.keys():
            words[each] += 1
         else:
            words[each] = 1
ticker = 0
sorted_words = dict(sorted(words.items(), key=operator.itemgetter(1), reverse=True)) #sorts then prints the words
print("The top " + str(LIMIT) + " words:")
for word in sorted_words:
    if ticker < LIMIT:
       print(word + ": " + str(sorted_words.get(word)))
       ticker = ticker + 1
    else:
       break

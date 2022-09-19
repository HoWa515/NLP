import json
import os
import string
import nltk
import numpy as np
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plot

# fan chart print
def fanPrint(l,counter):
    if l == 1:
        for key, value in counter.items():
            labels = [key]
            values = np.array([value])
            plot.pie(values, labels=labels, autopct='%.1f%%')
            plot.title("Result of")
            plot.show()
    if l == 2:
        a2, b2 = counter.items()  # type(a2): tuple
        # a2Per = a2[1] / total
        # print(a2[0], a2Per)
        # b2Per = b2[1] / total
        # print(b2[0], b2Per)

        labels = [a2[0], b2[0]]
        values = np.array([a2[1], b2[1]])
        plot.pie(values, labels=labels, autopct='%.1f%%')
        plot.title("Result of")
        plot.show()
    if l == 3:
        a3, b3, c3 = counter.items()

        labels = [a3[0], b3[0], c3[0]]
        values = np.array([a3[1], b3[1], c3[1]])
        plot.pie(values, labels=labels, autopct='%.1f%%')
        plot.title("Result of")
        plot.show()

with open("moreThan20/mentors_gov.txt",'r',encoding='utf-8') as f2:
                text=f2.read()
                lower_case=text.lower()
                clean_text=lower_case.translate(str.maketrans('','',string.punctuation))
                with open("cleanText.txt", 'w', encoding='utf-8') as f3:
                   f3.write(clean_text)
                #tokenize
                tokenized_words = word_tokenize(clean_text)
                # remove stopwords
                stop_words = set(stopwords.words('english'))

                withoutStopwords=[]
                for word in tokenized_words:
                    if word not in stop_words:
                        withoutStopwords.append(word)

                #emotions
                emotion_list=[]
                with open('categorizedEmotion.txt','r',encoding='utf-8') as file:
                     for line in file:
                        clear_line=line.replace("\n",'').replace(" ",'').replace('_','').replace('-','').replace('+','').strip()
                        word,emotion=clear_line.split(':')
                        for w in withoutStopwords:
                           if word==w:
                              emotion_list.append(emotion)

                #list to dict, for count keys
                countEmotion=Counter(emotion_list)
                print("Emotion count:")
                print(countEmotion)

                # emoji
                emoji_list = []
                with open('categorizedEmoji.txt', 'r', encoding='utf-8') as file:
                    for line in file:
                        clear_line = line.replace("\n", '').replace(" ", '').replace('_', '').replace('-','').replace('+', '').strip()
                        word, emoji = clear_line.split(':')
                        for w in withoutStopwords:
                            if word == w:
                                emoji_list.append(emoji)

                # list to dict, for count keys
                countEmoji = Counter(emoji_list)
                print("Emoji count:")
                print(countEmoji)

                #drwa emotion /emoji result
                l1 = len(countEmotion);
                fanPrint(l1,countEmotion)
                l2=len(countEmoji)
                fanPrint(l2,countEmoji)








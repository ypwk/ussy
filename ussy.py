from errno import EMSGSIZE
import re
from nltk.tokenize import word_tokenize
import nltk

print("Downloading relevant resources...")
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def findLastApplicableConsonant(word):
    punct = ".,?!;"
    if word in punct:
        return -1
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    common_end = ["ion", "en", "er", "ent", "ual", "il"]
    for a in common_end:
        if word.endswith(a):
            return len(word) - len(a) - 1

    for a in range(len(word) - 1, 0, -1):
        if word[a] not in vowels:
            return a
    return 0

print("Type +QUIT to quit.")
inp = ""
while(inp != "+QUIT"):
    inp = input("Enter message to make better: ")
    if inp == "+QUIT":
        break

    #format input
    message = word_tokenize(inp)
    tagged_message = nltk.pos_tag(message)
    output = ""

    for a in range(len(tagged_message)):
        space = "" if a != len(message) - 1 and message[a + 1] in ",.!?;" else " "
        ussy = ""
         #singular noun and adjective and verb and cardinal digit and proper noun
        if tagged_message[a][1] == "NN" or tagged_message[a][1] == "VB" or tagged_message[a][1] == "CD" or tagged_message[a][1] == "NNP":
            ussy = "ussy"
            if tagged_message[a][0][-3:] == "ing": #case ing
                message[a] = message[a][:-3]
                ussy = "ussing"  
        elif tagged_message[a][1] == "NNS" or tagged_message[a][1] == "NNPS"  or tagged_message[a][1] == "VBZ" and message[a] != "is": 
            ussy = "ussies"#plural noun or plural proper noun or 3rd person singular present
            if tagged_message[a][0][:-3] == "ies": #case "ies"
                message[a] = message[a][:-3]
            elif tagged_message[a][0][:-2] == "es": #case "es"
                message[a] = message[a][:-2]
            else: #case "s"
                message[a] = message[a][:-1]
        elif tagged_message[a][1] == "RB" or tagged_message[a][1] == "RBR" or tagged_message[a][1] == "RBS": #adverbs and variations
            ussy = "ussy"
            if tagged_message[a][0][-2:] == "ly": #case "ly"
                message[a] = message[a][:-2]
                ussy = "ussily"
        elif tagged_message[a][1] == "VBD" or tagged_message[a][1] == "VBN": # verb past tense and past participle
            if tagged_message[a][0][-2:] == "ed": #case "ed"
                message[a] = message[a][:-2]
                ussy = "ussied"
        elif tagged_message[a][1] == "VBG": # verb past tense gerund
            message[a] = message[a][:-3]
            ussy = "ussing" 
        elif tagged_message[a][1] == "JJR": #comparative adjective
            ussy = "ussy"
            if tagged_message[a][0][-3] == "ier":
                ussy = "ussier"
        elif tagged_message[a][1] == "JJS": #superlative adjective
            ussy = "ussy"
            if tagged_message[a][0][-4] == "iest":
                ussy = "ussiest"
        elif tagged_message[a][1] == "JJ": #adjective
            ussy = "ussy"
            if tagged_message[a][0][-2:] == "ed": #case "ed"
                message[a] = message[a][:-2]
                ussy = "ussied"
            elif tagged_message[a][0][-3:] == "ing": #case ing
                message[a] = message[a][:-3]
                ussy = "ussing" 
        l = findLastApplicableConsonant(message[a])
        if l != -1 and ussy != "":
            output = output + message[a][:l + 1] + ussy + space
        else:
            output += message[a] + space
    print(output)
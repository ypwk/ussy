import re

def findLastApplicableConsonant(word):
    # punct = ".,?!;"
    # if word in punct:
    #     return -1
    if len(word) < 5:
        return -1
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if word[-1] == "s":
        word = word[:-1]

    common_end = ["ion", "ed", "en", "er", "ent", "ual"]
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
    message = re.findall(r"[\w']+|[.,!?;]", inp)
    output = ""
    for a in range(len(message)):
        l = findLastApplicableConsonant(message[a])
        space = "" if a != len(message) - 1 and message[a + 1] in ",.!?;" else " "
        ussy = "ussies" if message[a][-1] == "s" and len(message[a]) > 3 else "ussy"
        if l != -1:
            output = output + message[a][:l + 1] + ussy + space
        else:
            output += message[a] + space
    print(output)

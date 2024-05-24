file_path=__file__
for i in range(len(file_path)):
    if file_path[len(file_path)-i-1]=="\\":
        file_path=file_path[:len(file_path)-i]+"bannedwords.txt"
        break

print("Hello, welcome to the 'control center', here you can remove and add words to the list, to remove words type -word and to add words type the word.\nTo clean the list type *Clean*.")

while True:
    #gathers the banned words
    r = open(file_path, "r")
    bannedwords=list(r.read().split(","))
    r.close()
    wordRemovedAdded=0 #in case a word doesn't get removed/added
    word=input()

    if word=="*Clean*": #this will clean the list from duplicates
        text=""
        for i in range(len(bannedwords)): #this is the word it might remove
            hit=0
            for z in range(len(bannedwords)): #this is the word it looks in
                if z!=i: #checks if the word is itself
                    start=0
                    end=len(bannedwords[z])
                    while end<=len(bannedwords[i]):
                        if bannedwords[i][start:end]==bannedwords[z]:
                            print(bannedwords[i],"foud in word:",bannedwords[z])
                            hit=1
                        start+=1
                        end+=1
            if hit==0: #if a word isn't a duplicate it gets added
                text+=bannedwords[i]+","
        f = open(file_path, "w")
        f.write(text[:-1])
        f.close()

    elif word[0]!="-": #this checks if the word is supposed to be added
        for i in range(len(bannedwords)): #checks if the word is already in the list
            if bannedwords[i]==word:
                wordRemovedAdded=1
                print('word already existed')
                break
        if wordRemovedAdded==0: #if the word isn't already in the list it gets added
            f = open(file_path, "a")
            bannedwords.append(word)
            f.write(","+word)
            f.close()
            print('word added')

    else: #it goes here to remove a word
        word=word[1:]
        for i in range(len(bannedwords)):
            if bannedwords[i]==word:
                f = open(file_path, "w")
                del bannedwords[i]
                newList=""
                for z in range(len(bannedwords)):
                    newList+=bannedwords[z]+","
                f.write(newList[:-1])
                f.close()
                print('removed word')
                wordRemovedAdded=1
                break
        if wordRemovedAdded==0: print("didn't find word")
#removes ands adds words to lists saved in a txt file

file_path=__file__
for i in range(len(file_path)):
    if file_path[len(file_path)-i-1]=="\\":
        file_path=file_path[:len(file_path)-i]+"bannedwords.txt"
        break

#gathers the banned words
f = open(file_path, "r")
bannedwords=list(f.read().split(","))
f.close()
bannedwords2=""
print("Every single word you banned will show up here, type 1 if you want to keep it and 2 if you want to delete it")
for i in range(len(bannedwords)):
    print(bannedwords[i])
    if input()=="1": bannedwords2+=bannedwords[i]+","
f = open(file_path, "w")
f.write(bannedwords2[:-1])
f.close()

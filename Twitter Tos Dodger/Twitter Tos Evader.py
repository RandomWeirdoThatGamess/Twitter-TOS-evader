import pyperclip

print("All credit goes to me :), you are free to do whatever you want with this I hold no liability")

file_path=__file__
for i in range(len(file_path)):
    if file_path[len(file_path)-i-1]=="\\":
        file_path=file_path[:len(file_path)-i]+"bannedwords.txt"
        break

def newpaste(): #this is for when the laptop is off
    try: pyperclip.waitForNewPaste()
    except: newpaste()

text=pyperclip.paste() #this is the input text that will be modified
extraletters="𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩      𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭      𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ      𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ      ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙      𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳" #this is font
switch=0 #this is used as a switch between things
switchend=len(extraletters)/58
while True:
    f = open(file_path, "r")
    bannedwords=list(f.read().split(","))
    f.close()
    if True:
        output="" #this is the final outcome
        place=0 #used to know where in the text you are
        skipstart=[] #stores when a number should be skipped
        skipend=[] #stores to where in the text it should skip to
        lookforskip=0 #this keeps track of how many times something in the text needs to be skipped
        text2=text.lower() #to avoid weird shit with uppercase lowercase naughty words
        start=0 #looks for the beginning of skippable text
        while start<=len(text):
            for place2 in range(len(bannedwords)):
                word=bannedwords[place2] #this is the banned word that might get you oopsied
                if len(word)<=len(text)-start:
                    end=len(word)+start
                    if text2[start:end]==word:
                        while 123>ord(text2[start-1])>96 and start!=0: start-=1 #this is used to look for the start of words when a keyword gets hit
                        skipstart.append(start)
                        try:
                            while 123>ord(text2[end])>96: end+=1
                        except: pass
                        skipend.append(end)
                        start=end
            start+=1
        skipstart.sort()
        skipend.sort()
        skipstart.append('n')
        while place<len(text): #changes the banned words
            if place==skipstart[lookforskip]:
                while place!=skipend[lookforskip]: #actually changes the banned words
                    if text[place]!=" ":
                        output+=extraletters[(ord(text[place]))-65+switch*58]
                        switch+=1
                        if switch==switchend:
                            switch=0
                    else: output+=" "
                    place+=1
                lookforskip+=1
            else:
                output+=text[place]
                place+=1
    print(output)
    pyperclip.copy(output)

    text="" #this is so images don't get fucked :3 oh yeah btw fag don't remove this like you did previously you are a retard and a disgrace :3
    while text=="" or text[:4]=="http":
        newpaste()
        text=pyperclip.paste()

# Decodes Levels 1-9 of https://www.trytodecrypt.com 
#For level 9 uncomment both comments in line 25 & 49 (might change)


import mechanicalsoup
import string


browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.trytodecrypt.com/decrypt.php?id=5")

for i in range(5):
    textInput = " " if i==0 else string.ascii_lowercase if i==1 else string.ascii_uppercase if i==2 else  "-_.,;:?!" if i==3 else "0123456789"
    browser.refresh()
    browser.select_form(nr=1)
    browser["text"]=textInput
    response = browser.submit_selected(btnName="encrypt")
    message = browser.get_current_page().find_all("div", class_="panel-body", style="word-wrap: break-word;")
    alphabet = message[1].text
    if i==0: 
        length= len(alphabet)
        space= alphabet
        continue
    splits = [alphabet[i:i+length] for i in range(0,len(alphabet), length)]
    #splits=splits[::-1]
    if i==1:dictslc = dict(zip(splits,string.ascii_lowercase))
    elif i==2:dictsuc = dict(zip(splits,string.ascii_uppercase))
    elif i==3: dictssc = dict(zip(splits,"-_.,;:?!"))
    else: dictsnum = dict(zip(splits,"0123456789"))

def match(input):
    if input in dictslc:
        return (dictslc[input])
    elif input in dictsuc:
        return (dictsuc[input])
    elif input in dictssc:
        return (dictssc[input])
    elif input in dictsnum:
        return (dictsnum[input])
    elif input==space:
        return " "
    else:
        return None


toDecypher = browser.get_current_page().find("div", class_="panel-body")
print(toDecypher.text)
splitEncrption= [toDecypher.text[i:i+length] for i in range(0,len(toDecypher.text), length)]
#splitEncrption=splitEncrption[::-1]
answer= list(map(lambda x:match(x),splitEncrption))
print(answer)

if not None in answer:
    Decryption= ''.join(answer)
    print(Decryption)

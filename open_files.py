#lets open the file from an existing location
afile = '../Resources/input.txt'

with open (afile, 'r') as text:
    print(text)
    contentFile = text.read()
    
    print(contentFile)

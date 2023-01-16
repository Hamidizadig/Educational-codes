import io
myfile = open('D:\\data\\1.txt','wt')
while True:
    sentence = input('Enter a sentence : ')
    if len(sentence) != 0:
        sentence += '\n'
        myFile.write(sentence)
    else:
        break
myFile.close()

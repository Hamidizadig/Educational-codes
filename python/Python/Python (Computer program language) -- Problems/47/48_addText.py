import io
myf = open('D:\\data\\1.txt','at')
while True:
    line=input('Enter a sentence : ')
    if line !='':
        line +='\n'
        myFile.write(line)
    else:
        break
myFile.close()
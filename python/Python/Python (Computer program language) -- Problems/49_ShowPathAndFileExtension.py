import os.path
for path in['test.txt','filename','/user/system/test.txt','/']:
    print('"%s":'%path,os.path.path.splitext(path))
          
"test.txt":('test','txt')
"filename":('filename')
"/user/system/test.txt":('/user/system/test'.'txt')
"/":('/',")
"":(",")
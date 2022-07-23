'''
Manipulating Files Methods
'''

#Creating or opening a file:
file = open('notetab.txt', 'a')

#Writing in a file:
file.write('Hello World!')

#Iterable object:
phrases = list()
phrases.append('\rPython \r')
phrases.append('Django \r')
phrases.append('Files')

#Adding iterable objects to the file:
file.writelines(phrases)

#Reading a file and printing it:
file = open('notetab.txt', 'r')
print(file.readline(3))

    #Reading all the files and printing it:
print(file.readlines())


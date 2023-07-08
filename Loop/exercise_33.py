fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0

for i in range(0, fibonacciIterations):
    a3 = a1 + a2
    (a1, a2) = (a2, a3)
print(a3)

print('#######################')

text = 'Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn’t do the job. Python was compared to other languages, such as Tcl and Perl, and chosen because it’s an easier-to-learn language that the organization can implement incrementally. In addition, Python can be embedded within a larger software system as a scripting language, even if the system is written in a language such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which some languages can’t.'
textSplit = text.split(' ')
print(textSplit[0])

for word in textSplit:
    if 'p' or 'P' in word:
        print(word)

print('#######################')

dictionary = {'A': '80%-10%', 'B': '60%-80%', 'C': '50-60%', 'D': 'less than 50%'}
for word in dictionary.keys():
    print(word, '-', dictionary[word])


print('###########################')

text='''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn't do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it's an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can't.
'''
listOfWords = text.replace("\n"," ").split(' ')
wordDictionary = {}
print(listOfWords)

for word in listOfWords:
    if wordDictionary.get(word) is None:
        wordDictionary[word] = 1
    else:
        wordDictionary[word] = wordDictionary.get(word) + 1


print(wordDictionary)

print('###########################')


wordDictionary = {}
for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word] + 1
    else:
        wordDictionary.setdefault(word, 1)

print(wordDictionary)
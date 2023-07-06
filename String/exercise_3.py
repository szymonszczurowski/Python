article = '''This article is about the comedy group. For their TV show frequently called Monty Python, see Monty Python's Flying Circus.
"Pythonesque" redirects here. For the play by Roy Smiles, see Pythonesque (play).
"The Pythons" redirects here. For the documentary film about the group, see The Pythons (film).
'''
article = article.upper()
print(article)
article = article.lower()
print(article.replace('monty','flying'))

replace = article.count('python')
print(replace)
text = 'word python appears ' + str(replace) + ' times'
print(text)

print("The best hits of '80s!!!")
print('The best hits of \'80s!!!')


ValueAdText = 123.45
factor = 1.23

print('value is ' + str(ValueAdText) + ' factor is ' + str(factor) + ' value*factor= ' + str(float(ValueAdText) * factor) )

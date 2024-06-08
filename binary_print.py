word="wasdaw awdasdwa sdafaes asfasdasdwasdwasdawfa sfaawfas afwasdaew"
words=word.split(" ")

n=''
for w in words:
    if len(n)<len(w):
        n=w
        
print(f"the len of the longest word + the word {len(n),n}")
    

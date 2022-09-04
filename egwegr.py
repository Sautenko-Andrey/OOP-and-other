vowels='aeuio'
stroka='aasgsgsgeertrgbbvdesgrgreporwee'

#s[1]-->s[2]
#s[3]-->s[4]
#s[i]-->s[i+1]

n=len(stroka)
for word in range(n-1):
    if stroka[word] in vowels and stroka[word+1] in vowels:
        print(stroka[word],stroka[word+1])

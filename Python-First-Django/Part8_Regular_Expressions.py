import re

patterns=['term1','term2']

text='This is a string with term1 , but it dose not have the other term'
for pattern in patterns:
    print ('Searching for "%s" in: \n"%s"' % (pattern, text))
    if re.search(pattern,text):
        print ('\n')
        print ('Match was found. \n')
    else:
        print ('\n')
        print ('No Match found. \n')

pattern='term'
text='This is a string with term1, but it dose not have the other term'
match=re.search(pattern,text)
print(type(match))
print(match.start())
print(match.end())


split_term='@'
phrase="what is the domain name fo someone with the email:hello@gmail.com"
print(re.split(split_term,phrase))

print(re.findall('match','test phrase match is in middle'))


re.findall('march','test phrase match is in middle')

def multi_re_find(patterns,phrase):

    for pattern in patterns:
        print('Searching the phrase using the recheck: %r' %pattern)
        print (re.findall(pattern,phrase))
        print ("\n")

test_phrase='sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns=['sd*']
multi_re_find(test_patterns,test_phrase)
test_patterns=['sd+']
multi_re_find(test_patterns,test_phrase)

test_patterns=['sd?']
multi_re_find(test_patterns,test_phrase)
test_patterns=['sd{3}']
multi_re_find(test_patterns,test_phrase)
test_patterns=['sd{2,3}']
multi_re_find(test_patterns,test_phrase)


test_phrase='sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns=['[sd]']
multi_re_find(test_patterns,test_phrase)

test_patterns=['s[sd]+']
multi_re_find(test_patterns,test_phrase)


test_phrase='sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
re.findall('[^!.?]+',test_phrase)


test_phrase='This is an emxample sentence. Lets see if we can find some letters.'
test_patterns=['[a-z]+']
multi_re_find(test_patterns,test_phrase)

test_patterns=['[A-Z]+']
multi_re_find(test_patterns,test_phrase)

test_patterns=['[a-zA-Z]+']
multi_re_find(test_patterns,test_phrase)

test_patterns=['[A-Z][a-z]+']
multi_re_find(test_patterns,test_phrase)

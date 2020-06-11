import re
# speak if you want
# to know if i can hear you
string = 'The quick brown fox jumps over the lazy dog.'
words = ['fox', 'dog', 'horse']

regex = ''
for word in words:
    regex = regex + '(?=.*' + word + ')'
    
search = re.search(regex, string)

if search is None:
    print('Not match these words')
else:
    print('Words matched!')
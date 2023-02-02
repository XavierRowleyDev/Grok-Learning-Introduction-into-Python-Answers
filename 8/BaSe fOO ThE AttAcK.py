chopper = input('code: ')
code = chopper.split(' ')
answer = []
if chopper != '':
  for i in code:
    if i[0].isupper():
      answer.append(i)
answer.reverse()
answer  = ' '.join(answer)
answer = answer.lower()
print('says: ' + answer)
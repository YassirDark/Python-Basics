import random

name = 'Yassir'
question = 'Am i the best player in the world ?'
answer = ''
random_number = random.randint(1,11)

if name =='':
  name += 'Question :'
else:
  name += ' question :'

if question != '':
    if random_number == 1 :
      answer += 'Yes - definitely'
    elif random_number == 2:
      answer += 'It is decidedly so'
    elif random_number == 3:
      answer += 'Without a doubt'
    elif random_number == 4:
      answer += 'Reply hazy, try again'
    elif random_number == 5:
      answer += 'Ask again later'
    elif random_number == 6:
      answer += 'Better not tell you now'
    elif random_number == 7:
      answer += 'My sources say no'
    elif random_number == 8:
      answer += 'Outlook not so good'
    elif random_number == 9:
      answer += 'Very doubtful'
    elif random_number == 10:
      answer += 'Of course'
    elif random_number == 11:
      answer += 'I can say YES !'
    else :
      answer += 'Error'
if question =='':
  question +='print out a message to the user'
  answer += 'please write a question first'
print(name,[question])
print("Magic 8-Ball's answer:",[answer])
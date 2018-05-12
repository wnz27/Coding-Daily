#! pyhton3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and Values are their capitals.
capitals = {
    'Alabama':'Montgomery',
    'Alaska':'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California':'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida':'Tallahassee',
    'Georgia':'Atlanta',
    'Hawaii':'Honolulu',
    'Idaho':'Boise',
    'Illinois':'Springfield',
    'Indiana':'Indianapolis',
    'Iowa':'Des Moines',
    'Kansas':'Topeka',
    'Kentucky':'Frankfort', 
    'Louisiana':'Baton Rouge',
    'Maine':'Augusta',
    'Maryland':'Annapolis',
    'Massachusetts':'Boston',
    'Michigan':'Lansing',
    'Minnesota':'Saint Paul',
    'Mississippi':'Jackson',
    'Missouri':'Jefferson City',
    'Montana':'Helena',
    'Nebraska':'Lincoln',
    'Nevada':'Carson City',
    'New Hampshire':'Concord',
    'New Jersey':'Trenton',
    'New Mexico':'Santa Fe',
    'New York':'Albany',
    'North Carolina':'Raleigh',
    'North Dakota':'Bismarck',
    'Ohio':'Columbus',
    'Oklahoma':'Oklahoma City',
    'Oregon':'Salem',
    'Pennsylvania':'Harrisburg',
    'Rhode Island':'Providence',
    'South Carolina':'Columbia',
    'South Dakota':'Pierre',
    'Tennessee':'Nashville',
    'Texas':'Austin',
    'Utah':'Salt Lake City',
    'Vermont':'Montpelier',
    'Virginia':'Richmond',
    'Washington':'Olympia',
    'West Virginia':'Charleston',
    'Wisconsin':'Madison',
    'Wyoming':'Cheyenne'
}

#Generate 35 quiz files.
for quizNum in range(35):
    #TODO: Creat the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1),'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1),'w')
   
    #TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    #TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #TODO: Write the question and answer to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
        for i in range(4):
            quizFile.write('%s.%s    ' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n\n')

        #TODO: Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()



#先要import os
#os.getcwd()获取当前目录名
#os.chdir(目录名)更换到目录名位置
#.当目录名时指的当前目录
#..当目录名时指的是父目录，也就是上一层目录
#os.makedirs()创建新文件夹，不管你用相对路径还是绝对路径，路径里经过的所有文件目录名如果没有都会被新建

# Quiz App

# Class Question
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True or False

# Class Quiz
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()         
#       - displayQuestion()     => displays the object retrieved by getQuestion().
#       - displayScore()        => displays score information.
#       - displayProgress()     => displays progress in test.

import random


class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer =  answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("False Drop!")
           
        elif answer == self.answer:
            print("Correct!")

        else:
            print("False!")


class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions,len(questions))
        self.questionIndex = 0
        self.score = 0
        self.correct = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        op = input("To exit the test (e/E) :")
        if op == "e" or op == "E":
            exit()
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print("-" + q)
        
        ans = input("Your answer :")
        if question.checkAnswer(ans):
            puan = 100 / len(self.questions)
            self.score += puan
            self.correct +=1
         
        self.questionIndex += 1
        self.loadQuestion()

    def loadQuestion(self):
        if self.questionIndex != len(self.questions):
            self.displayProgress()
            self.displayQuestion()
        else :
            self.displayScore()

    def displayScore(self):
        print("Score : ",self.score )
        print("Correct Count : ",self.correct)
    
    def displayProgress(self):

        print(f" You are on question {self.questionIndex + 1} of {len(self.questions)} questions.".center(100,"-"))


def main():
    q1 = Question("What is the best programming language?",["python","c#","java","dart"],"python")
    q2 = Question("What is the most popular programming language?",["python","java","c#","dart"],"python")
    q3 = Question("What is the most rewarding programming language?",["python","java","dart","c#"],"python")

    questions = [q1,q2,q3]
    quiz = Quiz(questions)
    print(quiz.loadQuestion())

main()
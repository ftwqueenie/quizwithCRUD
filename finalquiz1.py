
"""
Created on Sun Sep 29 16:38:32 2020

@author: Queenie
"""
#import
import os.path
from os import path

#the variables
questions = ['UAE', 'UK', 'Philippines', 'Belgium', 'Egypt', 'China', 'Japan', 'Bulagaria']
answers = ['Abu Dhabi', 'london', 'Manila', 'Brussels', 'Cairo', 'Beijing', 'Tokyo', 'Sofia']
correct = []
score = len(correct)
global scorer
global namescore
global scorelist
global rater
namescore = []
scorer = []
rater = []


print("The Capital quiz")
name = input('What is your name: ')

#The functions
def intro(name):
        print ("Hello ", name)
        namescore.append(name)
       

def rating(score):
    print("your score is ",score)
    if score == len(questions):
        print("Perfect! You're a walking atlas")
        rater.append('Passed')
    elif score >= len(questions) * 0.7:
        print("Wow! You're quite great at geography")
        rater.append('Passed')
    else:
        print("Tough luck, pal. Study more and you'll get there")
        rater.append('Failed')
    scorer.append(score)
    
    
def quiz(questions, answers):
    i=0
    for question in questions:
        print("What is the capital of ",question,"?")
        your_ans = input('answer:')
    
        if your_ans.title() == answers[i].title():
            print("Correct!")
            correct.append('yes')
           
        else:
            print("Wrong!")
           
        i = i+1
        
def loadscores():
   
    for name in namescore:
        numscores = 0
                
        if path.exists("scoreboard.txt"):
            scoreboard = open("scoreboard.txt","a")
            scoreboard.write(str(namescore).replace('[', '').replace(']','')+"\t")
            scoreboard.write(str(scorer).replace('[', '').replace(']','')+"\t")
            scoreboard.write(str(rater).replace('[', '').replace(']','')+"\n")
            last_list = open("scoreboard.txt","r")
            plsread = last_list.readlines()
           
            for line in plsread:
                last_list.close()
                numscores+=1
            if numscores>=3:
                del plsread[0]
             
                newscore = open("scoreboard.txt", "w")
                for line in plsread:
                    newscore.write(line) 
                newscore.close()
        else: 
            scoreboard = open("scoreboard.txt","w")
            scoreboard.write(str(namescore).replace('[', '').replace(']','')+"\t")
            scoreboard.write(str(scorer).replace('[', '').replace(']','')+"\t")
            scoreboard.write(str(rater).replace('[', '').replace(']','')+"\n")
            last_list = open("scoreboard.txt","r")
    
            plsread = last_list.readlines()
           
            for line in plsread:
                last_list.close()
                numscores+=1
            if numscores>=3:
                del plsread[0]
                newscore = open("scoreboard.txt", "w")
                for line in plsread:
                    newscore.write(line) 
                newscore.close()

 
#function call

intro(name)
quiz(questions, answers)
score = len(correct) 
rating(score)
loadscores()
          
#end
       
          



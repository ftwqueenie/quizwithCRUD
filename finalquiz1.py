
"""
Created on Sun Sep 29 16:38:32 2020

@author: Queenie
"""
#import
import os.path
from os import path

#the variables
global questions
global answers
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
def initializer():
    
    print("MENU:")
    user_choice = input("Please select your action\n[1]play game \n[2] admin mode\n")
    write_question()
    if user_choice == "1":
        quiz(questions, answers)
        score = len(correct) 
        rating(score)
        loadscores()
    elif user_choice == "2":
        print("Welcome to admin mode")
        admin_mode()
    else:
        print("\nInvalid choice, please choose again")
        initializer()
        
def admin_mode():
    admin_choice = input("Hi admin "+name+"!,\nPlease select your action\n[1]add questions\n[2] delete questions\n")
    if admin_choice == "1":
        print("===Add Question===\n")
        add_question()
    elif admin_choice == "2":
        print("===Delete Question===\n")
        del_questions()
    else:
        print("Choice Invalid! Please try again\n")       
def write_question():
    global answers
    global questions
    qa_pool = open("qa.txt","w")
    i=0
    for question in questions:
        qa_pool.write("country: "+question+"\t")
        qa_pool.write("capital: "+answers[i].title()+"\n")
        i=i+1
        
def add_question():
    new_question=""
    new_answer=""
    new_question = input("What country would you like to add? ")
    questions.append(new_question)
    print(questions)
    new_answer = input("What is the capital of "+new_question+"? ")
    answers.append(new_answer)
    print("Question successfully added!")
    qa_pool = open("qa.txt","a")
    qa_pool.write("country: "+new_question+"\t")
    qa_pool.write("capital: "+new_answer.title()+"\n")
    
def del_questions():
    for index, question in enumerate(questions):
        place = str(index)
        print("["+place+"]\t"+question)
        
        
        
        
    del_choice = input("Please select the index of the question you would like to delete.")
    questions.pop(int(del_choice))
    answers.pop(int(del_choice))
    qa_pool = open("qa.txt","r")
    plsread = qa_pool.readlines()
    del plsread[int(del_choice)]
    qa_pool.close()
    newquest = open("qa.txt", "w")
    
    for line in plsread:
        newquest.write(line) 
    newquest.close()
   
    print("Here are the remaining questions")
    for index, question in enumerate(questions):
        place = str(index)
        print("["+place+"]\t"+question)
    
    
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
    print("MOST RECENT SCORES")
    for name in namescore:
        numscores = 0
        
        if path.exists("scoreboard.txt"):
            scoreboard = open("scoreboard.txt","a")
            scoreboard.write(str(namescore).replace('[', '').replace(']','')+"\t")
            #print(str(namescore).replace('[', '').replace(']','')+"\t"+str(scorer).replace('[', '').replace(']','')+"\t")
        
            scoreboard.write(str(scorer).replace('[', '').replace(']','')+"\t")
            scoreboard.write(str(rater).replace('[', '').replace(']','')+"\n")
            #print(str(namescore).replace('[', '').replace(']','')+"\t"+str(scorer).replace('[', '').replace(']','')+"\t"+str(rater).replace('[', '').replace(']','')+"\n")
            last_list = open("scoreboard.txt","r")
            plsread = last_list.readlines()
           
            for line in plsread:
                last_list.close()
                
                numscores+=1
            if numscores>=10:
                del plsread[0]
             
                newscore = open("scoreboard.txt", "w")
                for line in plsread:
                    newscore.write(line) 
                    print(line)
                newscore.close()
            print(str(namescore).replace('[', '').replace(']','')+"\t"+str(scorer).replace('[', '').replace(']','')+"\t"+str(rater).replace('[', '').replace(']','')+"\n")
        else: 
            scoreboard = open("scoreboard.txt","w")
            scoreboard.write(str(namescore).replace('[', '').replace(']','')+"\t")
            scoreboard.write(str(scorer).replace('[', '').replace(']','')+"\t")
            scoreboard.write(str(rater).replace('[', '').replace(']','')+"\n")
        
            last_list = open("scoreboard.txt","r")
    
            plsread = last_list.readlines()
           
            for line in plsread:
                last_list.close()
                #print(line)
                numscores+=1
            if numscores>=10:
                del plsread[0]
                newscore = open("scoreboard.txt", "w")
                for line in plsread:
                    newscore.write(line) 
                    print(line)
                newscore.close()
            print(str(namescore).replace('[', '').replace(']','')+"\t"+str(scorer).replace('[', '').replace(']','')+"\t"+str(rater).replace('[', '').replace(']','')+"\n")

 
#function call

intro(name)
initializer()

          
#end
       
          



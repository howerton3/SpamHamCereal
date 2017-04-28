'''
Kenneth Howerton, Sarah Gore, Yasmeen Cherry
Phishing and Anti-Spam Classification for Python
CSC 130
April 2017

This code classifies Cereal utilizing a sudo Bayesian
method as spam or ham (unhealthy or healthy). It only
assumes a score of greater than 50% as Spam. 
'''

import csv
from decimal import *

def csv_reader():
    #Declare temporary list and cereal ingredient list.
    tempList=[]
    cerealIngredients=[]
    #read the csv data for parsing
    with open("cereal.csv","r") as f_obj:
        reader = csv.reader(f_obj)
        for row in reader:
            tempList.append(row)
    #parse the list
    for i in tempList:
        words = str(i[0]).split(";")
        cerealIngredients.append(words)
        
    #for testing: print(cerealIngredients)
    #return to be used in other methods
    return cerealIngredients

def bagOfWords():
    '''This method sets two bags of known ingredients that are either ham
    or spam.
    '''
    ham = ['vitA','vitB','vitC','vitD','vitE','minerals','raisins','fruit','rice',\
           'bran','oats']

    spam = ['gmo','soy','bht','bha','yellow5','yellow6','red3','red40','hfcp',\
            'green3','red2']

    #print(ham)
    #print(spam)
    return ham, spam

def cereal():
    #create list of cereal names
    cerealNames=[]
    cereals = csv_reader()

    for i in cereals:
        cerealNames.append(i[0])

    #print(cerealNames)
    return cerealNames
    
def ingredients():
    #create list of ingredients corresponding to each cereal
    ingredientList=[]
    ingredients = csv_reader()

    for i in ingredients:
        ingredientList.append(i[1:])

    return ingredientList

def checkSpamHam():
    #iterate through each ingredient in the list of lists, determine
    #if it is in spam or ham
    getcontext().prec=3
    ingredient = ingredients()
    Ham,Spam = bagOfWords()
    print(Ham)
    print(Spam)
    cerealName = cereal()
    runningTotal=0
    count = 0
    '''
    These lists can be used for more in depth Bayesian analysis.
    spamProbList=[]
    spam=[]
    ham=[]
    gmo=[]
    bht=[]
    bha=[]
    yellow5=[]
    yellow6=[]
    red3=[]
    red40=[]
    hfcp=[]
    green3=[]
    red2=[]
    '''
    while count < len(cerealName):
    #iterate through each ingredient in the list of lists, determine
    #if it is in spam or ham
        for i in ingredient:
            total=0
            countSpam=0
            countHam=0
            #spamProb=[]
            #spamHam = Decimal((0.3*0.3*0.4*0.6*0.5*0.9*0.9*0.6*0.7*0.8)+((1-.3)*(1-.3)*(1-.4)*(1-.6)*(1-.5)*(1-.9)*(1-.9)*(1-.6)*(1-.7)*(1-.8)))
            for j in i:
                if j in Spam[:]:
                    countSpam +=1
                    '''
                    This portion of the code can be used to develop a more in depth Bayesian calculation based on
                    the individual occurences of each known spam word.  Instead of going in depth, we utilize an
                    an unbiased approach stating if the spamScore is greater than 50%, it is spam. Typically, in email
                    it is usually considered 80%; however it was not necessary to use such a high number given less
                    natural language is utilized in the spam data.
                    if j == 'gmo':
                        spamProb.append(Decimal(0.3))
                    elif j == 'bht':
                        spamProb.append(Decimal(0.3))
                    elif j == 'bha':
                        spamProb.append(Decimal(0.4))
                    elif j == 'yellow5':
                        spamProb.append(Decimal(0.6))
                    elif j == 'yellow6':
                        spamProb.append(Decimal(0.5))
                    elif j == 'red3':
                        spamProb.append(Decimal(0.9))
                    elif j == 'red40':
                        spamProb.append(Decimal(0.9))
                    elif j == 'hfcp':
                        spamProb.append(Decimal(0.6))
                    elif j == 'green3':
                        spamProb.append(Decimal(0.7))
                    elif j == 'red2':
                        spamProb.append(Decimal(0.8))
                        '''
                else:
                    countHam +=1
  
            spamScore = Decimal((countSpam*10)/100)
            hamScore = Decimal((countHam*10)/100)
            
            if spamScore>=.5:
                print(cerealName[count],"is spam")
                #spam.append(count)
            else:
                print(cerealName[count],"is ham")
                #ham.append(count)
            count+=1
    '''
    If going more in depth, the below line can be ran in order to calculate the final Bayesian probability for
    independent variables.
    
            #spamProbList.append(spamScore*hamScore)
            #runningTotal += spamScore*hamScore

    spamProbList[:]=[x/runningTotal for x in spamProbList]
    
    while count < len(cerealName):

        for i in spamProb:
               
            spamProb=runningTotal*spamProbList
            if spamProb >= 0.5:
                print(cerealName[count],"has a spam probability greater than 50%.  Probability it is spam =",spamProb)
            if spamProb < 0.5:
                print(cerealName[count],"has a spam probability greater than 50%.  Probability it is spam =",spamProb)
            count+=1
            
    '''
def enter_cereal_info():
    #Get the cereal's information: Brand, type, sugar/vitamin content, and grains(yes or no)
              brand = input("enter brand: ")
              ctype = input("enter cereal type: ")
              sugar =int(input("enter sugar in grams: "))
              vitamins=int(input("enter number of vitamins: "))
              grains=input("enter y for whole grains or n for not:")
              
              return brand + "," + ctype + \
                     ","+ str(sugar) +\
                     "," + str(vitamins) +\
                     "," + grains +'\n'
def add_cereal_to_records(cer_rec_file):
    #Call enter_cereal_info to add a cereal to our file
              cer_file_obj = open(cer_rec_file, 'a')  # append file
              cer_info = enter_cereal_info()
              cer_file_obj.write(cer_info)
              cer_file_obj.close()

def search_cereal(ctype, cer_rec_file):
    #Use a cereal type to check if it is in our file
              found = False
              cer_file_obj = open(cer_rec_file, 'r')
              cer_rec = cer_file_obj.readline() #empty string = end of file
              temp_cer_rec=" "
              while cer_rec != '':
                            new_cer_rec = cer_rec.rstrip('\n')
                            new_cer_list = new_cer_rec.split(',')
                            if new_cer_list[1] == str(ctype):
                                          found = True
                                          temp_cer_rec=new_cer_rec
                                          cer_rec = ''
                            else:
                                          cer_rec = cer_file_obj.readline()
              cer_file_obj.close()
              return found, new_cer_rec
def display_cereal_info(ctype,cer_rec_file):
    #Search our file for a cereal and display its info, if there.
    cer_file_obj=open(cer_rec_file,'r')
    cer_rec=cer_file_obj.readline()
    if ctype == cer_rec:
        print(cer_rec)
    cer_file_obj.close()
def calculate_nutrition(ctype, cer_rec_file):
    #First, search file for cereal
        found, cer_rec=search_cereal(ctype, cer_rec_file)
        if found:
            #Turn the cereal information into a list
            new_cer_rec=cer_rec.rstrip('\n')
            new_cer_list=new_cer_rec.split(',')
            #begin with cereal suagr content. Subtract number of vitamins * 25
            adjusted_score=float(new_cer_list[2]) - \
                            float(new_cer_list[3])*25
            if new_cer_list[4]=="Y" or new_cer_list[4]=="y":
                #If cereal is whole grain, take 25 percent of the previous figure
                net_score = adjusted_score*.25
            elif new_cer_list[4]=="N" or new_cer_list[4]=="n":
                #If not whole grain, take 15 percent. This is totally arbitrary, obviously.
                net_score= adjusted_score*.15
        else:
            #10's just kind of a default value. 
            return 10
        #Return our "nutrition score"
        return net_score

def menu():
              quit = False
              while not quit:
                  #Print menu options, because I can never remember which is which
                            print("0: add to cereal record. 1: quit.")
                            print("2: search for cereal type. 3: display cereal type.")
                            print("4: Calculate nutrition score (bigger number means worse nutrition.)")
                            print("5: Access preexisting file of cereals and ingredients to view scores.")
                            command = int(input("Enter a command: "))
                            if command == 0:
                                          add_cereal_to_records("cerRec.txt")
                            elif command == 1:
                                quit= True
                            elif command == 2:
                                #Get a cereal kind to search for, then call search function
                                          ctype = input("enter cereal type: ")
                                          print(search_cereal(ctype, "cerRec.txt"))
                            elif command == 3:
                                #get a cereal type, search for it, then print it
                                ctype = input("enter cereal type: ")
                                print(display_cereal_info(cer_id, "cerRec.txt"))
                            elif command == 4:
                                #Hilariously arbitrary "score" calculated here
                                ctype=input("enter cereal type: ")
                                net_score=calculate_nutrition(ctype, "cerRec.txt")
                                print(net_score)
                            elif command == 5:
                                checkSpamHam()
                           


checkSpamHam()
menu()

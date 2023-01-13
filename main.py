from imports import *

def tokenize(ques):
  ques = ques.lower()
  ques=word_tokenize(ques)
  return ques

def replace(ques):
  t=(random.choice(string.ascii_letters))
  if "{" and "}" in ques:
    for n,i in enumerate(ques):
      
     if ques.index("{") < n < ques.index("}"):
        if(ques[n] in string.ascii_letters):
         ques[n]=random.choice(string.ascii_letters)
        try:
          if isinstance(int(i),int):
             ques[n]=str(random.randint(-50,50))
        except ValueError:
          continue
     else:
        if(ques[n] in string.ascii_letters):
            ques[n]=str(t)
        try:
           if isinstance(int(i),int):
             ques[n]=str(random.randint(-50,50))
     
        except ValueError:
         continue


  else:
    for n,i in enumerate(ques):
     if(ques[n] in string.ascii_letters):
         ques[n]=str(t)
     try:
         if isinstance(int(i),int):
             ques[n]=str(random.randint(-50,50))
        
     except ValueError:
       continue


  temp=' '.join(ques)
  temp=temp.capitalize()
  return temp

def replacefloat(ques):
  for n,i in enumerate(ques):
    try:
      if(float(ques[n])):
        ques[n]=str(round(random.uniform(-33.33,66.66),5))
    except ValueError:
      continue
   
  temp = ' '.join(ques)
  temp=temp.capitalize()
  return temp

def randomlist():
  size=random.randint(0,15)
  word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
  response = urlopen(word_site)
  txt = response.read()
  WORDS = txt.splitlines()
  newlist=[]
  for i in range(0,size):
    n=str(random.choice(WORDS))
    newlist.append(n[2:-1])

  return newlist

def randomintlistques():
  size=random.randint(2,15)
  list1=[]
  for x in range(0,size):
    list1.append(random.randint(-50,50))

  ques = "Given a list, mylist = "+str(list1)+" \n print(len(mylist)) \n print(mylist[-1])"
  return ques

def randomfloatlistques():
  size=random.randint(2,15)
  list1=[]
  for x in range(0,size):
    list1.append(round(random.uniform(-33.33, 66.66), 2))

  ques = "Given a list, mylist = "+str(list1)+" \n print(len(mylist)) \n print(mylist[0])"
  return ques

def randomcharlistques():

  string.ascii_letters
  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  size=random.randint(2,15)
  list1=[]
  for x in range(0,size):
    list1.append(random.choice(string.ascii_letters))

  ques = "Given a list, mylist = "+str(list1)+" \n print(len(mylist)) \n print(mylist[-1])"
  return ques

def listques(newlist, poststr):
    pre = "What will be the output of the python code: \n list1 = "
    ques = pre+str(newlist)+"\n"+str(poststr)
    return ques

def cprogramques():
  allcodes=cdata.split('#include <stdio.h>')
  ccode=(str(random.choice(allcodes)))
  ques = "What will be the output of the following c program \n:" + ccode
  return ques

with open('inputs/input1.csv', newline = '') as f:    
  r=csv.reader(f)
  input1 = []
  for line in r:
    input1.extend(map(str,line)) 

with open('inputs/input2.csv', newline = '') as f:    
  r=csv.reader(f)
  input2 = []
  for line in r:
    input2.extend(map(str,line)) 

with open('inputs/input3.csv', newline = '') as f:    
  r=csv.reader(f)
  input3 = []
  for line in r:
    input3.extend(map(str,line)) 

with open('inputs/cprograms.txt') as f:
  cdata=str(f.read())

with open("outputs/output1.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for x in input1:
        for i in range(0,500):
            writer.writerow([replace(tokenize(x))])

    for x in input2:
        for i in range(0,500):
            writer.writerow([replacefloat(tokenize(x))])

   
    for x in input3:
        for i in range(0,1000):
            writer.writerow([listques(randomlist(), x)])

    for i in range(0,1000):
      writer.writerow([cprogramques()])

    for i in range(0,500):
      writer.writerow([randomintlistques()])
    
    for i in range(0,500):
      writer.writerow([randomfloatlistques()])

    for i in range(0,500):
      writer.writerow([randomcharlistques()])

                

# fid = open("outputs/output1.csv", "r")
# li = fid.readlines()
# fid.close()

# random.shuffle(li)

# with open("outputs/output1_shuffled.csv", 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(li)

from imports import*
import string
string.ascii_letters
'abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
random.choice(string.ascii_letters)
size=random.randint(0,10)
randomlist=[]
     

code1=[]
codes1=[]
with open('questions/looptype.csv', newline = '') as f:          
  r=csv.reader(f)
  looptype = []
  for line in r:
    looptype.extend(map(str,line))
with open('questions/looptype0.csv', newline = '') as f:          
  r=csv.reader(f)
  looptype0 = []
  for line in r:
    looptype0.extend(map(str,line))
with open('questions/looptype1.csv', newline = '') as f:          
  r=csv.reader(f)
  looptype1 = []
  for line in r:
    looptype1.extend(map(str,line))
with open('questions/looptype2.csv', newline = '') as f:          
  r=csv.reader(f)
  looptype2 = []
  for line in r:
    looptype2.extend(map(str,line))
with open('questions/looptype3.csv', newline = '') as f:          
  r=csv.reader(f)
  looptype3 = []
  for line in r:
    looptype3.extend(map(str,line))
with open('questions/looptype4.csv', newline = '') as f:          
  r=csv.reader(f)
  looptype4 = []
  for line in r:
    looptype4.extend(map(str,line))
with open('answers/answers1.csv', newline = '') as f:          
  r=csv.reader(f)
  answers1 = []
  for line in r:
    answers1.extend(map(str,line))
    
    with open("output.csv", 'w', newline='') as csvfile:
     writer = csv.writer(csvfile)
     writer.writerow(['QUESTIONS'])

     
     with open('input.csv', 'r') as f:
      data = csv.reader(f, delimiter="\t")
      for row in data:
       question = row
       question = ''.join(question)
       question = question.lower()
       codes=question.split('?')
       code=codes[1]
       code=word_tokenize(code)

       if "range" in code:
        if any(y in code for y in looptype):
          for y in code:
              if y in looptype0:
                index = code.index(y)
                for x in range(0,10000):
                  for i in looptype0:
                    temp =code[:index]+[i]+code[index+1:]
                    temp = ' '.join(temp) 
                    temp1=codes[0]
                    temp2=temp1+":"+" "+temp+"?"
                    row1=[]
                    row1.insert(0,temp2)
                    writer.writerow(row1)
        
                
       if "range" in code:
          if any(y in code for y in looptype):
            for y in code:
              if y in looptype2:
                index=code.index(y)
              if y in looptype1:
                index=code.index(y)
                for x in range(0,10000):
                  for j in looptype1:
                    for k in looptype2:
                      tempt1="while"+"("+(k)+ "<"+(j)
                      temp2=code[index+1:]
                      temp=" "
                      tempm=temp.join(temp2)
                      temp3=tempt1+(tempm)
                      tempx=codes[0]
                      temp4=tempx+":"+(k)+"=0"+" "+temp3+"?"
                      row1=[]
                      row1.insert(0,temp4)
                      writer.writerow(row1)
     with open('input2.csv', 'r') as f1:
      data1 = csv.reader(f1, delimiter="\t")
      for row1 in data1:
        question1 = row1
        question1 = ''.join(question1)
        question1 = question1.lower()
        codes1=question1.split('?')
        code1.append(codes1[-1])
        code1 = ''.join(code1)
        code1=word_tokenize(code1)
        if "while" in code1:
          if any(y in code1 for y in looptype):
            for y in code1:
              if y in looptype3:
                index=code1.index(y)
              if y in looptype1:
                index=code1.index(y)
                for x in range(0,10000):
                  for j in looptype1:
                    for k in looptype3:
                      tempt1="for"+" "+(k)+" "+"in"+" "+"range"+"("+(j)
                      temp2=code1[index+1:]
                      temp=" "
                      tempm=temp.join(temp2)
                      temp3=tempt1+(tempm)
                      tempx=codes1[0]
                      temp4=tempx+":"+temp3
                      row1=[]
                      row1.insert(0,temp4)
                      writer.writerow(row1)
     with open('input3.csv', 'r') as f3:
      data3 = csv.reader(f3, delimiter="\t")
      for row3 in data3:
       question3 = row3
       question3 = ''.join(question3)
       question3 = question3.lower()
       ques=word_tokenize(question3) 
       for x in range(0,10000):
        t=(random.choice(string.ascii_letters))
        for n, i in enumerate(ques):
          if(ques[n] in string.ascii_letters):
            ques[n]=str(t)
          temp=' '.join(ques) 
          row3=[]
          row3.insert(0,temp)
          writer.writerow(row3)
     with open('input4.csv', 'r') as f4:
      data4 = csv.reader(f4, delimiter="\t")
      for row4 in data4:
       question4 = row4
       question4 = ''.join(question4)
       question4 = question4.lower()
       ques4=word_tokenize(question4) 
       for x in range(0,10000):
        for n, i in enumerate(ques4):
          try:
            if isinstance(int(i), int):
              ques4[n]=str(random.randint(-50,50))
          except ValueError:
            continue
          temp=' '.join(ques4) 
          row4=[]
          row4.insert(0,temp)
          writer.writerow(row4)
     with open('input5.csv', 'r') as f5:
      data5 = csv.reader(f5, delimiter="\t")
      for row5 in data5:
        question5 = row5
        question5 = ''.join(question5)
        question5 = question5.lower()
        ques5=word_tokenize(question5)
        for x in range(0,10000):
          for n, i in enumerate(ques5):
            try:
              if isinstance(int(i), int):
                ques5[n]=str(random.randint(-50,50))
            except ValueError:
              continue
            temp=' '.join(ques5) 
            row5=[]
            row5.insert(0,temp)
            writer.writerow(row5)
     with open('input6.csv', 'r') as f6:
      data6 = csv.reader(f6, delimiter="\t")
      for row6 in data6:
        question6 = row6
        question6 = ''.join(question6)
        question6 = question6.lower()
        ques6=word_tokenize(question6)
        for x in range(0,10000):
          t=str(random.choice(looptype4))
          for n, i in enumerate(ques6):
            if(ques6[n] in looptype4):
              ques6[n]=str(t)
              temp=' '.join(ques6) 
              row6=[]
              row6.insert(0,temp)
              writer.writerow(row6)
  

                  
                    
      

    
            
      
        
          
        
          
            
              
          
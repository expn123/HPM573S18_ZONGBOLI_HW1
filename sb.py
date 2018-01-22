#Problem 1: Object
x=17

y1=int(x)
print(y1,type(y1))

y2=float(x)
print(y2,type(y2))

y3=str(x)
print(y3,type(y3))

y4=bool(x>9)
print(y4,type(y4))

text="The value of x is "+y3+'.'
print(text)

#Problem 2

text="I "+"love "+"learning "+"how "+"to "+"code!"
print(text)

#Problem 3
#iterative
def sum_it(n):
    sum=0
    for i in range(1,n+1):
        sum +=i
    return sum
print(sum_it(100))

##recursive
def sum_rec(n):
    if n==1:
       return 1
    else:
      return n+sum_rec(n-1)
print(sum_rec(100))

#Problem 4
yours=['Yale','MIT','Berkeley']
mine=['PKU','SDSZ','SDF']
ours1=mine+yours
ours2=[]
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)
#ours1 is a list which is made up of by two lists-yours and mine.
#ours2 is a list which has two lists in it-ours1 and ours2.
yours[1]='MIT1'
print(ours1)
print(ours2)
#Because ours1 is already defined before by combining yours and mine in line 44 however the ours2 is based on yours and mine.
#As a result, if i change yours, ours2 will change but ours1 will not. 

#question5
dayNumber={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'Octobor':10,
           'November':11,'December':12,
           1:'January',2:'February',3:'March',4:"April",5:'May',6:'June',7:'July',8:'August',9:'September',10:'Octobor',
           11:'November',12:'December'}
print("The sixth number is "+dayNumber[6]+".")
print("February is "+str(dayNumber['February'])+".")

#there are two types of loops 
#1 for loops
#2 while loops


#while it is also known as infinite loop
# x=0
# while(x<5):
#     print(x)
#     x=x+1

#for loops
# for x in range(5,10):
#     print(x)

#array
days=["mon","tue","wed","thu","fri","sat","sun"]
for x in days:
    #if(x=="fri"):break #stop loop
    if(x=="mon"):continue #skip
    print(x)

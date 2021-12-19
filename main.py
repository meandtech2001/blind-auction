from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bid_list=[]
def info(name1,bid1):
  new={}
  new["name"]=name1
  new["bid"]=bid1
  bid_list.append(new)

def comparebid():
  maxnum=0
  name=""
  for i in bid_list:
    if i["bid"] > maxnum:
      maxnum =  i["bid"]
      name= i["name"]
  print(f"The winner is {name} with a bid of ${maxnum}")


flag=0

while(flag==0):
 
 name=input("What is your name? : ")
 bid=int(input("What's your bid? : "))
 choice=input("Are there anymore bidders? Type 'yes' or 'no'. ")
 info(name,bid)

 clear()

 if choice == 'no':
   comparebid()
   flag=1

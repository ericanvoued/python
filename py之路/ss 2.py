#import time;
#import time as t;
#from time import time,localtime;
from time import *;
import copy;
import pickle;

print(localtime(),time())
a = True;
while a:
    x = input("input your number:");
    if x==str("1"):
        print("your number is:",x);
        a=False;
    else:
        pass;
print("finish")

try:
    file=open("eee","r+");
except Exception as e:
    print("there is no file eee!");
    responce = input("Do you want to creat a new file(y/n):");
    if responce=='y':
        file=open("eee","w");
    else:
        pass;
else:
    file.write("sss");
    print("sss had been write")
file.close();

aa=[1,2,3,4];
bb=[5,6,7,8];
print(zip(aa,bb));
print(list(zip(aa,bb,aa)));

for i,j,z in zip(aa,bb,aa):
    print(i/1,j*2,z*3);
def fun1(x,y):
    print(x+y);
print(fun1(2,3))
fun2 = lambda x,y:x+y;
print(fun2(21323,223423))
list(map(fun1,aa,bb));

xx=[123,23,12];
yy=xx;
print(id(xx),id(yy));
yy[0]=0;
print(xx)
zz=copy.copy(xx);
print(id(xx)==id(zz));
kk=copy.deepcopy(xx);
print(id(xx)==id(kk));

adist = {"da":111,2:[222,333,444],"ss":{"qq":"ghff"}};
file = open("pickle_example.pickle","wb");
pickle.dump(adist,file);
file.close()

file = open("pickle_example.pickle","rb");
a_dict = pickle.load(file);
file.close();
print(a_dict)

with open("pickle_example.pickle","rb") as file:
    a_dict = pickle.load(file);
    print(a_dict)

char_list=[1,2,3,4,5,6,4,2,4,2,1,2,4,5,9,55];
sentence = "welcome back to to";
print(set(sentence));
print(set(char_list));
print(type(set(char_list)))

unique_char = set(sentence);
unique_char.add("x")
print(unique_char)
#unique_char.clear();
print(unique_char);
unique_char.discard("w");
print(unique_char);
set2 = {"f","b"};

print(unique_char.difference(set2));
print(unique_char.intersection(set2));


    

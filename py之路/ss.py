c = 1;
while c<10:
    print(c);
    c = c+1;

a,b,d,s=1,2,3,4;
print(a,b,d,s)



example_list=[1,23,3,4,1,2,3,4,3,2,2,2,3,4,4,4];
for i in example_list:
    print(i)
    print("inner for");
print("outer");

for i in range(1,10):
    print(i)

for i in range(1,20,5):
    print(i)


x,y,z=1,2,3;
if x<y:
    print("x less than y");
if x<y<z:
    print("x less than y,y less than z");

xx,yy,zz=2,3,4;
if xx>yy:
    print("xx");
else:
    print("yy");

def fun():
    cc=xx+yy;
    print("this is a function");
    print(cc);
fun();
def sale_car(price,color,brand,is_second_hand=True):
    print(
        'price:',price,
        "color:",color,
        "brand:",brand,
        "second_hand:",is_second_hand
    )
    
def fn():
    aa=10;
    print(aa);
    return aa+100;

sale_car(1999,"red","carmry")
print(fn());

APPLE=1000;
AAA = None;
def func():
    global AAA;
    AAA = 20;
    print(AAA)
    return AAA+100;
print(func(),AAA)

text="this is the first\nthis is second\n3";

my_file=open('myfile.txt','w')
append_text = "\nThis is the append text;"
my_file.write(text);
my_file.close();
my_file = open("myfile.txt","a");
my_file.write(append_text);
my_file.close();
file = open("myfile.txt","r");

content1=file.readline();
secondline = file.readline();
contentlist = file.readlines();

print(content1);
print(secondline);
print(contentlist);

class Calculate:
    name = "Good calculator";
    price = 18;
    
    def __init__(self,name,price,height,width,weight):
        self.name = name;
        self.price = price;
        self.height = height;
        self.width = width;
        self.weight = weight;
        self.add(45,23)
    def add(self,x,y):
        print(self.name);
        result = x+y;
        print(result);
    def minus(self,x,y):
        result = x-y;
        print(result);
    def times(self,x,y):
        result = x*y;
        print(result);
    def divide(self,x,y):
        result  = x/y;
        print(result);
calcul = Calculate("bad calculate",12,23,12,32);

print(calcul.name);
print(calcul.price);
print(calcul.minus(2,3))

a_input = int(input("Please give me an input:"));
print("your input is:",a_input)
if a_input==1:
    print("your input is:1");
elif a_input==2:
    print("your input is 2");
else:
    print("your input is:",a_input);
a_tuple = (1,2.3,34,4,43,2,2,443)
a_list = [221,2223,122,122,1,2,2,11,1]

for i in a_tuple:
    print(i);
for index in range(len(a_list)):
    print("index is:",index,"number in a_list is:",a_list[index])
a_list.append(888);
print(a_list);
a_list.insert(0,000);
print(a_list);
a_list.remove(122);
print(a_list);
print(a_list[-1]);

print(a_list[0:3]);#bubaokuo disige
print(a_list[-3:]);
print("this index is:",a_list.index(221))
print("2 times:",a_list.count(2))
a_list.sort()
print(a_list);
a_list.sort(reverse=True)
print(a_list)

dic = {"apple":1,2:"pear"}
print(dic[2],dic['apple'])
del dic['apple'];
dic['dd']=20;
print(dic)

arrr = [1,2,3,4,2,2,1,3,4]
for index in range(len(arrr)):
    print(index)





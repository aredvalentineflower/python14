fruits = ("apple" , "banana" , "cherry")
print(fruits[0])
fruits = ("apple" , "banana" ,  "cherry" , "orange" , "kiwi" , "melon" , "mango")
print(fruits[2:5])
print(fruits[:5])
print(fruits[2:])
#เพิ่มค่าใน
x = ("apple" , "banana" , "cherry")
y = list(x)   #แปลงเป็นlistแล้วเก็บค่าเข้า y
y[1] = "kiwi"
x = tuple(y)
#แปลงlistเป็นtupleแล้วกลับมาเก็บค่าx
print(x)
#ลบค่าในtuple
x = ("apple" , "banana" , "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
#join
tuple1 = ("a" , "b" , "c")
tuple2 = (1 , 2 , 3)
tuple3 = tuple1 + tuple2
print(tuple3)
x  = range(3, 6)
for n in x:
    print(n)
x = range(3, 20, 2)
for n in x:
    print("rangeแบบstep2:", n)
#นางสาวณัฐณิชา อุ่นแก้ว ม.6/14 เลขที่37
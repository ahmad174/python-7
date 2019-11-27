import numpy



"""  Ques 1  """
e = numpy.zeros( (10) )
print (e)

e = numpy.ones( (10) )
print (e)

e = numpy.ones( (10) )*5
print (e)



"""  Ques 2  """
mynumber = numpy.arange(30,70)
print(mynumber)




"""  Ques 3  """
mynumbers = numpy.arange(30,70,2)
print(mynumbers)




"""  Ques 4  """
array_numbers = numpy.array([[17,66,840],[15,65,32],[45,50,20]])
for array in array_numbers:
    for item in array:
        print(item)




"""  Ques 5  """

myrandom = numpy.random.normal(0,1)
print(myrandom)


"""  Ques 6  """
a=numpy.arange(10,22).reshape((3,4))
for x in a:
    print(x)



"""  Ques 7  """

b=numpy.arange(0,20)
for x in b:
    if ( x > 9 and x < 15 ):
        x=x*-1
    print(x)


"""  Ques 8  """
print("  Ques 8  ")
x=[1,8,3,5]
y=numpy.random.randint(0,11,4)
print("x*y:",x*y)




"""  Ques 9  """

rr = numpy.arange(20).reshape(5,4)
print(rr)
print("rr.size",rr.size)
print ("rr shape: ", rr.shape)
print ("rr ndim: ", rr.ndim)
print ("rr dtype.name: ", rr.dtype.name)
print ("rr itemsize: ", rr.itemsize)


"""  Ques 10  """

x = numpy.random.random((3, 3, 3))
print(x)


"""  Ques 11  """

a = numpy.array([9,-1,2,5])
b = numpy.array([1,-6,0,10])
c = numpy.array([[1,8,2,5],[3,1,7,9]])

print(" a - b", a - b )
print(" a * b", a *b )
print(" a.dot(b)", a.dot(b) )
print(" a * 2 ", a * 2 )
print(" numpy.sin(a) : ", numpy.sin(a) )
print(" a < 3 ", a < 3 )
print("a.sum():" ,a.sum())
print("a.sum(axis = 0):", a.sum(axis = 0))
print("c.sum():", c.sum())


print("c.sum(axios = 0):", c.sum(axis = 0))
print("a.min():", a.min())
print("a.max():", a.max())
print("a.mean():", a.mean())
print("a.average:", numpy.average(a))
print("a.median():", numpy.median(a))
print("a.std():", a.std())
print("a.var():", a.var())
print("c.cumsum():", c.cumsum())
print("a[1:2]:", a[1:2])
print("a[2:]:", a[2:])
print("c[-1]:", c[-1])

"""  Ques 12  """



print('Q12')   
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()


"""  Ques 13  """

import matplotlib.pyplot as plt
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.legend()
plt.show()


"""  Ques 14  """

t = numpy.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


"""  Ques 15  """


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

x = ['Python' , 'Java' , 'PHP' , 'JAVASCRIPT' ,'C#','C++']
y_pos = np.arange(len(x))
popularity = [ 22.2 , 17.6 , 8.8 , 8 , 7.7 , 6.7 ]

plt.bar(y_pos, popularity, align='center', alpha=1)
plt.xticks(y_pos, x)
plt.ylabel('popularity')
plt.title(' popularitY of Programming language ')

plt.show()



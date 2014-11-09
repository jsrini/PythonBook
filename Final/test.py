# Chapter 2
print("Chapter 2")

from stats import *
average(1,5)

from ghost import *
g = Ghost("red",0,0)
g.move_up()
g.print_position()


from ghost2 import *

A = GhostA("red",0,0)
A.move_up()
A.print_position()
B = GhostB("green")
B.move_up()
B.print_position()


import fibonacci
fibonacci.fibonacci(10)

import fibonacci2
fibonacci2.fibonacci(10)

import fibonacci3
fibonacci3.fibonacci(10)

import fibonacci4
fibonacci4.fibonacci(10)


# Chapter 3

print("Chapter 3")

import linked_list
el=linked_list.Element(5)
mylist=linked_list.LinkedList(el)
mylist.head.data

mylist = linked_list.LinkedList()

mylist.insert_head_element(2)
mylist.insert_head_element(1)
mylist.insert_tail_element(3)
mylist.insert_tail_element(5)
mylist.insert_tail_element(6)
mylist.insert_tail_element(7)

def my_own_print(element):
    print('element is: ' + str(element.data))

def my_list_processor(element,params):
    if element.data == params[0]:
        el = linked_list.Element(params[1])
        element.add_successor(el)

    if element.data == params[2]:
        element.delete_successor()

mylist.process_list_elements(my_own_print)
mylist.process_list_elements(my_list_processor,[3,4,6])
mylist.print_list()


import queue2
q = queue2.Queue(5)
q.enqueue(10)
q.dequeue()
q.dequeue()
print(q.is_empty())


from vector import Vector
x = Vector((1,1,1))
y = Vector((0,1,0))
x + y
x - y
x * y
x ^ y
x += y
x
x -= y
x
x^= y
x


from contacts import Contacts
cl = Contacts()
cl.add_contact('John','Doe','123-456-7890','john@host.com')
cl.add_contact('Jane','Doe','123-456-7890','jane@host.com')
cl.print_names()
cl.get_contact_by_full_name('John Doe')
cl.search_by_name('Doe')
cl.search_by_name('Jane')


import test_linked_list

# Chapter 4
print("Chapter 4")

import matrix
import matrix2
import matrix3
import matrix4
import matrix5
import matrix6

print("Matrix")
a = matrix.Matrix([[1,2],[3,4]])
b = matrix.Matrix([[5,6],[7,8]])

print(a+b)
print(a-b)
print(a)
a[1,1]


print("Matrix 2")
a = matrix2.Matrix([[1,2],[3,4]])
b = matrix2.Matrix([[5,6],[7,8]])

print(a*b)
print(a+b)
print(a-b)
print(a)
a[1,1]


print("Matrix 3")
a = matrix3.Matrix([[1,2],[3,4]])
b = matrix3.Matrix([[5,6],[7,8]])

print(a*b)
print(a+b)
print(a-b)
print(a)
a[1,1]

print("Matrix 4")
a = matrix4.Matrix([[1,2],[3,4]])
b = matrix4.Matrix([[5,6],[7,8]])

print(a*b)
print(a+b)
print(a-b)
print(a)
a[1,1]
a.transpose()
print(a)
print(a*b)

print("Matrix 5")
a = matrix5.Matrix([[1,2],[3,4]])
b = matrix5.Matrix([[5,6],[7,8]])

print(a*b)
print(a+b)
print(a-b)
print(a)
a[1,1]
a.transpose()
print(a)
print(a*b)


print("Matrix 6")
a = matrix6.Matrix([[1,2],[3,4]])
b = matrix6.Matrix([[5,6],[7,8]])

print(a*b)
print(a+b)
print(a-b)
print(a)
a[1,1]
a.transpose()
print(a)
print(a*b)
print("Identtity")
print(a*a.inverse())

# Chapter 5
print("Chapter 5")
import tree_traversals
print("Test bin heap")
import test_binary_heap

# Chapter 6
print("Chapter 6")
import graph
G = graph.Graph(3)
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 0)
G.print_graph()

print("Graph example")
import graph_example


print("Graph matrix example")
import graph_matrix_example

print("Depth traverse")
G.depth_first_traverse()

print("Breadth traverse")
G.breadth_first_traverse()

print("Test bellman")
import test_bellman


print("Test dijkstra2")
import test_dijkstra2

print("Test floyd warshall")
import test_floyd_warshall


print("Test kruskal")
import test_kruskal

print("Test prim")
import test_prim


print("Weighted graph")
import weighted_graph_example

# Chapter 7
print("Chapter 7")

from msm import *
PRNG = MSM(123)
PRNG.random()
PRNG.random()

PRNG = MSM()
PRNG.random()
PRNG.random()


for i in range(100):
    R0 = (10**2 + math.sqrt(10**4+i*4*10**6))/2
    if R0 % 1 == 0:
        print(str(i) + ": " + str(R0))

from msm import *
a = MSM(100)
a.random()
a.random()
b = MSM(2500)
b.random()
b.random()
c = MSM(7600)
c.random()
c.random()


from lcg import *
from benchmark_prng import *
a = LCG(25214903917,11,2**48)
benchmark_prng(a)

a = LCG(5,1,2**8)
benchmark_prng(a)

a = LCG(23,3,2**8)
benchmark_prng(a)

import random
random.seed()

random.randint(0,10)
random.random()
import random
random.seed()
from benchmark_prng import *
benchmark_prng(random)


import random
prng = random.SystemRandom()
prng.random()
prng.randint(0,10)

import math
def CDF(x):
    return 0.5*(1 + math.erf(x/math.sqrt(2)))

from sample_cdf import *
sample_prng = SampleCDF(CDF,-10,10,1000)
sample_prng.random()

from benchmark_prng import *
benchmark_prng(sample_prng)

from benchmark_prng2 import *
benchmark_prng(sample_prng)

from calculate_pi import *
print(str(calculate_pi(10)))
print(str(calculate_pi(1000)))
print(str(calculate_pi(100000)))

from blackjack import *
print(str(blackjack_win_prob(1000)))

# Chapter 8
print("Chapter 8")


import hashlib
hashobj = hashlib.sha1()
hashobj.update(b"1234")
print(str(hashobj.hexdigest()))

import hmac
msg = 'Test message'
key = 'this_is_the_key'
hm = hmac.new(bytes(key.encode('UTF-8')),
              msg.encode('UTF-8'),
              hashlib.sha1)
print(str(hm.hexdigest()))

# Chapter 9
print("Chapter 9")

import math
def f(x):
    return 3/math.exp(x) - x

def fp(x):
    return -3/math.exp(x)-1

from newton import *
print(str(newton(5,.1,100,f,fp)))
print(str(newton(5,.01,100,f)))

def yp(xn,yn):
    return (yn**(2/3))*xn

from euler import *
print(str(euler(0,1,10,.1,yp)))

def yp(xn,yn):
    return (yn**(2/3))*xn

def ypp(xn,yn0,yn,dx):
    return 2*yn-(yn-yn0)/dx

from euler2o import *
print(str(euler2o(0,1,0,4,0.01,ypp)))

print(str(2/3*math.exp(4) + 1/3*math.exp(-2*4)))


def ypp(xn,yn0,yn,dx):
    return 2*yn-(yn-yn0)/dx

from shooting import *
print(str(shooting(1,0,1,5,10,0.01,0.005,10,ypp)))


print(str(euler2o(0,1,-1.786674,5,0.01,ypp)))



# Chapter 10
print("Chapter 10")


print("Test graham scan")
#import graham_scan


print("Test dnc conv hull")
#import test_dnc_convex_hull




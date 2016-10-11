import tensorflow as tf
import numpy as np

#this gets a list of 10 random numbers between 0 - 1
#NumPy is more effecient than lists
data = np.random.randint(2, size=10)
x = tf.constant(3, name='x')
y = tf.Variable(x + 2)
xArray = tf.constant([3, 2, 1], name='xArray')
yArray = tf.Variable(xArray + 2)
dataArray = tf.Variable(data + 6)


#this will never print 5 because y is an equation object. 
"""
y isn’t given “the current value of x + 5” as in our previous program. 
Instead, it is effectively an equation that means 
“when this variable is computed, take the value of x (as it is then) 
and add 5 to it”. The computation of the value of y is never actually 
performed in the above program.
"""
print(y)

#To fix the above issue:
model = tf.initialize_all_variables()

with tf.Session() as session:
	session.run(model)
	print(session.run(y))
	print(session.run(yArray))
	print(data)
	print(session.run(dataArray))

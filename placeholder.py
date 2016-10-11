import tensorflow as tf

"""
"So far we have used Variables to manage our data, 
but there is a more basic structure, the placeholder. 
A placeholder is simply a variable that we will assign 
data to at a later date. It allows us to create our 
operations and build our computation graph, without 
needing the data. In TensorFlow terminology, we then 
feed data into the graph through these placeholders."
"""
x = tf.placeholder("float", 3) #3 indicated the size of the array but you can put None there to say it can be an array of any length
y = x * 2
x2 = tf.placeholder("float", [None, 3]) #any amount of arrays of 3
y2 = x2 * 2

with tf.Session() as session:
	result = session.run(y, feed_dict={x: [1, 2, 3]})
	print(result)
	x2Data = [[1,2,3],[4,5,6],]
	result2 = session.run(y2, feed_dict={x2: x2Data})
	print(result2)

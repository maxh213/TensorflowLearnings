import tensorflow as tf

x = tf.constant(0, name='x')
print(x)
y = tf.Variable(x + 1, name = 'y')

with tf.Session() as session:
	merged = tf.merge_all_summaries()
	writer = tf.train.SummaryWriter("/graphData/basic", session.graph)
	model = tf.initialize_all_variables()
	session.run(model)
	print(session.run(y))
 

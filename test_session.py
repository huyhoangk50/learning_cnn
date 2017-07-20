import tensorflow as tf 

graph = tf.Graph()

with graph.as_default():
	c = tf.Variable(0.0, name="c")
	init = tf.global_variables_initializer()
	x = tf.constant(5.0)
	y = tf.constant(4.0)
	for i in range(1, 100):
		c = c + 0.1

sess = tf.Session(graph = graph)
sess.run(init)
print 'c = ', sess.run(c)
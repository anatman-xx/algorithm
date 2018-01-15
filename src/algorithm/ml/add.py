import tensorflow as tf

v1 = tf.placeholder(tf.float32)
v2 = tf.placeholder(tf.float32)

o = tf.add(v1, v2)

with tf.Session() as sess:
    print(sess.run(o, feed_dict={v1: [[1, 2], [3, 4]], v2: [[1, 2], [1, 1]]}))

if __name__ == '__main__':
    pass

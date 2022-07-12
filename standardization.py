import tensorflow as tf 
import cv2
tf.compat.v1.disable_eager_execution()
image = cv2.imread("original.png")
cv2.imshow( "input", image)
std_image = tf.image.per_image_standardization(image)
with tf.compat.v1.Session() as sess:
    result = sess.run(std_image) 
    cv2.imshow("result", result) 
    print(result)
cv2.waitKey(0)
cv2.destroyAllWindows()
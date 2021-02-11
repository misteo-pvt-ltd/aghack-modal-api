import tensorflow as tf
import numpy as np
import cv2
from PIL import Image


model = tf.keras.models.load_model('./baseline_model.h5')

classes = 	{0 : 'Bacterial Spot',
 			1 : 'Cold Injury',
 			2 : 'Early Blight',
			3 : 'Healthy',
			4 : 'Little Leaf',
			5 : 'Nutritional Disorder',
			6 : 'Spider Mite Damage',
			7 : 'Tomato Yellow Leaf Curl'}

def predict(image):
	"""
	Just Give an RGB image
	"""
	image = cv2.imread(image)
	image = tf.image.resize(image, [320,320])
	# image = image.numpy()[:,:,3]
	image = np.expand_dims(image, axis = 0)
	prediction = model.predict(image)
	prediction = np.argmax(prediction)
	prediction = classes[prediction]
	print('prediction=',prediction)
	return prediction

# predict('/home/amjadh/Desktop/Misteo/aghack/images/bacterialspot.png')
# predict('/home/amjadh/Pictures/Screenshot from 2021-02-11 22-31-40.png')

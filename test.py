import tensorflow as tf
import numpy as np
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

def predict(image_path):
    """
    Just Give an image path
    """
    image = Image.open(image_path)
    image = np.array(image)
    image = tf.image.resize(image, [320,320])
    image = image.numpy()[:,:,:3]
    image = np.expand_dims(image, axis = 0)
    prediction = model.predict(image)
    prediction = np.argmax(prediction)
    prediction = classes[prediction]
    return prediction
predict("/home/amjadh/Desktop/Misteo/aghack/images/bacterialspot.png")
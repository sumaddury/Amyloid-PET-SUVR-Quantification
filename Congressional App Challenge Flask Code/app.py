from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
# from PIL import Image
# import numpy as np
# import scipy
import os
import scipy
from pandas import DataFrame
import glob

try:
	import shutil
	location = "uploaded"
	img_dir = "image"
	path = os.path.join(location, img_dir)
	shutil.rmtree(path)
	os.mkdir(path)

	print()
except:
	pass


# print("Reading H5 model")
# pre_model = tf.keras.models.load_model("EffNetV2SModel.h5")
# print("Writing pb model")
# pre_model.save("saved_model")
# quit(0)

model_file = "model"
model_file = os.path.join(model_file, "saved_model.h5")
#model = tf.keras.models.load_model('model')
model = load_model(model_file)
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploaded/image'

@app.route('/')
def upload_f():
	return render_template('upload.html')

def finds():
	test_datagen = ImageDataGenerator(rescale = None)

# vals = ['Cat', 'Dog'] # change this according to what you've trained your model to do
# test_dir = 'uploaded'

	test_dir = 'uploaded'
	test_dir = os.path.join(test_dir, 'image')
	glob_srch = os.path.join(test_dir, "*")
	l = glob.glob(glob_srch)
	l.sort(key=os.path.getmtime, reverse=True)
	f = os.path.basename(l[0]).split()
	v = [-1]
	df = DataFrame(list(zip(f,v)), columns=['ID', 'Value'])

	test_generator = test_datagen.flow_from_dataframe(
		dataframe=df,
		directory=test_dir,
		x_col="ID",
		y_col="Value",
		target_size =(224, 224),
		batch_size=1,
		class_mode='raw',
		shuffle = False)

	pred = model.predict(test_generator)
#return str(vals[np.argmax(pred)])
	value = str(pred[0][0])
	output_string = "Composite Amyloid-Beta SUVR = " + value + " ±  0.0477"
	return str(output_string)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
		val = finds()
		return render_template('pred.html', ss = val)

if __name__ == '__main__':
	app.run()

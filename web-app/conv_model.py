from keras.models import load_model
model = load_model('kaggle-ip/conv_model_final.hdf5')
model.summary()
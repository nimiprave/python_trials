import tensorflow as tf
import numpy as np
import os
from keras import Sequential
from keras.layers import Dense

# remove the warning of oneDNN
#print(os.environ['TF_ENABLE_ONEDNN_OPTS'])
#os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


#preparing the models
l0 = Dense(units=1, input_shape=[1])
model = Sequential(l0)
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0,0.0,1.0,2.0,3.0,4.0], dtype=float)
ys = np.array([-3.0,-1.0,1.0,3.0,5.0,7.0], dtype=float)

model.fit(xs,ys,epochs=300)
print(model.predict([10.0]))
print("Here is what I learned: {}".format(l0.get_weights()))
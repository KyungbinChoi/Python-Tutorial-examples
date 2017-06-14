from keras.models import Sequential
from keras.layers import Dense, Dropout
import keras
import numpy

dataset = numpy.loadtxt("diabetes.txt", delimiter = ",")

X = dataset[:,0:8]
Y = dataset[:,8]
X_train = X[:600,:]
Y_train = Y[:600]
X_test = X[600:,:]
Y_test = Y[600:]

batch_size = 15
epochs = 200

model = Sequential()
model.add(Dense(16, kernel_initializer='normal',activation= 'relu',input_dim=8))
model.add(Dropout(0.2))
model.add(Dense(10, kernel_initializer='he_normal',activation= 'relu'))
model.add(Dropout(0.2))
model.add(Dense(1, kernel_initializer='normal',activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, Y_train, epochs= epochs, batch_size = batch_size,verbose=1)
score= model.evaluate(X_test,Y_test, verbose=0)

print("Test loss" , score[0])
print("Test accuracy" , score[1])
print(model.summary())
# Load dependencies
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
#
from sklearn.preprocessing import StandardScaler
#
# Load data
# dataset = np.loadtxt('./chennai_reservoir_levels.csv', delimiter='|', skiprows=1, usecols=(1,2,3,4))
n_samples = 100


def myFunction(X):
    # return 2 * X[0] + 3 * X[1] + 1
    return 2 * X[0] + 1


dataset = []
for i in range(n_samples):
    # x = [i, i + 1]
    x = [i]
    y = myFunction(x)
    line = np.concatenate((x, [y]))
    dataset.append(line)


##Standard Scaling all features
dataset = np.array(dataset)
scaler = StandardScaler()
dataset = scaler.fit_transform(dataset)
###


# Shuffle dataset
np.random.shuffle(dataset)

###
# Separate features and targets
# colOfY = 2
colOfY = 1
X = dataset[:, 0:colOfY]
Y = dataset[:, colOfY]
###

# Set the input shape
input_shape = (colOfY,)
print(f'Feature shape: {input_shape}')

# Create the model
model = Sequential()
model.add(Dense(16, input_shape=input_shape, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

# Configure the model and start training
model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_squared_error'])
# model.fit(X, Y, epochs=250, batch_size=1, verbose=1, validation_split=0.2)
model.fit(X, Y, epochs=250, batch_size=1, verbose=1, validation_split=0.2)


Y_result = model.predict(X)

temp = 0

#https://medium.com/@am.benatmane/keras-hyperparameter-tuning-using-sklearn-pipelines-grid-search-with-cross-validation-ccfc74b0ce9f
#https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/
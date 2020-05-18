import numpy as np
import sklearn
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.preprocessing import StandardScaler

n_samples = 100


def myFunction(X):
    # return 2 * X[0] + 3 * X[1] + 1
    return 2 * X[0] + 1


seed = 7
np.random.seed(seed)

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
input_shape = (colOfY,)


###

# Function to create model, required for KerasClassifier
def create_model(loss='mean_absolute_error'):
    model = Sequential()
    model.add(Dense(16, input_shape=input_shape, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='linear'))

    # Configure the model and start training
    model.compile(loss=loss, optimizer='adam', metrics=['mean_squared_error'])

    # model.fit(X, Y, epochs=250, batch_size=1, verbose=1, validation_split=0.2)
    return model


# Keras não faz parte dos métodos do scikit, mas a KerasRegressor faz a interface com o KERAS
model = KerasRegressor(build_fn=create_model, epochs=100, batch_size=10, verbose=0, loss='mean_absolute_error')
# define the grid search parameters

# batch_size = [1, 2, 5]
# epochs = [50, 100]
batch_size = [1, 2, 3]
epochs = [13, 15, ]

param_grid = dict(batch_size=batch_size, epochs=epochs)

# metrics_for_cv = ['neg_mean_absolute_error', 'neg_mean_squared_error']
metric_for_cv = 'neg_mean_absolute_error'  # or neg_mean_squared_error, see more: sklearn.metrics.SCORERS.keys()
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3, scoring=metric_for_cv)
grid_result = grid.fit(X, Y)
# GridSearchCV faz o fit de cada model com as combinações do param_grid
# Após isso roda um cross-validition (cv) com os dados e avalia com a métrica scoring
# O próprio keras tem sua mátrica interna (sendo definida em create_model)
# Como best result ele retorna retorna o que teve a maior média com base na métrica scoring
# A métrica neg_mean_absolute_error é o negativo do mean_absolute_error, pois quanto menor o MAE melhor (e o GridSearchCV busca pelos maiores valores

# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
#

# Com os melhores parâmetros é só recriar o método e pegar o resultado
model = KerasRegressor(build_fn=create_model, **grid_result.best_params_)
print(KerasRegressor)
model.fit(X, Y)
Y_result = model.predict(X)

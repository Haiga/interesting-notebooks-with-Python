import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.utils import shuffle
from scipy.stats import pearsonr, ttest_ind


seed = 11

# Collection with 442 samples x 10 features
dataset = load_diabetes()

X = dataset.data
y = dataset.target

X, y = shuffle(X, y, random_state=seed)

X_unchanged = np.array(X)
y_unchanged = np.array(y)

X = np.array(X)
y = np.array(y)


def np3(arr):
    return np.power(arr, 3)


def np4(arr):
    return np.power(arr, 3)


def np_m1(arr):
    return np.power(arr, -1)


def np_m2(arr):
    return np.power(arr, -2)


def normal(arr):
    return arr


some_functions = [normal, np.log, np.log1p, np.log2, np.log10, np.cbrt, np.square, np.sqrt, np.sin, np.cos, np.tan,
                  np.arccos,
                  np.arccosh, np3, np4, np_m1, np_m2]

for col in range(X.shape[1]):
    max_corr = 0
    best_func = normal
    for func in some_functions:
        transformer = FunctionTransformer(func)
        current_column = X[:, [col]].reshape(1, -1)[0]
        temp_column = transformer.transform(current_column)
        try:
            corr, _ = pearsonr(temp_column, y)
        except Exception:
            continue

        if abs(corr) > max_corr:
            max_corr = abs(corr)
            best_func = func

    if best_func != normal:
        transformer = FunctionTransformer(best_func)
        new_column = transformer.transform(X[:, [col]])
        # print(X[0][col])
        X[:, [col]] = new_column
        # print(X[0][col])
        print('changed')

my_scores = []
normal_scores = []
num_replicacoes = 20

for replicacao in range(num_replicacoes):
    kf = KFold(n_splits=5, shuffle=True, random_state=None)

    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        model = RandomForestRegressor(random_state=seed)
        model.fit(X_train, y_train)
        y_predicted = model.predict(X_test)

        my_scores.append(mean_squared_error(y_test, y_predicted))

        X_train, X_test = X_unchanged[train_index], X_unchanged[test_index]
        y_train, y_test = y_unchanged[train_index], y_unchanged[test_index]

        model = RandomForestRegressor(random_state=seed)
        model.fit(X_train, y_train)
        y_predicted = model.predict(X_test)

        normal_scores.append(mean_squared_error(y_test, y_predicted))

# print(my_scores)
# print(normal_scores)

print('mean my scores: %f ' % np.mean(my_scores))
print('mean normal scores: %f ' % np.mean(normal_scores))

stat, p = ttest_ind(normal_scores, my_scores)

print('t=%.3f, p=%.3f' % (stat, p))


# mean my scores: 3392.325248
# mean normal scores: 3390.724636
# t=-0.024, p=0.981

# Conclusion: Como as alterações não tem diferença estatística,
# não é possível dizer que houve uma melhora/piora dos resultados
# Trabalhos futuros, variar as funções (existem uma infinidade0
# Aplicar alguma heurística para escolher um grupo de funções
# Testar com outras coleções

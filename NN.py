# import numpy as np
# import pandas as pd
# from sklearn import metrics
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier, export_graphviz
# from sklearn.model_selection import train_test_split
# from six import StringIO
# from IPython.display import Image
# import pydotplus

# from dicts import MAIN_DICT

# # Чтение данных из .xlsx файла и конвертация в .csv
# file_path = 'DataBase.xlsx'
# df = pd.read_excel(file_path)
# df.to_csv(index = True)

# # Транспонирование таблицы, чтобы симптомы были фичами
# df_transposed = df.set_index('Кейс').transpose()

# # print(df_transposed.head) 

# # Кодирование симптомов
# deseases = {'НЕТ': 0, 'ДА': 1, 'ЛЮБОЙ ответ из трех возможных': 0.5}

# # Кодируем значения наличия симптомов
# df_transposed.replace(deseases, inplace=True)

# # Создаем обучающую выборку и предсказываем по ней
# X_train = df_transposed.loc[:, df_transposed.columns[1]:]
# y_train = df_transposed.index

# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_train)

# # accuracy = clf.score(X_train, y_train)
# # print(f'Accuracy: {accuracy*100:.2f}%')

# # Генерируем дерево решений
# dot_data = StringIO()
# export_graphviz(clf, out_file=dot_data, 
#                 feature_names=df_transposed.columns[1:].tolist(),
#                 class_names=y_train.unique().tolist(),
#                 filled=True, rounded=True, 
#                 special_characters=True)

# # Создаем граф pydotplus
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

# # Сохраняем в файл
# graph.write_png("decision_tree.png")

# # print(MAIN_DICT[int(y_pred[2].split('№')[1])].conclusion , MAIN_DICT[int(y_pred[2].split('№')[1])].comment)


import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from six import StringIO
from IPython.display import Image
import pydotplus
from supertree import SuperTree

from dicts import MAIN_DICT

# Чтение данных из .xlsx файла и конвертация в .csv
file_path = 'DataBase.xlsx'
df = pd.read_excel(file_path)
df.to_csv(index = True)

# Транспонирование таблицы, чтобы симптомы были фичами
df_transposed = df.set_index('Кейс').transpose()

# print(df_transposed.head) 

# Кодирование симптомов
deseases = {'НЕТ': 0, 'ДА': 1, 'ЛЮБОЙ ответ из трех возможных': 0.5}

# Кодируем значения наличия симптомов
df_transposed.replace(deseases, inplace=True)

# Создаем обучающую выборку и предсказываем по ней
X_train = df_transposed.loc[:, df_transposed.columns[1]:]
y_train = df_transposed.index

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_train)

tree = SuperTree(clf, feature_names=list(X_train), target_names=list(y_train))
tree.save_html("./decision_tree.html")

# accuracy = clf.score(X_train, y_train)
# print(f'Accuracy: {accuracy*100:.2f}%')

# Генерируем дерево решений
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, 
                feature_names=df_transposed.columns[1:].tolist(),
                class_names=y_train.unique().tolist(),
                filled=True, rounded=True, 
                special_characters=True)

# Создаем граф pydotplus
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

# Сохраняем в файл
graph.write_png("decision_tree.png")

# print(MAIN_DICT[int(y_pred[2].split('№')[1])].conclusion , MAIN_DICT[int(y_pred[2].split('№')[1])].comment)

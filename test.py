import pandas as pd
import xlsx
# df1 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/accountants.csv',index_col=[0], parse_dates=[0])
# df2 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/ceo.csv',index_col=[0], parse_dates=[0])
# df3 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/pm.csv',index_col=[0], parse_dates=[0])
# df4 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/SE_Virtusa.csv',index_col=[0], parse_dates=[0])
# df5 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/SE_Zone.csv',index_col=[0], parse_dates=[0])
# df6 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/TL.csv',index_col=[0], parse_dates=[0])
# df7 = pd.read_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/vitusa_final.csv',index_col=[0], parse_dates=[0])
#
# finaldf = pd.concat([df1, df2, df3,df4,df5,df6,df7], axis=1, join='inner').sort_index()
# finaldf.to_csv('E:/IIT/4th year/Project/Data Set/Cleaned Data/final.csv')
# df1 = pd.read_excel('E:/IIT/4th year/Project/Data Set/Cleaned Data/accountant.xlsx')
# print

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseNotFound,HttpResponseServerError
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score
from django.http import HttpResponse
from django.template import loader




dataset = pd.read_csv('E:/IIT/4th year/Project/Data Set/manual/updated.csv', na_values="?")


dataset.dropna(inplace=True, axis=0, how="any")

dataset.apply(pd.to_numeric)

X = dataset.loc[:,"gender":"years_org_5"]
print(X)

y = dataset["years_org_2"]

# print('print X_test', X)
# print('print X_test', y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# print('print X_test', X_test)
# print('print', X_train)

# clf = tree.DecisionTreeClassifier()
# clf.fit(X_train, y_train)
#
# accuracy1 = []
# predictions = clf.predict(X_test)
# y_pred = clf.predict(X_test)
# print("printing chances: ", y_pred[:10])
# accuracy = float(accuracy_score(y_test, predictions))
# accuracy1.append(accuracy)
# print("acuracy score is ", accuracy1)
# prediction = clf.predict(['1','5','0','0','0'])
#
# print('prediction is ', prediction)
# loader.get_template('application/form.html')
# template = loader.get_template('application/prediction.html')
# context = {
#     'allUsers': prediction,
#     'accuracy': accuracy1,
# }


import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.cross_validation import KFold
from sklearn import metrics


dataset=pd.read_csv('E:/IIT/4th year/Project/Data Set/manual/demaCSV.csv')


        
X = dataset.loc[:,"Education ":"years_org_5"]
y = dataset["avg_years_int"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)



from sklearn import svm

clf=svm.SVC()
clf.fit(X_train, y_train)

testing=[2,2,2,2,2,2.8,0.8,2.1,1.9]
prediction=clf.predict([testing])
print('printing prediction ',prediction)
predictions = clf.predict(X_test)
y_pred=clf.predict(X_test)
print("printing chances: ",y_pred[:30])
print("acuracy score is ",accuracy_score(y_test, predictions))
print("printing the confusion matrix of the system ",metrics.classification_report(y_test,y_pred))

print(metrics.classification_report(y_test,y_pred))



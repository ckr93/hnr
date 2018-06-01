from django.contrib.auth import authenticate, login
from django.template import loader
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseNotFound, HttpResponseServerError
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score
from django.http import HttpResponse
from django.template import loader
from sklearn import metrics
from django.http import HttpResponse
from datetime import datetime
from dateutil.relativedelta import relativedelta


def index(request):
    return render(request, 'application/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                c = {}
                return render(request, 'application/logged.html', c)
            else:
                return render(request, 'application/index.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'application/index.html', {'error_message': 'Invalid login'})
    return render(request, 'application/index.html')


def form(request):
    return render(request, 'application/form.html')


def prediction(request):

    name = request.POST.get('name')
    org_1_start = request.POST.get('org_1_start')
    designation = request.POST.get('title')
    education = request.POST.get('education')
    years_org_2 = request.POST.get('years_org_2')
    org2_title = request.POST.get('org2_title')
    years_org_3 = request.POST.get('years_org_3')
    org3_title = request.POST.get('org3_title')
    years_org_4 = request.POST.get('years_org_4')
    org4_title = request.POST.get('org4_title')
    years_org_5 = request.POST.get('years_org_5')
    org5_title = request.POST.get('org5_title')


    userInputs = [education, org2_title, org3_title, org4_title, org5_title, years_org_2, years_org_3, years_org_4,
                  years_org_5]

    if org_1_start is None:
        print("its null")
    else:
        dataset = pd.read_csv('C:/Users/Chanaka Rathnakumara/Downloads/demaCSV.csv')

        X = dataset.loc[:, "Education ":"years_org_5"]
        y = dataset["avg_years_int"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        from sklearn import svm

        clf = svm.SVC()
        clf.fit(X_train, y_train)

        testing = [userInputs]
        prediction = clf.predict([testing])
        print('printing prediction ', prediction)
        predictions = clf.predict(X_test)
        y_pred = clf.predict(X_test)
        print("printing chances: ", y_pred[:30])
        print("acuracy score is ", accuracy_score(y_test, predictions))
        print("printing the confusion matrix of the system ", metrics.classification_report(y_test, y_pred))

        war_start = org_1_start
        currrent_data = '2018.03.01'
        LeaveData2 =[]
        a = war_start.replace(".", "")
        b = currrent_data.replace(".", "")
        print(a)
        print(b)
        x = datetime.strptime(a, "%Y%m%d").date()
        y = datetime.strptime(b, "%Y%m%d").date()
        print(x)
        print(y)
        print(prediction)
        leaveDate = x + relativedelta(years=+prediction)
        print(leaveDate)
        leaveDate1 = str(leaveDate.strftime('%m/%d/%Y'))
        LeaveData2.append(leaveDate1)
        difference_in_years = relativedelta(leaveDate, y).years
        print(difference_in_years)

        le = 0
        messeage1  = []

        if difference_in_years < 0:
            le = 1
        else:
            le = 0


        print(metrics.classification_report(y_test, y_pred))
        loader.get_template('application/form.html')
        template = loader.get_template('application/prediction.html')
        context = {
            'allUsers': prediction,
            'leaveDate': LeaveData2,
            'leaving:': le,
        }

        return HttpResponse(template.render(context, request))
    template = loader.get_template('application/form.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def home(request):
    return render(request, 'application/homepage.html')


def search(request):
    return render(request, 'application/search.html')


def last_search(request):
    return render(request, 'application/last_search.html')


def manage_recruitments(request):
    return render(request, 'application/manage_recruitments.html')


@ensure_csrf_cookie
def search_result(request):
    return render(request, 'application/search_result.html')

# def custom_404(request, ):
#     return render(request, 'application/404.html')
#
# def custom_500(request, ):
#     return render(request, 'application/500.html')

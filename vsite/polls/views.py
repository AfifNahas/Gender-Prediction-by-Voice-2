import re
from unittest import result
from urllib import request
from django.shortcuts import render
import pandas as pd
import pickle, os, random

#sd,median,Q25,Q75,IQR,skew,sp.ent,mode,centroid,meanfun,minfun,maxfun,mindom,maxdom,label

def Voice(request):
    result = None
    if request.POST.get('voice_button'):
        name = request.POST['Person Name']
        sd = request.POST['sd']
        median = request.POST['median']
        Q25 = request.POST['Q25']
        Q75 = request.POST['Q25']
        IQR = request.POST['IQR']
        Skew = request.POST['Skew']
        spent = request.POST['spent']
        Mode = request.POST['Mode']
        Centroid = request.POST['Centroid']
        meanfun = request.POST['meanfun']
        minfun = request.POST['minfun']
        maxfun = request.POST['maxfun']
        mindom = request.POST['mindom']
        maxdom = request.POST['maxdom']
        #modindx = request.POST['modindx']

        results = Finder(name, sd, median, Q25, Q75, IQR, Skew, spent, Mode, Centroid, meanfun, minfun, maxfun, mindom, maxdom)
        results = results[0]
        print(results)

    else:
        print('Not Working')
    return render(request, 'mainpage.html', {'result': results})


def Finder(name, sd, median, Q25, Q75, IQR, Skew, spent, Mode, Centroid, meanfun, minfun, maxfun, mindom, maxdom):

    if name != '':

        df = pd.DataFrame(columns=['sd', 'median', 'Q25', 'Q75', 'IQR', 'Skew', 'spent', 'Mode', 'Centroid', 'meanfun', 'minfun', 'maxfun', 'mindom', 'maxdom'])

        df2 = {'sd': float(sd), 'median': float(median), 'Q25': float(Q25), 'Q75': float(Q75), 'IQR': float(IQR), 'Skew': float(Skew), 'spent': float(spent),
         'Mode': float(Mode), 'Centroid': float(Centroid), 'meanfun': float(meanfun), 'minfun': float(minfun), 'maxfun': float(maxfun), 'mindom': float(mindom), 'maxdom': float(maxdom)}

        df = df.append(df2, ignore_index = True)

        filename = r'polls/voice_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))
        res = loaded_model.predict(df)

        return res

    else:
        return None





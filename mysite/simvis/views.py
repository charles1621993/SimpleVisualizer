from io import StringIO
import pandas as pd
import csv
import matplotlib.pyplot as plt

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {}
    if request.method == "POST":
        print("Received")
        data_text = request.POST.get('message')
        testdata = StringIO(data_text)
        print(testdata)
        df = pd.read_csv(testdata, sep=",")
        dfcolumns = df.columns.tolist()
        print(type(dfcolumns))
        dfcolumnx = dfcolumns[1:]+ dfcolumns[:1]
        dfcolumny = dfcolumns[2:]+ dfcolumns[:2]
        for a in df.columns:
            print(a)
        print(df)

        if request.POST.get('x') is not None:
            xval = request.POST.get('x')
        if request.POST.get('y') is not None:
            yval = request.POST.get('y')
        if request.POST.get('ind') is not None:
            indval = request.POST.get('ind')
        
        df = df.set_index(indval)   

        fig = plt.figure()
        plt.plot(df[xval], df[yval])

        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        figscatter = plt.figure()
        plt.scatter(df[xval], df[yval])

        imgdata = StringIO()
        figscatter.savefig(imgdata, format='svg')
        imgdata.seek(0)


        figbar = plt.figure()
        plt.bar(df[xval], df[yval])
        datascatter = imgdata.getvalue()

        imgdata = StringIO()
        figbar.savefig(imgdata, format='svg')
        imgdata.seek(0)

        databar = imgdata.getvalue()


        figstem = plt.figure()
        plt.stem(df[xval], df[yval])

        imgdata = StringIO()
        figstem.savefig(imgdata, format='svg')
        imgdata.seek(0)

        datastem = imgdata.getvalue()

        context ={
            'data':data,
            'dfcolumns':dfcolumns,
            'dfcolumnx':dfcolumnx,
            'dfcolumny':dfcolumny,
            'datascatter':datascatter,
            'databar':databar,
            'datastem':datastem,
            'value':data_text
        }
        #reader = csv.reader(data_text.split('\n'), delimiter=',')
        #for row in reader:
        #    print('\t'.join(row))
    return render(request, "simvis/index.html", context)

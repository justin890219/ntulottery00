
from django.shortcuts import render
import csv
# Create your views here.


def home(request):
    return render(request, "home.html")


def sort1(request):
    with open(r'C:\Users\User\Desktop\PFP3\sort\output.csv', newline='', encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        results = []
        for row in rows:
            content, date, likes, comments, link = row
            results.append(dict(content=content, date=date,
                           likes=likes, comments=comments, link=link))
    return render(request, "sort1.html", {'results': results})


def sort2(request):
    with open(r'C:\Users\User\Desktop\PFP3\sort\output.csv', newline='', encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        results = []
        for row in rows:
            content, date, likes, comments, link = row
            if likes == "":
                likes = "0"
            if comments == "":
                comments = "0"
            results.append(dict(content=content, date=date,
                           likes=likes, comments=comments, link=link))
            results.sort(key=lambda x: int(x["likes"]))
    return render(request, "sort2.html", {'results': results})


def sort3(request):
    with open(r'C:\Users\User\Desktop\PFP3\sort\output.csv', newline='', encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        results = []
        for row in rows:
            content, date, likes, comments, link = row
            if likes == "":
                likes = "0"
            if comments == "":
                comments = "0"
            results.append(dict(content=content, date=date,
                           likes=likes, comments=comments, link=link))
            results.sort(key=lambda x: int(x["comments"]))
    return render(request, "sort3.html", {'results': results})


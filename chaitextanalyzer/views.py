#I have created this file- chaithra
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'chai','place':'Chikkamagaluru'}
    return render(request,'index.html',params)
def analyze(request):

    djtext=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunc =='on' and (len(djtext)>0):
        punctuations=''';..!<<>>@'",?|/:'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
             analyzed=analyzed+char
        params={'purpose':'Remove punctuation','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'change to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !='\n' and char!="\r":
              analyzed=analyzed+char
        params = {'purpose': '  To Remove New Line ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(spaceremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + char
        params = {'purpose': '  To Remove Space', 'analyzed_text': analyzed}


    if(removepunc == "off" or spaceremover == "off" or newlineremover == "off"  or  fullcaps == "off"):
        return HttpResponse("<h1>Somthing is wrong Please check once and try again</h1>")

    return render(request, 'analyze.html', params)


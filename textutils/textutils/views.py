# I have created this file - Indrajeet
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # we can give parameters like this
    # params = {'name': 'Indrajeet', 'place': 'Mars'}
    # return render(request, "index.html", params)

    return render(request, "index.html")

    # Returns only simple response without any template
    # return HttpResponse("Home")

def about(request):
    return HttpResponse("About")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    params = {}

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Changed to Uppdrcase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
               analyzed = analyzed + char

        params = {'purpose': 'Removed Extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcounter == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Removed Extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcounter != 'on':
        return HttpResponse("Please Select any operation and try again.")

    return render(request, 'analyze.html', params)


# # def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#
#     # Analyze the text
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("character count")




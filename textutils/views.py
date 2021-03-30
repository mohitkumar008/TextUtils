# I have created this file - Mohit Kumar
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get Text
    djtext = request.POST.get('text', 'default')
    
    # Get Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charCount = request.POST.get('charCount', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')
    
    # Remove Puncuations
    if removepunc == 'on':
        # analyzed = djtext
        PUNCTUATION = '''!()-[]{};:"'\,<>./?@#$%^&*_`~'''
        analyzed = ""
        for char in djtext:
            if char not in PUNCTUATION:
                analyzed += char
        params = {'purpose': 'Removed Puncuations', 'analyzed_text': analyzed}
        
        djtext = analyzed

    
    # Change to Uppercase
    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        
        djtext = analyzed
        
    # Count Character
    if charCount == 'on':
        analyzed = len(djtext.replace(' ', ''))
        countchars = f"The numbers of characters in the string are {analyzed}"
        params = {'purpose': 'New Line Removed', 'analyzed_text': countchars}
        
        djtext = analyzed

    
    # New line remover
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        
        djtext = analyzed

    
    # Extra Space Remover
    if extraSpaceRemover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index + 1] == " ":
                pass
            else:
                analyzed += char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        
    ######### Results are here: #########
    if (removepunc != 'on' and fullcaps != "on" and charCount != 'on' and newlineremover != 'on' and extraSpaceRemover != 'on'):
        return HttpResponse('Please choose one of the option and try again')
    
    #Return
    return render(request, 'analyze.html', params)
        
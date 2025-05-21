# this file is  created by Samman vies return the https request
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
#we create a function for views and add it to the urls and give path
def index(request):
   return  render(request,'home.html')  
def Analyser(request):
    djtext =request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    lowercase = request.GET.get('lowercase','off')
    newlineRemover = request.GET.get('newlineRemover','off')
    allspaceremover = request.GET.get('allspaceremover','off')
    spaceremover = request.GET.get('spaceremover','off')
    charcounter = request.GET.get('charcounter','off')
    wordcounter = request.GET.get('wordcounter','off')
    if removepunc == "on":
        puncutation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in puncutation:
                analyzed +=char
        params={'purpose':'removed the punctuation error in text','analysed_text':analyzed}
        return render(request,'Analys.html',params)
    elif (fullcaps== "on"):
        analyzed =""
        for char in djtext:
            analyzed += char.upper()
            params={'purpose':'convert the text in upper case','analysed_text':analyzed}
        return render(request,'Analys.html',params)
    elif (lowercase== "on"):
        analyzed =""
        for char in djtext:
            analyzed += char.lower()
            params={'purpose':'convert the text in lower case','analysed_text':analyzed}
        return render(request,'Analys.html',params)
    elif (newlineRemover== "on"):
        analyzed =""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed += char
        params={'purpose':'Remove the new line','analysed_text':analyzed}
        return render(request,'Analys.html',params)
    elif (allspaceremover == "on"):
        analyzed = djtext.replace(" ", "")
        params = {'purpose': 'It removes all spaces from the sentence', 'analysed_text': analyzed}
        return render(request, 'Analys.html', params)
    elif(spaceremover=="on"):
        analyzed= "   "
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]== " "):
                analyzed+=char
        params = {'purpose': 'It removes all spaces from the sentence', 'analysed_text': analyzed}
        return render(request, 'Analys.html', params)
    elif charcounter == "on":
        count = len(djtext)
        params = {'purpose': 'Counted all characters', 'analysed_text': f'Total characters: {count}'}
        return render(request, 'Analys.html', params)
    elif wordcounter == "on":
        words = djtext.split()
        count = len(words)
        params = {'purpose': 'Counted words', 'analysed_text': f'Total words: {count}'}
        return render(request, 'Analys.html', params)

    else:
        return HttpResponse("Your Removepucn is not on please on it and retry it ")





# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")
#my NAEM IS ZAFAR



def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newLineRemover = request.GET.get('newLineRemover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charctercount=request.GET.get('charctercount', 'off')
    Input = request.GET.get('text', 'Using Default Text as no input was detected.')

    # here to work all the operation togethe we are making djtext=analyzed and not returning render only on last and
    # making all return comment

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}

        djtext=analyzed
        # return render(request, 'analyzed_text.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyzed_text.html', params)
        djtext = analyzed

    try:
     if(extraspaceremover=="on"):
        analyzed =" "
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index+1]==" " ):
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Removed extra space', 'analyzed_text': analyzed}
        djtext = analyzed

    except:

        params = {'purpose': 'you are in exeption', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyzed_text.html', params)



    if newLineRemover == "on" and (len(Input) > 0):

        analyzed = ""

        # MyList = Input.splitlines()  #splitline() method is used to split the lines at line boundaries.
        #                                 # The function returns a list of lines in the string, including the
        #                                 #       line break(optional).
        # print(MyList) #see in command promt it list type
        #
        # for i in MyList:
        #     analyzed = analyzed + i

        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed=analyzed+char
            else:
                print("new line") # see in terminal

        params = {'purpose': 'After removing New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyzed_text.html', params)

    if charctercount == "on":
        analyzed = 0
        for char in djtext:
            analyzed += 1
        params = {'purpose': 'no of character count', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyzed_text.html', params)

        # if (charctercount != "on" and newLineRemover != "on" and newLineRemover != "on" and extraspaceremover!="on" and fullcaps!="on" and removepunc != "on" ):
        #
        #      return HttpResponse("please slect any operation and try again")
        #
    return render(request, 'analyzed_text.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")
# I have created this website(File) - Pushpendra Gaur
from django import http
from django.shortcuts import render

# Code for learning basics

# def index(requt):
#     return http.HttpResponse("<h1>Pushpendra's First Django website</h1>")
# def about(request):
#     return http.HttpResponse("About Hello Pushpendra")
# def txt(request):
#     with open("1.txt") as f:
#         content = f.read()
        
#     return http.HttpResponse("<h1>"+content+"</h1>")

# code for the main textutils Project
# def index(request):
#     return http.HttpResponse('''Home<br> <button><a href='/captalizefirst'>Capitalize</a></button><br> <button><a href='/newlineremove'>New Line remove</a></button><br><button><a href='/charcount'>Count char</a></button>''')
# def captalizeFirst(request):
#     return http.HttpResponse("captalizeFirst <button><a href='/'>Back</a></button>")
# def newlineremove(request):
#     return http.HttpResponse("newlineremove <button><a href='/'>Back</a></button>")
# def charcount(request):
#     return http.HttpResponse("charcount <button><a href='/'>Back</a></button>")

# code for the main Django templating

# def index(request):
#     params = {'name': 'Pushpendra',
#             'address':'Unnao, Kanpur',
#             'salary':3.5}
#     return render(request, 'index.html',params)

# Main code for textutils Project starts here

def index(request):
    
    return render(request, 'index.html')

def analyze(request):
    # Get the text from our html file
    # print(request.GET.get('text', 'default'))
    # print(request.GET.get('removepunc', 'off'))
    djtext = request.POST.get('text', 'default')
    check = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    # Analyze the text 
    # analyzed = ""
    params = {'purpose' : '', 'analyzed_text': ""}
    if(djtext != ''):
        if(check == 'on'):
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed += char
            params['purpose'] = "Removed Punctuation"
            params['analyzed_text'] = analyzed
            
            djtext = analyzed
            # return render(request, 'analyze.html', params)
        if(upper == 'on'):
            analyzed = ""
            analyzed = djtext.upper()
            params['purpose'] = 'UPPERCASE'
            params['analyzed_text'] = analyzed
            djtext = analyzed
            # return render(request, 'analyze.html', params)
        if(newlineremove == 'on'):
            analyzed = ""
            for char in djtext:
                if not(char == '\n' or char =='\r'):
                    analyzed += char
                
                    
                params['purpose'] = 'Removed New Lines'
                params['analyzed_text'] = analyzed 
                djtext = analyzed  

            # return render(request, 'analyze.html', params)
        if(extraspaceremove == 'on'):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] ==" " and djtext[index+1]==" "):
                    analyzed += char
                
                    
            params['purpose'] = 'Removed Extra Spaces'
            params['analyzed_text'] = analyzed
            djtext = analyzed
            # return render(request, 'analyze.html', params)
        if(charcount == 'on'):
            analyzed = ""
            params['purpose'] = 'Total character in Paragraph'
            params['charcount'] = 'No. of charcters in text :' +str(len(djtext))
            params['analyzed_text'] = djtext
            
        if(check != 'on' and upper != 'on' and newlineremove != 'on' and extraspaceremove != 'on' and charcount != 'on'):
            return http.HttpResponse("Error!! Please select any operation.")
        return render(request, 'analyze.html', params)
    else:
        params = {"djtext":"","errorResponse":"Please enter the Text in above textarea !!"}
        return render(request, 'index.html', params)


    
    

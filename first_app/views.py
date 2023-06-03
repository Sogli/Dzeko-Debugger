from django.shortcuts import render

def index(request):
    my_dict={'insert_content':"Hello, im from first_app"}
    return render(request, 'first_app/index.html', context=my_dict)

def help(requestt):
    help_dict={'help_me':"Help stranica"}
    return render(requestt, 'first_app/help.html', context=help_dict)


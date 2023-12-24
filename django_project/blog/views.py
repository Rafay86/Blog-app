from django.shortcuts import render

posts = [
    {
        'author':'rafay',
        'title':'Blog post1',
        'content':'first page content',
        'date': 'august,27,2023'

    },
    {
         'author':'sami',
        'title':'Blog post2',
        'content':'second page content',
        'date': 'august,28,2023'

    }
]

def home(request):
    context={
        'posts': posts
    }
    return render(request,'blog/home.html',context)



def about(request):
    return render(request,'blog/about.html',{'title':'about'})


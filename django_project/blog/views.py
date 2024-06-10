from django.shortcuts import render

posts = [
    {
        'author': 'Keerti',
        'title': 'blog-post1',
        'content': 'first post content',
        'date_posted': '6 june,2024'
    },
    {
        'author': 'saurabh',
        'title': 'blog-post2',
        'content': 'second post content',
        'date_posted': '5 june,2024'
    }
]


def home(request):
    context={
        'posts': posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')    

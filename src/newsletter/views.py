from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def home(request):
    # if request.user.is_authenticated():
        
    #     title = 'My title %s' %(request.user)
    title = 'Welcome'
    
    # if request.method == 'POST':
    #     print(request.POST)
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = 'Ahmed'
        instance.save()

    context = {
        'title':title,
        'form':form
    }
    return render(request, 'home.html', context)
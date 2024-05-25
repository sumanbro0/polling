from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Profile, Question, Submission
from django.contrib import messages




# Create your views here.
from django.core.paginator import Paginator
def index(request):
    poll_list = Poll.objects.filter(is_active=True).order_by('-id').all()
    paginator = Paginator(poll_list, 6)  # Show 6 polls per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

def poll_detail(request, id):
    poll=Poll.objects.get(id=id)
    return render(request, 'poll_detail.html', {'poll': poll})


@login_required
def submit_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        submissions = []
        for question in poll.question_set.all():
            answer = request.POST.get(f'question{question.id}')
            if answer:  # Only add to submissions if an answer was provided
                submissions.append(Submission(user=request.user, question=question, answer=answer))
            else:
                messages.error(request, 'All questions must be answered.')
                return redirect('poll_detail', poll_id=poll.id)
        Submission.objects.bulk_create(submissions)
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.credit += 1
        profile.save()
        messages.success(request, 'Thank you for submitting the poll')
        return redirect('index')
    else:
        messages.error(request, 'Error submitting form...')
        return redirect('poll_detail', poll_id=poll.id)
    

from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        next=request.GET.get('next')
        if next:
            messages.info(request, 'You need to login to access this page.')
    return render(request, 'login.html')

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']


        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Enter a valid email address.')
            return redirect('signup')

        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')


        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        Profile.objects.create(user=user)


        messages.success(request, 'You have successfully registered.')
        return redirect('login')
    else:
        return render(request, 'signup.html')
    
from django.contrib.auth import logout
def lout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

def delete_poll(request, id):
    poll = get_object_or_404(Poll, pk=id)
    poll.delete()
    messages.success(request, 'Poll deleted successfully.')
    return redirect('index')


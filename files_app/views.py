from django.shortcuts import render
from django.http import FileResponse
from . import forms
from files_app.helpers.converter import get_generate

global SELECTED_OPTION


def home_view(request):
    if request.method == 'POST':
        SELECTED_OPTION = request.POST.get('selected_option')
        print("*************")
        print(SELECTED_OPTION)
    return render(request, 'home/index.html')


def resume_view(request):
    if request.method == 'POST':
        SELECTED_OPTION = request.POST.get('selected_option')
        form = forms.ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            summary = form.cleaned_data['summary']
            education = form.cleaned_data['education']
            experience = form.cleaned_data['experience']    
            skills = form.cleaned_data['skills']
            certifications = form.cleaned_data['certifications']

            data_dict = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number,
                'address': address,
                'summary': summary,
                'education': education,
                'experience': experience,
                'skills': skills,
                'certifications': certifications}

            print("*************")
            print(SELECTED_OPTION)

            path = get_generate(SELECTED_OPTION, data=data_dict)

            return FileResponse(open(path, 'rb'),
                                content_type='application/pdf')
        else:
            context = {'form': form}
            return render(request, "forms/resume.html", context)
    else:
        context = {'form': forms.ResumeForm()}
        return render(request, "forms/resume.html", context)


def user_registration_view(request):
    context = {}
    context['form'] = forms.UserRegistrationForm()
    return render(request, "forms/user_registration.html", context)


def contact_view(request):
    context = {}
    context['form'] = forms.ContactForm()
    return render(request, "forms/contact.html", context)


def feedback_view(request):
    context = {}
    context['form'] = forms.FeedbackForm()
    return render(request, "forms/feedback.html", context)


def Survey_view(request):
    context = {}
    context['form'] = forms.SurveyForm()
    return render(request, "forms/survey.html", context)


def event_registration_view(request):
    context = {}
    context['form'] = forms.EventRegistrationForm()
    return render(request, "forms/event_registration.html", context)


def product_order_view(request):
    context = {}
    context['form'] = forms.ProductOrderForm()
    return render(request, "forms/product_order.html", context)


def newsletter_subscription_view(request):
    context = {}
    context['form'] = forms.NewsletterSubscriptionForm()
    return render(request, "forms/newsletter_subscription.html", context)


def custum_view(request):
    return render(request, "forms/custum.html", )

from django.urls import path
from .views import (
    home_view,
    resume_view,
    user_registration_view,
    contact_view,
    feedback_view,
    Survey_view,
    event_registration_view,
    product_order_view,
    newsletter_subscription_view,
    )

app_name = 'files_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('resume/', resume_view, name='resume'),
    path('user-registration/', user_registration_view,
         name='user_registration'),
    path('contact/', contact_view, name='contact'),
    path('feedback/', feedback_view, name='feedback'),
    path('survey/', Survey_view, name='survey'),
    path('event-registration/', event_registration_view,
         name='event_registration'),
    path('product-order/', product_order_view, name='product_order'),
    path('newsletter-subscription/', newsletter_subscription_view,
         name='newsletter_subscription'),
]

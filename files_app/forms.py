from django import forms
from datetime import datetime
from django.utils.translation import gettext_lazy as _


class GenderChoise(forms.ChoiceField):
    MALE = 'male', _('Male')
    FEMAIL = 'femail', _('Femail')
    OTHER = 'other', _('Other')


class FormatForm(forms.Form):
    class FileFormat(forms.ChoiceField):
        PDF = 'Pdf', _("PDF")
        word = 'Word', _("WORD")
        img = 'Img', _('IMAGES')
        text = 'Text', _('TEXT')
    file_format = forms.ChoiceField(
        choices=FileFormat.choices, label='File Formet')


class ResumeForm(forms.Form):
    image = forms.ImageField(label='Image', required=False)
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    address = forms.CharField(max_length=200, label='Address')
    summary = forms.CharField(widget=forms.Textarea, label='Summary')
    education = forms.CharField(widget=forms.Textarea, label='Education')
    experience = forms.CharField(widget=forms.Textarea, label='Experience')
    skills = forms.CharField(widget=forms.Textarea, label='Skills')
    certifications = forms.CharField(
        widget=forms.Textarea, label='Certifications')


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class ContactForm(forms.Form):
    class DepartmentChoise(forms.ChoiceField):
        SALES = 'sales', _('Sales')
        SUPPORT = 'support', _('Support')
        BILLING = 'billing', _('Billing')
        GENERAL = 'general', _('General Inquiry')

    class UrgencyChoise(forms.ChoiceField):
        LOW = 'low', _('Low')
        MEDIUM = 'medium', _('Medium')
        HIGH = 'high', _('High')

    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    department = forms.ChoiceField(
        choices=DepartmentChoise.choices, label='Reasom for Contacting Us')
    urgency = forms.ChoiceField(
        choices=UrgencyChoise.choices, label='Urgency')
    attachment = forms.FileField(required=False, label='Attachment')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise forms.ValidationError(
                "You must provide either an email address or a phone number.")

        return cleaned_data


class FeedbackForm(forms.Form):
    class FeedbackTypeChoise(forms.ChoiceField):
        GENERAL = 'general', _('General Feedback')
        BUG_REPORT = 'bug_report', _('Bug Report')
        FEATURE_REQUEST = 'feature_request', _('Feature Request')
        COMPLAINT = 'complaint', _('Complaint')

    class FeedbackRatingChoise(forms.ChoiceField):
        EXCELLENT = 'excellent', _('Excellent')
        GOOD = 'good', _('Good')
        AVERAGE = 'average', _('Average')
        POOR = 'poor', _('Poor')

    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    feedback_type = forms.ChoiceField(
        choices=FeedbackTypeChoise.choices, label='Feedback Type')
    feedback_rating = forms.ChoiceField(
        choices=FeedbackRatingChoise.choices, label='Feedback Rating')
    feedback_details = forms.CharField(
        widget=forms.Textarea, label='Feedback Details')
    additional_comments = forms.CharField(
        widget=forms.Textarea, required=False, label='Additional Comments')
    attachment = forms.FileField(required=False, label='Attachment')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise forms.ValidationError(
                "You must provide either an email address or a phone number.")

        return cleaned_data


class SurveyForm(forms.Form):
    class EducationLevelChoise(forms.ChoiceField):
        HIGH_SCHOOL = 'high_school', _('High School')
        COLLEGE = 'college', _('College')
        GRADUATE_SCHOOL = 'graduate_school', _('Graduate School')
        OTHER = 'other', _('Other')

    class SatisfactionRatingChoise(forms.ChoiceField):
        VERY_DISSATISFIED = 1, _('1 - Very Dissatisfied')
        DISSATISFIED = 2, _('2 - Dissatisfied')
        NEUTRAL = 3, _('3 - Neutral')
        SATISFIED = 4, _('4 - Satisfied')
        VERY_SATISFIED = 5, _('5 - Very Satisfied')

    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    age = forms.IntegerField(label='Your Age')
    gender = forms.ChoiceField(
        choices=GenderChoise.choices, label='Your Gender')
    education_level = forms.ChoiceField(
        choices=EducationLevelChoise.choices, label='Your Education Level')
    occupation = forms.CharField(max_length=100, label='Your Occupation')
    country = forms.CharField(max_length=100, label='Your Country')
    satisfaction_rating = forms.ChoiceField(
        choices=SatisfactionRatingChoise.choices,
        label='Overall Satisfaction Rating')
    favorite_feature = forms.CharField(
        max_length=200, label='Your Favorite Feature')
    improvement_suggestions = forms.CharField(
        widget=forms.Textarea, label='Improvement Suggestions', required=False)
    interested_in_future_updates = forms.BooleanField(
        label='Interested in Future Updates', required=False)
    would_recommend = forms.BooleanField(
        label='Would Recommend', required=False)
    additional_comments = forms.CharField(
        widget=forms.Textarea, label='Additional Comments', required=False)


class EventRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100, label=_('Full Name'))
    email = forms.EmailField(label=_('Email'))
    phone_number = forms.CharField(max_length=20, label=_('Phone Number'))
    event_name = forms.CharField(max_length=200, label=_('Event Name'))
    event_date = forms.DateField(label=_('Event Date'))
    dietary_restrictions = forms.CharField(
        widget=forms.Textarea, label=_('Dietary Restrictions'), required=False)
    additional_guests = forms.IntegerField(
        label=_('Number of Additional Guests'), min_value=0, initial=0)
    emergency_contact_name = forms.CharField(
        max_length=100, label=_('Emergency Contact Name'), required=False)
    emergency_contact_phone = forms.CharField(
        max_length=20, label=_('Emergency Contact Phone'), required=False)
    special_requests = forms.CharField(
        widget=forms.Textarea, label=_('Special Requests'), required=False)
    agree_to_terms = forms.BooleanField(
        label=_('I agree to the terms and conditions'), required=True)

    def clean(self):
        cleaned_data = super().clean()
        event_date = cleaned_data.get('event_date')

        if event_date and event_date < datetime.date.today():
            raise forms.ValidationError(_('Event date cannot be in the past.'))

        return cleaned_data


class ProductOrderForm(forms.Form):
    class SizeChoise(forms.ChoiceField):
        SMALL = 'small', _('Small')
        MEDIUM = 'medium', _('Medium')
        LARGE = 'large', _('Large')

    full_name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    address_line1 = forms.CharField(max_length=200, label='Address Line 1')
    address_line2 = forms.CharField(
        max_length=200, label='Address Line 2', required=False)
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=100, label='State/Province')
    country = forms.CharField(max_length=100, label='Country')
    zip_code = forms.CharField(max_length=20, label='ZIP/Postal Code')
    product_name = forms.CharField(max_length=200, label='Product Name')
    quantity = forms.IntegerField(label='Quantity', min_value=1, initial=1)
    size = forms.ChoiceField(
        choices=SizeChoise.choices, label='Size')
    color = forms.CharField(max_length=50, label='Color')
    additional_notes = forms.CharField(
        widget=forms.Textarea, label='Additional Notes', required=False)
    terms_and_conditions = forms.BooleanField(
        label='I agree to the terms and conditions', required=True)


class NewsletterSubscriptionForm(forms.Form):
    email = forms.EmailField(label=_('Email'), max_length=100)
    first_name = forms.CharField(
        label=_('First Name'), max_length=50, required=False)
    last_name = forms.CharField(
        label=_('Last Name'), max_length=50, required=False)
    gender = forms.ChoiceField(
        label=_('Gender'), choices=GenderChoise.choices, required=False)
    age = forms.IntegerField(
        label=_('Age'), min_value=0, max_value=150, required=False)
    city = forms.CharField(
        label=_('City'), max_length=100, required=False)
    country = forms.CharField(
        label=_('Country'), max_length=100, required=False)
    interests = forms.CharField(
        label=_('Interests'),
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        help_text=_('Enter your interests separated by commas.')
    )
    receive_promotions = forms.BooleanField(
        label=_('Receive Promotions'),
        required=False,
        initial=True
    )
    receive_news = forms.BooleanField(
        label=_('Receive News'),
        required=False,
        initial=True
    )
    terms_and_conditions = forms.BooleanField(
        label=_('I agree to the Terms and Conditions'),
        required=True
    )


class CustumForm(forms.Form):
    pass

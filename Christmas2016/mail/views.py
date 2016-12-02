from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib.auth.models import User

from config.settings.base import get_secret

import utils, mail

def translate_tags(subject, message, name=None, username=None, password=None):
    """
    Translates the following tags contained in an e-mail template and/or subject line
    to whatever they represent from the User Model and the secrets.json file. The following tags are supported:
        <name>: first_name from User Model
        <username>: username from User Model
        <password>: password from secrets.json file
            the password is indexed in the secrets.json file with an all caps version of the individual's username
    :return: a subject string and a message string with all the tags filled in.
    """
    subject = subject.replace('<name>', name)
    message = message.replace('<name>', name)
    message = message.replace('<username>', username)
    message = message.replace('<password>', password)
    return subject, message

class ManageEmail(View):
    template_name = 'mail/manage_emails.html'

    def get(self, request):
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory()})


class SendInvitation(View):
    template_name = 'mail/send_invitation.html'

    def get(self, request):
        return render(request, self.template_name,
                      { 'display_memory': utils.get_memory(),
                        'users': User.objects.all() })

    def post(self, request):
        recipients = request.POST.getlist('family_member')
        msg_file = open('mail/static/mail/invitation.txt')
        orig_message = msg_file.read()
        for member in recipients:
            user = User.objects.get(username=member)
            password_key = user.username.upper()
            password = get_secret(password_key)
            subject, message = translate_tags("<name>'s Login Information for this Year's Family Christmas Website",
                                              orig_message,
                                              user.first_name,
                                              user.username,
                                              password)

            send_mail(
                subject,
                message,
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
        return redirect('gift_list')


class MailCompose(View):
    template_name = 'mail/compose.html'

    def get(self, request):
        return render(request, self.template_name, {})


class MailManageTrade(View):
    template_name = 'mail/trade_mail.html'

    def get(self, request):
        return render(request, self.template_name, {})

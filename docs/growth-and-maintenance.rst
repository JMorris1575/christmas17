======================
Growth and Maintenance
======================

This document will keep track of the changes I made to the Christmas 2017 website after its original deployment on
December 7, 2017. Some of these changes will be in the way of maintenance, others may be new developments.

Making Info Boxes Consistent in Appearance
==========================================

I noticed that the login page and the error pages, at least, have a different look to the info boxes because I never
finished updating them with::

    <div class="border-outer">
        <div class="border-middle">
            <div class = "info">
                ...
            </div>
        </div>
    </div>

I found several template files for which I needed to do that. Once I get them all copied over to webfaction the site
will look a little better.

Need to Improve Logging In and Logging Out
==========================================

In the process of doing the above I noticed that some of the templates in the user app are never used -- at least I
don't think they are. I will need to look over how to get the login/logout system to work smoothly and in a
user-friendly fashion.

.. index:: Problem; migrations

Problem with Migrate
====================

When I ran ``python managa.py migrate`` on the rectory computer after changing the name of the model ``TriviaChoices``
to ``TriviaChoice`` it would not run, complaining that
``django.db.utils.ProgrammingError: relation "trivia_triviachoice" does not exist``. I tried to resolve this by removing
all of the migrations from ``trivia/migrations`` and running ``python manage.py makemigrations`` followed by
``python manage.py migrate`` but, though makemigrations worked alright, migrate claimed there were no migrations to
apply, and in the admin, neither Trivia choices nor Trivia user responses could be displayed. I will try to run
``python manage.py loaddata all-2017-12-08.json`` and see if that helps.

It did not. It still says "trivia_triviachoice" does not exist.

I looked into pgAdmin4 and found the c17database and attempted to change the name of the table from
``trivia_triviachoices`` to ``trivia_triviachoice``. It seemed to take, and I think it did, but it still couldn't load
the data since the choice with pk=18 had a text value that was too long -- it was still expecting a length of 60 where
I had increased it yesterday to 255. Upon changing that in pgAdmin4 I tried to loaddata again and this time the error
had something to do with::

    Could not load contenttypes.ContentType(pk=15): duplicate key value violates unique constraint
    "django_content_type_app_label_model_76bd3d3b_uniq"
    DETAIL:  Key (app_label, model)=(trivia, triviachoice) already exists.

This looks familiar. Something like it just happened yesterday. Yes, it did. I solved it then by dumping and loading
only my models. I will try loading again using the ``mine-2017-12-07.json`` file I created yesterday. (I'll have to get
it through TeamViewer.)

Now everything is working as it should. I didn't have to re-created the TriviaChoice(s). I wish I'd thought of using
the version of pgAdmin on WebFaction yesterday. It would have saved me a lot of trouble.

By the way, I also corrected trivia question number 6, the former grammar of which confused Janet -- because it WAS
confusing.

Working on the Trivia Compose Question Page
===========================================

Having a single page on which I can enter both the questions and that question's choices of answers will make it a lot
easier to keep up the Trivia pages. First I need to think it through:

URL Scheme for the trivia app
-----------------------------

Starting with what I have :ref:`here<orig_trivia_urls>`, I will add pages to enter, edit and delete questions and the
answer choices that go with them; as well as a page for the users to be able to review their answers -- but not change
them:

.. csv-table:: **Updated URLs for the trivia app**
    :header: URL, Page(s) Addressed
    :widths: auto

    /trivia/scoreboard/, the scoreboard page (scoreboard.html)
    /trivia/question/n/, question n's page (trivia_question.html)
    /trivia/question/n/review, question n's review page (trivia_review.html)
    /trivia/result/n/, question n's results page (trivia_result.html)
    /trivia/question/n/compose, question n's composition page (trivia_compose.html)
    /trivia/question/n/edit, question n's edit page (trivia_edit.html)
    /trivia/question/n/delete, question n's delete confirmation page (trivia_delete.html)

So I have four new urls to implement. I will start with the compose page:

Building the Compose Page
-------------------------

Here are the steps:

#. Create a link in the header for the administrator only
#. Connect the link through a view to the template to display a stub page
#. Create the necessary forms on the compose page
#. Make sure the database gets properly updated when the forms are submitted

Creating the Link in the Header
+++++++++++++++++++++++++++++++

.. csv-table::**Does a link to Compose Trivia Questions appear in the header for administrators only?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, no such thing appears in the header, update header.html to include such a link for administrators only
    Yes, shows for me but not for Janet, ``href="/trivia/compose/"`` :ref:`see new urls below<trivia_urls_corrected>`.

.. csv-table::**Does clicking Compose Trivia Questions send me to the /trivia/compose/ page?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, I get a Page not found error as expected, create a url pattern for ``/trivia/compose/``
    No, template does not exist, create a stub
    No, template still does not exist, correct the name in the view
    Yes, the stub appears

.. csv-table::**Does the trivia_compose page have an "Add Question" Button?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, just the stub, add a button

Filling Out the Compose Page
++++++++++++++++++++++++++++

I'm thinking the page should list all of the available questions so that they can be selected for editing, each one
having a selection box next to it, and an "Edit Selected Question" button at the bottom of the list to send me to an
edit filled out with the current form of the question and its choices. There should also be an "Add Question(s)" button
near the top which would send me to a blank edit page.

Looking ahead, I can see that there might be a need on the editing page to add choices, or choose how many choices that
question will have. Further, like the admin app, it would be good to make it possible to either save a question and quit
or save a question and add another.

Finally, I might want to add a boolean field called "published" to the Question model with a default of False so that
the non-published questions in the database do not appear or affect any counts on line.

Come to think of it, I need to make sure the computation of percentage is being done correctly, dividing by the number
of questions a user has attempted rather than the total number of questions. [

.. _trivia_urls_corrected:

 The corrected version of the trivia URLs is below:

.. csv-table:: **Updated URLs for the trivia app**
    :header: URL, Page(s) Addressed
    :widths: auto

    /trivia/scoreboard/, the scoreboard page (scoreboard.html)
    /trivia/question/n/, question n's page (trivia_question.html)
    /trivia/question/n/review, question n's review page (trivia_review.html)
    /trivia/result/n/, question n's results page (trivia_result.html)
    /trivia/list/, administrator's page to elect to add new or select previous questions to edit (trivia_list.html)
    /trivia/edit/n/, question n's editing page (trivia_edit.html)
    /trivia/delete/n/, question n's delete confirmation page (trivia_delete.html)

Listing the Available Questions
+++++++++++++++++++++++++++++++

I'm just getting back to this section after a lot of work on the :ref:`problem below<trivia_error_checking>`. From
reading the above material I just changed what had been ``trivia/trivia_compose.html`` to ``trivia/trivia_list.html``. I
wonder if using a ListView would be helpful here. I will study the documentation at:
https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/

From my reading so far I'm not sure what the advantage is but I think I might be able to try it. Here is a
QuestionList view closely following their example::

    class QuestionList(ListView):

        model = TriviaQuestion

        def get_context_data(self, **kwargs):
            context = super(QuestionList, self).get_context_data(**kwargs)
            context['display_memory'] = utils.display_memory()
            return context

I wonder if that ``get_context_data`` thing will help with the :ref:`violation of DRY`<dry_violation>` I was dealing
with below. I may find out later.

The corresponding url should be::

    url(r'list/$', QuestionList.as_view(), name='question_list')

Finally, here is the body of the ``trivia_list.html`` template in a form that only lists the questions, rather than
giving the opportunity to edit any of them::

    {% block content %}
        <h2>Select a question to edit or click the Add New button below.</h2>
        <ul>
        {% for question in object_list %}
            <li>{{ question.number }}. {{ question }}</li>
        {% empty %}
            <li>No questions have been composed yet.</li>
        {% endfor %}
        </ul>
    {% endblock %}

Perhaps that ``{% empty %}`` tag may be an advantage here, simplifying the error checking I suppose. Let's see if this
actually works. (Note: you will also have to change the Add Trivia Question link in ``header.html``.

.. csv-table::*Does clicking the "Add Trivia Questions" link display the list of questions?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, it displays the compose.html stub, make the changes above
    No, it couldn't find the template ``triviaquestion_list``, add a ``template_name = `` line in the view
    No, "No questions have been composed yet.", add ``return context`` to end of ``get_context_data()`` (edited above)
    Yes, the memory displays along with the current list of questions

I can see how this makes things easier for those cases where the list is based on a single model. All I have to do is
tell it which model.

This ``get_context_data()`` should not have to be added to every view, though. There must be a way to do it with a
Mixin. I will save that adventure for later.

Converting the List to a Form
+++++++++++++++++++++++++++++

Let's go for broke and place a check-box next to each question. When the Edit button is clicked those questions will be
slated for editing... somehow.

I've already done check-boxes in the mail app. I'll look to see what I did there.

**mail/compose.html**::

    {% block content %}

        {{ block.super }}

        <div class="content">

            <h2>This page allows an administrator to compose and send e-mails to selected users.</h2>

            <form class="form-left" action="/mail/compose/" method="post">{% csrf_token %}
                <ul class="form-left">
                    {% for user in users %}
                        <li>
                            <input type="checkbox" name="family_member" value="{{ user }}"/>
                            {{ user.userprofile.get_name }}<br />
                        </li>
                    {% endfor %}
                </ul>
                <p class="instructions"><label for="sbjct">Subject:</label></p>
                <p><textarea id="sbjct" name="subject" rows="1" cols="40"></textarea></p>
                <p class="instructions"><label for="msg">Enter your message below:</label></p>
                <p><textarea id="msg" name="message" rows="10" cols="40"></textarea></p>
                <p><button class="my-button" type="submit">Send</button></p>
            </form>

            <a class="form-left" href="/gift/list/">
                <button class="my-button">Cancel</button>
            </a>

        </div>

    {% endblock %}

So I suspect I'll end up with what is below (since I will keep editing it until I get it right).

**trivia/trivia_list.html**::

    {% extends parent_template|default:"trivia/base_trivia.html" %}
    {% load static %}

    {{ block.super }}

    {% block content %}

        <h2>Select the questions you want to edit or click the Add New button below.</h2>
        <form action="/trivia/edit/" method="post">
            {% csrf_token %}
            <ul>
            {% for question in object_list %}
                <li>
                    <input type="checkbox" name="trivia_question" value="{{ question.number }}"/>
                    {{ question.number }}. {{ question }}
                </li>
            {% empty %}
                <li>No questions have been composed yet.</li>
            {% endfor %}
            </ul>
            <p><button type="submit">Edit Selected</button></p>
        </form>

    {% endblock %}

Now to check it out...

.. csv-table::**Do the questions appear in a form with checkboxes on the trivia_list page?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, just the list; no checkboxes, edit ``trivia_list.html`` as above
    Yes, but the bullets for the <li> tag still appear, fix it later in css

.. csv-table::**Does selecting a single question and clicking "Edit Selected" display the stub of the edit page?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, I stay at the url ``/trivia/list/`` but the page is blank, change the form action to ``/trivia/edit/``
    No, got a 404 Page not found error, add a url for ``/trivia/edit/`` and a TriviaEdit view
    No, got a TemplateDoesNotExist error, create the ``trivia_edit.html`` template
    Yes, after the correction of a slight copy/paste error

Getting the Trivia Edit Page to Work
++++++++++++++++++++++++++++++++++++

Something tells me I'm going about this the wrong way but I'm thinking of using the ``get`` method to display each
successive edit page ``/trivia/edit/n/``. First I'll have to figure out how to get it the series of questions.

.. csv-table::**Does selecting a single question and clicking "Edit Selected" display that question on the edit page?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, it only displays the stub, have the TriviaEdit get() method redirect to ``/trivia/edit/n/``
    Yes, , the relevant changes appear below

**from trivia/views.py**::

    class TriviaEdit(View):
        template_name = 'trivia/trivia_edit.html'

        def get(self, request):
            question_numbers = request.GET.getlist('trivia_questions')
            for question_number in question_numbers:

                return render(request, self.template_name)

        def post(self, request):
            print('Got to the post method of TriviaEdit')
            return redirect('gift_list')

    def trivia_list_edit(request):
        question_numbers = request.GET.getlist('trivia_questions')
        for number in question_numbers:
            question = TriviaQuestion.objects.get(number=number)
            choices = TriviaChoice.objects.filter(question=question.pk)
        return render(request, 'trivia/trivia_edit.html', {'question': question,
                                                           'choices': choices,
                                                           'display_memory': utils.get_memory(),})


    class ComposeTrivia(View):
        template_name = 'trivia/trivia_compose.html'

        def get(self, request):
            return render(request, self.template_name, {'display_memory': utils.get_memory(),})


**from trivia/urls.py**::

    url(r'^list/$', QuestionList.as_view(), name='question_list'),
    url(r'^edit/$', trivia_list_edit, name='trivia_list_edit'),
    url(r'^compose/$', login_required(ComposeTrivia.as_view())),

**from trivia/trivia_edit.html**::

    {% block content %}

        <h2>New improved trivia_edit page.</h2>
        <p>{{ question.number }}. {{ question }}</p>
        {% for choice in choices %}
            <p>    {{ choice.index }}{{ choice }}</p>
        {% endfor%}

    {% endblock %}

.. _edit_idea:

In the process of doing that I thought of a simple method to edit both the questions and the choices: create a section
for each question and it's choices, put a link to 'Edit' each question and each of it's choices, and put an 'Add Choice'
button to the bottom of each section. There should also be a 'Cancel' button which sends them back to the list page. Let
me try to implement the 'Cancel' button first:

.. csv-table::**Does a working 'Cancel' button appear on the edit page?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, only the first of the selected questions, add a link with type="button" link back to 'question_list'
    No, I get a link rather than a button, put a <button> between the <a>, </a> tags
    Yes, and it works too1

Now let's see if I can get the 'Edit' links in there and pointing to the right pages

.. csv-table::**Does selecting a single question to edit display an edit page as :ref:`described above<edit_idea>`?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, no edit links or buttons are visible with each question, add them in trivia_edit.html
    No, kept getting 'Could not parse remainder' errors, use the correct syntax: {% url 'url-name' parm_1 parm_2... %}
    No, NoReverseMatch error as expected, update urls to include 'question_edit' and 'choice_edit'
    No, ImportError in terminal: cannot import name 'QuestionEdit', create views for QuestionEdit and ChoiceEdit
    Yes, 'Edit Question' and 'Edit Choice' appear in the right places, simplify it to say 'Edit' - redundant otherwise

Now to get the 'Edit' links to work. Since these are edits to single models I can use Django's UpdateView.

.. csv-table::**Does selecting a single question and clicking "Edit" next to the question get to a question edit page?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, 'QuestionEdit is missing a QuerySet', tell the view to use model = TriviaQuestion
    No, 'AttributeError' having to do with Generic detail view QuestionEdit, try supplying a template and its suffix
    No, 'Generic detail view QuestionEdit must be called with either an object pk or a slug', complete update form html
    No, same problem, update urls to use (?P<pk>\d+) since you are sending pks
    No, NoReverseMatch for 'choice_edit', delete reference to question in choice link in trivia_edit.html
    No, ImproperlyConfigured error - not using 'fields' attribute is prohibited, use 'fields' attribute in view
    No, TemplateDoesNotExist, add the 'trivia/' and the '.html' to the template name
    Yes, , now work on getting the edits to work

First I got the 'Edit' links for the choices to work using what I learned above. When I click 'Update' on the form,
however, it complains that there is no URL to redirect to. I believe this is because I left the ``action`` blank in the
<form> tag. I'll work on it later.

But I notice how easy it is to use the built-in forms in Django in those cases where they apply to what I'm doing. I do
have less control, I don't get to have everything called what I would like, but there are probably ways to override the
default behavior that I don't know about yet.

Actually Editing Questions and Choices
++++++++++++++++++++++++++++++++++++++

I think all that remains is to come up with a place for the forms to redirect to. I think the most logical place is the
page that displays the questions and all of their choices, in other words, ``trivia/edit/question/n/`` which is named:
``question_edit``. Thus the action lines should say::

    action="{% url 'question_edit' {{ question.number }} %}"

Let's try that...

No, that didn't work. For one thing, I don't think the double braces are required around question.number. For another,
that is not the place that all the selected questions are listed along with their choices. Meanwhile, I don't know how
to keep the list of selected questions through the different views and templates that are used.

Changing My Approach to Editing
+++++++++++++++++++++++++++++++

I think I will be better off putting an 'Edit' link next to each question in the question list. That should send me to
a page with that question and it's coices available for editing. After editing either the question or one of the
choices, it should direct me back to the page with that question and its choices. When I click 'Done Editing' I should
go back to the whole question list page. Here is a step-by-step process for doing all that:

.. csv-table::**Do radio buttons appear at the beginning of each question on the trivia_list page?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, I have bullet point dots and checkboxes, edit trivia_list.html to eliminate checkboxes and add Edit links
    Yes, and they work to get me to the question edit page for that question too!

.. csv-table::**Does clicking 'Update' on the question or choice_edit page return to the edit page for that question?**
    :header: Success?, Result, Action to be Taken
    :widths: auto

    No, it gets me to that page but without the question and its choices showing
    No, and I made so many changes without documenting them I lost track of what I was doing, restart the whole process


Starting Over Again on Add/Edit Trivia
--------------------------------------

I think I need to take a more careful, more systematic approach, defining url patterns, etc. ahead of time and thinking
things through more carefully. I also need to do a more careful study of Class Based Generic Views in Django so that I
have a better understanding of what they do and how I can use them.

New Add/Edit Trivia URL Patterns
++++++++++++++++++++++++++++++++

.. csv-table::**URL Patterns for Add/Edit Trivia**
    :header: url pattern, view called, name, notes
    :widths: auto

    /trivia/list/, TriviaList.as_view(), trivia_list, lists all of the trivia questions with radio buttons for selection
    /trivia/create/n/, TriviaCreate.as_view(), trivia_create, allows entry of question and choices for question n
    /trivia/edit/n/, TriviaEdit.as_view(), trivia_edit, allows editing of question n
    /trivia/delete/n/, TriviaDelete.as_view(), trivia_delete, double checks and accomplishes deletion of question n





.. _trivia_error_checking:

Catching Submits with no Choices Selected
=========================================

While working on the compose page above, it occurred to me that users might accidentally, or on purpose, click the
Submit button on a question_display page without actually making any choices. What should happen in such cases is that
the page will redisplay and inform them they must select a choice before submitting the page.

I think I can do this by modifying both the DisplayResult view and the trivia_question.html template. That probably
means I also have to modify the DisplayQuestion view.

Currently, when I try to submit an unanswered question form, it generates a MultiValueDictKeyError at /trivia/result/n/.
Let's see if the DisplayResult view receives any errors from the dictionary named ``errors``. (See *Django Unleashed*,
pp. 213-216) I will insert a print statement at the beginning of the ``post`` method::

    print('errors = ', request.POST.errors)

It complained that 'QueryDict' object has no attribute 'errors'.

Perhaps I can catch the error in the post method of the DisplayResult view. I modified the code to include::

    if request.POST.choice:
        choice_index = request.POST['choice']
    else:
        return redirect(reverse('display_question'))

It still gives me ``AttributeError: 'QueryDict' object has no attribute 'choice'`` so I will try a try...except
approach::

    try:
        choice_index = request.POST['choice']
    except AttributeError:
        return redirect(reverse('display_question'))

``AttributeError`` was recognized, but in this case a ``MultiValueDictKeyError`` was thrown. Since that error was not
recognized (PyCharm had a wavy red line under it) I decided to use a blank ``except:`` as follows::

    try:
        choice_index = request.POST['choice']
    except:
        return redirect(reverse('display_question'))

Now I got a NoReverseMatch. Not knowing how to supply the ``question_number`` to ``reverse`` I decided to supply the url
more directly::

    try:
        choice_index = request.POST['choice']
    except:
        return redirect('/trivia/question/' + str(question_number) + '/')

That works, but doesn't display any error message. Various things I tried to get an error message at least delivered to
the template did not work. I will check the django tutorial to see if they covered this.

Yes, they did cover this in Tutorial 4. They set up their try/except sequence as follows::

    try:
        selected_choice = question.choice_set.get(pk=request.POST'choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

So I will try the following::

    try:
        choice_index = request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'trivia/question', {'question_number': question_number,
            'error_message': 'You need to select one of the following choices.'}
        )

Perhaps question_number gets into the url by means of the context dictionary but I don't remember knowing that before.

I will also have to modify ``trivia_question.html`` to do something with the ``error_message``.

I may also want to try ``return render(request, reverse('display_question'), {'question_number'.... }) to see if that
works.

No, none of that works. What is coming closest so far is::

    try:
        print('************ Got into the try')
        choice_index = request.POST['choice']
    except (KeyError, TriviaChoice.DoesNotExist):
        print('*************** Got into the except')

        return redirect(reverse('display_question', args=(question_number,),), permanent=True,
                        display_memory=utils.get_memory(),
                        error_message='You must choose one of the responses below.')

but the error_message just isn't getting sent to the template for some reason. The display_memory seems to make it, but
not the error_message. Strange.

I did notice, however, that the Django tutorial used a function-based view called vote. Perhaps that's what I need to do
instead of going directly to DisplayResult.

Attempted Solutions
-------------------

After a great deal of trial-and-error I finally got something to work here are the three files mainly involved:

**trivia/urls.py**::

    from django.conf.urls import url
    from django.contrib.auth.decorators import login_required
    from django.views.generic import RedirectView
    from django.urls import reverse
    from .views import (Scoreboard, DisplayQuestion, DisplayResult,
                        EndOfQuestions, AlreadyAnswered, ComposeTrivia,
                        TemporarilyClosed, trivia_choice)

    urlpatterns = [
        url(r'^$',
            RedirectView.as_view(
            url='/trivia/scoreboard/')),
        url(r'^scoreboard/$',
            login_required(Scoreboard.as_view()),
            name='scoreboard'),
        url(r'^question/$',
            RedirectView.as_view(pattern_name='scoreboard')),
        url(r'^question/(?P<question_number>[0-9]+)/$',
            login_required(DisplayQuestion.as_view()),
            name='display_question'),
        url(r'^process_choice/(?P<question_number>[0-9]+)/$',
            trivia_choice, name='trivia_submit'),
        url(r'^result/$',
            RedirectView.as_view(pattern_name='scoreboard')),
        url(r'^result/(?P<question_number>[0-9]+)/$',
            login_required(DisplayResult.as_view()),
            name='display_result'),
        url(r'^no_more_questions/$', login_required(EndOfQuestions.as_view()), name='end_of_questions'),
        url(r'^already_answered/$', login_required(AlreadyAnswered.as_view()), name='already_answered'),
        url(r'^compose/$', login_required(ComposeTrivia.as_view())),
        url(r'^temporarily_closed/$', login_required(TemporarilyClosed.as_view()), name='temporarily_closed',)
    ]

Note the addition of a ``trivia/process_choice/n/`` url. This points to a new functional view in ``trivia/views.py``
called ``trivia_submit``:

**trivia/views.py**::

    from django.shortcuts import render, redirect
    from django.urls import reverse
    from django.views.generic import View
    from django.http import HttpResponseRedirect

    from .models import TriviaQuestion, TriviaChoice, TriviaUserResponse
    from django.contrib.auth.models import User
    from user.models import UserProfile

    from operator import itemgetter

    import utils

    (...)

    class DisplayQuestion(View):
        template_name = 'trivia/trivia_question.html'

        def get(self, request, question_number=None, error_message=None):
            if int(question_number) > request.user.userprofile.get_next_trivia():  # prevents going beyond the next question
                question_number = request.user.userprofile.get_next_trivia()
                return redirect('/trivia/question/' + str(question_number) + '/')
            if int(question_number) > len(TriviaQuestion.objects.all()):
                return redirect(reverse('end_of_questions'))
            question = TriviaQuestion.objects.get(number=question_number)
            choices = TriviaChoice.objects.filter(question=question.pk)
            return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                        'question': question,
                                                        'choices': choices,
                                                        'error_message':error_message})


    class DisplayResult(View):
        template_name = 'trivia/trivia_result.html'

        def get(self, request, question_number=None, context=None):
            return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                        'q_number': question_number})

    (...)

    def trivia_choice(request, question_number=None):
        if int(question_number) < request.user.userprofile.get_next_trivia():
            return redirect(reverse('already_answered'))
        question = TriviaQuestion.objects.get(number=question_number)
        choices = TriviaChoice.objects.filter(question=question.pk)
        try:
            choice_index = request.POST['choice']
        except (KeyError, TriviaChoice.DoesNotExist):
            return render(request, 'trivia/trivia_question.html',
                          {'question': question,
                           'choices': choices,
                           'display_memory': utils.get_memory(),
                           'error_message': 'You must choose one of the responses below.'})
        else:
            choice = TriviaChoice.objects.filter(question=question).get(number=choice_index)
            correct_choice = TriviaChoice.objects.filter(question=question).get(correct=True)
            user_response = TriviaUserResponse(user=request.user, question=question, response=choice)
            user_response.save()
            profile = request.user.userprofile
            profile.trivia_questions_attempted += 1
            if choice.correct:
                profile.trivia_answers_correct += 1
            profile.save()
            return render(request, ('trivia/trivia_result.html'), {
                            'display_memory': utils.get_memory(),
                            'question': question,
                            'choice': choice,
                            'correct_choice': correct_choice})

This is what probably caused most of the trouble. First I had a hard time determining what error to try to catch in the
``try-except`` section. I found out by studying part 4 of the Django tutorial.

But the greatest difficulty lay in trying to get back to the same question page one has just left and display the error
message there. One thing I learned is that ``render`` renders a template, while ``redirect`` uses a url to redirect to.
This url can often be found through using the ``reverse`` function.

What I still don't understand is how something like ``return render(request, ('trivia/trivia_result.html'), {...}``
knows which url to go to -- or does it? I will try now to see what url I go to when I give a response to a trivia
question...

It goes to ``/trivia/process_choice/n/``, the one from the form action on the ``trivia_question.html`` template. It
still seems that I need to use ``redirect`` to get to the results page but I don't know how to do that and still send
a context or a bunch of variables.

In the tutorial, ``render`` was used to get back to the ``polls/detail.html`` page with the ``error_message`` in the
context.  ``HttpResponseRedirect`` was used if there WAS a vote cast but, aside from the ``args=(question.id,)`` to
indicate which question, there were no other variables sent -- like the ``display_memory`` I have to send to
``header.html``. Also, the tutorial warns that an ``HttpResponseRedirect`` must always be returned after successfully
dealing with POST data so that the data won't be entered twice if the user hits the Back button.

So, I have to figure out how to use a ``redirect`` (which, I believe, returns the necessary ``HttpResponseRedirect``,)
and still get the proper context information sent to the final template.

Perhaps this needs to be done within the receiving view. If I use::

    return redirect('trivia_result', args=(question_number,))

I should get to the ``get`` method of the ``DisplayResult`` view. Somehow, this needs to be given the choice the user
made but I don't see that anything else is necessary. Perhaps this will work:

**last line of trivia_choice view**::

    return redirect('trivia_result', args=(question_number,),
                    user_choice=choice,
                    question=question,
                    correct_choice=correct_choice)

Then, for the view:

**DisplayResult view**::

    class DisplayResult(View):
        template_name = 'trivia/trivia_result.html'

        def get(self, request, question=None, user_choice=None, correct_choice=None):

            return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                        'question': question,
                                                        'user_choice': user_choice,
                                                        'correct_choice': correct_choice})

.. _trivia_result_edit_01:

Then the ``trivia/trivia_result.html`` template would say::

    {% extends parent_template|default:"trivia/base_trivia.html" %}
    {% load static %}

        {{ block.super }}

        {% block content %}
            <div class="trivia width-40">
                <h3>Question {{ question.number }}: {{ question }}</h3>
                <h3>You chose  {{ user_choice.index }}{{ user_choice }}</h3>
                <h2>
                    {% if user_choice.correct %}
                        You are right!
                    {% else %}
                        Sorry, that isn't correct. The correct answer is {{ correct_choice.index }}{{ correct_choice }}.
                    {% endif %}
                </h2>
                <h4>
                    Out of {{ user.userprofile.trivia_questions_attempted }} questions attempted so far, you have gotten
                    {{ user.userprofile.trivia_answers_correct }} of them right. That gives you a score of
                    {{ user.userprofile.score }}.
                </h4>
                <p class="center-button">
                    <a href="{% url 'display_question' user.userprofile.get_next_trivia %}">
                        <button>Next Question</button>
                    </a>
                </p>
            </div>

        {% endblock %}

This did not work either. I kept getting the dreaded "No reverse found" error.

.. _dry_violation:

The Real Solution
-----------------

This may not be the best solution, since it violates DRY, but I think it will do for now.

It seems that when using ``redirect`` any data passed has to be in the url itself. I finally got it working by changing
the ``trivia_result`` (note the name change :ref:`from before<orig_trivia_urls>`) to include the user's choice number::

    url(r'^result/(?P<question_number>[0-9]+)/(?P<choice_number>[0-9]+)/$',
        login_required(DisplayResult.as_view()),
        name='trivia_result'),

Thus the ``trivia_choice`` view that calls it looks like this::

    def trivia_choice(request, question_number=None):
        if int(question_number) < request.user.userprofile.get_next_trivia():
            return redirect(reverse('already_answered'))
        question = TriviaQuestion.objects.get(number=question_number)
        choices = TriviaChoice.objects.filter(question=question.pk)
        try:
            choice_index = request.POST['choice']
        except (KeyError, TriviaChoice.DoesNotExist):
            return render(request, 'trivia/trivia_question.html',
                          {'question': question,
                           'choices': choices,
                           'display_memory': utils.get_memory(),
                           'error_message': 'You must choose one of the responses below.'})
        else:
            choice = TriviaChoice.objects.filter(question=question).get(number=choice_index)
            user_response = TriviaUserResponse(user=request.user, question=question, response=choice)
            user_response.save()
            profile = request.user.userprofile
            profile.trivia_questions_attempted += 1
            if choice.correct:
                profile.trivia_answers_correct += 1
            profile.save()
            return redirect('trivia_result', question_number=question_number, choice_number=choice.number)

Notice that ``question_number`` comes from the url "calling" this view, and is a string. Meanwhile, ``choice_number``,
coming from ``choice.number`` is an integer. The ``redirect`` shortcut must take care of the conversion for me. I was
thinking that the question number and response number had to be passed through
``args=(question_number, choice_number,)`` but they are to be given as parameters as they are here.

The ``trivia_result.html`` template works as shown :ref:`above<trivia_result_edit_01>`.

I'm ready to copy the following files to WebFaction:

* trivia/trivia_question
* trivia/trivia_result
* trivia/views
* trivia/urls
* christmas17.css

Temporarily Closed Page for Trivia App
======================================

I decided, while I'm working on something better, to add a page to the trivia app to let people who try to enter it
know that I'm adding questions and that they should try back in a few minutes. Here is the url pattern::

    url(r'temporarily_closed/', TemporarilyClosed.as_view, name='temporarily_closed'),

Then, when I am adding questions and responses, I can replace the header with a version that links the Trivia menu item
to ``temporarily_closed``. That will not help when people enter the urls directly but, hopefully, nobody does that. I
still need to work on a method for doing it within the website itself.

But, when it came down to using it, I realized I might be cutting somebody off in the middle of their work. I don't
know what would happen in such a case. I decided to add the questions and corresponding choices locally and then
transfer them by a dumpdata/loaddata sequence. The dumpdata command was::

    python manage.py dumpdata trivia.TriviaQuestion trivia.TriviaChoice > trivia_update_2017_12_10.json

That, and the corresponding::

    python3.6 manage.py loaddata trivia_update_2017_12_10.json

worked like a charm. Now see if the Player Rankings work out the way they are supposed to.


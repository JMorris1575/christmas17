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
    /trivia/compose/, a page for the administrator to add new questions or edit previous questions (trivia_compose.html)
    /trivia/edit/n/, question n's edit page (trivia_compose.html)
    /trivia/delete/n/, question n's delete confirmation page (trivia_delete.html)


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

Then the ``trivia/trivia_result.html`` template would say::

    {% extends parent_template|default:"trivia/base_trivia.html" %}
    {% load static %}

        {{ block.super }}

        {% block content %}
            <div class="trivia width-40">
                <h3>Question {{ question.number }}: {{ question }}</h3>
                <h3>You chose  {{ user_choice.index }}{{ user_choice }}</h3>
                <h2>
                    {% if choice.correct %}
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

The Real Solution
-----------------

This may not be the best solution, since it violates DRY, but I think it will do for now.

It seems that when using ``redirect`` any data passed has to be in the url itself. I finally got it working by changing
the ``trivia_result`` (note the name change from before) to include the user's choice number::

    url(r'^result/(?P<question_number>[0-9]+)/(?P<choice_number>[0-9]+)/$',
        login_required(DisplayResult.as_view()),
        name='trivia_result'),

(continue explanation)


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


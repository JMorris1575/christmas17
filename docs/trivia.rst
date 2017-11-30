.. _trivia_app_document:

==============
The Trivia App
==============

I have decided to document the creation of the trivia app here instead of in the ``new_apps.rst`` document. It should
make for shorter, more manageable documents.

Initial Thoughts
----------------

To build the trivia app I'm thinking I will have to:

#. Use ``python manage.py startapp trivia`` to create the app
#. Include a line saying ``'trivia.apps.TriviaConfig'`` in the ``INSTALLED_APPS`` setting in ``base.py``
#. Settle on a URL scheme for navigating the pages of the app
#. Implement the URL scheme in ``trivia.urls.py``
#. Update ``config.urls.py`` to include the trivia urls
#. Add a menu item in the header to direct the users to the trivia pages
#. Decide on the models needed to implement the app
#. Create the models needed in ``trivia.models.py``
#. Implement the views needed in ``trivia.views.py``
#. Implement the templates needed in ``trivia.templates``
#. Make the templates look good

The first two steps are easy. I have just completed them. The others I have rearranged so that I can take a TDD approach
to building the new app.

The Trivia URL Patterns
-----------------------

Looking over the ``new_apps.rst`` file I see my first idea for the url patterns:

.. csv-table:: **URLs for the trivia app**
    :header: URL, Page(s) Addressed
    :widths: auto

    /trivia/scoreboard/, the scoreboard page (scoreboard.html)
    /trivia/question/n/, question n's page (trivia_question.html)
    /trivia/result/n/, question n's results page (trivia_result.html)

Something tells me I am going to need more but this will do for a start. Here are the url patterns to be tried in
``trivia.urls.py``::

    urlpatterns = [
        url(r'^$',
            RedirectView.as_view(
            url='/trivia/scoreboard/')),
            url(r'^scoreboard/$',
                Scoreboard.as_view(),
                name='scoreboard'),
            url(r'^question/(?P<questionNumber>[0-9]+)/$',
                DisplayQuestion.as_view(),
                name='display_question'),
            url(r'^result/(?P<questionNumber>[0-9]+)/$',
                DisplayResult.as_view(),
                name='display_result'),
    ]

I will try to implement them one at a time, stub in the views, and create place-holder html files.

Building and Testing the URL Patterns
+++++++++++++++++++++++++++++++++++++

The /trivia/ and /trivia/scoreboard/ Patterns
*********************************************

For now I will test the patterns simply by entering them in the address line. Here is a test to see if entering
``/trivia/`` redirects to ``/trivia/scoreboard/``

.. csv-table:: **Does entering /trivia/ in the address line redirect to /trivia/scoreboard/?**
    :header: Result, Action to be Taken
    :widths: auto

    No, include the trivia urls in ``config/urls.py``
    Yes, proceed to test ``/trivia/scoreboard/``

|

.. csv-table:: **Does entering ``/trivia/scoreboard/`` in the address line display a fake scoreboard page?**
    :header: Result, Action to be Taken
    :widths: auto

    No, create a ``get`` method in the ``Scoreboard`` class
    No, TemplateDoesNotExist error; create the ``scoreboard.html`` file along with ``base_trivia.html``
    Yes, once I got the details right - like putting the html files in ``templates`` rather than ``static``

The /trivia/question/n/ Pattern
*******************************

.. csv-table:: **Does entering /trivia/question/n/ result in the diplay of a fake question page for that question?**
    :header: Result, Action to be Taken
    :widths: auto

    No, create the url pattern
    No, (in terminal: Method Not Allowed (GET)); add get method to DisplayQuestion view
    No, unexpected keyword argument 'questionNumber'; add ``question_number=None`` to get's arguments; change in urls.py
    No, TemplateDoesNotExist; create the ``trivia_question.html`` file
    No, it displays without referring to which question it is pretending to display; add ``q_number`` to render and html
    Yes, go on to test /trivia/results/n/

The /trivia/result/n/ Pattern
*****************************

.. csv-table:: **Does entering /trivia/result/n/ result in the diplay of a fake result page for that question?**
    :header: Result, Action to be Taken
    :widths: auto

    No, Page not found; create the url pattern
    No, GET method not allowed; add get() method to DisplayResult view
    No,  TemplateDoesNotExist; create the ``trivia_result.html`` template
    Yes, now test for authentication

Preventing access by Unauthenticated Users
++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: **Does the system prevent an unauthenticated user from entering any page in the trivia app?**
    :header: Result, Action to be Taken
    :widths: auto

    No, I entered /trivia/scoreboard/ without being authenticated; add ``login_required`` to urls
    Yes, the website is safe once again!

Displaying the Header on Each Trivia Page
+++++++++++++++++++++++++++++++++++++++++

.. index:: Problems; breaking the static files references

Because I had made a mistake earlier in placing my .html files in a newly created trivia/static/ directory instead of
a trivia/templates/ directory where they belong, I had done a refactor in PyCharm without thinking it through very
carefully. Because I allowed it without looking it went and changed several references throughout the program that were
supposed to say 'static' to 'templates'. I think I got them all, two in base.html, two in dev.py and two in prod.py.
If things seem to go haywire later, look around for references to 'templates' that should be to 'static'.

This also broke the display of the header and footer on all of the pages of the website (since it couldn't find the
static files). I got the header back once fixing the references but I might as well add the display of memories to the
trivia pages also.

.. csv-table:: **Do the Memories appear on each of the trivia pages?**
    :header: Result, Action to be Taken
    :widths: auto

    No, Add the context {'display_memory': utils.get_memory()} and the import of utils to each trivia view
    Yes, but entering something like /trivia/question/ results in a PageNotFound error.

Redirecting Badly Formed trivia urls to the Scoreboard Page
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: **Does entering /trivia/question/ or /trivia/result/ without the /n/ redirect to the scoreboard page?**
    :header: Result, Action to be Taken
    :widths: auto

    No, Page not found error; add url patterns to redirect to scoreboard
    Yes, but it didn't work the way I thought. See below.

In order to redirect to the scoreboard I had to use::

    RedirectView.as_view(pattern_name='scoreboard'))

I found this in *Django Unleashed* page 398.

Adding a Trivia Menu Item to the Header
---------------------------------------

This should be easy, just add a list item and direct it to the scoreboard.

.. csv-table:: **Does the header include a working Trivia link after "Question of the Day"?**
    :header: Result, Action to be Taken
    :widths: auto

    No, add a <li> item to the header page.
    Yes, time for bed

Moving to Kalamazoo Again
-------------------------

Through PyCharm I did a Git Pull, which required me to do a revert since I did a make html after the last commit and it
changed some files in _build I didn't really care about.

I tried to do a migrate and it informed me I needed to makemigrations first. I did that, then the migrate. Both seemed
to work fine.

I did a ``python manage.py loaddata all.json`` and it seemed to work perfectly, including the UserProfile data in the
database. It kept last year's questions in the database so I deleted them through the ``/admin`` app.

Now I should be ready to proceed.

Working on the Models
---------------------

Now that the URLs are working it is time to start working on the models. I have already designed, or at least partially
designed the models :ref:`here<trivia_model_design>`. That seems like as good a starting point as any, except that the
fields of the "TriviaUserProgress" model should probably just be added to the UserProfile Model.

Creating the Trivia Models
++++++++++++++++++++++++++

Here are the trivia models as I created them::

    from django.db import models
    from django.conf import settings

    # Create your models here.

    class TriviaQuestion(models.Model):
        number = models.IntegerField(unique=True)
        text = models.TextField()
        attempted = models.IntegerField()
        correct = models.IntegerField()

        def __str__(self):
            return self.text

        class Meta:
            ordering = ['number']


    class TriviaChoices(models.Model):
        question = models.ForeignKey(TriviaQuestion)
        number = models.IntegerField()
        text = models.CharField(max_length=60)
        correct = models.BooleanField(default=False)

        def __str__(self):
            return self.text

        class Meta:
            unique_together = ('question', 'number')
            ordering = ['number']


    class TriviaUserResponses(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL)
        question = models.ForeignKey(TriviaQuestion)
        response = models.ForeignKey(TriviaChoices)

        def __str__(self):
            text = self.user.get_name() + "'s response to question " + str(self.question.number) + ": " + self.response
            return text

        class Meta:
            ordering = ['question.number']


    class TriviaConversation(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL)
        entry = models.CharField(max_length=300)

        def __str__(self):
            return self.user.get_name() + ': ' + self.entry

I also modified the UserProfile model as follows::

    class UserProfile(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL)
        gift_selected = models.ForeignKey(Gift, null=True, blank=True)
        added_memories = models.BooleanField(default=False)
        trivia_questions_attempted = models.IntegerField()
        trivia_answers_correct = models.IntegerField()

        def __str__(self):
            return 'Profile for ' + self.user.get_full_name()

        def get_name(self):
            name = self.user.first_name
            if name == 'Brian':
                name += ' ' + self.user.last_name
            return name


Finally, the trivia.admin.py program had to have some additions to it::

    from django.contrib import admin
    from .models import TriviaQuestion, TriviaChoices, TriviaUserResponses, TriviaConversation

    # Register your models here.

    admin.site.register(TriviaQuestion)
    admin.site.register(TriviaChoices)
    admin.site.register(TriviaUserResponses)
    admin.site.register(TriviaConversation)

I will do a commit here before trying to use these models.

Using the Trivia Models
***********************
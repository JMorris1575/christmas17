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
            ordering = ['question']


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

Migrations with the New Trivia Models
*************************************

First I will need to do a makemigrations and a migrate... I got an error::

    ERRORS:
    trivia.TriviaUserResponses: (models.E015) 'ordering' refers to the non-existent field 'question.number'.

so I guess I can't do it that way, but I suppose with TriviaQuestion already being ordered by number I can just use::

    class Meta:
        ordering = ['number']

in the TriviaUserResponses model.

Tried to do a **makemigrations** again and this time got a non-nullable field: ``trivia_answers_correct`` in my
UserProfile updates. I will set the default of both of the new fields to zero (0).

This time **makemigrations** worked and I added both of the new migration files to Git. Running **migrate** worked
without any problems.

Entering Data into the Trivia Models
************************************

I haven't actually decided on a set of trivia questions yet so, except for the first question, for development I will
add a bunch of fake questions and choices to the models through the admin app.

When I entered the first question it complained that I hadn't entered anything for ``attempted`` or ``correct``. I will
supply defaults, do another **makemigrations** and another **migrate**. This was done with no problems.

While entering the data into the TriviaChoice model I decided to modify the ordering of that model. That line now
contains ``ordering = ['question', 'number']``

Entering the data this way is quite painful. Either the ``/admin`` app allows two related models to have data entered at
the same time or I can work on a page to create questions and their possible choices.

Building the Trivia App
-----------------------

With the models in place I can start building the app, step by step, using my modified version of Test Driven
Development (TDD). Here is an initial plan -- which will probably not be adhered to very closely:

#. Have the game rules appear on the scoreboard page.
#. Have a 'First Question'/'Next Question' button appear on the scoreboard page.
#. Clicking the 'First Question' button sends them to the first question page which identifies itself as such.
#. The question page displays the question.
#. The question page displays the possible answers with radio buttons next to each.
#. The question page displays a working 'Submit' button
#. Clicking the submit button sends the user to the results page.
#. The results page informs them of whether their answer was correct
#. The results page displays the user's statistice: questions answered, number correct, percentage correct
#. The results page displays a 'Next' button which sends the user to the next question
#. Entering the url for later questions still sends the user to the next question in line for them
#. The scoreboard page displays participating user scores
#. The scoreboar page displays participating user scores in descending sequence
#. The scoreboard page displays participating user scores in groups depending on the number of questions completed.

Game Rules
++++++++++

.. csv-table:: **Do the game rules appear on the scoreboard page?**
    :header: Result, Action to be Taken
    :widths: auto

    No, Write them into scoreboard.html
    Yes, I also centered it

Question Button
+++++++++++++++

.. csv-table:: **Does a question button (First Question or Next Question) appear on the scoreboard page?**
    :header: Result, Action to be Taken
    :widths: auto

    No, write it into scoreboard.html directing it to a ``next_trivia_question`` url (:ref:`See below.<question_button>`)
    No, modify UserProfile model to include a get_next_trivia function and use it in template
    No, It is not a button; enclose a <button> element within the <a> tag.
    No, "Next Question" not "First Question"; change 'if' statement to user.userprofile.trivia_questions_attempted==0

|

.. csv-table:: **Is the question button centered horizontally on the screen?**
    :header: Result, Action to be Taken
    :widths: auto

    No, create a ``center-button`` css class and use it in ``scoreboard.html`` (:ref:`See below<ctr_btn_class>`.)
    No, put the button in some sort of outer wrapper: <p> or <div> and center that
    Yes, I chose the <p> element; my css needs a LOT of work!

.. _question_button:

Here is the initial html for the question button::

    {% if user.trivia_questions_attempted == 0 %}
        <a type="button" href="{% url 'next_page' %}">First Question</a>
    {% else %}
        <a type="button" href="{% url 'next_page' %}">Next Question</a>
    {% endif %}

.. _ctr_btn_class:

Here was my first attempt at creating a class to center buttons::

    .center-button {
        width: 150px;
        margin-left: auto;
        margin-right: auto;
        }


Displaying the Trivia Question Page
+++++++++++++++++++++++++++++++++++

.. csv-table:: **Does clicking on the 'First Question' get the user to the first question page?**
    :header: Result, Action to be Taken
    :widths: auto

    No, it reloads scoreboard; edit the ``get_next_trivia`` function in user.models.py (:ref:`See below<gt_nxt_trv>`.)
    No, still reloads scoreboard; edit ``scoreboard.html`` to say ``href="user.userprofile.get_next_trivia"``
    No, Page not found looking for ``trivia/scoreboard/1``; create the appropriate {% url ... %} tag
    Yes, it took a while to find the :ref:`appropriate<new_next_ques_btn>` tag but it works now

.. _gt_nxt_trv:

Originally, I had self.user.trivia_questions_attempted, but that was silly! Here is the final form::

        def get_next_trivia(self):
            next_ques = self.trivia_questions_attempted + 1
            print('next_ques = ', next_ques)
            return next_ques

.. _new_next_ques_btn:

After a lot of trial and error, this is what I found to work::

    {% if user.userprofile.trivia_questions_attempted == 0 %}
        <p class="center-button">
            <a href="{% url 'display_question' user.userprofile.get_next_trivia %}">
                <button>First Question</button>
            </a>
        </p>
    {% else %}
        <p class="center-button">
            <a href="{% url 'display_question' user.userprofile.get_next_trivia %}">
                <button>Next Question</button>
            </a>
        </p>
    {% endif %}

Currently, however, it only displays the stubbed in ``trivia_question.html`` page.

Displaying Questions on the Question Page
+++++++++++++++++++++++++++++++++++++++++

.. csv-table:: **Does the question page display the corresponding question?**
    :header: Result, Action to be Taken
    :widths: auto

    No, only stub; update :ref:`DisplayQuestion<disp_ques_view>` view and :ref:`trivia_question.html<new_trv_ques_html>`
    Yes, worked (almost) the first time

.. _disp_ques_view:

Here is the first attempt at updating DisplayQuestion::

    class DisplayResult(View):
        template_name = 'trivia/trivia_result.html'

        def get(self, request, question_number=None):
            question = TriviaQuestion.objects.get(number=question_number)
            return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                        'question': question})

I also had to import TriviaQuestion of course.

.. _new_trv_ques_html:

Here is the somewhat improved version of ``trivia_question.html``::

    {% block content %}
        <h2>Question Number: {{ question.number }}</h2>
        <p>
            {{ question }}
        </p>
    {% endblock %}

Displaying Possible Responses on the Question Page
++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: **Do the possible responses to a question display with the corresponding question?**
    :header: Result, Action to be Taken
    :widths: auto

    No, adjust DisplayView to send the possible choices in the context and loop through them in ``trivia_question.html``
    Yes, now make them into radio buttons

Displaying Possible Responses as Radio Buttons
++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: **Do the possible responses display as radio buttons?**
    :header: Result, Action to be Taken
    :widths: auto

    No, Change them to <input type="radio">
    Yes, after some :ref:`experimentation<expt>` and adding a :ref:`method<choice_index>` to the TriviaChoices model

.. _expt:

Here is the html currently displaying the possible responses to the trivia questions::

    {% for choice in choices %}
        <p>
            <input type="radio" name="choice" value={{ choice.number }}>{{ choice.index }}{{ choice }}</input>
        </p>
    {% endfor %}

.. _choice_index:

Here is the new index method added to the TriviaChoices model::

    def index(self):
        return ' ' + chr(64 + self.number) + ') '


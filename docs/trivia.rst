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

.. csv-table:: **URLS for the trivia app**
    :header: 'URL', 'Page(s) Addressed'
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

.. csv-table::*Does entering /trivia/ in the address line redirect to /trivia/scoreboard/?*
    :header: 'Result', 'Action to be Taken'
    :widths: auto

    No, include the trivia urls in ``config/urls.py``
    Yes, proceed to test ``/trivia/scoreboard/``

.. csv-table::*Does entering ``/trivia/scoreboard/`` in the address line display a fake scoreboard page?*
    :header: 'Result', 'Action to be Taken'
    :widths: auto

    No, create a ``get`` method in the ``Scoreboard`` class
    No, TemplateDoesNotExist error; create the ``scoreboard.html`` file along with ``base_trivia.html``
    Yes, once I got the details right - like putting the html files in ``templates`` rather than ``static``

The /trivia/question/n/ Pattern
*******************************

.. csv-table::*Does entering /trivia/question/n/ result in the diplay of a fake question page for that question?*
    :header: 'Result', 'Action to be Taken'
    :widths: auto

    No, create the url pattern

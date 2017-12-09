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


.. trivia_urls_corrected::

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

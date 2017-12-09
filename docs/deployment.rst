==========
Deployment
==========

This section describes the process of deploying the Christmas2017 website on webfaction.

Initial Notes
=============

Christmas2016
-------------

The Christmas2016 website is located at:  :ref:`christmas.jmorris.webfactional.com`. I want to keep that url so I will
have to figure out how to do that. Also, I would like to keep the Christmas2016 website working and intact, at least while
deploying Christmas2017, for comparison purposes.

After visiting Webfaction.com (see below), I typed in the domain: christmas15.jmorris.webfactional.com and got to my
Christmas2015 website.

Learned on a Visit to Webfaction.com
------------------------------------

My webserver is now: web506.webfaction.com

I notice I have four websites:

* Christmas15 - christmas15.jmorris.webfactional.com
* christmas16 - christmas.jmorris.webfactional.com
* PythonClass - pythonclass.jmorris.webfactional.com
* TDD-StagingTutorial - No domains

I have the following domains:

* jmorris.webfactional.com
* christmas.jmorris.webfactional.com
* christmas15.jmorris.webfactional.com
* pythonclass.jmorris.webfactional.com

I pay $6.50 a month for my account and I have $59.40 left in my balance so I have more than enough to make it through
the Christmas season but I will have to do something about that later this year.

I see on the "Make a one-off payment" tab::

    Your account is paid up until 19 Sep 2018. We will charge your active payment source for the next period on
    20 Sep 2018. Thank you.

I don't have an "active payment source" set up though so I will have to add one before September 20, 2018. Three years
will cost $234, which still comes to $6.50 a month.

I have the following databases, all of which are PostgreSQL databases:

* c16database
* christmas15
* christmas2015
* mvpland
* pgdbase

There are four database users listed. They are:

* jamesmorris
* jim
* jim_test
* jmorris

Here is a table of my applications:

.. csv-table::
    :header: Name, Type, Server
    :widths: auto

    c16, Django 1.10.4 (mod_wsgi 4.5.9/Python 3.5), Web506
    c16_static, Static only (no .htaccess), Web506
    christmas15, Django 1.8.7 (mod_wsgi4.4.21/Python 3.4), Web506
    christmas15_static, Static only (no .htaccess), Web506
    htdocs, Static only (no .htaccess), Web506
    mvpland1, Django 1.8.5 (mod_wsgi 4.4.13/Python 3.4), Web506
    mvpland1_media, Static only (no .htaccess), Web506
    mvpland1_static, Static only (no .htaccess), Web506
    pythonclass, Django 1.11.4 (mod_wsgi 4.5/Python 3.5), Web506
    tdd2_staging, Django 1.9.6 (mod_wsgi 4.5.2/Python 3.5), Web506
    tdd2_static, Static only (no .htaccess), Web506


Using FileZilla
===============

To use FileZilla enter the following::

    Host: Web506.webfaction.com
    Username: jmorris
    Password: (DylanSelfie)
    Port: 21

Other ports may work too, that's just what I happened to use.


Getting Christmas2016 to work at christmas16.webfactional.com
=============================================================

First I used Webfaction's control panel to create the new domain:  christmas16.webfactional.com

Then I used it to change the christmas16 website to the domain: christmas16.webfactional.com

Then I used FileZilla to change two settings in prod.py::

    STATIC_URL = 'http://christmas16.jmorris.webfactional.com/static/'
    ALLOWED_HOSTS.append('christmas16.jmorris.webfactional.com')

I did this by right-clicking the file and selecting "View/Edit" which opened the file in Notepad++. Saving from
Notepad++ changed the file on the server.

Finally, I got into SSH and restarted the apache server by going to ``webapps/c16`` and typing::

    apache2/bin/restart

To be honest, it didn't seem to work right away. Said something about trying to start, so I entered::

    apache2/bin/start

and it said something about already being started. Harumph!

Anyway, it's working now.

Creating the christmas17 Website
================================

This will require several steps, I think. Here are my original thoughts:

#. Use WebFaction's control panel to create a new website
#. Create a c17 app and a c17_static app with WebFaction's control panel
#. Create a c17database for the website using WebFaction's control panel
#. Use FileZilla to copy all of the files in Christmas2017 to the proper place
#. Make the necessary changes in that wsgi thing and whatever else there is
#. Do a migrate
#. Do a loaddata to copy the current form of the local database to the remote server

Creating the New Website
------------------------

I viewed the *Getting Started with Django on WebFaction* video linked to on the WebFaction's dashboard. From that I see
that the process is:

#. Click DOMAINS/WEBSITES
#. Click on Websites
#. Click Add new website
#. Choose a name for the website (c17)
#. Choose a domain name (christmas.jmorris.webfactional.com)
#. Click Add an application
#. Click Create a new application
#. Give the django application a name (christmas17)
#. Choose Django in the App category
#. Select the latest Django and Python in App type
#. Click Save to save the application
#. Click Save again to create the website

I did all of those things and I should have a Django website. ``christmas.jmorris.webfactional.com`` still displayed
the ``Site not configured`` page so, after some thrashing around, I got into ssh with::

    ssh jmorris@web506.webfaction.com

Meanwhile, the "It worked!" Django page started displaying at ``christmas.jmorris.webfactional.com``.

Getting into FileZilla, which makes the directory structure easier to see, I see that what I entered as the app name,
``christmas17`` is a folder under ``webapps`` and contains the ``myproject`` folder that will be replaced by
``Christmas2017`` and the inner ``myproject`` folder that will be replaced by ``config``. I don't think I will have to
make any changes to the ``wsgi.py`` file as the necessary changes have already been made in my ``Christmas2017`` files.

I will, however, have to make changes to the ``christmas17/apache2/conf/httpd.conf`` file which directs the server to
the right directories. Now it is being directed to ``myproject`` and ``myproject/myproject``. I will have to change
those to:  ``Christmas2017`` and ``Christmas2017/config``.




Creating the c17_static app
---------------------------

Since the ``christmas17`` app was already created as part of creating the website, now I only have to create the
``c17_static`` app and get it properly configured in ``prod.py``, if it isn't already.

By looking at the document at https://docs.webfaction.com/software/django/getting-started.html I discovered I could have
added the static app when I created the website just by adding another app. It can still be done now by going to my
``c17`` website and clicking on Add an application. The steps for adding the static application are:

#. Click Add an application
#. Click Create a new application
#. Enter a name in the Name field (c17_static)
#. Select Static in the App category menu
#. In the URL field enter static
#. Click the Save button to save the new app
#. Click the Save button to save the edited website

I did all this and now FileZilla shows a new ``c17_static`` folder in the ``webapps`` directory.

Creating the c17database
------------------------

According to https://docs.webfaction.com/software/django/getting-started?highlight=create%2520database#creating-a-database
these are the steps I should follow:

#. Click Databases > Databases
#. Click the Add new database button.
#. In the Name field, enter a name for the database. (c17database)
#. In the Database type menu, click to select PostgreSQL.
#. Choose (or created) a database owner (jamesmorris)
#. Click the Save button.

This seemed to work without any problems. I have edited ``secrets.json`` to say::

  "PROD_DATABASE_NAME": "c17database",

Creating an "Under Construction" Page
-------------------------------------

It seems I should be able to use the ``myproject`` default project to display a temporary "Under Construction" page in
case any family members try to get into the site before it's ready.  Through ssh I can try the following::

    python manage.py startapp under_construction

    create an under-construction.html page which includes segments from base.html and header.html as well as its own
    markup

    write the appropriate url

    copy it all over to myproject

I never succeeded in doing this. I was too sloppy and I didn't want to waste any further time on it. I think perhaps I
should create a separate django project for this, or maybe an app I can include in any django project I build. Think
about it later!

Connecting to the Mailbox
-------------------------

Before I can get the website up and running I will need to connect my new c17 website to my old mailbox.

Ah! Lo and behold, looking at https://my.webfaction.com/domains I find that my mailboxes are associated with the
domain ``christmas.jmorris.webfactional.com`` rather than being associated with the website itself. I don't think I have
to do anything to connect to the mailbox!

Moving the Website to WebFaction
--------------------------------

According to the WebFaction documentation at https://docs.webfaction.com/software/django I need to:

#. Open an SSH session to my account. (jmorris@web506.webfaction.com)
#. Get into the directory of the django_app (christmas17)
#. Enter ``rm -rf ./myproject`` and press Enter.
#. Use FileZilla to copy most\* of the files in Christmas2017 to ``webapps.christmas17``
#. Edit ``webapps.christmas17.apache2/conf/httpd.conf`` changing ``myproject`` to ``Christmas2017``
#. Also change WSGIScriptAlias to refer to ``Christmas2017`` and ``Christmas2017/config``

\* The files I left out were the outdated .json files I've been using to synchronize the databases on each of my
computers, but I did include the latest one:  ``all-2017-12-07.json`` which has everything currently in my local
database.

I think I have already edited ``prod.py`` to configure Django to connect to the c17database but the ENGINE given in the
documentation was::

    'django.db.backends.postgresql_psycopg2'

rather than just::

    'django.db.backends.postgresql'

I changed the setting to include ``_psycopg2`` but if it doesn't work I can always go back.

I think I have set INSTALLED_APPS, STATIC_FILES_DIRS, and STATIC_ROOT appropriately, and I think I am ready to send
e-mail messages.

So the last things to do are to use ssh to send the following commands::

    python3.6 manage.py migrate
    python3.6 manage.py collectstatic

then restart apache with::

    ../apache2/bin/restart

I couldn't run the migrate command at first. It kept giving me an error about
``no pg_hba.conf entry for host "127.0.0.1", user "Jim", database "c17database", SSL off``

I finally figured out that it was because I was still using ``from .dev import *`` in config's ``__init__.py`` file. I
commented that line, and uncommented ``from .prod import *`` and the migrate worked.

I ran ``collectstatic`` and it acted like it was working, but nothing seemed to move. Maybe I need to restart FileZilla.
Nope, that didn't seem to do anything.

Ah, well, somehow they are there. I'm not sure if this was it, but when I clicked the upper pane in FileZilla's Remote
site: window, everything updated.


.. index:: Problem; Key(app_label, model)=([myapp], [mymodel]) already exists.

Getting the Online Database Up To Date
--------------------------------------

Using ssh, and in the ``websites/christmas17/Christmas2017`` directory, give the command to update the database::

    python3.6 manage.py loaddata all-2017-12-07.json

and hope that it works.

It didn't. Gave me some kind of complaint about userprofile already existing. I couldn't log into the website, or get
into the admin until I created a superuser:

username: jmorris
e-mail: frjamesmorris@gmail.com
password: DylanSelfie

Now I can get into the admin and I see that there are NO entries in any of the database models. Maybe try the
``loaddata all-2012-12-07.json`` again...

Nope, I got the same problem:  ``DETAIL: Key (app_label, model)=(user, userprofile) already exists.``

I may have to dump and load the information for each and every app in Christmas2017. Just to check, I'll start with
the user app.

Same problem with the user app. (user, userprofile) already exists. I may have to re-enter the entire user database --
ugh!!!

I finally got it to work by dumping and loading auth and then dumping and loading just my models by means of the
following commands::

    In PyCharm (the local files):

    python manage.py dumpdata auth > auth.json
    python manage.py dumpdata gifts mail memory question story trivia > mine-2017-12-07.json

    I used FileZilla to copy auth.json and mine-2017-12-07.json to the remote location on WebFaction.com and then,
    in ssh:

    python3.6 manage.py loaddata auth.json
    python3.6 manage.py loaddata mine-2017-12-07.json

    I didn't do all this in exactly this order. There were some failed attempts too.

Testing the Website
-------------------

Go to ``christmas.jmorris.webfactional.com`` and look around to see if everything is working. If so, send out the
invitation e-mail.

I could login as JIM (I think... it was held over from my logging into the admin.) I could also login as Abby and see
the gift_list page. Clicking on the Question of the Day link seemed to work fine.

Clicking on **Trivia** however, failed. As it tried to get to ``/trivia/scoreboard/`` it threw a server error. The
notification in my e-mail said::

    Internal Server Error: /trivia/scoreboard/

    NoReverseMatch at /trivia/scoreboard/
    Reverse for 'display_question' with arguments '('',)' not found. 1 pattern(s) tried: ['trivia/question/(?P<question_number>[0-9]+)/$']

I'm guessing the problem is either in the url configuration or in the ``scoreboard.html`` page itself. I will look
there first.

What I saw there was a couple of lines containing::

    <a href="{% url 'display_question' user.userprofile.get_next_trivia %}">

If user.userprofile does not exist, that would explain the problem.

I accidentally discovered that I can create userprofile for each user in the admin. This may not be the easiest way but
going to each User, scrolling down to the User Profile section, faking an entry (I used Added memories), then clicking
save. Seems to create the userprofile for that user. I had to remember to change the entry back to its original form of
course.

In the process I noticed that no one was credited with adding any memories. Not surprising since userprofile had not
existed before. I listed all the memory contributers and then set the 'Added memory' flag correctly.




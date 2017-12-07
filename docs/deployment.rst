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

Copying the Files
-----------------



Editing Control Files
---------------------

Getting the Database Up To Date
-------------------------------

Testing the Website
-------------------



Converting Christmas2016 to Christmas2017
=========================================

This document chronicles the development of the Christmas 2017 website from the point the Christmas 2016 website was
cloned locally and gotten to work.

Initial Thoughts
----------------

* I can start by refactoring the folder named Christmas2016 to Christmas2017. I think I can accept the default changes
  PyCharm wants to make.

* I will need to create a new PostGreSQL Database for this year and probably need to copy the old one over. This will
  require some study.

* I want to redesign the look and feel of the website. This will test my artistic skills, such as they are, and will
  probably require some changes to the base.html, header.html and footer.html templates.

Getting Up and Running on the Rectory Computer
----------------------------------------------

Refactoring the Main Folder
+++++++++++++++++++++++++++

Changing Christmas2016 to Christmas2017 was no problem in PyCharm after I closed any windows or programs that might be
using it. Before that I got some obscure java script error. I may still find some things that need changing, like
comments that refer to Christmas2016.

.. index:: Database; creating new

Switching to a New Database
+++++++++++++++++++++++++++

Creating the New Database
*************************

Again, checking the Christmas2016 documentation I was reminded how to create a new PostgreSQL database:

#. Open pgAdminIII

#. Double-click PostgreSQL and enter the password (Dylan Selfie).

#. Right click Databases and select New Database...

#. Add the name (I chose c17database).

#. Select an Owner (I selected Jim).

#. Update the secrets.json file to refer to c17database instead of c16database.

I tested to see if I could get into the website and found I had to do:

``>manage.py migrate``

before I could even get to the login page. The login page, unsurprisingly, wouldn't let me in. I don't have any users
in the database yet.

.. index:: Django; admin, Django; createsuperuser

I did learn how to get into the admin pages though, do a:

``> manage.py createsuperuser``

After creating Jim as a superuser with DylanSelfie as the password I could get into the Christmas 2017 Admin file,
though it is still calling itself Christmas 2016 Admin. The structure was there with headings AUTHENTICATION AND
AUTHORIZATION, GIFTS, MAIL, MEMORY, QUESTION, and STORY, but none of the tables had any entries and the QUESTION tables
didn't work at all for some reason.

I just found out where the admin site gets its heading. It is given in the ``urls.py`` file in the ``config`` folder. I
changed it to Christmas 2017.

I wonder if there is a way to delete a superuser too.

.. index:: Database; migrating

Initial Migration
*****************

In order to get the database working (apparently there was some problem with the question app) I did a

``manage.py makemigrations``

It wanted to know if I had renamed response.author to response.responder, which I'm sure I did :-), and corrected some
"non-nullable" fields to include a default. I just selected the suggested default of ``timezone.now`` for most of them
and "Test Question" for the non-nullable field 'response.' Obviously not a great default. I hope I can change it in the
model file later.

Finally it was happy with me and said::

    Migrations for 'question':
    question\migrations\0002_auto_20171024_2115.py
    - Change Meta options on question
    - Rename field author on response to responder
    - Add field date to question
    - Add field entered to response
    - Add field response to response

Then I did a ``manage.py migrate`` and got this response::

    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, gifts, mail, memory, question, sessions, story, user
    Running migrations:
    Applying question.0002_auto_20171024_2115... OK

.. index:: Database; copying data

Copying Data to c17Database from c16database
********************************************

To copy the c16Database I used ``manage.py dumpdata`` in the c16 environment to create a bunch of files from the various
models used by the website: to_c17_user.json, to_c17_gifts.json, to_c17_mail.json, to_c17_memory.json and
to_c17_question.json. Then I used ``manage.py loaddata <fixture>`` in the c17 environment to read them in. (Later I
learned how to do them as a group (:ref:`see below <loading-multiple-fixtures>`.) I still don't know why I
couldn't dump them as a group.)

The mail data seems to be empty but it didn't stop me from loading it all. Now the website works locally.

.. index:: Version Control; setting remote

Resetting the Remote to c17Development
++++++++++++++++++++++++++++++++++++++

Because my current files were all cloned from the origin:

``https://github.com/JMorris1575/christmas16``

that repository was the remote pointed to in PyCharm. To change that I went to ``VCS>Git>Remotes`` and changed it to:

``origin	https://github.com/JMorris1575/christmas17``

After doing a commit and a push the files were all safely stored in the proper GitHub repository.


Getting Up and Running on the Home Computer
-------------------------------------------

.. index:: cloning, GitHub; cloning, PyCharm; cloning

Cloning the Website from GitHub
+++++++++++++++++++++++++++++++

This was not a difficult process, though I had to get into a project for which I had enabled Version Control. I used
``c16Development``. I went to ``VCS > Git > Clone...``, put in ``https://github.com/JMorris1575/christmas17`` for the
**Git Repository URL**, left the **Parent Directory** as ``C:\Users\frjam\Documents\MyDjangoProjects``, and changed the
**Directory Name** to ``c17Development``, then clicked the **Clone** button.

In order to write the paragraph above I had to get into the cloning dialog several times and noticed it was still set
to the c16 settings. I went to ``VCS > Git > Push...``, clicked on ``origin > Define Remote``, clicked ``OK`` and got
an error message:

``Couldn't add remote: remote origin already exists.``

Hmm... I seem to remember going through something like this last night just before pushing the website from my
Rectory computer. I think I had to change it in settings...

Nope, nothing there. Ah! Now I remember, it was under ``VCS > Git > Remotes...`` but it was already set correctly on
this, my home computer.

But I noticed I hadn't pushed the latest version to GitHub before leaving the Rectory Computer. I got into
TeamViewer and mucked around with it for a while but it seems to be correct now. I had to "stash" the changes I made
to this file before the pull would work. I may have to learn what that means. ;-)

..index:: Problems; Couldn't import Django

Installing Sphinx on the Home Computer
++++++++++++++++++++++++++++++++++++++

When I tried to compile these documents I discovered I had not yet installed Sphinx on this computer. I did:

``> pip install sphinx``

and it obediently installed Sphinx 1.6.5.

Interesting. Looking at my Startup document I found I DID install sphinx last week: Sphinx 1.6.4. I wondered about that
because I just typed ``manage.py`` at the command prompt in the c17 environment but it claimed it could not import
Django. I just checked and django IS available in the c17 environment's ``Lib/site-packages`` folder. Maybe it was
because I haven't run the ``chmod`` command yet. Time for a

``chmod +x ./manage.py``

command...

Nope! It still claims it can't import Django. Here is the error message::

    ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment
    variable? Did you forget to activate a virtual environment?

That error message, I find, is printed within ``manage.py`` itself. Maybe I should check the PYTHONPATH environment
variable. But where do I find it?

According to an entry on stackoverflow I can find it by entering ``python -c "import sys; print('\n'.join(sys.path))"``
on the command line. I did and I got::

    C:\Users\frjam\Envs\c17\Scripts\python36.zip
    C:\Users\frjam\Envs\c17\DLLs
    C:\Users\frjam\Envs\c17\lib
    C:\Users\frjam\Envs\c17\Scripts
    c:\program files\python36\Lib
    c:\program files\python36\DLLs
    C:\Users\frjam\Envs\c17
    C:\Users\frjam\Envs\c17\lib\site-packages

It looks to me that Django is on my PYTHONPATH. I'll try installing Django again...

That didn't work either. First it wouldn't let me because it was already installed, but even after I deleted the django
directories from the ``ENV\c17\site-packages`` directory and re-installed django I still have the same problem.

I've read about what ``chmod +x .\manage.py`` does and it changes the mode of a file, in this case the manage.py file,
to make it executable -- and it is! Otherwise I wouldn't be getting the error message at all.

I could run manage.py by typing ``python manage.py`` and it indicated it could not find psycopg2, which is not
surprising since I have not installed it yet on this computer. Since it looks for psycopg2 in ``base.py`` and I believe
it goes through ``base.py`` in the ``__init__.py`` script as it imports Django, maybe that is the problem. It doesn't
seem so, though, since I have temporarily added a ``print("***************** Hey! I got here! *****************")``
line to that program and, though it executes when I type ``python manage.py`` it does not run when I just type
``manage.py``. I'll try installing psycopg2 and see what happens...

Still the same! Except ``python manage.py`` works now that psycopg2 is installed. It must be using some other python
when I use just manage.py. I wonder if I can find out which one. I suppose it may be the main installation of Python 3.6
in the ``C:\Programs`` directory. I will try installing Django there and see what happens...

I had to get into an administrator command prompt to do it, but nothing changed, even after I deactivated c17 and then
reactivated it, even after I exited the old command window and got into a new one. Perhaps the computer is using still
another version of Python -- like the one that runs Forty Thieves.

I think I have just figured it out. I installed Django in the global installation of Python 3.5 by typing:

``pip3.5 install django``

Then, in the c17 environment, I got the complaint about "No module named 'psycopg2'." The program line it was
complaining about came from the Python35 installation of django. So that's the default python that .py files use
when their chmod mode is set to allow execution. But I don't like it using a global python for that. Rather defeats
the purpose of having a virtual environment it seems to me if I have to install everything in the global version of
Python.

.. index:: manage.bat; creation

I think I will do better with a batch file in the Christmas 2017 directory::

    echo off
    python manage.py %1

Let's try that...

It seems to work! The only problem is that, at the end after I do a ``manage runserver`` it asks "Terminate batch job
(Y/N)?" I'd rather it didn't do that but it may be a function of using Ctrl-Break to get out of the server.

..index:: Database; creating on a second computer

Creating the Database on the Home Computer
++++++++++++++++++++++++++++++++++++++++++

Now I can try re-creating the database. Currently, starting the server and going to ``localhost:8000`` results, when I
try to log in, with an:

``auth.user`` does not exist error.

It also complained that I had 19 unapplied migrations. So I got into a separate c17 environment and ran:

``manage migrate``

Now, when I try to get into the local website it sends me to the login page and won't let me get off it. It knows no
users as of yet.

.. _loading-multiple-fixtures:

Now I will try:

``manage.py loaddata to_c17_user.json to_c17_gifts.json to_c17_mail.json to_c17_memory.json to_c17_question.json``

.. index:: manage.bat; rewrite

It worked after I added some more %n values to the ``manage.bat`` file. (After adding a %2 it accepted only the first
"fixture," so I added %2 through %9.) Now I can get into the website locally! It took almost a day but I'm finally at
the same point on both computers. Time for a commit.




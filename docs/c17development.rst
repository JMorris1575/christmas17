Developing the Christmas 2017 Website
=====================================

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

Switching to a New Database
+++++++++++++++++++++++++++

.. index:: Database; creating new

Creating the New Database
*************************

Again, checking the Christmas2016 documentation I was reminded how to create a new PostgreSQL database::

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

.. index:: Database; copying data

Copying Data to c17Database from c16database
********************************************

Microsoft Windows [Version 10.0.15063]
(c) 2017 Microsoft Corporation. All rights reserved.

C:\Users\frjam_000>c17

C:\Users\frjam_000>echo off
(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py makemigrations
Did you rename response.author to response.responder (a ForeignKey)? [y/N] y
You are trying to add a non-nullable field 'date' to question without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> This is a test question
Invalid input: invalid syntax (<string>, line 1)
>>> timezone.now
You are trying to add the field 'entered' with 'auto_now_add=True' to response without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>> timezone.now
You are trying to add a non-nullable field 'response' to response without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> Test Question
Invalid input: unexpected EOF while parsing (<string>, line 1)
>>> Test
Invalid input: name 'Test' is not defined
>>> "Test Question"
Migrations for 'question':
  question\migrations\0002_auto_20171024_2115.py
    - Change Meta options on question
    - Rename field author on response to responder
    - Add field date to question
    - Add field entered to response
    - Add field response to response

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, gifts, mail, memory, question, sessions, story, user
Running migrations:
  Applying question.0002_auto_20171024_2115... OK

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py user.json to_c17_gifts.json to_c17_memory.json to_c17_mail.json to_c17_question.json
Unknown command: 'user.json'
Type 'manage.py help' for usage.

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py loaddata to_c17_user.json
Installed 27 object(s) from 1 fixture(s)

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py loaddata to_c17_gifts.json
Installed 30 object(s) from 1 fixture(s)

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py loaddata to_c17_mail.json
C:\Users\frjam_000\Envs\c17\lib\site-packages\django\core\management\commands\loaddata.py:205: RuntimeWarning: No fixture data found for 'to_c17_mail'. (File format may be invalid.)
  RuntimeWarning
Installed 0 object(s) from 1 fixture(s)

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py loaddata to_c17_memory.json
Installed 14 object(s) from 1 fixture(s)

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>manage.py loaddata to_c17_question.json
Installed 13 object(s) from 1 fixture(s)

(c17) C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development\Christmas2017>

.. index:: Database; migrating

Initial Migration
*****************

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
Git Repository URL, left the Parent Directory at ``C:\Users\frjam\Documents\MyDjangoProjects``, and changed the
Directory Name to ``c17Development, then clicked the **Clone** button.

In order to write the paragraph above I had to get into the cloning dialog several times and noticed it was still set
to the c16 settings. I went to ``VCS > Git > Push...``, clicked on ``origin > Define Remote``, clicked ``OK`` and got
an error message:

``Couldn't add remote: remote origin already exists.``

Hmm... I seem to remember going through something like this last night just before pushing the website from my
Rectory computer. I think I had to change it in settings...

Nope, nothing there. Ah! Now I remember,
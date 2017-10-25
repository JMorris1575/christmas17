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

.. index:: Database; migrating

Initial Migration
*****************


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
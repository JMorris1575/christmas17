Startup Notes
=============

**Christmas 2017 Website -- Started on October 20, 2017**

This document chronicles the initial steps for developing the Christmas 2017 website. Little of the actual website will
be discussed here. That will be in another document: ``c17development.rst``.

Laying the Groundwork
---------------------

.. index:: python, virtual environment

Python and the Virtual Environment
++++++++++++++++++++++++++++++++++

On my home computer I checked to see which version of Python was installed. It is Python 3.6 and
I learned, by running

``mkvirtualenv c17``

that virtualenvwrapper was installed under Python 3.6 also.

The setup on the rectory computer was the same so I created the c17 environment there as well.

.. index:: Django; installing django

Installing Django
+++++++++++++++++

Once in the c17 environment I installed django with:

``pip install django``

and it installed django-1.11.6. I did the same on the rectory computer.

.. index:: sphinx

Installing Sphinx
+++++++++++++++++

While in the c17 environment I did a:

``pip install sphinx``

to install Sphinx. It installed version 1.6.4.

I commanded:

``sphinx-quickstart``

to enter the Sphinx 1.6.4 quickstart utility. I used **Christmas 2017** as the Project name and **Jim Morris** as the
Author name. I used the defaults for most of the entries except the one about **todo** entries and the one about
creating a **.nojekyll** file to publish the document on GitHub pages.

I later discovered that the **todo** entries do not apply to these ``.rst`` files but probably only ``.py`` files. I
changed the setting in docs\\conf.py to:

``todo_include_todos = False``

.. index:: PyCharm

Starting with PyCharm
+++++++++++++++++++++

I wanted to update this document and so I entered and updated PyCharm. I am currently running version 2017.2.3. Upon
entering PyCharm I started a new project by clicking ``File>New Project...``. In the dialog that appeared I browsed to
the existing Location: ``C:\Users\frjam_000\Documents\MyDjangoProjects\c17Development`` and browsed to
``C:\Users\frjam_000\Envs\c17\Scripts\python.exe`` to set the Interpreter. I clicked on the ``Create`` button and then the
``Yes`` button to let it know I wanted a project from the existing documents.

I will have to do the same on my home computer when I get back there.

.. index:: GitHub; new repository

Setting up on GitHub
++++++++++++++++++++

This was simple. I just signed in to my GitHub account and clicked on the New Repository button. I named the new
repository ``christmas17``, gave it a quick description ``The family Christmas website for 2017`` but did not add a
README file or do any of the other things that were suggested. When I am ready I will push the file from PyCharm.

Setting up the Django Project
-----------------------------

This section may be pointless. See the Cloning Option section below.

Initial Thoughts
++++++++++++++++

I'm thinking what I will need to do is to go to the command prompt, start the django project, then change the directory
structure to what it was for Christmas 2016. This can be done in PyCharm along with the changes necessary within a
couple of the python files. This is outlined in the startup notes in the Christmas 2016 documentation files.

.. index:: Django; creating the project

Creating the Django Project
+++++++++++++++++++++++++++

In a regular command prompt (not administrator), I got into the c17development directory and issued the command:

``django-admin startproject Christmas2017``

In PyCharm I used Refactor to change the inner ``Christmas2017`` directory name to ``config``. It automatically found
the references in ``manage.py``, ``settings.py``, and ``wsgi.py`` that needed changing but also found three lines
in ``docs/conf.py`` that DIDN'T need changing. In the Refactoring Preview pane I clicked on ``docs`` and pressed
``Delete``. It complained about the code changing and made me "search again" but, when I highlighted the individual
files and clicked ``Delete`` for each one it did the refactoring properly.

In the command prompt window I switched to the Christmas2017 directory and entered:

``python manage.py runserver``

Upon going to ``localhost:8000`` in the browser I got to the "It worked!" page. Yay!

.. index:: chmod, c17.bat

Making My Life Easier
+++++++++++++++++++++

I remembered there was some way to simplify the command to just ``manage.py`` and I found a reference to it in the
documentation for BnB notes. This command should do it:

``chmod +x ./manage.py``

and it worked! I tried to learn more about the ``chmod`` command, specifically, what the ``+x`` did and why I used
``./`` in front of the ``magage.py`` but that information may be in the Test Driven Development book and I haven't
looked it up yet.


Also, I want to create a c17.bat file with the proper contents to more easily get to the right directory with the
proper environment variable set and in the proper virtual environment. Looking at ``c16.bat``, I created a batch file
named ``c17.bat`` as follows::

    echo off
    cd "Documents\MyDjangoProjects\c17Development\Christmas2017"
    set DJANGO_SETTINGS_MODULE=config.settings.dev
    workon c17

I used Notepad++ to create the file (copied and pasted the above) and saved it in ``C:\\Users\\frjam_000`` on the
rectory computer. It worked perfectly.

But now I'm wondering just what that environment variable does. I'm too tired right now to figure it all out but,
according to the notes in last year's ``startup.rst`` it may have something to do with separating development and
production settings.

.. index:: directory structure

Directory Structure
+++++++++++++++++++

Here is the directory structure I established based on last year's::

    \-MyDjangoProjects
     |-(other_projects)
     \-c17Development
       |-.gitignore
       |-requirements.txt
       |-docs
       \-Christmas2017
         |-manage.py
         |-templates
         \-config
           |-__init.py__
           |-settings.py
           |-urls.py
           \-wsgi.py

Starting Version Control
++++++++++++++++++++++++

.. index:: Database; changing to PostgrSQL

Changing the Database
+++++++++++++++++++++

.. index:: clone

Cloning Option
--------------

Introduction
++++++++++++

It occurred to me that starting a new Django project and then copying all the files to it may not be the way to go.
Maybe I can clone the Christmas 2016 files from GitHub and start from there.

Backing Things Up
+++++++++++++++++

I want to back up what I have done so far just in case so, outside of PyCharm to avoid it's refactoring,
I will rename the ``Christmas2017`` folder to ``Christmas2017BAK`` and then try to clone the ``Christmas2016``
website from GitHub.

Performing the Clone
++++++++++++++++++++

Under the VCS menu I selected ``Enable Version Control Integration`` and selected ``Git`` as my version control
system.

Then I was able to select ``VCS>Git...>Clone...`` and enter

``Git Repository URL: https://github.com/JMorris1575/christmas16``
``Parent Directory: C:\Users\frjam_000\Documents\MyDjangoProjects``
``Directory Name: christmas16``

This created a new folder named ``christmas16`` in the ``MyDjangoProjects`` directory which is not what I wanted. I
should have entered ``c17Development`` for the ``Directory Name``. However, I noticed that the ``christmas16`` folder
included the ``docs`` folder which I don't want to overwrite. I will rename it, clone the files, delete the new ``docs``
folder, then rename the original back to ``docs``. Here goes...

It did not allow me to clone to the existing c17Development folder. I will rename that folder then try again...

This time it worked, but upon renaming the folder PyCharm lost track of it, of course and asked me to open the newly
cloned folder. I did this and, after having to wait for PyCharm's lengthy indexing process, was able to drag and drop
the ``docs`` folder to ``c17Development`` but that actually MOVED the folder instead of copying it so I will copy it
back to ``c17DevelopmentBAK`` just to be safe.

Done!

.. index:: Database; Installing psycopg2

Testing the Local Website
+++++++++++++++++++++++++

Now to see if the website is working locally...

It did not. At first the problem was that it couldn't find ``secrets.json`` since that file was, sensibly, not in my
GitHub repository. After copying it over from ``c16Development`` the new problem was that it could find "no module
named psycopg2" which, of course, it couldn't because I haven't installed that module in the ``c17`` virtual
environment as yet.

Studying the Christmas2016 documentation::

    I got into the c16 environment and tried a migrate (manage.py migrate). It complained about an Error Loading
    psycopg2 which I should have expected. As explained in BnBNotes preliminaries.rst, I went to:

    ``http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg``

    and downloaded:

    ``psycopg2-2.6.2-cp35-cp35m-win_amd64.whl``

    and copied it to the c:directory. In the c:directory I typed:

    ``> pip install psycopg2-2.6.2-cp35-cp35m-win_amd64.whl``

    and it installed successfully. Trying a migrate again succeeded and I could open the website at localhost:8000.

    [Note: the cp35 in two positions in the psycopg2 filename indicates python 35. Be sure to download the version for
    the version of python you are using.]

I went to ``http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg`` and downloaded:

``psycopg2-2.7.3-cp36-cp36m-win_amd64.whl``

this was after checking that I had an AMD processor in this computer (the rectory computer) by going to
``Computer>System properties``.

Upon doing a:

``> pip install psycopg2-2.7.3-cp36-cp36m-win_amd64.whl``

and the 2016 Christmas website seems to be working!

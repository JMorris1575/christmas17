Starting the Project
====================

Creating the Virtual Environment
--------------------------------

The Christmas 2016 project was started on my rectory computer. I used the administrator version of the Windows 10
command prompt, which opens in C:\Windows\System32. I'm not sure it was necessary to use the administrator version to
create a virtual environment. I should try the regular version of the command prompt when I create the environment
on my home computer. [See note below.]

I typed the command::

    > mkvirtualenv c16

which created the virtual environment using Python 3.5

[**Note:** I did need to use the administrator version of the command prompt. It gave me a "PermissionError." I think
it may be because I was changing things in the Program Files/Python35 folder on the whole computer -- rather than just
in a virtual environment. I did have a little trouble before that however. Typing::

    > mkvirtualenv c16

it said it was using Python 3.4 for it's base. I discovered that, although both Python35 and Python34 appeared in the
path environment variable, virtual environment and virtual environment wrapper had never been installed for Python 3.5.
I ran::

    > pip install virtualenvwrapper-win

and, once I was using the administrator version of the command prompt, it installed both virtual environment and virtual
environment wrapper.]

Install Django
--------------

I got out of the administrator version and opened a regular version of the command prompt. Once entering into the
c16 virtual environment I typed::

    > pip install Django

which collected and installed Django 1.10.2.

[**Note:** I had no problem repeating this on the Kalamazoo computer. I also created the batch file ``c16.bat`` to cd to
the ``C:\Users\frjam\Documents\MyDjangoProjects\c16Development\Christmas2016`` directory.]

Creating the Django Project
---------------------------

I plan on using a project structure similar to the following (based on section 3.3 of Two Scoops of Django")::

    \-MyDjangoProjects
     |-(other_projects)
     \-c16Development
       |-.gitignore
       |-requirements.txt
       |-docs
       |-readme.md
       \-Christmas2016
         |-manage.py
         |-templates
         \-config
           |-__init.py__
           |-settings.py
           |urls.py
           \-wsgi.py

To accomplish this I used the command prompt to enter into the c16Development directory and ran the command::

    > django-admin startproject Christmas2016

and renamed the inner Christmas2016 directory to config.

Using Sphinx
------------

To create this document I followed the instructions on www.sphinx-doc.org/en/stable/tuturial.html. Sphinx is already
installed on this computer so I simply ran::

    > sphinx-quickstart

while in the c16Development directory. I used all the defaults except for saying 'y' to the "autodoc" extension as
recommended in the sphinx-doc tutorial. I added this document to the ..toctree:: as follows::

    Contents:

    .. toctree::
       :maxdepth: 2

       startup.rst

Then, moving to the c16Development/docs directory I ran the following command::

    make html

Later I will play with the conf.py document to give the documentation its own personality.

[Note: I settled on using the alabaster theme (the default) with some html_theme_options and an html_logo set in
the conf.py file.]

[**Note:** Spinx was also installed on the Kalamazoo computer so, after updating this file, I tried to use ``make html``
but got::

    Theme error:
    unsupported theme option 'fixed_sidebar' given

After deactivating the c16 virtual environment, and learning (again) that I had to be in the administrator version of
the command prompt, I upgraded sphinx via::

    > pip install --upgrade sphinx

I noticed that the upgrade included alabaster 0.7.9, among other things, and, when I ran ``make html`` again it worked
properly. I should probably upgrade sphinx on the rectory computer also.]

Testing the Website
-------------------

Changing the name of the inner Christmas2016 directory to config means that a couple of changes need to be made.  First,
in manage.py::

    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

Then, in wsgi.py::

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

To test the website I typed::

    > manage.py runserver

but I got an error::

    ImportError: No module named 'Christmas2016'

I found the following entry in the settings file::

    WSGI_APPLICATION = 'Christmas2016.wsgi.application'

and changed it to::

    WSGI_APPLICATION = 'config.wsgi.application'

but it gave me the same ImportError.

In the settings file there was also an entry::

    ROOT_URLCONF = 'Christmas2016.urls'

so I changed that to::

    ROOT_URLCONF = 'config.urls'

and it worked! Going to http://localhost:8000/ got me to the Welcome to Django page.

The ROOT_URLCONF and the WSGI_APPLICATION settings were also present in the settings.py file in Django 1.8 so I'm
guessing I just forgot to mention them when I was writing the BnB_Development preliminaries.rst file on which this
work is based.

.. _setting_env_variables:

[**Note:** When I tried to run ``manage.py runserver`` on my home computer I got::

    ImportError: No module named 'config.settings.dev'; 'config.settings' is not a package

After digging through the stack trace I learned that it was getting ``config.settings.dev`` from the ENVIRONMENT_VARIABLE.
I remembered setting this while working on *Task Driven Development* and wanted to look there to see how to reset it but
alas, I apparently didn't keep notes like this while I was working on that. (Yes I did. They turned up in my BnB notes.)
After a lot of mucking around and trying various things I learned that my ``c16.bat`` file was setting it -- DUH! I had
copied it without thinking from the ``bnb.bat`` file.  When I tried, again, to run the server I now got a psycopg2 error.
After pip installing it in the c16 virtual environment and using pgAdminIII to create the c16database I was finally
able to run the server.]

Changing the Database to PostgreSQL
-----------------------------------

PosgreSQL 9.5 was already installed on this computer (my rectory computer) and so all I had to do was

#. Open pgAdminIII.

#. Double-click ``PostgreSQL 9.5`` and enter the password (Dylan Selfie).

#. Right click Databases and select ``New Database...``

#. Add the name (I chose c16database).

#. Select an Owner (I selected Jim).

#. Update the settings.py file to include::

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'c16database',
        'USER': 'Jim',
        'PASSWORD': 'DaysOf49',
        'HOST': '127.0.0.1',
        'PORT': '5432'
        }
    }

Before you store this project on github you will want to settle on a means of keeping the secrets from the general
public.

I got into the c16 environment and tried a migrate (``manage.py migrate``).  It complained about an Error Loading
psycopg2 which I should have expected. As explained in BnBNotes preliminaries.rst, I went to:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg

and downloaded:

``psycopg2-2.6.2-cp35-cp35m-win_amd64.whl``

and copied it to the c:\ directory. In the c:\ directory I typed::

    > pip install psycopg2-2.6.2-cp35-cp35m-win_amd64.whl

and it installed successfully. Trying a migrate again succeeded and I could open the website at localhost:8000.

[Note: the cp35 in two positions in the psycopg2 filename indicates python 35. Be sure to download the version for
the version of python you are using.]

Keeping Secrets
---------------

Looking into the information in chapter 5 of *Two Scoops of Django* I learned that the Apache server, such as is
used on webfaction.com, prevents the use of environment variables to store secrets. It suggests what it calls the
**secrets file pattern.** It says::

    "To implement the secrets file pattern, follow these three steps:
        1. Create a secrets file using the configuration format of choice,
           be it JSON, Config, YAML, or even XML.
        2. Add a secrets loader (JSON-powered example below) to manage the
           secrets in a cohesive, explicit manner.
        3. Add the secrets file name to the .gitignore or .hgignore."

I tried it, saving the SECRET_KEY as well as the DATABASE_NAME, USER, PASSWORD, HOST and PORT in a ``secrets.json`` file,
and it worked! I have to remember, tough, to add all the other secrets, such as e-mail configuration, to the
``secrets.json`` file.

Separating Development and Production Settings
----------------------------------------------

For the time being, at least, I think all I have to do to separate development settings from production settings is:

#. Create a module named settings in the config directory creating a blank __init__ file.

#. Move the existing settings.py and secrets.json files to that directory, renaming settings.py to base.py.

#. Change the ``with open`` line in base.py to say ``with open("config/settings/secrets.json") as f:``

#. Create a dev.py file and a prod.py file for development and production respectively. The only difference for now
   is the DEBUG setting. In dev.py it should be DEBUG = True, in prod.py it should be DEBUG = False.

#. Insert a line in dev.py and prod.py saying ``from .base import *``

#. Modify the c16.bat file to include ``set DJANGO_SETTINGS_MODULE="config.settings.dev"`` again.
   :ref:`(See note on Testing the Website above.) <setting_env_variables>`

Initializing Version Control
----------------------------

I've decided to use git from the command line instead of using it through PyCharm. I hope to learn it better and avoid
some of the problems I have had when using it through PyCharm. I am downloading the most recent version of Git, version
2.10.1 64-bit and will install it afterward. Looking at Chapter One of the book *Pro Git*, I learned a little about
``git config``. I can list all the configuration variables by typing::

    > git config --list

Doing so I saw these at the end::

    core.editor=notepad
    user.name=JMorris157
    user.email=FrJamesMorris@gmail.com

According to *Pro Git* the user name and e-mail are used in every commit, and the core.editor is the default text
editor. I changed it to Notepad++ by typing the following::

    > git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe -multiInst -nosession"

(I had to use the online version of ProGit, accessed through git-scm.com/book/en/v2/Getting-Started_First-Time-Git-Setup
since the command line ran off the end of the page in the pdf file.)

To start using git on Christmas2016 I typed the following in the command line set to the c16 virtual environment and
having cd'd to the ``C:\Users\frjam\Documents\MyDjangoProjects\c16Development directory`` ::

    > git init
    > cd docs
    > git add conf.py
    > git add index.rst
    > git add startup.rst
    > cd ../Christmas2016
    > git add manage.py
    > cd config
    > git add __init__.py
    > git add urls.py
    > git add wsgi.py
    > cd settings
    > git add __init__.py
    > git add base.py
    > git add dev.py
    > git add prod.py

I must admit, PyCharm's method is easier -- although git's own GUI might be of assistance here too.

PyCharm had a nice method of adding untracked files to .gitignore. When I created the .gitignore file in the
``c16Development`` directory, it asked me if I wanted to add the untracked files. When I agreed, it did -- very nice!

I went to github.com and created a christmas16 repository, clicked on the New Repository button, did NOT add a readme.md
file, then followed their instructions for pushing an existing repository from the command line::

    > git remote add origin https://github.com/JMorris1575/christmas16.git
    > git push -u origin master

This asked for my username and password (JMorris1575, pet_kzoo) and seemed to work perfectly. Now I will try to
"Enable version control integration" in PyCharm and commit and push the changes that have taken place in this file.

It worked! . . . but now I have to do it again.

Getting my Rectory Computer Up To Date
--------------------------------------

First I tried a ``git clone https://github.com/JMorris1575/christmas16`` after typing ``> c16`` and that resulted in
the project being placed in the Christmas2016 folder in a folder named for the github repository: ``christmas16``.

I didn't notice until I tried to build these documentation files on the rectory computer and it told me there was
nothing to change. I may have tried to get PyCharm to synchronize its Version Control System and do a pull but, of
course, that didn't change anything either.

When I noticed my mistake I erased the ``christmas16`` folder from the ``Christmas2016`` folder and tried another clone
to the ``c16Development`` folder. That, of course, copied a ``christmas16`` folder into the ``c16Development``
directory. I moved it to the desktop, copied its contents to the ``c16Development`` folder, and PyCharm gave me some
error about the git configuration. I clicked configure but it didn't seem I could do anything. I initialized PyCharm's
Version Control System and, I hope, all will work well now. At least it indicates that secrets.json and settings.py
(which shouldn't be there any more) are not included in version control.

I've just copied secrets.json to the ``config/settings`` folder. It makes sense that it wasn't there before because it
is NOT included under version control. I also deleted the extra ``settings.py`` which is now in
``config/settings/base.py``.

Otherwise, things seem to be working as they should. I just made some changes in the ``planning.rst`` file and ``git
status`` tracked them properly -- along with the changes in this file.

Wow! It even reverts back to 'unchanged' when I delete the new section!

A Commit Changes... and a Git/Push... both worked!

Building this documentation, however, showed me that I have not put PoinsettaCandles.png under version control so it
wasn't copied in the clone. I've copied it now, and put the ``docs/_static`` folder under version control (I think) so
I'll have to see if it takes.

Ah, now I remember! I put ``docs/_static`` into the ``.gitignore`` file because the image for the docs will probably be
stored in the main program's static folder.

Upgrade to Django 1.10.3
------------------------

On November 9, 2016, I upgraded to Django 1.10.3 on my computer in Kalamazoo.  This was as I kept getting "Programming
Errors" in django code when trying to delete what I thought was going to be a temporary user.  I still haven't deleted
it.  I did enter myself, so I could just leave it in and use it or I could try to delete it through pgAdminIII.









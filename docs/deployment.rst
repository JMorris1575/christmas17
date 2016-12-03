Deploying the Website
=====================

Hmm... I created this file yesterday, and added a title exactly like the above. I did a ``make html`` and it created
a ``deployment.html`` file in the ``_build`` directory. But, when I got back into PyCharm this morning there was no
sign of ``deployment.rst`` anywhere -- not in any of my Git branches, not on GitHub, not in the c16Development
directory on my hard drive. Strange! I don't know what might have happened. I just recreated the file to start over.
Fortunately, the title is all it contained.

Overall Plan
------------

Here are my initial thoughts as to the steps to follow to deploy the website:

#. Experiment with the static files to see how they can be served by a separate static app.

#. Study Webfaction's documentation to see how to include e-mail.

#. Study Migrations and whether or not the ``migrations`` directory for each app should be included in version control
   and on the server.

#. Make a list of what directories and files should be transferred to the server.

#. Use FileZilla to make the transfer.

#. Test the Website.

#. Send the invitation e-mail (find out if Scott's significant other & family will be there on Christmas.)

Stupid Mistake
--------------

What was I thinking? I put a list of everyone's usernames, passwords, e-mails, first and last names in the
``building.rst`` on GitHub! I'm not sure how to remedy that. I may have to start a whole new remote repository, branches
and all, and delete the current one. That shouldn't be too bad since I really don't intend to revert anything back to a
former state.

I ended up having to:

#. Delete the christmas16 repository on GitHub and then add it in again to blank it out.

#. Backup the c16Development directory then delete .idea, .git and .gitignore.

#. Re-open ``c16Development`` in PyCharm, set up version control again, set the connection to GitHub in settings, then
   do a push.

#. I had to update the database with the new user information and the new gift information but the latter, at least, I
   would have had to do anyway.

#. I may still be able to salvage the work I've done on the ``css_work`` branch and the (non-existent) work I've done on
   the ``new_features`` branch. It may not be worth it, though. Perhaps I should wait until I'm ready to work on them
   anew.

By the way, it seems changing the app names in the middle of the game has caused some problems. I can't just do a
``manage.py loaddata c16data.json`` because it contains some references to ``gift_exchange.gift`` which it says
already exists. Be careful about that in the future!

Serving Static Files
--------------------

Webfaction wants static files collected and served from a separate static application that is in the same ``webapps``
directory as my website. Thus, it seems to me, that setting STATIC_ROOT to something like:

``os.parent(BASE_DIR)/<static_app_name>/`` might just do it. First, some experiments to see if I've got the Python
correct:

Here is the line that worked in the ``dev.py`` file:

``STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_collection')``

When I ran ``manage.py collectstatic`` the system obediently collected all my static files in the ``static_collection``
directory next to the ``Christmas2016`` directory. Unfortunately, however, none of the static files were served from
there.

I could get it to SAY it was getting files from there if I changed the ``STATIC_URL`` to:

``STATIC_URL = '/c16Development/static_collection/'``

But it still seemed to be getting the files from the apps themselves. Perhaps I will only be able to deal with this
when I get to actual deployment.

Adding E-mail
-------------


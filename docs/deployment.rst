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
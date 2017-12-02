=====
Notes
=====

This file is for various notes I think of as I am developing the website. The hope is that I will have a place to look
when I have the same problems in future projects.

.. index:: Problems; question app migrations

Recovering from a failed migration
----------------------------------

I neglected to include all of the migrations for the question app in git so, when I tried a migrate here on the rectory
computer, it failed. I tried a makemigrations --merge, as PyCharm suggested, but that didn't work either. I just deleted
all the migration files from the question/migrations folder, ran makemigrations, and then migrate worked.

.. note::
    **Remember to do the same on the Home Computer!!!!!**

.. index:: Workflow

Suggested Workflow when Changing Computers
------------------------------------------

I find a good pattern to follow when moving from one computer to another is to:

#. Do a Git pull
#. Do a migrate
#. Do a loaddata with any json files from the other computer


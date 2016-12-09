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

#. Use Webfaction's control panel to create new webapps - one for Christmas2016, one for
   ``c16_static``.

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

Copying the Revised Files to my Kalamazoo Computer
++++++++++++++++++++++++++++++++++++++++++++++++++

What I finally ended up doing was to make a backup of the c16Development directory, erase all the files in the original
``c16Development`` directory, then do a ``git->clone...`` from the VCS menu. I had to make sure it went to the
``Documents/MyDjangoProjects`` directory, and make sure the directory name was ``c16Development``. I had to copy
``secrets.json`` from my Rectory computer and decided to copy ``c16_datadump.json`` from there too. To get sphinx to
work I decided to copy the following::

    _build
    _static
    _templates

from my backup of ``c16Development``. Doing ``manage.py runserver`` allowed me to get into the local version of the
website and running ``make html`` worked but warned me that this file ``deployment.rst`` and ``private.rst`` aren't
in any toctree. I don't think I put them there but I will now.

I did, and all seems well.

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

I watched the video linked to from my home page at webfaction and opened a ticket (FRQ-636108) about re-enabling, or
deleting, my old, compromised, morrischristmas mailbox. Their support personnel will get back to me "shortly."

Wow! Webfaction is really good! Mary H. had probably responded to me while I was writing the above. She restated the
instructions I had been given before::

    Hello Jim,

    > My morrischristmas mailbox had to be disabled last June because it had been compromised.  I'm glad you caught
    that but I couldn't correct it at the time and now I can't find the instructions.  How do I either re-enable that
    mailbox or delete it?

    The message we sent previously contained this text:

    ***
    This message is concerning your "jmorris" hosting account with WebFaction.
    Today we noticed a very high volume of spam messages being sent from your "morrischristmas" mailbox. An example is
    attached.

    It is very likely that your mailbox password has been compromised and that spammers are using your mailbox to relay
    spam emails to other users on the Internet.

    To prevent further abuse, we've taken the following actions:

    - Reset the mailbox password to a random value.

    - Disabled SMTP access for the mailbox so that no further mail can be sent.

    If you would like us to re-enable SMTP access for the mailbox, then please scan your local systems for viruses and
    other malware, since those are common methods for stealing passwords.

    Once you have verified that your systems are clean, let us know and we'll then re-enable the mailbox.

    Once it has been re-enabled, you can reset your mailbox password via our control panel. When you do, please be
    sure to use a random password that cannot be easily guessed. We have some information about strong passwords at
    http://docs.webfaction.com/user-guide/passwords.html
    ***

    Please let us know if you need anything else.

    Regards,

    Mary H.
    WebFaction Support
    --
    WebFaction - Smarter web hosting
    http://webfaction.com
    http://twitter.com/webfaction - http://facebook.com/webfaction

I did as the instructions said, both here on the rectory computer on, through TeamViewer11, on my home computer and
they have re-enabled the mailbox. I'm using a new password I will put in secrets.json. I haven't yet read the material
at http://docs.webfaction.com/user-guide/passwords.html but I will and, possibly, change the password again.

Configuring Django
------------------

This section of Webfaction's documentation has a number of things I need to know:

https://docs.webfaction.com/software/django/config.html

Here is a summary:

#. How to set up a static media application to serve static files.

#. Configuring the ALLOWED_HOSTS setting.

#. Configuring Django to use Memcached (which I don't think I'll do.)

#. Configuring Django to Send Mail.

#. Configuring Django's Time Zone.

#. Mounting a Django Application on a Subpath (whatever that means).

#. Password Protecting a Django Application. (From family members using it or from people accessing webfaction?)

#. Restarting a Django Application.

#. Setting Up a Database. (Including a link to creating a new database.)

#. Upgrading your Django Libraries. (In case the version provided is not up to date? Can't I use pip install?)

#. Using the Latest Django Trunk. (Not something I'm likely to want to do.)


In playing with number 1 above I discovered what works in development to serve static files from a collected location::

    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_collection')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static', 'site'),
                        'c:/Users/frjam_000/Documents/MyDjangoProjects/c16Development/static_collection', )

I don't really want to do that during development, though, so I will delete ``static_collection``.

To configure Django to send mail I entered the required information::

    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = '<mailbox>'
    EMAIL_HOST_PASSWORD = '<password>'
    DEFAULT_FROM_EMAIL = '<address>'
    SERVER_EMAIL = '<address>'

into ``secrets.json`` and placed the following into ``prod.py``::

    EMAIL_HOST = get_secret('EMAIL_HOST')
    EMAIL_HOST_USER = get_secret('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = get_secret('DEFAULT_FROM_EMAIL')
    SERVER_EMAIL = get_secret('SERVER_EMAIL')


Getting Old Christmas Website to Work
-------------------------------------

I wanted to keep last year's Christmas website online, at least for a while until I can decide what to do with it, so I
fiddled around on the Webfaction Control panel to move it to the url:  christmas15.jmorris.webfactional.com.

It seemed to be working, but I didn't look closely enough. I was getting the "Bad Request Error" page.

I found a couple of settings in the base.py file and the production.py file through FileZilla and updated them to
christmas15.jmorris.webfactional.com.

I thought it might be that I just had to restart the server, as I sometimes have had to do during development, so I
tried to SSH into my webfactional site with:

``ssh jmorris@Web419.webfactional.com`` as it says at https://docs.webfaction.com/user-guide/access.html#ssh but I only
got ``ssh: Could not resolve hostname web419.webfactional.com: Name of service not known`` I thought it might be because
ssh doesn't work on Windows without using PuTTY so I downloaded the ``putty-0.67-installer.msi`` from
http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html and installed it.

Before I tried it, though, I noticed I had not actually followed the instructions. I was supposed to enter
``ssh jmorris@Web419.webfaction.com`` (note: ``webfaction``, not ``webfactional``. Just for fun, I tried that first at a
command prompt and, ignoring the authenticity warning, was able to get into the site without using PuTTY. Hmm... I'm not
sure why, but maybe later I'll find out.

It seemed to take the ``webapps/christmas15/apache2/bin/restart`` command without complaint and the old website now
seems to be working at the new URI.

Setting Up the New Webapp
-------------------------

I would like the file structure on webfaction to be as follows::

    webapps
    \
     |-c16_static
     |-Christmas2016
     \
      |-apache2
      |-bin
      |-config
      |-gifts
      |-mail
      |-memory
      |-question
      |-static
      |-story
      |-templates
      |-user
      |-manage.py
      |-model_mixins.py
      |-utils.py
      |-temporary json files to copy database

I should be able to do that by creating the Christmas2016 webapp through Webfaction's control panel but I will try to
find a tutorial first. There was a link on the dashboard entitled *Getting Started with Django on Webfaction*. Here is a
summary of the instructions and the results::

    Get into control panel
    Click Domains/Websites
    Click Websites
    Click Add new website
    Enter the name of the website (he used "my_django_site"
    Choose a domain name (in my case christmas.jmorris.webfactional.com)
    Click Add an application
    Click Create a new application
    Give the django application a name (he used "django_demo")
    Choose Django under App category
    Select the version of Django, and Python, you want to use
    Click Save to create the application
    Click Save again to create the website

    The file structure he got was:

    webapps
    \
     |-django_demo
     \
      |-apache2
      |-bin
      |-lib
      |-myproject
      |\
      | |-myproject
      | \
      |  |-settings.py
      |-manage.py

    Looking at the ``mvpland1`` site that I still have on Webfaction I see it has a similar structure:

    webapps
    \
     |-mvpland1
     \
      |-apache2
      |-bin
      |-lib
      |-src
      \
       |-newsletter
       |-static_in_pro
       |-templates
       |-trydjango18
       |\
       | |-settings
       | \
       |  |-init.py
       |  |-base.py
       |  |-production.py
       |-manage.py

    So it seems to me that I should use this file structure instead:

    webapps
    \
     |-c16_static
     |-c16
     \
      |-apache2
      |-bin
      |-lib
      |-Christmas2016
      \
       |-config
       |-gifts
       |-mail
       |-memory
       |-question
       |-static
       |-story
       |-templates
       |-user
       |-manage.py
       |-model_mixins.py
       |-utils.py
       |-temporary json files to copy database

    I can do this by using ``c16`` as the application name and anything I want (``christmas16``?) as the website name.
    Then I can change ``myproject`` in the ``.conf`` and ``.wsgi`` files to ``Christmas2016`` and/or
    ``Christmas2016.config`` and copy all the appropriate files over.

I will try that. Now to copy the files...

Files copied, ``httpd 2.conf`` changed, server restarted, and I got an Internal Server Error, probably because of a
misconfiguration of the site. Do I have my database hooked up? Should be according to the settings in ``prod.py`` and
``secrets.json``. Does it read in ``prod.py``? I don't think it was, so I changed one line in
``c16/Christmas2016/config/wsgi.py`` to:

``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")``

restarted the server but got the same Internal Server Error. The ``wsgi.py`` file suggests studying this:

https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/

so I will . . .

He showed that the static application had to be added when creating the website, so I added it to ``christmas16``. I
couldn't have it served by ``christmas.jmorris.webfactional.com`` so I chose
``christmas_static.jmorris.webfactional.com``. Restarting the server I got the same Internal Server Error. Continue
with the video...

Deployment Problems
-------------------

I kept getting the Internal Server Error until I finally was able to run ``python3.5 manage.py migrate``. I was able to
run that because I changed the line in ``manage.py`` that said:

``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")`` to
``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")``. I made a similar change in the ``wsgi.py``
file. I don't know why this is necessary. I didn't have to do that last year.

I just found out. Last year the ``__init__.py`` file in the configuration directory (called ``christmas15``) included
these lines::

    from .base import *

    try:
        from .local import *
    except:
        pass

    try:
        from .production import *
    except:
        pass

I can do something similar this year and avoid having to make changes to ``manage.py`` and ``wsgi.py``.

For now, though, I decided not to do that. I want to figure out where it came from and whether that is the best way to
do it. Perhaps *Two Scoops of Django* will give me some guidance since that is where I got the idea for the directory
structure I'm using.

Here is a temporary solution. In ``config/settings/__init__.py`` enter the following::

    """
    This is a rather klunky solution to the problem of how to use different settings files on different servers.
    Uncomment the appropriate line according to which machine is being used.
    On the development machine, use dev.py, on the production machine, use prod.py
    """

    from .dev import *

    # from .prod import *

That, hopefully, will select the correct file in each appropriate setting. I also changed the appropriate lines in
``manage.py`` and ``wsgi.py`` back to ``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")``.

Collecting the Static Files
---------------------------

After some messing around, I discovered that ``STATIC_ROOT`` needed to be set as follows:

``STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'c16_static')``.

Now I can get to the login page but nowhere else. I imagine it's because I need to copy my database information over
to the ``c16database`` online.

Copying the Database to Webfaction
----------------------------------

I tried to use ``pgAdminIII`` to delete the ``gift_exchange`` table reference but, upon doing
``manage.py dumpdata > c16_datadump.json`` it still appeared in the ``.json`` file, along with the output of some
debugging print statements I had in the ``config/settings/base.py`` file. I got rid of the print statements, and looked
again with ``pgAdminIII`` for any remnants of ``gift_exchange`` and tried again. (Note: I did perform a VACUUM on a few
of the tables as recommended when I clicked the table under ``c16database/Schemas/public/tables/`` or perhaps that box
popped up when I clicked on the View Data button.) The entry:

``{"model": "contenttypes.contenttype", "pk": 7, "fields": {"app_label": "gift_organizer", "model": "gift"}},``

was still  there but I will try to use it to ``python3.5 loaddata c16_datadump.json`` on the Webfaction server. (After
modifying ``config/__init__.py`` of course and copying over the most recent versions of the ``manage.py`` and
``wsgi.py`` files.

It didn't work. This time the problem was ``DETAIL: Key (app_label, model)=(admin, logentry) already exists.``

So I will have to load all the .json files with a:

``python3.5 manage.py loaddata user.json userprofile.json gifts.json memories.json``.

Hurray! The website seems to be working!

Last Minute Fixes and Improvements
----------------------------------

#. The Add Memory button should only appear for authenticated users.

#. There should be a special page for login errors instead of just going back to the login page without explanation.

#. There should be default files for all the possible html errors.

#. I need to check to see if the e-mail is actually working.

Here are the results of the above:

#. This one was easy. I just had to put a {% if user.is_authenticated %} ... {% endif %} block around the memory
   section.

#. This took a bit more effort. I had to create a ``login_error.html`` page, change a couple url patterns (see below)
   and write a new view (see below).

#. I created default html files for 400, 403, 404 and 500 errors, just as I did last year. These were placed in
   Christmas2016/templates.

#. I will try to send myself the invitation e-mail . . . it did not work. I got a "Server Error (500)" I will have to
   work on this tomorrow.

Here are the changes to ``user/urls.py``::

    url(r'^login/$',
        auth_views.login,
        {'template_name': 'user/login_error.html',
         'redirect_authenticated_user': True },
        name='login'),
    url(r'login/error/$',
        LoginError.as_view()),

And here is the new view that was required in user/views.py::

    class LoginError(View):
        template_name = 'user/login_error.html'

        def get(self, request):
            return render(request, self.template_name, {})

Getting Mail to Work
--------------------

When I tried to send an invitation to myself I got a "Server Error (500)." I didn't know why. Unknown to me, at first,
was that an error log was sent to me at jmorris@ecybermind.net. (It will be good to figure out if this is something from
a django settings file or if it came from me having a superuser account.

After mucking around for a while, and looking at the error message in the e-mail, I've decided that the problem is that
I am attempting to get ``invitation.txt`` from the folder it is in, ``jmorris/webapps/c16_static/mail/`` but that is
being served by the static-only server, or that one app is simply not allowed to reach into another one to get files.

In either case, I have decided to copy ``invitation.txt`` to a folder accessible to ``Christmas2016/mail/views.py``. I
will create a folder named ``mail_templates`` and put it there then figure out how to find it from the SendInvitation
view.

Trying it locally worked. The invitation e-mail was displayed on the console running ``runserver``. Now to try it
online and ... I still got "Server Error (500)." Checking my e-mail and found:

``No such file or directory: 'http://christmas.jmorris.webfactional.com/static/mail/invitation.txt'``

even though this line:

``msg_file = open('mail/mail_templates/invitation.txt')`` is in the ``views.py`` file.

Nothing I tried ever got that to work so I searched the web for ``how to open txt files from a django view`` and
didn't come up with much either.

In the meantime I thought of putting ``invitation.txt`` into a model in the ``mail`` app and accessing it that way.
Thus, I created the following model::

    class EmailTemplate(models.Model):
        name = models.CharField(max_length=15, blank=False)
        template = models.TextField()

        def __str__(self):
            return self.name

referred to it in ``mail.admin.py`` as follows:

``admin.site.register(EmailTemplate)``

and tested it out on a development machine. I had to ``makemigrations`` and ``migrate`` of course but with all the
changes involved with correcting my mistake of listing everyone's e-mails and passwords above, and possibly from
having changed the names of some existing model fields, I was having trouble with ``makemigrations``. I decided to
delete all previous migrations and start anew with ``manage.py makemigrations`` and ``manage.py migrate``. It all seemed
to work.

Once I use django's ``admin`` app to enter an ``invitation`` EmailTemplate I tried it on the development machine and it
worked. I copied everything over to the production site, deleted its old migrations files, and did

``manage.py dumpdata mail > emailtemplates.json`` on the development machine, copied the .json file, and did

``manage.py loaddata emailtemplates.json on the production machine, tested sending an invitation to myself and IT
WORKED!!!

Now I just have to update the wording and send it out to the family.

One thing, though, trying to reply to it, thus sending the reply to Jim@christmas.jmorris.webfactional.com but I don't
know if it was sent there or not because I can't access it! I'll have to study up on how webfaction's e-mail system is
supposed to work.

Ah! I'm supposed to enter the **mailbox** name, not my username! When I did that I found all my Jim@etc. emails and a
host of spam e-mails that were sent last June as well.

Time to update the invitation...

Building the Website
====================

Here are my notes about what went on as I built the Christmas 2016 website.

Original Stubs
--------------

Overview
++++++++

The :ref:`table <urls_views_templates>` of urls, views, and templates in the planning document gives me a good starting
point for building the website. I plan to:

#. Create the urls.py files in config, gift_organizer, mail and memories

#. Create stubs of all the corresponding templates importing a base.html file with only the head, and a line telling
   what this html file is

#. Gradually write class views to connect the two.

The First App
+++++++++++++

I was going to start by creating the ``gift_organizer`` application but, thinking about doing the urls in some kind of
logical order, I wanted to do the one for '/' first. But that leads either to authentication or to the gift list and I
need to study authentication. Alternately I could just skip authentication for now and send it right to my dummy gift
list page. I think I will do it that way.

    ``manage.py startapp gift_organizer``

seemed to work without a hitch and I added the whole gift_organizer directory to git. I don't know if I should have
added the migrations folder however.

I added:

**gift_organizer.models.py**::

    from django.db import models
    from django.conf import settings
    from django.contrib.auth.models import User

    class Gift(models.Model):
        gift_number = models.IntegerField()
        description = models.TextField()
        wrapped = models.BooleanField(default=True)
        selected = models.BooleanField(default=False)
        receiver = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
        receiver_name = models.CharField(max_length=10, blank=True)

        def __str__(self):
            return 'Gift ' + str(self.gift_number)

**gift_organizer.views.py**::

    from django.shortcuts import render

    from django.views.generic import ListView
    from gift_organizer.models import Gift

    class GiftList(ListView):
        model = Gift

**config.urls.py**::

    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        url(r'^', include('gift_organizer.urls')),
        url(r'^admin/', admin.site.urls),
    ]

**gift_organizer.urls.py**::

    from django.conf.urls import url

    from . import views

    urlpatterns = [

        url(r'^$', 'views.gift_list', name='main_list'),
    ]

Problems and Migration
++++++++++++++++++++++

I had to update my c16.bat file on this computer to include the ``set DJANGO_SETTINGS_MODULE=config.settings.dev`` line
to get runserver to work at all. Once it did I still got several errors, the easiest of which to fix was that I had
not yet included ``gift_organizer`` into the installed apps and I've added a database without doing a migration.

There seems to be something new, though. Instead of just typing ``gift_organizer`` into the INSTALLED_APPS setting in
``settings.base.py``, the Django `tutorial <https://docs.djangoproject.com/en/1.10/intro/tutorial02/>`_ implies
that I should insert ``gift_organizer.apps.GiftOrganizerConfig``. I'm not sure why but the explanation is certainly in
the documentation someplace, so I will type it in, do a:

    ``manage.py makemigrations``

and a
    ``manage.py migrate``

and see what happens.

What happened was several more errors. Some were just typos which I have fixed in the code and above. But some were
based on my lack of understanding. Right now I'm dealing with the improper configuration of the gift_organizer urls.
It should say ``.as_view`` someplace. Looking at the
`Built-in class-based generic views <https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-display/>`_
tutorial I modified my gift_organizer.urls.py to say:

**gift_organizer.urls.py**::

    from django.shortcuts import render

    from django.views.generic import ListView
    from gift_organizer.models import Gift

    class GiftList(ListView):
        model = Gift

and ``manage.py makemigrations`` finally worked.

So did ``manage.py migrate``.

So did ``manage.py runserver`` but going to localhost:8000 resulted in:

TemplateDoesNotExist at /
    gift_organizer/gift_list.html

which, indeed, it doesn't.  I forgot to write it! I'll do it tomorrow.

Templates
+++++++++

I noticed that christmas15 had all of it's templates collected in one place:  a ``templates`` directory in the outer
``christmas15`` directory.  To accomplish that there was an entry in ``settings/base.py``:

    ``'DIRS': [os.path.join(BASE_DIR, 'templates')],``

I added the same line to ``c16Development/Christmas2016/config/settings/base.py`` and created a ``templates`` directory
in the ``Christmas2016`` folder.

But I noticed, from a print statement in ``settings/base.py``, that the BASE_DIR was the ``config`` directory instead of the
``Christmas2016`` directory. I fixed this by adding another level of ``os.path.dirname( ... )`` to the computation of
``BASE_DIR`` to account for the extra ``settings`` folder.

I got the same error as before. It is looking for gift_list.html to be in the gift_organizer app. Should it be? Or is
there some setting someplace that I have to set to get it to look to the common templates directory for all the
templates. Let's see where other people have placed the templates...

tdd2 placed a templates directory in the folder for the lists app. It did not have any other templates directory.

DjangoUnleashed had a templates directory in each app with another directory inside with the app name and the actual
templates inside that folder. I think I remember this bit of wierdness. Django is looking for
``gift_organizer/gift_list.html`` and it needs to be in a ``gift_organizer/templates/gift_organizer`` folder.

DjangoUnleashed had a templates directory in the BASE_DIR too. Within it it had a ``site`` directory and the
``base.html`` file.

After moving ``gift_list.html`` to the proper folder the root url (localhost:8000) displayed the current form of
``gift_list.html``

Creating a base.html file
+++++++++++++++++++++++++

Following the method used in DjangoUnleashed, I created a ``base.html`` file in ``Christmas2016/templates/site`` that
looked like this:

**base.html**::

    {% load staticfiles %}
    <!DOCTYPE html>
    <html lang="en">

        <head>
            <meta charset="utf-8">
            <title>
                {% block title %}
                    Christmas 2016
                {% endblock %}
            </title>
            <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!--[if IE]><script
                src="http://html5shiv.googlecode.com/svn/trunk/html5.js"-->

            {% block head %}{% endblock %}

        </head>

        <body>

            <main>
                {% block content %}
                    This is default content!
                {% endblock %}
            </main>


            <footer>
                <p>
                    &copy; 2016, Jim Morris
                </p>
            </footer>

        </body>

    </html>

and altered the ``Christmas2016/gift_organizer/templates/gift_organizer.gift_list.html`` file to look like this:

**gift_list.html**::

    {% extends parent_template|default:"base.html" %}

    <h2>This is going to be the gift_list.html file.</h2>

When reloading localhost:8000 I got an error saying:  **TemplateDoesNotExist at /** and it listed **base.html** on the
next line. The "Template-loader postmortem" said that it was looking for it in ``.../templates/base.html`` where ... =
``BASE_DIR``. I wonder how, and why, DjangoUnleashed got it to notice the ``site`` folder.

Putting ``base.html`` directly into the ``.../templates/`` directory worked better, but did not include
``gift_list.html``, probably because I didn't have a content block in that file. Correcting ``gift_list.html`` to::

    {% extends parent_template|default:"base.html" %}

    {% block content %}

        <h2>This is going to be the gift_list.html file.</h2>

    {% endblock %}

made it work properly. (But I think I want to add a stub header to ``base.html``. I did. It worked.)

I will have to read up in the book *Django Unleashed* to see how and why he used the ``site`` folder.

Ah! A closer look showed me that ``base.html`` was NOT under the ``site`` folder but along side of it! The ``site``
folder contained an ``about.html`` page. Now I can proceed to add templates and urls and stub in most of the website.

Adding More Pages
+++++++++++++++++

I find that when I mapped ``gift/select/`` and ``gift/n/`` to DetailViews I could not get to the right page (actually,
I never made a page for ``gift/select/``.) Instead I got an error::

    AttributeError at /gift/select/

    Generic detail view Select must be called with either an object pk or a slug.

That could be because I've never added any gifts to the database. I know there is a way to add test gifts but I don't
know if I'm up to it.

Reading a bit of Chapter 5 of *Django Unleashed*, I've learned that I can create my own Class Based Views (CBVs) by
inheriting from View::

    from django.views.generic import View

    ...

    class GiftList(View)

    def get(self, request)
        ...
        return render(request, *template*, {*context*})

This might avoid the AttributeError above and serve as a more gentle introduction to Generic Class Based Views (GCBVs).

Results of Using Class Based Views (CBVs)
+++++++++++++++++++++++++++++++++++++++++

The GiftList view and the Select view seemed to work well. In fact, I was able to direct the Select view to the
``gift_list.html`` template.

I had a learning experience when testing the SingleGift view however. The url pattern I am using:

    ``url(r'^(?P<gift_number>[0-9]+)/$', SingleGift.as_view()),``

sends ``gift_number`` as an attribute to the ``get`` method of the SingleGift CBV. It took a while to realize that I had
to code the ``get`` method as follows::

    def get(self, request, gift_number=None):
        return render(request, self.template_name, {})

Now let's see if I can use the ``gift_number`` in the template:

**single_gift.html**::

    {% extends parent_template|default:"base.html" %}

    {% block content %}

        <h2>This is going to be the single_gift.html page.</h2>
        <h3>It will display gift number {{ gift_number }}</h3>

    {% endblock %}

That didn't work. It only displayed '**It will display gift number**' on the second line. Perhaps I have to include it
in the context somehow.

Yep, that was it! Here is the return line in the SingleGift view:

    ``return render(request, self.template_name, {'gift_number':gift_number})``

Continuing to Stub in the Website
+++++++++++++++++++++++++++++++++

It occurs to me that the urls as defined in the :ref:`planning document <urls_views_templates>` are not quite right. The
urls for comments, remarks and perhaps trades, need to have a reference to which gift is being commented on, which trade
is being initiated, responded to, or remarked upon. Thus, the urls should be:

+------------------------------+------------------------------+--------------------------------+
| url                          | view                         | template                       |
+==============================+==============================+================================+
| /                            | authenticate                 | login.html or redirect to list |
+------------------------------+------------------------------+--------------------------------+
| /gift/list/                  | gift_organizer.giftlist      | gift_list.html                 |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/                     | gift_organizer.gift          | single_gift.html               |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/comment/             | gift_organizer.edit_comment  | comment_edit.html              |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/comment/edit/        | gift_organizer.edit_comment  | comment_edit.html              |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/comment/delete/      | gift_organizer.erase_comment | comment_delete.html            |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/trade/initiate/      | gift_organizer.request_trade | trade_request.html             |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/trade/respond/       | gift_organizer.answer_trade  | trade_answer.html              |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/trade/remark/        | gift_organizer.remark        | trade_remark.html              |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/trade/remark/edit/   | gift_organizer.remark.edit   | trade_remark_edit.html         |
+------------------------------+------------------------------+--------------------------------+
| /gift/n/trade/remark/delete/ | gift_organizer.erase_remark  | delete_remark.html             |
+------------------------------+------------------------------+--------------------------------+
| /mail/invitation/            | mail.send_invitation         | invitation.html                |
+------------------------------+------------------------------+--------------------------------+
| /mail/compose/               | mail.compose                 | compose.html                   |
+------------------------------+------------------------------+--------------------------------+
| /memories/create/            | memories.create              | memory_edit.html               |
+------------------------------+------------------------------+--------------------------------+
| /memories/edit/              | memories.edit                | memory_edit.html               |
+------------------------------+------------------------------+--------------------------------+
| /memories/delete/            | memories.erase               | memory_delete.html             |
+------------------------------+------------------------------+--------------------------------+

I'll try this out with an attempt to access a ``get__comment.html`` page. I will need to:

#. Create the page expecting a gift_number to be displayed.

#. Create the Comment model in ``gift_organizer/models.py``.

#. Write the urlconf to call the view.

#. Write the view to call the page.

When I tried it and it worked -- first time!

I will try to create a urlconf to call the same page for editing a comment (later this will have to be limited, somehow,
to the user who made the comment.)

    urlconf:  ``url(r'^(?P<gift_number>[0-9]+)/comment/edit/$', EditComment.as_view()),``

That worked too, though I later decided to call the view CommentEdit to be consistent with the urlconf.

Adding the ``comment_delete.html`` page was a simple extension of the process: create the template, write the urlconf,
write the view class.

By the way, so far I am only writing a ``get()`` method in each view class. Later I will at least have to add ``post()``
methods.

The Memories App
++++++++++++++++

The next easy thing is to add the urlconfs for the Memories app. This will require:

#. Creating the app.

#. Add the app to the ``settings.py`` file under ``INSTALLED_APPS``. (I forgot to do this and it couldn't find my
   templates. Then it couldn't find ``memory.apps.MemoryConfig`` because I created the app as "memories" and later
   changed it to "memory." I got into apps.py and changed the name to MemoryConfig and all was well.)

#. Writing its templates in the proper directory.

#. Writing its urlconfs.

#. Include its urls in config/urls.py

#. Creating its model(s)

#. Writing its view classes.

The Mail App
++++++++++++

I suppose the next easy one to do is the ``mail`` app or perhaps I should call it the ``email`` app. I think ``email``
is a more descriptive term for what it is supposed to do, which is to manage sending admin e-mails and trading e-mails.
(It turned out that I can't use email because "'email' conflicts with the name of an existing Python module and cannot
be used as an app name.")

I will:

#. Create the app:  ``manage.py startapp mail``.

#. Add it to version control.

#. Add the app to the ``base.py`` file in the ``settings`` folder under ``INSTALLED_APPS``.

#. Write its templates (``email_invitation.html``, ``email_compose.html``, ``email_trade.html``).

#. Write its urlconfs and connect them through ``config/urls.py``.

#. Write its view classes.

After a few battles with typos and changes of mind as to the naming of things, it all worked. But it's quite clear I
have to better define what, exactly, the trading feature is supposed to be.

I decided NOT to use the :ref:`Trading Post idea <trading_post_ideas>`. It didn't seem to be a lot of fun for the amount
of work it was going to cause. Instead I might be able to implement a
:ref:`Christmas Story idea <replacement_for_trading_post>` in which family members collaborate on writing a crazy
Christmas Story. This may require learning some things I don't know how to do, but it would be more worth it than the
Trading Post idea!

The User App
++++++++++++

Until I figure out how to start on the :ref:`Christmas Story <replacement_for_trading_post>` idea this should be the
last app to implement before beginning to fill out the stubs I have now. The implementation of the user profile in
*Django Unleashed* will be worth looking at before I start on this however...

Following Chapter 19
********************

Chapter 19 of *Django Unleashed* is about creating login and logout pages.  I'm going to try to follow the whole setup
there and then adapt it to my own wishes.

Preliminaries
^^^^^^^^^^^^^

Following the information in the chapter I created a user app:

    ``manage.py startapp user``

added it to INSTALLED_APPS in base.py following the new syntax:

    ``'user.apps.UserConfig',``

created a ``user/urls.py`` file::

    urlpatterns = [

    ]

.. _rooturl:

and pointed ``config/urls.py`` to that file (see last line below)::

    urlpatterns = [
    url(r'^', include('gift_organizer.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^gift/', include('gift_organizer.urls')),
    url(r'^memory/', include('memory.urls')),
    url(r'^mail/', include('mail.urls')),
    url(r'^user/', include('user.urls')),
    ]

:ref:`See a later change to the file above. <two_changes>`

Url Patterns
^^^^^^^^^^^^

Then I got working on creating a login page. First, the urlpattern:

**user/urls.py**::

    from django.conf.urls import url
    from django.contrib.auth import views as auth_views
    from django.contrib.auth.forms import AuthenticationForm
    from django.views.generic import RedirectView

    urlpatterns = [
        url(r'^login/$',
            auth_views.login,
            {'template_name': 'user/login.html'},
            name='login'),
    ]

I'm not sure I'm going to be keeping the AuthenticationForm but I like what he's showing me about overriding the
'template_name' parameter by making it a key in a dictionary.

After some discussion about how he wanted to include the login form on the logged out page, which is something I want to
do too, he presented the necessary url for logging out::

        url(r'^logout/$',
            auth_views.logout,
            {'template_name': 'user/logged_out.html',
             'extra_context': {'form': AuthenticationForm}},
            name='logout'),

But, he says, there's a problem. This is going to be over-ridden by the login and logout patterns in the admin app, so
I need to update the r'^user/' entry in the config/urls.py file like so::

    url(r'^user/',
        include('user.urls',
                app_name='user',
                namespace='dj-auth')),

Then, in order to get the login page when one first enters the site, the following is added as the first urlpattern in
**user/urls.py**::

    url(r'^$',
        RedirectView.as_view(
            pattern_name='dj-auth:login',
            permanent=False)),

The Login Template
^^^^^^^^^^^^^^^^^^

He created a new base_user.html file, which in my program will extend the ``Christmas2016/templates/base.html`` file, to
form the foundation of all the user templates:

    ``{% extends parent_template|default:"base.html" %}``

I haven't done this yet, but it might be a good practice to follow. I'll have to read about why he does it that way.
Here is my version of his ``login_form.html`` file::

    <form
        action="{% url 'dj-auth:login' %}"
        method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">
            {{ login_button|default:'Log in' }}
        </button>
    </form>

Then, at last, the ``login.html`` file:

**user/templates/user/login.html**::

    {% extends parent_template|default:"user/base_user.html" %}

    {% block title %}
        {{ block.super }} - Login
    {% endblock %}

    {% block content %}
        {% include "user/login_form.html" %}
    {% endblock %}

Testing the Login Template
^^^^^^^^^^^^^^^^^^^^^^^^^^

This will be ugly without all the css formatting but all I'm doing now is seeing if it works. If it does I will spend
some time below explaining each part to myself.

I did get to the login page, and there was a form there I could use to login. When logging in as the superuser I made of
myself last night, I got a "Page not found" error, which was not unexpected since I haven't created a place for it to go
yet. It tries to go to a non-existent /accounts/profile/ URL which is explained in section 19.5.4 of *Django Unleashed*.

The logged_out.html Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One only gets to this by clicking on a Logout button. That is probably why it is called ``logged_out.html`` instead of
``logout.html``. I add that button in the step after this one. Here is the file:

**user/templates/user/logged_out.html**::

    {% extends parent_template|default:"user/base_user.html" %}

    {% block title %}
        {{ block.super }} - Logged Out
    {% endblock %}

    {% block content %}
        <p>You have successfully logged out.</p>
        {% include "user/login_form.html"
            with login_button='Log Back In' %}
    {% endblock %}

Following the instructions to get this to work I edited the <main> tag of the ``Christmas2016/templates/base.html`` file
as follows:

**Christmas2016/templates/base.html**::

            <main>
                {% block content %}
                {% if user.is_authenticated %}
                    <li><a href="{% url 'dj-auth:logout' %}">
                        Log Out</a>
                    </li>
                {% else %}
                    <li>
                        <a href="{% url 'dj-auth:login' %}">
                            Log In
                        </a>
                    </li>
                {% endif %}
                    This is default content!
                {% endblock %}
            </main>

Also, I added an import near the top of ``config/base.py``:

    ``from django.core.urlresolvers import reverse_lazy``

and added the following constants to the bottom::

    LOGIN_REDIRECT_URL = reverse_lazy('gift_list')
    LOGIN_URL = reverse_lazy('dj-auth:login')
    LOGOUT_URL = reverse_lazy('dj-auth:logout')

Testing the New Pages
^^^^^^^^^^^^^^^^^^^^^

I learned that I had to include ``{{ block.super }}`` in the ``{% block content %}`` blocks of both ``login.html`` and
``logged_out.html`` in order for it to get the new content under the ``{% block content %}`` of ``base.html``. I need
to do that in the other templates as well it seems to me.

Also, I learned that ``{% include "user/login_form.html" with login_button='Log Back In' %}`` seems to need to be on one
line. I can't let it wrap to the next line apparently.

Now to figure out how all this stuff works:

The Workings of the Login and Logged_Out Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A user who is not logged in types ``user/login/`` into the browser's address line. Django uses the url pattern:::

    url(r'^user/',
        include('user.urls',
                app_name='user',
                namespace='dj-auth')),

from ``config/urls.py`` to direct attention, via the app_name parameter, to ``user.urls`` where this pattern:::

    url(r'^$',
        RedirectView.as_view(
            pattern_name='dj-auth:login',
            permanent=False)),

is used to call the view class named ``RedirectView`` from ``django.views.generic``. This actually sends the response to
``user/templates/user/login.html`` where:

    ``{% extends parent_template|default:"user/base_user.html" %}``

makes it include/extend the ``user/base_user.html`` template which in turn contains:

    ``{% extends parent_template|default:"base.html" %}``

which makes it include/extend the ``base.html`` file in the site's template folder: ``Christmas2016/templates/``.

The first part of that file::

    {% load staticfiles %}
    <!DOCTYPE html>
    <html lang="en">

        <head>
            <meta charset="utf-8">
            <title>
                {% block title %}
                    Christmas 2016
                {% endblock %}
            </title>
            <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!--[if IE]><script
                src="http://html5shiv.googlecode.com/svn/trunk/html5.js"-->

            {% block head %}{% endblock %}

        </head>

loads the staticfiles, which I am currently not using, provides the html header information along with a Django block
named ``title`` for the browser tab containing "Christmas 2016" and another block named ``head`` which other templates
may use to include optional information for the html <head> section.

The second part of the ``base.html`` file::

        <body>

            <header>
                <p>
                    <h1>Christmas 2016</h1>
                </p>
            </header>

            <main>
                {% block content %}
                    {% if user.is_authenticated %}
                        <li><a href="{% url 'dj-auth:logout' %}">
                            Log Out</a>
                        </li>
                    {% else %}
                        <li>
                            <a href="{% url 'dj-auth:login' %}">
                                Log In
                            </a>
                        </li>
                    {% endif %}
                    This is default content!
                {% endblock %}
            </main>


            <footer>
                <p>
                    &copy; 2016, Jim Morris
                </p>
            </footer>

        </body>

    </html>

creates the body of the stubbed in webpage. The <header> simply says "Christmas 2016" while the <main> section provides
a content block which, if the user is authenticated already, creates a "Log Out" link. If the user is not logged in, it
creates a "Log In" link. Then it inserts a line of "default content." The <main> section is followed by the <footer>
section.

The rest of ``login.html``:::

    {% block title %}
        {{ block.super }} - Login
    {% endblock %}

    {% block content %}
        {{ block.super }}
        {% include "user/login_form.html" %}
    {% endblock %}

overrides the ``title`` block by adding " - Login" to the "Christmas 2016" title provided by ``base.html``. Then it
overrides/replaces the ``content`` block by taking everything in the ``content`` block in ``base.html`` (by means of
``{{ block.super }}`` and including the template ``user/login_form.html``.

**user/templates/login_form.html**::

    <form
        action="{% url 'dj-auth:login' %}"
        method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">
            {{ login_button|default:'Log in' }}
        </button>
    </form>

The ``login_form.html`` file, which is included in ``login.html`` and ``logged_out.html`` to make it easier to log back
in, defines an html <form> whose ``action`` is to call the ``dj-auth:login`` url and whose ``method`` is ``post``. The
rest of the form accesses the ``{% csrf_token %}`` and creates a "Log in" button. There is a:

    ``{{ form.as_p }}``

line that actually builds the Django form and places it into html ``<p>`` tags. The form is supplied, invisibly in our
case, by the view which is Django's RedirectView.

.. _two_changes:

Two Small Changes
+++++++++++++++++

**First**, the url patterns in :ref:`config/urls.py <rooturl>` was pointing the root url to the gift_exchange. When someone enters
the site I want them to be directed to the login page.  If they enter the root url in the browser address bar, then I
want them directed to the gift_exchange. As a start I changed the root url pattern in ``config/urls.py`` to:

    ``url(r'^', include('user.urls')),``

This directs the entering user to the login page immediately, which is what I wanted, but if they should type in the
root url as a logged in user, it still sends them to the login page. That shouldn't be too difficult to change ... but
how?

**Second**, I decided to change the name of the ``gift_organizer`` app to be simpler to write. Using PyCharm's refactoring,
I changed it simply to ``gifts``. It seemed to be working from within PyCharm but, when trying to access a page I
learned that it had missed an (unused) import statement in ``gifts/views.py``. Fixing that seemed to solve the problem,
at least ``manage.py runserver`` worked but I discovered the change was not applied within the ``gifts/templates``
directory. Inside that was still the ``gift_organizer`` folder containing the templates. Changing its name only got me
a little farther though. All of the template tags that said
``{% extends parent_template|default:"gift_organizer/base_gift_organizer.html" %}`` had to be changed also. Fixing that
finally got it to work . . . at least I think it did.

Filling Out the Stubs
---------------------

It would be good to get the basic website working while I figure out how to implement the
:ref:`Christmas Story <replacement_for_trading_post>` idea, but to do that I will have to, once again, figure out how
to do the authentication.

The base.html File
++++++++++++++++++

This file, which appears on all of the pages, should be filled in first. I plan to copy it from last year's site step by
step.

The first thing I noticed was that the ``base.html`` file last year was a bare skeleton that provided a simple approach
to the html overhead, the <title> and the link to the css file. In the <body> tag there were a couple of includes, one
for ``header.html`` and the other for ``footer.html``. The ``header.html`` file was where, obviously, the header was
designed. It included a ``{% block content}`` section but I'm not sure it needed to, the ``footer.html`` file did not.
Also, all the templates included a Django tag: ``{% load staticfiles %}`` near the top.

I like the idea of separate ``header.html`` and ``footer.html`` files. I will build them up gradually.

Simply copying what I had for the header and footer in ``base.html`` and writing the ``{% include <file> %}`` tags in
``base.html`` worked without a hitch. Removing the rest of what I had under the ``<main>`` tag in ``base.html`` to being
within the ``<header>`` tag of ``header.html`` also worked without difficulty. Now I need to study a bit on static files
again before I decide on the best way to include the static files such as my css file and the images. Webfaction wants
them in a whole separate static app, and I remember a whole rigamarole about a ``collectstatic`` command that I never
really understood. Time to study.

Static Files
++++++++++++

Information on how Webfaction handles static files and how to use ``collectstatic`` can be found here:
https://docs.webfaction.com/software/django/getting-started.html?highlight=static%2520files#configuring-django-to-serve-static-media

Without further study, my thoughts are that once I have designated the static app that is to keep the static files, and
once I have all my static files in the places they belong: gift images to the gifts app, header image, css files and the
like to a static folder in Christmas2016?, then I run collect static and they all go to the right place which is used to
serve them later. I need to test this, though, to make sure the files are not being served from their original folders.
I can make changes in the files in one place or the other to test this. What I'm still not clear on, however, is whether
I have to store all those unused static files when I deploy the program online. That would seem wasteful, but that is
what they seem to be recommending. More study is necessary.

*Django Unleashed*, Chapter 16, pages 373 through 381, has a fairly clear explanation:

#. Django has a built-in staticfiles app that works much like the template system

#. It automatically looks for static files in apps in the folder named according to the STATIC_URL in the settings file

#. I should "namespace" the files in the ``static`` folder just like with the template system:
   ``app_folder/static/appname/file``

#. If I have any static files that I want to save outside any of the apps, I should include it in the
   STATICFILES_DIRS tuple in the settings file.  (See example on page 376)

#. The tag {% load staticfiles %} is placed at the top of html templates to allow the static files to be used. I gather
   it is something like ``import`` in Python

#. I gather that the ``collectstatic`` command is mostly for deployment, allowing all of the static files from all the
   apps to be collected into one place, the STATIC_ROOT folder.  -- such as the folder for the static app on webfaction.

Yet, I've seen ``collectstatic`` used before during development. Perhaps just for educational purposes?

The Django documentation has some more information, of course. It can be found at:

https://docs.djangoproject.com/en/1.10/howto/static-files/

and

https://docs.djangoproject.com/en/1.10/howto/static-files/deployment/

and the pages they refer to.

The Django documentation, however, indicates that the template tag for loading static files is:

``{% load static %}`` instead of ``{% load staticfiles %}``.  Hmm...

I think I will add a series of ``/static/`` folders to my app directories, a ``/static/`` folder to my main
``Christmas2016`` directory for the whole site, and a ``collected_static_files`` folder in the ``c16Development``
directory just to be able to experiment with it all and see how it works.

Site-wide Static Files
++++++++++++++++++++++

In the ``Christmas2016`` folder I created a ``static`` folder with another ``site`` folder inside it for namespacing.
In the ``site`` folder I created three other folders:  ``css``, ``fonts``, and ``images``. I copied all of last year's
common static files into these directories, changing the name of ``christmas15.css`` to ``christmas16.css``.

I experimented with the ``STATICFILES_DIRS`` tuple in the ``config/settings/base.py`` file and learned that the proper
setting is:

    ``os.path.join(BASE_DIR, 'static', 'site')``

Filling out the header.html template
++++++++++++++++++++++++++++++++++++

I am carrying over the christmas15 header.html file piece by piece. When trying to login, however, it wasn't taking any
of my expected logins. I hadn't named myself a superuser on this computer yet: the one at the rectory in South Haven.
Doing a ``manage.py createsuperuser`` with a username of Jim, e-mail of FrJamesMorris@gmail.com and a password of
``ChristmasJim2016`` the superuser was created successfully and allowed me to enter into the programs /admin/ page.
Logging in through the paritially completed ``header.html`` template worked perfectly.

I copy/pasted the whole second section -- the {% else %} part and had to make some other changes too. My first name
wasn't given after the "Merry Christmas " message so I got into the /admin/ page and added my first and last names. The
<form action="/accounts/auth/" ... from last year did not work, and I didn't want to add the actual url so I figured
out that inserting {% url 'dj-auth:login' %} did the trick. I'm still getting some extra login edit boxes on the logout
page so I will have to change it.

That was easy enough. I just had to remove the line that brought in the ``login_form.html`` template.

But I noticed that going to the root url, even when already logged in, sends me to the ``/user/login/`` page. That
can't be right. Maybe adding some logic in the view will help.

But there are no views! At least not any that I've programmed. I'm using Django's ``auth_views.login`` and
``auth_views.logout`` and I can't remember what, exactly, they do. Time to study *Django Unleashed* again.

Actually, I may have found what I needed on the Django website:

https://docs.djangoproject.com/en/1.10/topics/auth/default/#using-the-views

I will try adapting the url to:

**user/urls.py**::

        url(r'^login/$',
            auth_views.login,
            {'template_name': 'user/login.html',
             'redirect_field_name': 'gifts/gift_list.html',
             'redirect_authenticated_user': True },
            name='login'),

That seemed to do the trick!

At some point I'll have to make sure only authenticated users can enter the other templates. According to the
documentation, I can use a ``login_required()`` decorator.  See
https://docs.djangoproject.com/en/1.10/topics/auth/default/#using-the-views

Unauthenticated Visitors
++++++++++++++++++++++++

The original login page needs a message. Currently it is blank. I think the message simply needs to be added to the
``login.html`` page. Copying and adapting from last year's ``login.html`` page worked well but I don't like the way it
is styled. Changing the .info information in ``christmas16.css`` as follows::

    .info {
        margin-bottom: 20px;
        margin-left: 150px;
        padding: 10px;
        height: auto, 100px;
        width : 60%;
        border: 2px solid green;
        background-color: #f0f0f0;
        color: #208020;
        font-family: Alpine;
        font-size: 120%;
        font-style: bold;
        }

adding the margin-left, width and border properties improved the appearance but I wonder if there is some sort of
centering ability in css. A quick look didn't show me any but, in the process, I noticed my header doesn't look too
good with a narrow screen -- like on a cell phone. I may have to leave it that way for now. Maybe I can fix it later.

I still have to update the header file to this year's version. Namely, I need to add a means for the users to add their
Christmas memories to the site themselves and give them a way to access the Christmas Story we will, hopefully, be
writing together.

Thoughts: It may look best if I put the memory below the bottom red line, and add a couple of buttons or text links
between the red line and the comment. That way the appearance of the top part of the header would always be the same
and there would be no variation in how the bottom of the logo image affects the placement of the other elements of the
header.

I should copy some old memories over to the new site to see how this will look. I'm thinking I need to get into the
actual site online, get into the /admin/ page, then see if I can somehow copy them all at once or if I need to copy them
one at a time.

Using the Admin App
+++++++++++++++++++

I was surprised to find out that only the ``Users`` model was available on the ``/admin/`` page. The ``/admin/`` app is
discussed in *Django Unleashed* chapter 23. To get my other models recognized I have to import them into each app's
``admin.py`` file and register them with a line like:

``admin.site.register(<model_name>)``

I did this for the gifts app and the memory app and now I have the models available.

Finishing the User Model
++++++++++++++++++++++++

But to be able to add memories, I need to have a set of users. As long as I have to do that I might as well learn how
to add a user profile to Django's default user model. Time for more study!

I found some information in *Django Unleashed*, Chapter 23, section 23.4.4 but it seemed more complicated than what I
had last year and what I need for this year. In the end I just copied what I had last year.

**user/admin.py**::

    from django.contrib import admin
    from django.contrib.auth.models import User
    from django.contrib.auth.admin import UserAdmin

    from .models import UserProfile

    # Register your models here.
    class UserProfileInline(admin.StackedInline):
        model = UserProfile
        can_delete = False
        verbose_name_plural = 'user profiles'

    class UserAdmin(UserAdmin):
        inlines = (UserProfileInline, )

    admin.site.unregister(User)
    admin.site.register(User, UserAdmin)

Now I have to enter all the users over again, and Django now seems to be insisting that passwords contain at least
eight characters. Here is a table of this year's family information:

<Deleted and moved to ``private.rst``>

Perhaps I can write a quick program to generate passwords from family members' first and last names in a consistent
way.

I did. I put it in a new folder inside c16Development and do not include in in version control. Here it is::

    # generate_passwords.py

    """
    This program is written to generate passwords from the first and last names of family members for use in the
    Christmas2016 website. It takes a list of tuples containing the first and last names, selects the lower case of
    the first lettes of the family member's first and last name, then computes a six-digit number to follow the two
    letters. The sum of the ascii codes and the product of the ascii codes of all of the letters of the first and last
    names are added together and truncated, if necessary, to six digits.
    """

    import random

    NAMES = [
        ('Ben', 'Ruby'),
        ('Bill', 'Jay'),
        ('Bob', 'Cable'),
        ('Brian', 'Morris'),
        ('Brian', 'Ruby'),
        ('Charlie', 'Cable'),
        ('Chau', 'Morris'),
        ('Craig', 'Morris'),
        ('Dave', 'Morris'),
        ('Evan', 'Cable'),
        ('Harry', 'Barr-Morris'),
        ('Jacob', 'Cable'),
        ('Janet', 'Cable'),
        ('Jim', 'Morris'),
        ('Joyce', 'Morris'),
        ('Katelyn', 'Cable'),
        ('Kevin', 'Morris'),
        ('Madeline', 'Jay'),
        ('Marisa', 'Ruby'),
        ('Matt', 'Cable'),
        ('Nancy', 'Barr'),
        ('Nolan', 'Cable'),
        ('Scott', 'Morris'),
        ('Tom', 'Cable')
    ]

    def generate(name):

        two_char = name[0][0].lower() + name[1][0].lower()
        full_name = name[0] + name[1]
        char_product = 1
        for char in full_name:
            char_product *= ord(char)
        numeric_string = str(char_product)[0:6]

        return two_char + numeric_string

    for name in NAMES:
        print(generate(name))

The results are seen in the table above and I have entered them into the User data table through the ``/admin/`` page.

Database Administration
+++++++++++++++++++++++

I didn't want to have to enter all that information again so I did some studying and, through the Django documentation
at:

https://docs.djangoproject.com/en/1.10/ref/django-admin/

I learned that typing

    ``manage.py dumpdata > datadump.txt``

I was able to create a ``datadump.txt`` file containing all the information I had entered. I do not want it in version
control but it is on the rectory computer in the Christmas2016 directory so I can use it to try to load the data into
my home computer by:

    ``manage.py loaddata datadump.txt``

I think I should do a git pull first, though, just to have all the models in place.

Kalamazoo: I just did that git pull successfully. I happened to think, though, loaddata may not work before doing a
migration first. I created the UserProfile model on the Rectory computer. Does this one know anything about it? I'll
just try ``loaddata`` before doing the migrate to find out what happens. First, though, I need to copy the files which
I transferred through OneDrive.

Hmm... the error I got was:

    ``CommandError: Problem installing fixture 'datadump': txt is not a known serialization format.``

so I need to study to figure out the format I should have used. ... According to the Django documentation the default
format is JSON, so I'll change the extension to .json and see if that works. ... It didn't, but I'm not sure migrating
will help. It gave me the following error:

``django.db.utils.IntegrityError: Problem installing fixture 'C:\Users\frjam\Documents\MyDjangoProjects\``
``c16Development\Christmas2016\datadump.json': Could not load contenttypes.ContentType(pk=1): duplicate key value``
``violates unique constraint "django_content_type_app_label_76bd3d3b_uniq"``
``DETAIL:  Key (app_label, model)=(admin, logentry) already exists.``

I'll try makemigrations and migrate just in case. ... I did the migration but got the same error. Perhaps I can figure
out how to do a ``datadump`` of just the User and UserProfile models. ... Perhaps this will work (after getting into my
rectory computer through TeamViewer:

``manage.py dumpdata User > user.json``

I had to do:

``manage.py dumpdata auth.User > user.json`` and ``manage.py dumpdata user.UserProfile > userprofile.json``

After doing this, and copying the files to Christmas2016, I was able to load the data in the user.json file but the
userprofile.json file was only two bytes in size and produced an error when I tried to load it. Checking the /admin/
page, the user information is there and it is, somehow, linked to the UserProfile model.

Getting Memories to Display
+++++++++++++++++++++++++++

This took some experimentation but I ended up with adding a function to the ``gifts/views.py`` file::

    def get_memory():
        return random.choice(Memory.objects.all())

and called it in each of the response returning functions in the various view classes. For instance::

        def get(self, request):
            return render(request, self.template_name, {'memory': get_memory() } )

I also had to change the __str__ function in the Memory model to include the whole post and not just the first few
characters.

Cleaning up the URLs
++++++++++++++++++++

I noticed that the gift list was showing up at the url: ``/gift/`` instead of ``/gift/list/``. To fix this I first
commented out the first url pattern in ``gifts/urls.py`` and copied its name to the second::

    urlpatterns = [
        # url(r'^$',
        #     GiftList.as_view(),
        #     name='gift_list'),
        url(r'^list/$',
            GiftList.as_view(),
            name='gift_list'),
        url(r'^select/$', Select.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/$', SingleGift.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/comment/$', EditComment.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/comment/edit/$', EditComment.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/comment/delete/$', DeleteComment.as_view())
    ]

but now, if someone enters just ``/gift/`` they get a page not found error. There must be a way to redirect them to the
proper place. Maybe this::

    urlpatterns = [
        url(r'^$',
            RedirectView.as_view(),
            pattern_name='gift/list/'
            permanent=False),
        url(r'^list/$',
            GiftList.as_view(),
            name='gift_list'),
        url(r'^select/$', Select.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/$', SingleGift.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/comment/$', EditComment.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/comment/edit/$', EditComment.as_view()),
        url(r'^(?P<gift_number>[0-9]+)/comment/delete/$', DeleteComment.as_view())
    ]

That didn't work for a couple of reasons. First, the pattern_name and permanent attributes are parameters of
RedirectView.as_view(), not of url(). Second, the correct parameter to use to redirect to a url is ``url``. Thus the
correct approach to the first urlpattern is::

        url(r'^$',
            RedirectView.as_view(
            url='/gift/list/',
            permanent= False)),

but, since the default value of permanent is already ``False`` I don't really need it.

Adding the Add Memory Button
++++++++++++++++++++++++++++

Aside from the html and css changes to display the button where I wanted it to be displayed (more or less), which I
don't want to discuss here, I learned (or re-learned) that the button had to be in an html ``<form>`` tag with the
``action`` attribute set to ``/memory/create/`` and that I had to override the ``post`` method in the ``MemoryEdit``
class since the ``get`` method was not being used.

To get the memory to display properly in the header I created a ``utils.py`` file in the main ``Christmas2016``
directory which contains the ``get_memory`` method. Doing an ``import utils`` at the beginning of each app's
``views.py`` file and using ``{ 'memory': utils.get_memory(), ... } at the appropriate place in the ``return render()``
statement seems to work to get the memory displayed on every page without breaking the DRY commandment (Don't Repeat
Yourself) -- except for having to have the ``import utils`` etc. in every ``views.py`` file.

A fairly simple ``{% if memory.user == user %}`` statement preceding the Edit Memory button prevents it from being visible
unless the user who wrote it is logged in.

I changed the urlpatterns in ``memory/urls.py`` so they would indicate the memory being edited or deleted. Here is the
new form::

    urlpatterns = [
        url(r'^create/$', MemoryCreate.as_view()),
        url(r'^edit/(?P<memory_id>[0-9]+)/$', MemoryEdit.as_view()),
        url(r'^delete/(?P<memory_id>[0-9]+)/$', MemoryDelete.as_view()),
    ]

Note that I also have to write a MemoryCreate view.

I will have to figure out a way NOT to display the Add, Edit or Delete Memory buttons on the
``memory_edit.html`` or ``memory_delete.html`` pages. That would not make sense. I will have to put them into some kind
of an {% if ... %} block, but what is the condition?

I decided to change the way memories are edited. The way it was, one would have to wait until the memory came up that
one wanted to edit before editing was possible. Instead I decided to use an "Edit Memories" button that becomes visible
only when the current user has added at least one memory. To make this easier, I added a field "added_memories" to the
UserProfile model with a default of "False." It will have to be updated in the CreateMemory and DeleteMemory views.

It turned out to be a bit of a trick to refer to this new field in the ``header.html`` file.
``{% if user.userprofile.added_memories %}`` finally did the trick.

The Main Gift Page
++++++++++++++++++

Now to work on the site's main page:  ``gift_list.html``. There are some preliminaries that have to take place before I
can test this. I will have to:

#. Copy the gift image files, for both wrapped and unwrapped gifts into a ``gifts/static/gifts`` folder that I will
   create. I thought of just entering the gifts held over from last year but that might complicate the order the gifts
   appear when they are entered into the model before the others.

#. Use ``/admin/`` to enter the gifts into the database.

#. Gradually build the ``gift_list`` page.

Well, I wrote the list above some time ago and did a lot of other work first -- mostly on the User and UserProfile
models as well as on the ``header.html`` file.

Last year, the administrators e-mail buttons were on the main gift_list page. This year I am putting just one button,
"Send Emails..." in the ``header.html`` file. I think that's where it belongs, except it is another case where the
``header.html`` template is going to have to have some way of knowing what page it is heading so that it will not
render the "Send Emails..." button on the ``manage_emails.html`` page.

Copying the Gift and Comment Database Tables
++++++++++++++++++++++++++++++++++++++++++++

To copy the Gift and Comment database tables I got into ssh by opening a command prompt, without bothering to get into
a special environment like ``c16``, and typed:

``ssh jmorris@jmorris.webfactional.com``

followed by my *Dylan Selfie* password. Getting into the ``christmas15`` webapp I found that manage.py worked with the
following lines:

``python3.4 manage.py dumpdata gift_exchange.Gift > gift.json``
``python3.4 manage.py dumpdata gift_exchange.Comment > comment.json``

I used FileZilla by entering the following information:

Host: jmorris.webfactional.com
Username: jmorris
Password: *Dylan Selfie*
Port: 21

Then I could easily copy the two json files to this computer.

Now, in the c16 environment, after copying the json files to the Christmas2016 folder, I should be able to do:

``manage.py loaddata gift.json``

and

``manage.py loaddata comment.json``

Nope! I got an ``Invalid model identifier: 'gift_exchange.gift'``. Looks like a job for find and replace.

I loaded the gift.json file into PyCharm, did a find 'gift_exchange' replace with 'gifts' and so far so good. Now the
error is ``Gift has no field named 'receiverName'``. Of course not. Now it's called ``receiver_name``. Back to find and
replace.

Might as well do the same thing with ``giftNumber`` --> ``gift_number``. Now I get ``Gift has no field named
'receiverID'. Right, now it's called ``receiver``. Here we go again. Finally I had to fix "receiver": 28 and
"receiverName": "Harry" to say "receiver": null and "receiverName": "" since I don't have a user number 28 this year. (I
did the same with user 26.) This time ``manage.py loaddata gift.json`` worked.

On to the comments! Same problem with ``gift_exhange`` but that may be all this time. It was!

I had to use the ``/admin/`` page to correct set all the gifts to unselected, wrapped and selected by no one and correct
the names on the comments (since the IDs have changed). Now I should make new ``gift.json`` and ``comment.json`` files
to take to the rectory computer.

Adding the Gift Panels
++++++++++++++++++++++

Now I think I'm finally ready to finish the ``gift_list.html`` file. I'll start with just the pictures and their
captions::

    {% for gift in gift_list %}
        <div class="container">
            <div class="left-col">
                {% if gift.selected %}
                    <a href="/gift/{{ gift.gift_number }}" title="Click for larger image">
                        <img class="selected-image" alt="Image of {{ gift }}" src="{% static gift.get_image_filename %}"
                            height="100" width="150" />
                    </a>
                    <h4 class="selected-gift-text">{{ gift }}</h4>
                    <p class="selected-gift-text">Selected by {{ gift.receiver_name }}</p>
                {% else %}
                    <a href="/gift/{{ gift.gift_number }}" title="Click for larger image">
                        <img class="unselected-image" alt="Image of {{ gift }}" src="{% static gift.get_image_filename %}"
                            height="100" width="150" />
                    </a>
                    <h4 class="unselected-gift-text">{{ gift }}</h4>
                {% endif %}
            </div>
        </div>
    {% endfor %}

To get this to work I had to:

#. Modify the return statement in the GiftList view's get function to include a reference to gift_list::

    return render(request, self.template_name,
              {'memory': utils.get_memory(),
               'gift_list': Gift.objects.all().order_by('gift_number'),
               })

#. Import os into the gifts.models.py file and add a get_image_filename() function to the Gift model::

    def get_image_filename(self):
        if self.wrapped:
            status = 'wrapped'
        else:
            status = 'unwrapped'
        return os.path.join('gifts', 'images', 'gifts', status,
                            'Gift' + str(self.gift_number) + '.png')

Except for some initial confusion, since I had copied the html outside the <div class="container"> block, the
description and comment block copied over quite well from last year's version::

    <div class="text-col">
        <p class="description">{{ gift.description }}</p>
        {% for comment in gift.get_comments %}
            <p class="comment">{{ comment.comment }}</p>
        {% endfor %}
    </div>

I did remember, ahead of time, to copy over the ``get_comments()`` function from the models.py file::

    def get_comments(self):
        comments = Comment.objects.filter(giftID=self.id)
        return comments

The buttons went in without a hitch of any kind.

Plans for Finishing the Site
----------------------------

Here is a possible plan to follow while implementing the rest of the site:

#. Implement the individual gift page.

#. Implement gift selection.

#. Implement changing one's mind about a gift.

#. Implement adding a comment.

#. Implement editing a comment one has entered.

#. Implement deleting a comment one has entered.

#. Implement adding a memory.

#. Implement editing a memory one has entered.

#. Implement deleting a memory one has entered.

#. Getting e-mail to work.

#. Create a process for writing a Christmas Story and/or a Question of the Day.

Individual Gift Page
++++++++++++++++++++

This is the simplest one to implement. Here is what I copied and edited from last year::

    <div class="info">
        <p>
            Here is a larger image of {{ gift }} so that you can see it better.  Click this image to
            get back to the main page.
        </p>
    </div>

    <div>
        <a href="/gift/list/" title="Click here to return to main page.">
            <img alt="Large image of {{ gift }}" src="{% static gift.get_image_filename %}" />
        </a>

    </div>

I had to make a few changes to get it all to work. First, the ``href="/"`` from last year had to be changed to
``href="/gift/list/"`` for this year's url scheme.

More importantly, the view was not sending ``{{ gift }}`` to the page so I had to alter the SingleGift view's get
method to::

    def get(self, request, giftNumber=None):
        return render(request, self.template_name,
                      {'gift': Gift.objects.get(gift_number = giftNumber)})

Finally, since I changed the paramater ``gift_number`` to ``giftNumber`` so as not to conflict with the field name, I
had to change the corresponding urlpattern to ``url(r'^(?P<giftNumber>[0-9]+)/$', SingleGift.as_view())``. I will
probably have to do that in the other views and url patterns too.

Moving to Rectory Computer...
+++++++++++++++++++++++++++++

Just to note: I had forgotten to create a ``memory.json`` file for the memories I added to the Memory model so, through
TeamViewer, I got onto my HomeComputer, did that, and copied the ``memory.json`` file here. The file loaded fine with:
``manage.py loaddata memory.json`` but the errors I got when trying to open the root page suggested that I needed to do
a migrate. I did ``manage.py makemigrations`` and ``manage.py migrate`` and all is well.

Gift Selection
++++++++++++++

Last year this was handled by a separate view::

    def select(request):
        """
        This handles the selection of a gift by a user
        :param request:
        :return:
        """
        current_gift = Gift.objects.get(giftNumber=request.POST['gift_number'])
        current_gift.selected = True
        current_gift.receiverID = request.user
        current_gift.receiverName = request.user.username
        current_gift.save()
        request.user.userprofile.gift_selected = current_gift
        request.user.userprofile.save()
        context = { 'user': request.user,
                    'giftlist': Gift.objects.all() }
        context.update(csrf(request))
        return HttpResponseRedirect('/', context)

This year, I think, I can put it into the post section of the GiftList view.

Nope! I put it into a separate Select view. I had to be very careful about the variable names and field names. I had
some problems deciding when to use ``giftNumber`` and ``gift_number``. ``giftNumber`` is my choice for the variable name
and it becomes a key in the POST dictionary.  ``gift_number`` is the reference to the field in the Gift model. They
appear in ``gift_list.html``: ``<input type="hidden" name="giftNumber" value="{{ gift.gift_number }}" />`` and in the
Select view::

    def post(self, request):
        current_gift = Gift.objects.get(gift_number=request.POST['giftNumber'])
        current_gift.selected = True
        current_gift.receiver = request.user
        current_gift.receiver_name = request.user.username
        current_gift.save()
        request.user.gift_selected = current_gift
        request.user.save()
        return render(request, self.template_name,
                      {'memory': utils.get_memory(),
                       'gift_list': Gift.objects.all().order_by('gift_number'),
                       'user': request.user
                       })

This still isn't working correctly. It displays the list at ``/gift/select/`` instead of redirecting to ``/gift/list/``.
Also, when I manually return to ``/gift/list/``, although the "Changed My Mind" button appears correctly, all of the
other "Select" buttons are active except for that of a gift selected by a different family member.

First, I thought I'd try using RedirectView in the url setting for ``/gift/select/`` but that was dumb. It would never
get to the Select view to make the necessary changes in the database. I will look up some alternatives to
``return render()``. The Django Documentation at https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/ refers
to a ``redirect()`` shortcut function but it doesn't seem to include a context but maybe, after making the necessary
changes to the database, I could redirect it to the GiftList view with ``redirect(GiftList)``. I'll try that.

The first error I had to deal with was::

    NoReverseMatch at /gift/select/
    Reverse for 'gifts.views.GiftList' with arguments '()' and keyword arguments '{} not found. 0 pattern(s) tried: []

So, how am I supposed to use reverse? Given the url pattern::

    url(r'^list/$',
        GiftList.as_view(),
        name='gift_list'),

I tried ``redirect('gift_list')`` and that worked -- except that most of the Select buttons were still active. That may be
a problem in the ``gift_list.html`` template however.

Actually, it may be a problem elsewhere. Using the ``/admin/`` page to check the UserProfile I found that nothing was
entered under ``gift_selected``. Why not? There is a ``request.user.save()`` command in the Select view. Maybe there
also needs to be a ``request.user.userprofile.save()`` command.

I tried to load the UserProfile model first as the variable ``profile`` but it couldn't find a UserProfile matching the
query:  ``profile = UserProfile.objects.get(user=request.user)``.  Time to study *Django Unleashed*.

I experimented in ``manage.py shell`` and found that the following sequence of commands added a UserProfile for 'Jim':

``from django.contrib.auth.models import User``
``from user.models import UserProfile``
``jim = User.objects.gt(username='Jim')``
``profiles = UserProfile(user=jim)``
``profiles.save()``

I wrote a program intending to use it to create UserProfiles for each user as follows::

    # create_profiles.py

    """
    This program takes all the existing user instances and creates userprofiles for each one except if the
    username is 'Jim' because that profile has been created already.
    """

    from django.contrib.auth.models import User
    from user.models import UserProfile

    for a_user in User.objects.all():
        if a_user.username != 'Jim':
            profile = UserProfile(user = a_user)
            profile.save()

but it did not work. It kept throwing an ``ImportError: No module named 'config'``. I'm thinking that it has to be done
within manage.py to engage the whole of Django, perhaps through migrations. So it appears I have to learn about data
migrations. Chapter 10 of *Django Unleashed* is my starting point. Then I found an easier example to follow in the
Django Documentation at:

https://docs.djangoproject.com/en/1.10/topics/migrations/

I think I will need to create an empty migration in the user app like so:

``manage.py makemigrations --empty --name=add_userprofile user``

Then fill in the resulting file with::

    # -*- coding: utf-8 -*-
    # Generated by Django 1.10.2 on 2016-11-21 01:11
    from __future__ import unicode_literals

    from django.db import migrations, models
    from django.contrib.auth.models import User

    def connect_profiles_to_users(apps, schema_editor):
        # get the User model with the following line so that it gets the 'historical version'
        UserProfile = apps.get_model('user', 'UserProfile')
        for family_member in User.objects.all():
            profile = UserProfile(user=family_member)
            profile.save()

    class Migration(migrations.Migration):

        dependencies = [
            ('auth', '0008_alter_user_username_max_length'),
            ('user', '0002_userprofile_added_memories'),
        ]

        operations = [
            migrations.RunPython(connect_profiles_to_users),
        ]

This didn't work. It threw a ``ValueError: Cannot assign "<User: Matt>": "UserProfile.user" must be a "User" instance.``

He is, but I couldn't figure out how to convince it. Just to get on with it I will connect the Users to the UserProfiles
manually -- ugh! I did this by temporarily copy and pasting all the usernames here (from running a quick program in
``manage.py shell``, then eventually learned that, after importing the User and UserProfile models I could repeat the
following statements with each of the different names in the first line:

``user = User.objects.get(username='Matt')``
``profile = UserProfile(user=user)``
``profile.save()``

Now, will the Select buttons be shown correctly?

They were! But only after changing the reference back to ``user.userprofle.gift_selected`` in the ``gift_list.html``
template.

I notice the buttons all appear at a level below the lowest item in the middle column instead at the top of the column.
I'll worry about that another time.

Getting the Changed My Mind Button to Work
++++++++++++++++++++++++++++++++++++++++++

This should be relatively easy now that the necessary things have been done. I think what I need to do is to:

#. Make sure the urlpattern points to the right view

#. Update, or create, the view that will undo what the Select button does and redirect back to the ``gift_list.html``
   page.

#. Check to make sure all the buttons implemented so far work correctly.

That's pretty much the way it worked. I had to make sure the field names and variables were correct for this year's
setup. The biggest difficulty came in the third step until I finally figured out that, in the Select and the ChangeMind
views, it was the ``profile`` variable that had to be used to access ``gift_selected`` and be saved.

Adding a Comment
++++++++++++++++

Again, I had a lot of trouble with things I don't quite understand. This time I wasted a lot of time with an error
indicating that either get or post was getting an unexpected keyword argument gift_number. I finally just put it into
the argument list of the method definitions of the AddComment class. I still don't know how it is getting sent there.

I had to add a method to the UserProfile model to ``get_member_name`` to add the last name to the two Brians. This
duplicates something I already wrote in the ``memory/models.py`` file and so can probably be simplified . . . somehow.
That is for another day.

I did this, by the way, to add the "(author) says:" prefix to each comment.

Next I will have add a link to edit each comment that the current user entered. Because I currently have only one
``comment_edit.html`` form I will probably have to figure out how to divide it into two: ``comment_add.html`` and
``comment_edit.html`` with the middle section somehow the same -- or maybe just have two inserts for the form part
since that is where the ``action=`` has to be different. That, too, is for another day.

Editing and deleting a Comment
++++++++++++++++++++++++++++++

Here is what seems to be necessary:

#. Edit ``gift_list.html`` to include (edit) links after each comment written by the current user.

#. Study how the same comment editing form can be used both for comment creation and comment editing.

#. Create the appropriate urlpatterns (if necessary) and views to make it all work.

To complete #1 above I started with the following change to the section of ``gift_list.html`` where the comments are
printed::

    {% for comment in gift.get_comments %}
        {% if comment.user == user %}
            <p class="comment">{{ comment.comment }}
                <a href="/gift/{{ gift.gift_number }}/comment/edit/"> (edit)</a>
            </p>
        {% else %}
            <p class="comment">{{ comment.comment }}</p>
        {% endif %}

Testing it out, I finally got it to work when I changed the EditComment view to read as follows::

    def get(self, request, gift_number=None):
        return render(request, self.template_name,
                      {'gift': Gift.objects.get(gift_number=gift_number) })

I still don't know where it's getting ``gift_number`` from however.

To complete #2 above I looked at section 8.6 of *Django Unleashed* and decided NOT to try to use the same template to
create comments as I do to edit them. There is a way around this but, he says, it is very advanced -- and I don't even
know where it's getting ``gift_number`` from! I'll skip it for now.

To complete #3 above I have used PyCharm's Refactor tool to change the name of ``edit_comment.html`` to
``create_comment.html`` seemingly without incident. A copy and paste and some editing of that file will form my new
``comment_edit.html`` form.

In the process of editing the ``comment_edit.html`` file I thought of something. How is the system supposed to know
which comment is being edited? There must be some way to pass a comment number or something when the user clicks the
(edit) link to get the right comment.

Yes, there is! I can make the ``<a>`` tag say:
``<a href="/gift/{{ gift.gift_number }}/comment/{{ comment.pk }}/edit"> (edit)</a>`` and alter the corresponding
urlpattern to say:
``url(r'^(?P<gift_number>[0-9]+)/comment/(?P<comment_number>[0-9]+)/edit/$', EditComment.as_view())``. And this explains
where the extra arguments are coming from:  the uri itself, named in the url pattern!

So, I was able to edit the comments and, after creating a special page to confirm the deletion of comments, I am able to
delete them too.

The appearance of the pages is not good, at the very least I should be consistent on the left margin, but this will do
for now.

Improving the Look of the Edit Pages
++++++++++++++++++++++++++++++++++++

If I get one form looking more or less the way I like, the others will be easier via copy and paste. No grand and
glorious plans here, just getting things lined up better. I think I'll just need some changes to the html pages and
probably some new class tags in the css.

I only had to create one new css rule::

    .form-left{
        margin-left: 150px;
        }

and included ``class="form-left"`` in every tag on each of the comment edit pages. It still needs work, but it will do
for now until I learn a little more css.

By the way, I did learn, or relearn, that classes can be combined as in:

    ``class="description form-left"``

Adding, Editing and Deleting Memories
+++++++++++++++++++++++++++++++++++++

It should now be rather easy to make pages to create, update and delete memories. Except, here, I think it makes more
sense to allow a user who has added memories to edit or delete their descriptions of their memories on a separate page.
First I'll get the 'Add Memory' button to work.

Adding the ``memory_create.html`` page went fairly well. I just had to watch out to change all the references from what
I copy and pasted from.

On the user's ``memory_edit.html`` I imagine it should have some sort of instructions at the top followed by a list of
that user's memories with 'Edit' and 'Delete' buttons at the right similar to the 'Select' and 'Comment' buttons on the
``gift_list.html`` page. I should be able to copy some ideas from that page at least, if I don't copy and extensively
edit the page itself.

I discovered that the UserProfile model had not been fully populated on this computer, my Kalamazoo computer. Through
TeamViewer I created a userprofile.json file to load here. I had to delete the userprofiles that HAD been entered
however. Then I had to make sure the ``added_memories`` field was properly set. I also had to do a
``manage.py makemigrations`` and a ``manage.py migrate`` since I had changed ``giftID`` to ``gift`` and ``userID`` to
``user`` in the comment model.

The ``memory_edit_list.html`` page could be improved in its looks but it seems to be functional -- at least it will be
functional once I design some urlpatterns to read such things as ``/memory/n/edit/`` and ``/memory/n/delete/``. That
shouldn't be too hard.

The ``memory_edit.html`` and ``memory_delete.html`` pages went in without too many problems. I need to test whether "a
malicious user" could mess up my system by manually entering, for instance, ``/memory/14/delete/`` even though memory 14
was not composed by that person.

Sidebar on How Django Works
+++++++++++++++++++++++++++

I notice that I'm beginning to pick up on the way django works:

#. A user performs some action on a page that calls for a certain url.

#. A urlpattern catches the request and sends it to a view.

#. The view may process the information provided with the request and sends a response which, eventually, results in the
   display of a template: a new or altered page for the user.

#. The process repeats.

Testing Security
++++++++++++++++

Can unauthorized users get into any of the pages by manually entering the url? Yes! I logged out and entered:
``/gift/3/comment/`` and got to the new comment entry page for gift 3.

Can legitimate users alter or delete the entries of others? Yes! If an unauthorized user can do it, so can someone who
is authorized to be on the site but who did not write the particular entry being edited or deleted.

If so on either of these, what do I do about it? First I will read the appropriate sections of *Django Unleashed*.

Chapter 20 describes a technique of creating one's own decorator to decorate views on the class level to require login
and require that users have the necessary permissions to do what they want to do. I don't think that last part applies
to this site. I think I will have to add extra logic to assure that the authenticated user is the author of any item to
be edited or deleted -- or the superuser, of course. I could do something like that to make sure the user is logged in,
but I would have to add it to each and every method of each and every class and that would be a pain. I will try to
implement his final solution for ``class_login_required(cls)`` in Example 20.49 on page 492.

After writing that program and importing it into the ``gift/views.py`` file and putting an ``@class_login_required`` in
front of the ``AddComment`` class I got an "Unable to Connect" page from Firefox and an "AttributeError: 'NoneType'
object has no attribute 'as_view' with a reference to the urlpattern that had AddComment.as_view(). I suspect an error
in my new decorators.py file. -- Yes, I had the indentation wrong so that the creation of the decorator, etc. was all in
the ``if`` statement checking for an ``ImproperlyConfigured`` error. It worked fine after that and I applied it to all
the views in ``gifts`` and ``memory``.

It wasn't too hard to include a check that the current user was, in fact, the author of comments and memories being
edited or deleted. I put ``from django.contrib.auth import PermissionDenied`` at the beginning of the ``views.py`` files
in ``gifts`` and ``memory`` and inserted a check for the current user being the entry's author like so in the
EditComment class::

    @class_login_required
    class EditComment(View):
        template_name = 'gifts/comment_edit.html'

        def get(self, request, gift_number=None, comment_number=None):
            comment = Comment.objects.get(pk=comment_number)
            if request.user == comment.user:
                return render(request, self.template_name,
                              {'display_memory': utils.get_memory(),
                               'gift': Gift.objects.get(gift_number=gift_number),
                               'comment': comment})
            else:
                raise PermissionDenied

        def post(self, request, gift_number=None, comment_number=None):
            comment = Comment.objects.get(pk=comment_number)
            print('request.user = ', request.user, ', comment.user = ', comment.user)
            if request.user == comment.user:
                comment.comment = request.POST['comment_text']
                comment.save()
                return redirect('gift_list')
            else:
                raise PermissionDenied

Planning for E-mail
+++++++++++++++++++

First stop is to the Webfaction.com documentation: https://docs.webfaction.com/user-guide/email.html That link seems
best for setting up an using e-mail and doesn't talk about Django. This page does:
https://docs.webfaction.com/software/django/config.html and this page:
https://docs.webfaction.com/software/django/config.html#configuring-django-to-send-mail is specifically about sending
e-mail but only has the stuff that needs to go into the settings.py file. I think I will open a ticket and ask for
instructions on how to avoid the spam problem I had last year. (I started into that, realized that they probably
wouldn't have the reasons as to how I got hacked, and found a document about security that might help. It is located
here: https://docs.webfaction.com/user-guide/security.html#application-security

Chapter 11 of *Django Unleashed* also has some information about e-mail. I'll read that too.

Django's own documentation has some useful information too. It is located at:
https://docs.djangoproject.com/en/1.10/topics/email/

But I haven't given much thought, yet, as to what I want the mail app to do do and how I want it to do it. First, what I
want it to do is:

#. Send an e-mail to each family member inviting them to the site and giving them their login information.

#. Send e-mails to selected family members. I would select them from a checkbox list. Clicking on a "Select All"
   checkbox would select all family members. This could be used to send general messages about the site, such as new
   features just implemented.

#. Possibly, send periodic e-mails to family members informing them of new content since they last visited or some such
   thing. To do this I would have to figure out how to keep track of their visits and how to use the webfactional, or
   other system, to keep track of the time.

#. The mail system should allow for the composition of e-mails using templates. Thus, tags like <name>, <username>,
   <password> and the like could be written into the e-mail and then filled in with the appropriate information by the
   system before sending the mail.

Last year the invitation massage was composed by a series of ``message +=`` statements inside of a
``get_invitation_message`` function. That's dumb but it was probably all I could do in the amount of time that I had.
This year I should create a separate file in a ``static/mail/messages/`` folder the read in in through Python.

Both *Django Unleashed* and the official Django documentation explained how to test e-mail during development by
including the following in the settings file:

``EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'``

I will insert that and begin work on the invitation system.

Getting E-mail Invitations to Work
++++++++++++++++++++++++++++++++++

I did it. I just forgot to tell me how I did it. As I recall, first I composed the text of the e-mail, then programmed
the tag-converter, then got the html to work. The biggest thing I remember learning is that the get_secrets function
can be imported into other parts of the program through:  ``from config.settings.base import get_secret``. It did not
work to move this to the utils folder. Apparently the settings for django have to be dealt with before it is ready to do
anything with any models, and the utils module imported the ``memory.models``.

I also learned a little bit about how to deal with checkboxes. The POST information carries a list of the values of the
checked boxes and this information can be retrieved through ``request.POST.get('family_member')`` where
``family_member`` is the ``name=`` attribute for the ``<input type="checkbox" ... >`` tag.

Working on the Look and Feel
++++++++++++++++++++++++++++

I made a few changes to the ``gift_list.html`` file and the ``christmas16.css`` file to get a right column to appear on
the main page. I got the column to appear, but the footer was placed right underneath the right hand column instead of
being at the bottom of the page. I think I have to use a ``<div>`` structure as follows:

.. image:: ./_static/images/Christmas2016DivPlan.png

Now, looking at that diagram, I'm not sure I need a ``Page Container`` <div> but I have to be sure the
``Content Container`` <div> is outside the header and footer.

Nothing I tried actually worked. I need to learn more about css. I have downloaded the Skeleton Framework from:

http://getskeleton.com

but I think I need to focus on getting the website up and running first, with its new features if possible, then focus
on making it look better. I will try to get it back to a working state without the right column.

I did that, and it was fairly simple. I also learned a little something about how the buttons at the right of the
gift sections sometimes are beside the description and sometimes below. The buttons are a fixed width. The description
is set for a width of 70%. At times 70% of the screen size, plus the first column's width plus the buttons' width is
greater than the space available. That is when the buttons jump to a spot below the lowest line of the description and
comments, if any.

Adding the Story or Question of the Day Feature
+++++++++++++++++++++++++++++++++++++++++++++++

Let me plan both of the new apps here and then decide which one to tackle first.

The story app would require a database to keep track of entries and their order and the family member making each entry.
Thus the model could be::

    Story Model:
    entry: Text Field
    entry_number: integer field
    user: ForeignKey

A possible url scheme would be::

    story/ - displays the story with each user's entries marked with their name and edit links for the current user
    story/add/ - displays the story with an entry box at the end so the user can make a new entry
    story/n/edit/ - displays the nth entry of the story so the user who made it can edit it (it seems there should be
                    limits to how much they can delete)

The views necessary could be::

    StoryDisplay
    StoryAdd
    StoryEdit

The question app would require two models, one to keep track of the questions, the other to keep track of the
associated responses and who made them. Perhaps I can follow the structure of the polls app in the django online
tutorial. Here are my initial ideas::

    Question Model:
    question: text field

    Resonse Model:
    response: text field
    question: foreign key to question model
    user: foreign key to user model

A possible url scheme would be::

    question/ - displays the questions and their answers and the users who gave those answers. Questions and answers are
                displayed with the most recent questions at the top and the answers in the order they were entered.
    question/add/ - available only to the administrator (but consider making it available to all) that allows the entry
                    of new questions
    question/n/edit/ - edits the nth question either by the administrator or the person who entered it
    question/n/add_response/ - allows the addition of a response to the question by a user
    question/n/edit_response/n/ - allows for editing of a response by the user who made it (or the administrator?)
    question/n/delete_response/n/ - allows the deletion of a response by the user who made it (or the administrator?)

The views necessary could be::

    QuestionList
    QuestionAdd
    QuestionEdit
    ResponseAdd
    ResponseEdit
    ResponseDelete

With this quick analysis, it seems that the story app may be a little easier, though I will have to figure out a good
way to display the story -- how to do paragraph breaks, for instance, and how to associate the authors with the lines
they authored.

Working on the New URL Patterns
+++++++++++++++++++++++++++++++

I included the following lines::

    url(r'^story/', include('story.urls')),
    url(r'^question/', include('question.urls')),

into ``config/urls.py`` and am trying to eliminate the logout page by changing its url pattern to::

    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'user/login.html',
         'extra_context': {'form': AuthenticationForm}},
        name='logout'),

A quick test to see if this last part is working indicates that, after I set up some fake url patterns in the story and
question apps, it is working correctly.

Adding Views and Templates to the Story App
+++++++++++++++++++++++++++++++++++++++++++

Mostly by copying what I did in the ``gifts`` app this seems to be going fairly smoothly. I did, however, decide to add
a new field to ``story/models.py``. A user should be able to edit an item only if no one has added entries to the story
after that user's and they should get only a certain amount of time to do it. That requires a ``DateTimeField`` in the
model definition. The model now looks like this::

    class Story(models.Model, AuthorMixin):
        entry = models.TextField()
        entry_number = models.IntegerField()
        author = models.ForeignKey(settings.AUTH_USER_MODEL)
        publish_date_time = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.entry

But how much time should the user get? A minute? An hour? A day? What happens when another user is working on adding a
new entry at the same time the previous author is editing his or her entry? I think I'll ignore all that and let the
chips fall where they may. Perhaps I will start with a 15 minute grace period for editing, and only if there has been
no subsequent entry.

Adding a Menu List to the Header
++++++++++++++++++++++++++++++++

But now users will need access to four different things on the site:

#. Participating in the gift exchange (the main purpose)

#. Adding or editing memories being displayed.

#. Reading or Adding to the Family Christmas Story.

#. Responding to the Question of the Day.

Adding these four in a list across the top seems to be a good approach, if I can figure out how to do it. Maybe I
should put this into a different branch, too, just in case I can't get the new apps implemented soon.

Actually, now that the pictures are all ready (except maybe I'd like to make thumbnail images of the gifts to keep
the initial loading time down) I should add them to the database and concentrate on deployment.

I will add the thumbnails, update the gift descriptions, eliminate the old comments and maybe the old memories, make a
new branch called ``new_features``, then get back into the ``master`` branch to start on deployment.

New Features
------------

The website is online and working now (as of December 9, 2016) and so it's time to work on the new features. After
rejecting the trading idea I have three ideas left:

#. Christmas Story

#. Who Am I?

#. Question of the Day

Christmas Story
+++++++++++++++

I like this idea but it may be difficult to implement if I try to either prevent, or allow for, the possibility of two
users adding an entry at the same point in the story line. It is very much worth looking into but I might not have time
to implement it before Christmas.

Who Am I?
+++++++++

I haven't given this one too much thought yet but it seems relatively simple to implement. I would have to create one
model for the clues and another model for the guesses. The Clue model would have the fields::

    clue_giver: User
    clue_set: integer indicating which set of this user's clues this one belongs to
    clue: text field
    display_date: date field (the date on which the results will first be available - 3 days after clues posted?

The Guess model would have the fields::

    guesser: User
    guess: User
    clue: Clue
    comment: text field (guesser can give his or her reasons, or make other comments)
    correct: boolean, True if guess is correct, False otherwise

This may be more complicated than I thought, and it might not engage people's interest. It also might be hard for people
to give good clues. But, it might be worth the effort to try to implement.

Question of the Day
+++++++++++++++++++

Given that Janet has already supplied a set of questions, the most complicated part of this would be to learn how not to
display a question until its proper date. I would need two models, one for the Questions and one for the Responses. The
Question model would have these fields::

    question: text field
    date: date field giving the date to start being displayed

The Response model would have these fields::

    question: ForeignKey to Question
    user: ForeignKey to User -- the one giving the response
    entry_date_time: DateTimeField according to when this response was first created
    response: text field

This one might be the easiest of the three to implement. Let's see if I can imagine it in use:

Madeline clicks on the **Questions** menu item and goes to the question of the day page. There she sees, at the top
of the page contents, the most recent question and the answers of anyone who has answered it so far. Beneath that are
the questions and answers from previous questions. Madeline sees a button next to each entry. Entries on which she has
not yet given a response have a "Respond" button. Entries on which she has already responded have an "Edit My Response"
button instead.

Since she hasn't responded yet to the most recent question she clicks on its "Respond" button and is sent to a page that
displays the question and gives her a space to answer. After writing her response she clicks the "Save" button and
returns to the Questions page.

Now she sees that she can add to her response in the second question down and clicks on the "Edit My Response" button
next to it. This sends her to the same page she uses to enter her responses except that the response box is already
filled with her previous response. She starts to edit it but deletes something she didn't want to delete and can't
remember what, exactly, it said. She clicks the "Cancel" button and is returned to the Quesstions page with her original
response still intact. Entering the edit process again, she completes the edit the way she wants and presses the "Save"
button to return to the Questions page.

Having finished what she wanted to do, and having read the responses of other family members, listed in reverse order of
their insertion, Madeline clicks on the **Gifts** menu item to return to the main page.

Writing this story suggests to me that the Response model needs a DateTime field to keep track of when a response was
entered so that they can be listed in reverse order. I have added it to the model outline above.

Here is a table of urls, views and templates:

+--------------------------------+-----------------------+----------------------+
| URL                            | View                  | Template             |
+================================+=======================+======================+
| question/list/                 | QuestionList          | quetion_list.html    |
+--------------------------------+-----------------------+----------------------+
| question/n/response/create/    | CreateResponse        | response_edit.html   |
+--------------------------------+-----------------------+----------------------+
| question/n/response/r/edit     | EditResponse          | response_edit.html   |
+--------------------------------+-----------------------+----------------------+
| question/n/response/r/delete   | DeleteResponse        | response_delete.html |
+--------------------------------+-----------------------+----------------------+

Implementing the Question App
+++++++++++++++++++++++++++++

First I need to do a ``manage.py startapp question``. But, alas, ``'question' conflicts with th name of an existing
Python module and cannot be used as an app name.`` So lets try ``manage.py startapp questions``. Oops! I had already
done ``manage.py startapp question`` and that's why it was rejected. I will just delete the whole ``questions`` folder
and work with the existing (and version controlled) `question` app.

I created a new branch in PyCharm called question after commiting and pushing the current state of the master branch.
Then, once in the newly created ``question`` branch I pushed that to github too. Now to start work. I'll start with
the models. I discovered that I had already worked a little bit on the models. I updated them according to my
discoveries above and here is the resulting file:

**question/models.py**::

    from django.db import models
    from django.conf import settings

    from model_mixins import AuthorMixin as AuthorMixin


    class Question(models.Model):
        question = models.TextField()
        date = models.DateField()

        def __str__(self):
            return self.question


    class Response(models.Model, AuthorMixin):
        response = models.TextField
        question = models.ForeignKey(Question)
        author = models.ForeignKey(settings.AUTH_USER_MODEL)
        entered = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.response

I added the ``auto_now_add=True`` argument to the ``entered`` field so that the date and time would automatically be
saved when the response is created.

Discovering Problems in Previous Work
+++++++++++++++++++++++++++++++++++++

In creating the urlpatterns for the ``question`` app I wondered what would happen if a user entered a url without
completing it, such as ``gift/1/comment/27/`` instead of ``gift/1/comment/27/edit/``. I created a urlpattern for that
and redirected it to the edit page.

Similarly I wondered whether entering a non-existent number would crash the program and it did. I fixed this, in at
least some of the gift views, with a ``try: except:`` block.

Working on the Question/Response List
+++++++++++++++++++++++++++++++++++++

Little by little this is taking shape. I learned I can use the same ``container`` class that I did for the ``gift_list``
page to separate the questions with red lines. I learned how to use the view to send only the questions that are dated
on or before today's date. I puzzled for a while over how to create the link for a user editing his or her response. The
problem was that I had thought of using ``/question/n/response/r/edit/`` where n is the ``question.pk`` and r is the
``response.pk`` but the template has no way of knowing which response belongs to the current user. I decided to use
``/question/n/user/u/response_edit/`` instead where n is the ``question.pk`` and u is the ``user.pk`` and have the view
figure out which response belongs to that user.

In the process I've learned about filters and about reversing urls in templates instead of hard coding the urls as I've
been doing. I will have to apply that gradually to the already existing code.

The Create Response Page etc.
+++++++++++++++++++++++++++++

The next thing to do is work on the page used for creating responses ``create_response.html`` and the corresponding
view.

I did that and the rest of the response pages: ``response_edit.html`` and ``response_delete.html``. As explained above,
to use an ``Edit Response...`` button I had to change the url scheme to include the ``user.pk`` rather than the
``response.pk`` but it occurs to me that if I followed the same technique I did with the comments, placing an ``(Edit)``
link next to each response of the current user I could use the original url scheme. I'll think about that for a bit
before changing it. I'd like to deploy the new feature tonight and might not have enough time.

I would like to improve the looks of the ``question_list.html`` however. That should be relatively easy. -- It was! --

So easy, in fact, that I think I'll try for that more sensible url scheme. First I'll make some changes to
``question_list.html`` -- namely, adding the ``(Edit...)`` link.

After some errors, mostly just forgetting part of the interactions between files, it seems to be working now with the
original url scheme.

Last Steps Before Deploying the Question Feature
++++++++++++++++++++++++++++++++++++++++++++++++

#. Improve the appearance of the delete pages for comments and responses (and memories?)

#. Finish correcting the local passwords on this machine (the Kalamazoo machine).

#. Decide and implement the ordering of the questions -- which ones appear when.

#. Make sure there are no more responses lingering about.

#. Deploy.

Rethinking the Christmas Story Idea
-----------------------------------

After implementing the **Question of the Day** feature I'm thinking this one isn't as difficult as I originally thought.
I could create two models, one to hold the story lines and one for the branches that might be created. The ``Story``
model would have four fields: the branch for which each line is intended, the key to the preceding line, the user
supplying the line and the text they supply. The ``Branch`` model would have just one field, a comma-separated string of
integers indicating the order in which the story lines are to be displayed.

At first, there would only be one branch and it would contain a sequence of integers:

``1, 2, 3, 4,``

But if two or more users submit a story line intended for the same branch after the same preceding line a new branch is
created:

Original branch: ``1, 2, 3, 4, 5,``

First New Branch: ``1, 2, 3, 4, 6,``

Second New Branch: ``1, 2, 3, 4, 7,``

From then on the story branches would be displayed on separate pages and clicking the ``Add to Story`` button on a
branch's page adds to that branch.

Thinking through the details, when two users have accessed the ``/view_story/1/`` page and have both pressed
``Add to Story`` and been delivered to a ``/story/1/edit/4/`` page.  User 1 has clicked ``Save`` and the ``post`` method
of the view checks to see whether anyone else has already responded to line 4 (by checking the ``Story`` model's entries
for any containing line 4 - the line being continued). Finding no entries already there the ``post`` method creates a
new entry in the ``Story`` model and saves it. Now User 2 clicks ``Save`` and the ``post`` method DOES find a previous
entry responding to line 4. It checks through all the existing branches to see if any have "4" as their final entry and
none of them do so it creates a new branch by copying all of the entries so far and saving the new list to a new branch.
Now it goes back to check the existing branches for one with a "4" as its final entry and finds the newly created
branch. It creates and saves the new line to this newly created branch.

Now User 3 finally gets around to clicking ``Save`` and the process repeats, creating a third branch just as the second
was created.

Much of the logic, it seems can go into the model class perhaps with a ``check_entry(previous_line)`` method that
returns either ``True`` or ``False`` depending on whether ``continued_line`` is the last entry; and a
``create_branch(old_branch)`` method that creates a new branch from an ``old_branch`` and returns the branch number.

The display of the story could take place in a series of ``.story_line`` ``<div>``s with the author's name in the left
column, the story line itself in the center column and the ``Add to Story`` button appearing only on the last one.

Details of the Story App
++++++++++++++++++++++++

Here are the model definitions::

    Story
        story_line: TextField
        branch_number: integer
        user: ForeignKey to User -- the one writing the story line
        previous: integer -- the pk of the previous Story entry

        methods:
            __str__: the story line (up to 80 char?)
            display: displays the entire story_line

    Branch
        sequence: a string of space separated integers

        methods:
            __str__: sequence string
            as_list: converts sequence string to a list of integers
            check_entry(previous): returns True or False depending on whether previous is the last entry in sequence
            create_branch(from_branch): creates a new branch using the from_branch's sequence as a starting point

Here is the URL, View, Template table:

+--------------------------------+-----------------------+----------------------+
| URL                            | View                  | Template             |
+================================+=======================+======================+
| story/b/display/               | StoryDisplay          | story_display.html   |
+--------------------------------+-----------------------+----------------------+
| story/b/add/p/                 | StoryAdd              | story_add.html       |
+--------------------------------+-----------------------+----------------------+
| story/b/check/p/               | StoryCheck            | story_check.html     |
+--------------------------------+-----------------------+----------------------+

where b is the branch number and p is the number (pk) of the previous post.

Planning the Implementation of the Story App
++++++++++++++++++++++++++++++++++++++++++++

#. Commit, save, and push the master branch.

#. Create a new branch in git called ``story``.

#. Create (or update) ``story/models.py`` according to the outline above.

#. Perform ``makemigrations`` and ``migrate`` on the local machine.

#. Write ``story/urls.py`` according to the chart above.

#. Write the ``StoryDisplay`` view.

#. Write the ``story_display.html`` template.

#. Test the display of a fake story you create in ``/admin/`` Edit ``christmas16.css`` as necessary.

#. Create a branching story in ``/admin/`` and test its display.

#. Write the ``StoryAdd`` view and the ``story_add.html`` template.

#. Write the ``StoryCheck`` view and the ``story_check.html`` template.

#. Test adding lines to both fake branches of the story.

#. Simulate two people adding to the same point of the same branch.

#. Deploy!



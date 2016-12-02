Planning the Christmas 2016 Site
================================

Initial Thoughts
----------------

My thoughts are to keep basically the same style and function as last year while upgrading my approach behind the
scenes. Using what I've seen in *Django Unleashed* and guided by the principles in *Two Scoops of Django* I hope to
create a website that is more sensibly programmed than what I was able to accomplish last year.

.. _new-feature-label:

Yet I would also like to be able to add at least one new feature, yet to be discerned. I'd like something that would
engage the family and encourage interaction. The Christmas Memories addition from last year was good but I'd like to
come up with something to do in addition to that, some kind of Christmas game we can all play together. Maybe Janet will
have some ideas.

I will also have to be more careful about e-mail security than I was last year. The site was used to send spam of some
sort around June of last year. I was moving and couldn't deal with it at the time, and now my "support ticket," or
whatever WebFaction calls it, has been closed, so I may have to ask their help in addition to studying their
documentation on how to safely use e-mail on their site.

The Root URL
------------

I could try to keep the same root url: christmas.jmorris.webfactional.com or create a new one, perhaps:
christmas16.jmorris.webfactional.com.

My preference would be to keep the same url, it would be easier for the family, but that would involve replacing the
old site with the new and might still involve a compromised e-mail system. Since I'd like to have the old site online
while I'm building the new perhaps I could create a new application with the url: christmas15.jmorris.webfactional.com
and use that for the old site. That would also help me review procedures with webfaction.com and FileZilla and learn
how to correct the e-mail situation.

I will try to put the new site at the old url. During construction I can put up some sort of "Under Construction" page.
Maybe, if I get a target date for deployment, I can even include a "nn days to go" feature, or a "xx days until
Christmas" feature on the "Under Construction" page.

The Main Page
-------------

Last Year's Site
++++++++++++++++

.. _header-label:

The Header
**********

After authentication (see below), the user saw the "Christmas 2015" header with an image of three Christmas bells on
the left side, the title ("Christmas 2015") printed in an Old English style type next to it with a randomly chosen
Christmas Memory beneath the title. The Christmas Memory is printed in blue with a heading "Christmas Memory from
<name>" where <name> was the name of the family member who entered that memory. The memory was printed in blue
underneath that line after a blank line. To the right of the page was a greeting: "Merry Christmas <username>" printed
in a sans serif type where <username> was the name of the authenticated user. Finally, at the rightmost edge of the
header was a logout button which returned the user to the login page (although the url was:
christmas.jmorris.webfcational.com/accounts/logout/). There was a red line border both above and below this main
header which appeared on every page except, for some reason, the Christmas Memory does not appear on the individual
gift pages. :ref:`(See plans for this year.) <2016-header-label>`

.. _introduction-label:

The Introduction
****************

An introduction to the site was printed in a grey box in somewhat ornate green type. Last year it said: **"Welcome to the
2015 version of our family Christmas page. The design this year is much the same as last year but there are a lot of
changes "under the hood." Select one of the gifts below by clicking on the 'Select' button. You can change your mind
later by clicking on the 'Changed my mind' button that will appear after you make a selection. You may comment on any
of the gifts by clicking on the 'Comment' button. If you want to see a larger image of the gift, click the picture
itself."** :ref:`(See plans for this year.) <2016-introduction-label>`

.. _button-label:

Special Administrator Buttons
*****************************

When I was logged in, a special set of buttons appeared below the Introduction. A Send To All button enabled me to send
an e-mail to the whole group. A Send Invitation button seems to have been designed to be used just once to send the
original invitation to everyone. Fortunately, clicking on it today, got me to a server error. Maybe it will re-open my
ticket?

I noticed, when clicking the Send To All button that the header on that page did not include the Christmas Memory
either. :ref:`(See plans for this year.) <2016-button-label>`

.. _gift-list-label:

The Gift List
*************

Underneath the Introduction (or, for me, the two e-mail buttons described above) appeared the gift list. Each item
consisted of a small thumbnail image of the gift, wrapped or unwrapped according to whether it had yet been received, surrounded
by a red border if it had been selected or a green border if it was still open for selection.

Underneath the thumbnail was that gifts title (Gift 1, Gift 2, etc.) printed in green if it had not yet been chosen or
in red if it had. Also, if it had been chosen, the words Selected by <receiver> appeared in red below its title where
<receiver> was the name of the person selecting it.

To the right of the thumbnail was my description of the item in green and, if anyone had made comments on it, their
comments, listed the order of their inclusion, were printed in blue using the format: <commenter> says: <Comment> where
the meaning of <commenter> and <Comment> is obvious.

At the rightmost portion of the list item were a couple of buttons. The top button was marked "Select" and was enabled
only if the gift had not yet been selected except if the gift HAD been selected by the current user it was enabled and
marked "Changed My Mind" and immediately returned the user to the selection page. Upon pressing the "Select" button the
user was also redirected to the selection page with that gift now marked as selected.

The second button was marked "Comment" and enabled the user to add a comment to that gift.
:ref:`(See plans for this year.) <2016-gift-list-label>`

.. _footer-label:

Footer
******

Down at the bottom of the page was a footer that said, in small green print, "© Morris Family Christmas Website - 2015"
:ref:`(See plans for this year.) <2016-footer-label>`

This Year's Site
++++++++++++++++

.. _2016-header-label:

This Year's Header
******************

I foresee using basically the :ref:`same style <header-label>` as last year except to use an image of Christmas candles
instead of bells and, of course, that the title should be "Christmas 2016". I might also add an 'Add Memory' button to
enable family members to more easily add them.

.. _2016-introduction-label:

This Year's Introduction
************************

:ref:`Last year's <introduction-label>` format is fine with me for this year. The contents should change, though. Here
is a possibility:  **"The 2016 version of our family Christmas page has a few new features as well as basically the
same design as before. Select one of the gifts below by clicking on its 'Select' button. If you change your mind later
you can click the 'Changed My Mind' button that will appear. Click the 'Add Comment' button to make a comment on a gift
whether you select it or not. In the area above click the 'Add Memory' button to add a Christmas memory that will be
randomly selected. New this year is the ???"**

.. _2016-button-label:

This Year's Administrator Buttons
*********************************

The 'Send Invitation' button definitely has to be implemented better than it was :ref:`last year <button-label>`.
Perhaps I can send myself to a whole administrator e-mail page to simplify the sending of site-related e-mails to
individual family members.

.. _2016-gift-list-label:

This Year's Gift List
*********************

The gift list, I think, can be much the same as :ref:`last year <gift-list-label>`. Perhaps this year I can try to
implement a trading feature by which family members offer to trade gifts, convincing one another online for all to see.
This will take considerable thought to implement well. A gift list item would have to have an area for trading -- or
maybe there could be a link to a "Trading Post" page where all trades could be discussed and worked out. Perhaps
something like "Jim is asking Janet to trade Gift 2 for Gift 6. Jim says: "I'm sure you'd really rather have this." Janet
says: "Why? How is it better than my whoop-de-doodle fly trap?" Jim says: "Why? This looks to me like it could be an
elephant trap -- obviously much better than trapping flies since elephants are bigger!" Janet says: "Alright, you've
convinced me!" Think about this.

.. _2016-footer-label:

This Year's Footer
******************

This should be the same as :ref:`last year <footer-label>` but, of course, saying 2016 at the end.

URL Structure of the Site
-------------------------

Last Year
+++++++++

Here is a table of urls and the pages they pertained to on last year's site:

+---------------------+----------------------------------+
| URL                 | Page(s) Addressed                |
+=====================+==================================+
| /                   | authentication page or main page |
+---------------------+----------------------------------+
| /gift/n/            | Gift n's page                    |
+---------------------+----------------------------------+
| /gift/comment/      | Comment page for all gifts       |
+---------------------+----------------------------------+
| /mail/send_all/     | Send All e-mail page             |
+---------------------+----------------------------------+

Note: I got this by visiting the site and looking at the various urls that showed up. There were two url.py files that
are outlined :ref:`below <url_label>`.

This Year
+++++++++

This year perhaps the root url should point only to the authentication page and, once a user is authenticated, they
come automatically to the gift_list page. The table below shows this and other possible changes:

+---------------------+----------------------------------+
| URL                 | Page(s) Addressed                |
+=====================+==================================+
| /                   | authentication page              |
+---------------------+----------------------------------+
| /gift_list/         | the main page                    |
+---------------------+----------------------------------+
| /gift/n/            | Gift n's page                    |
+---------------------+----------------------------------+
| /gift/comment/      | Comment page for all gifts       |
+---------------------+----------------------------------+
| /gift/trading_post/ | Trading Post page                |
+---------------------+----------------------------------+
| /mail/send_invite/  | a page to send or resend invites |
+---------------------+----------------------------------+
| /mail/send_all/     | Send All e-mail page             |
+---------------------+----------------------------------+

Model Design
------------

I don't anticipate making too many changes to the model design, except for:

    #. Improving how the User model works with the Profile model if possible

    #. Adding fields for use with the trading idea

    #. Adding fields for other possible features as discussed :ref:`above <new-feature-label>`.

Last Year
+++++++++

Last year, the gift_exchange app had three models: Gift, Comment and UserProfile. The memories app had only one model:
Memory. Here is the structure of the tables:

Gift Model:

+---------------+---------------+----------------------------------------+
| Field Name    | Type          | Parameters                             |
+===============+===============+========================================+
| giftNumber    | IntegerField  |                                        |
+---------------+---------------+----------------------------------------+
| description   | TextField     |                                        |
+---------------+---------------+----------------------------------------+
| wrapped       | BooleanField  | default=True                           |
+---------------+---------------+----------------------------------------+
| selected      | BooleanField  | default=False                          |
+---------------+---------------+----------------------------------------+
| receiverID    | ForeignKey    | AUTH_USER_MODEL, null=True, blank=True |
+---------------+---------------+----------------------------------------+
| receiverName  | CharField     | max_length=10, blank=True              |
+---------------+---------------+----------------------------------------+

The Gift model had three functions defined for it:

*   ``__str__`` which returned a string 'Gift <n>' where <n> was the gift number

*   ``get_image_filename`` which checked for the wrapped or unwrapped status of the gift and included either 'wrapped' or
    'unwrapped' in the path name it returned (I suppose it should be called ``get_image_pathname``

*   ``get_comments`` which returned all the comments for that particular gift

.. _comment-model-label:

Comment Model:

+---------------+---------------+----------------------------------------+
| Field Name    | Type          | Parameters                             |
+===============+===============+========================================+
| giftID        | ForeignKey    | Gift                                   |
+---------------+---------------+----------------------------------------+
| userID        | ForeignKey    | settings.AUTH_USER_MODEL               |
+---------------+---------------+----------------------------------------+
| comment       | TextField     |                                        |
+---------------+---------------+----------------------------------------+

The Comment model had one function defined for it:

*   ``__str__`` which returned the first 10 characters of the comment followed by an ellipsis: '...'

UserProfile Model:

+---------------+---------------+----------------------------------------+
| Field Name    | Type          | Parameters                             |
+===============+===============+========================================+
| user          | OneToOneField | User                                   |
+---------------+---------------+----------------------------------------+
| gift_selected | ForeignKey    | Gift, null=True, blank=True            |
+---------------+---------------+----------------------------------------+
| password_text | CharField     | max_length=10, default=''              |
+---------------+---------------+----------------------------------------+

The UserProfile model had one function defined for it:

*   ``__str__`` which returned a string 'Profile for <name>' where <name> was the user's username

Memory Model:

+---------------+---------------+----------------------------------------+
| Field Name    | Type          | Parameters                             |
+===============+===============+========================================+
| post          | TextField     | max_length=400                         |
+---------------+---------------+----------------------------------------+
| user          | ForeignKey    | settings.AUTH_USER_MODEL               |
+---------------+---------------+----------------------------------------+

The Memory model had two functions defined for it:

*   ``__str__`` which returned the entire text of the post

*   ``author`` which returned the user's first name unless that name was 'Brian', then it returned both first and last
    name

This Year
+++++++++

The models from last year look pretty decent to me, though I may be able to make them "fatter" and use
``get_image_path`` as a more descriptive name for what that function does. Here is a first attempt at designing a Trade
model:

Trade Model:

+----------------+---------------+----------------------------------------+
| Field Name     | Type          | Parameters                             |
+================+===============+========================================+
| requester      | ForeignKey    | settings.AUTH_USER_MODEL               |
+----------------+---------------+----------------------------------------+
| requester_gift | ForeignKey    | Gift                                   |
+----------------+---------------+----------------------------------------+
| responder      | ForeignKey    | settings.AUTH_USER_MODEL               |
+----------------+---------------+----------------------------------------+
| responder_gift | ForeignKey    | Gift                                   |
+----------------+---------------+----------------------------------------+
| start_date     | Date(?)       | ?  (look this up)                      |
+----------------+---------------+----------------------------------------+

It should at least have an __str__ function:

*   ``__str__`` which returns a string saying '<requester> wants to trade <requester_gift> with <responder>'s
    <responder_gift>'

*   ``delay`` which returns the number of days the request has been made without the responder responding. After a
    certain number of days the request can be automatically withdrawn.

Come to think of it, the Trading Post idea will require another model to keep the conversation messages:

Remark Model (modified from the :ref:`Comment Model <comment-model-label>` above):

+---------------+---------------+----------------------------------------+
| Field Name    | Type          | Parameters                             |
+===============+===============+========================================+
| tradeID       | ForeignKey    | Trade                                  |
+---------------+---------------+----------------------------------------+
| userID        | ForeignKey    | settings.AUTH_USER_MODEL               |
+---------------+---------------+----------------------------------------+
| remark        | TextField     |                                        |
+---------------+---------------+----------------------------------------+

Like the Comment model before it, the Remark module should have at least one function:

*   ``__str__`` which returns the entire text of the remark.

Which Apps Should I Build?
--------------------------

Last year's project included two Apps: ``gift_exchange`` and ``memories``. This year seems to be working up to three
Apps: ``gift_exchange``, ``memories`` and ``trading_post``.

Templates
---------

Last Year
+++++++++

There were 17 templates used last year:

+-----------------+---------------------------------------------------------+
| 400             | Bad Request Error page                                  |
+-----------------+---------------------------------------------------------+
| 403             | Permission Error page                                   |
+-----------------+---------------------------------------------------------+
| 404             | Page Not Found Error page                               |
+-----------------+---------------------------------------------------------+
| 500             | Server Error page                                       |
+-----------------+---------------------------------------------------------+
| admin_mail      | a page I used for sending e-mails                       |
+-----------------+---------------------------------------------------------+
| bad_login       | for an incorrect username and/or password (duplicate?)  |
+-----------------+---------------------------------------------------------+
| base            | the html info and references to the header and footer   |
+-----------------+---------------------------------------------------------+
| comment         | page for users to add comments                          |
+-----------------+---------------------------------------------------------+
| footer          | the footer of every web page                            |
+-----------------+---------------------------------------------------------+
| gift_list       | the main page with all the gifts                        |
+-----------------+---------------------------------------------------------+
| header          | the header of every web page                            |
+-----------------+---------------------------------------------------------+
| invalid_login   | for an incorrect username and/or password (duplicate?)  |
+-----------------+---------------------------------------------------------+
| loggedin        | I don't think this was actually used in the final form  |
+-----------------+---------------------------------------------------------+
| login           | Login page displayed to unauthenticated users           |
+-----------------+---------------------------------------------------------+
| logout          | I don't think I used this in the final project          |
+-----------------+---------------------------------------------------------+
| sent_mail       | showed status message and button to return to main page |
+-----------------+---------------------------------------------------------+
| single_gift     | large picture of single gift, detail page               |
+-----------------+---------------------------------------------------------+

This Year
+++++++++

Here is a start:

+-----------------+---------------------------------------------------------+
| 400             | Bad Request Error page                                  |
+-----------------+---------------------------------------------------------+
| 403             | Permission Error page                                   |
+-----------------+---------------------------------------------------------+
| 404             | Page Not Found Error page                               |
+-----------------+---------------------------------------------------------+
| 500             | Server Error page                                       |
+-----------------+---------------------------------------------------------+
| admin_mail      | a page I used for sending e-mails                       |
+-----------------+---------------------------------------------------------+
| base            | the html info and references to the header and footer   |
+-----------------+---------------------------------------------------------+
| comment         | page for users to add comments                          |
+-----------------+---------------------------------------------------------+
| footer          | the footer of every web page                            |
+-----------------+---------------------------------------------------------+
| gift_list       | the main page with all the gifts                        |
+-----------------+---------------------------------------------------------+
| header          | the header of every web page                            |
+-----------------+---------------------------------------------------------+
| invalid_login   | for an incorrect username and/or password               |
+-----------------+---------------------------------------------------------+
| login           | Login page displayed to unauthenticated users           |
+-----------------+---------------------------------------------------------+
| logout          | I don't think I used this in the final project          |
+-----------------+---------------------------------------------------------+
| sent_mail       | showed status message and button to return to main page |
+-----------------+---------------------------------------------------------+
| single_gift     | large picture of single gift, detail page               |
+-----------------+---------------------------------------------------------+
| trade_detail    | displays the conversation pertaining to a trade         |
+-----------------+---------------------------------------------------------+
| trade_request   | a page for making a request for a trade                 |
+-----------------+---------------------------------------------------------+

.. _url_label:

URLs.py files
-------------

Last Year
+++++++++

Both the christmas15 folder (this year's config folder) and the gift exchange app had urls.py files. They are given
below:

christmas15.urls.py::

    urlpatterns = [
        url(r'^$', include('gift_exchange.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^gift/', include('gift_exchange.urls')),
        url(r'^mail/', include('gift_exchange.urls')),

        # user authorization urls
        url(r'^accounts/login/$', 'christmas15.views.login', name='login'),
        url(r'^accounts/auth/$', 'christmas15.views.auth_view', name='authorization'),
        url(r'^accounts/logout/$', 'christmas15.views.logout', name='logout'),
        url(r'^accounts/invalid/$', 'christmas15.views.invalid_login', name='invalid'),
    ]

gift_exchange.urls.py::

    urlpatterns = [

        url(r'^(?P<gift_number>[0-9]+)/$', views.single_gift, name='single_gift'),

        # gift_exchange urls
        url(r'^$', 'gift_exchange.views.gifts', name='root'),
        url(r'^select/$', 'gift_exchange.views.select', name='select'),
        url(r'^comment/$', 'gift_exchange.views.comment', name='comment'),
        url(r'^changedmind/$', 'gift_exchange.views.changemind', name='changemind'),
        url(r'^send_all/$', 'gift_exchange.views.full_group_mail', name='send_to_all'),
        url(r'^invitation/$', 'gift_exchange.views.invitation', name='send_invitation'),
    ]

These urlpatterns result in the following functionality as tested by going to the live site and typing in each of the
urls.  The Server Error for sending the invitation might be because of the site's e-mail being hacked and taken offline
by webfaction.  The Server Errors for the buttons, select, comment and changedmind, might be because no gift
information was sent.

+--------------------+-------------------------------------+----------------------------------+
| url                | view                                | What happened when entering url  |
+====================+=====================================+==================================+
| /                  | gift_exchange.views.gifts           | Got to gift list at root         |
+--------------------+-------------------------------------+----------------------------------+
| /admin/            | built-in admin site                 | Got to built-in admin site       |
+--------------------+-------------------------------------+----------------------------------+
| /gift/n/           | views.single_gift                   | Detail view of gift n            |
+--------------------+-------------------------------------+----------------------------------+
| /mail/send_all/    | gift_exchange.views.full_group_mail | Page to write and send e-mail    |
+--------------------+-------------------------------------+----------------------------------+
| /mail/invitation/  | gift_exchange.views.invitation      | ServerError                      |
+--------------------+-------------------------------------+----------------------------------+
| /accounts/login/   | christmas15.views.login             | Login page                       |
+--------------------+-------------------------------------+----------------------------------+
| /accounts/auth/    | christmas15.views.auth_view         | always sends to accounts/invalid |
+--------------------+-------------------------------------+----------------------------------+
| /accounts/logout/  | christmas15.views.logout            | Login page                       |
+--------------------+-------------------------------------+----------------------------------+
| /accounts/invalid/ | christmas15.views.invalid_login     | Invalid login page               |
+--------------------+-------------------------------------+----------------------------------+
| /gift/select/      | gift_exchange.views.select          | Server Error                     |
+--------------------+-------------------------------------+----------------------------------+
| /gift/comment/     |gift_exchange.views.comment          | Server Error                     |
+--------------------+-------------------------------------+----------------------------------+
| /gift/changedmind/ | gift_exchange.views.changemind      | Server Error                     |
+--------------------+-------------------------------------+----------------------------------+

This Year
+++++++++

I'm thinking I should have more apps this year and a clearer demarcation between them. I noticed in BnBDevelopment that
the config directory had a ``urls.py`` but not a ``views.py``. The same is true in tdd2, though the directory is called
superlists within the superlists folder instead of being named config. The same is also true for the DjangoUnleashed
project but, there again, the config file is called suorganizer inside of another suorganizer folder. I notice that
there is already a ``urls.py`` file in my ``config`` folder in the c16Development project. It connects /admin/ to the
``admin.site.urls``.

So, let's think in terms of the following apps:

+----------------+-------------------------------------------------------------------+
| app name       | app functions                                                     |
+================+===================================================================+
| gift_organizer | displays gift list, manages selections, comments, and trading     |
+----------------+-------------------------------------------------------------------+
| mail           | manages sending admin e-mails and trading e-mails                 |
+----------------+-------------------------------------------------------------------+
| memories       | manages the creation and display of Christmas memories            |
+----------------+-------------------------------------------------------------------+

.. _urls_views_templates:

Here are my thoughts on some urls and their corresponding views:

+----------------------------+------------------------------+--------------------------------+
| url                        | view                         | template                       |
+============================+==============================+================================+
| /                          | authenticate                 | login.html or redirect to list |
+----------------------------+------------------------------+--------------------------------+
| /gift/list/                | gift_organizer.giftlist      | gift_list.html                 |
+----------------------------+------------------------------+--------------------------------+
| /gift/n/                   | gift_organizer.gift          | single_gift.html               |
+----------------------------+------------------------------+--------------------------------+
| /gift/comment/             | gift_organizer.comment       | get_comment.html               |
+----------------------------+------------------------------+--------------------------------+
| /gift/comment/edit/        | gift_organizer.edit_comment  | edit_comment.html              |
+----------------------------+------------------------------+--------------------------------+
| /gift/comment/delete/      | gift_organizer.erase_comment | delete_comment.html            |
+----------------------------+------------------------------+--------------------------------+
| /gift/trade/initiate/      | gift_organizer.request_trade | trade_request.html             |
+----------------------------+------------------------------+--------------------------------+
| /gift/trade/respond/       | gift_organizer.answer_trade  | trade_answer.html              |
+----------------------------+------------------------------+--------------------------------+
| /gift/trade/remark/        | gift_organizer.remark        | trade_remark.html              |
+----------------------------+------------------------------+--------------------------------+
| /gift/trade/remark/edit/   | gift_organizer.remark.edit   | edit_trade_remark.html         |
+----------------------------+------------------------------+--------------------------------+
| /gift/trade/remark/delete/ | gift_organizer.erase_remark  | delete_remark.html             |
+----------------------------+------------------------------+--------------------------------+
| /mail/invitation/          | mail.send_invitation         | invitation.html                |
+----------------------------+------------------------------+--------------------------------+
| /mail/compose/             | mail.compose                 | compose.html                   |
+----------------------------+------------------------------+--------------------------------+
| /memories/create/          | memories.create              | create_memory.html             |
+----------------------------+------------------------------+--------------------------------+
| /memories/edit/            | memories.edit                | edit_memory.html               |
+----------------------------+------------------------------+--------------------------------+
| /memories/delete/          | memories.erase               | delete_memory.html             |
+----------------------------+------------------------------+--------------------------------+

As I wrote the table above I realized that many of the html pages and some of the models are repeating themselves. The
delete or erase views will always go to some sort of "Are you sure?" page which should be able to be designed so that
one html page can provide functionality for deleting gift comments, trade remarks and memories. I suppose the same is
true for composing each of those texts. Perhaps I can have just one comment model with a field indicating the sort of
comment being made: gift comment, trade remark or memory. I'll have to think about that though.

Views
-----

Views, it seems to me, control the information that gets to the html templates to be displayed on the page. Views are
entered by means of the urlconf patterns in the various urls.py files.

Last Year
+++++++++

Last year I used function based views exclusively. I either didn't know about, or didn't understand class based views.

The christmas15 folder, this year's config folder, had a views.py file that contained 4 views as outlined in the
following table:

+------------------------+-------------+-------------------------------------------------+
| Name                   | Parameters  | Functions                                       |
+========================+=============+=================================================+
| login                  | request     | created a csrf context and rendered             |
|                        |             | ``login.html``                                  |
+------------------------+-------------+-------------------------------------------------+
| auth_view              | request     | checks to see that the user is authentic. If    |
|                        |             | so, redirects to '/', if not, redirects to      |
|                        |             | '/accounts/invalid'                             |
+------------------------+-------------+-------------------------------------------------+
| invalid_login          | request     | renders the ``invalid_login.html`` page.        |
+------------------------+-------------+-------------------------------------------------+
| logout                 | request     | renders the ``login.html`` page.                |
+------------------------+-------------+-------------------------------------------------+

I wonder, should I create a separate app for authentication? It doesn't seem to make sense to use what is now the
cofig folder for things that should apply to an individual application. I'll have to study some more -- probably
*Django Unleashed*.

The ``gift_exchange`` app had 7 views and one helper function as outlined in the following table:

+------------------------+-------------+-------------------------------------------------+
| Name                   | Parameters  | Functions                                       |
+========================+=============+=================================================+
| gifts                  | request     | selected random memory; created context of      |
|                        |             | ``user``, ``giftlist`` and the selected memory; |
|                        |             | displayed either ``gift_list.html`` or          |
|                        |             | ``login.html`` depending on authentication      |
+------------------------+-------------+-------------------------------------------------+
| single_gift            | request     | created context of ``user`` and ``gift``        |
|                        | gift_number | as per ``gift_number``; displayed               |
|                        |             | ``single_gift.html`` or ``login.html``          |
|                        |             | depending on user authentication.               |
+------------------------+-------------+-------------------------------------------------+
| select                 | request     | handled the selection of a gift by a user;      |
|                        |             | created context of ``user`` and ``giftlist`` to |
|                        |             | redirect to the '/' page.                       |
+------------------------+-------------+-------------------------------------------------+
| changemind             | request     | unselected the previously chosen gift; created  |
|                        |             | context of ``user`` and ``giftlist`` to         |
|                        |             | redirect to the '/' page.                       |
+------------------------+-------------+-------------------------------------------------+
| comment                | request     | if comment is present, saved it (adding last    |
|                        |             | names to Brians); redirect to '/' page with     |
|                        |             | context of ``user`` and ``giftlist``            |
|                        |             | otherwise, with a context of ``user`` and       |
|                        |             | ``gift`` rendered the ``comment.html`` page.    |
+------------------------+-------------+-------------------------------------------------+
| full_group_mail        | request     | if ``message_text`` is present, send the e-mail |
|                        |             | otherwise go to the ``admin_mail.html`` page    |
|                        |             | with the context of ``user``.                   |
+------------------------+-------------+-------------------------------------------------+
| invitation             | request     | automatically sends an invitation message to    |
|                        |             | users then renders the ``sent_mail.html`` page. |
|                        |             | This view uses a helper function to create the  |
|                        |             | raw text for the e-mail and then fills in the   |
|                        |             | name, username, and password in the appropriate |
|                        |             | places.                                         |
+------------------------+-------------+-------------------------------------------------+

The ``memories`` app had no views.


This Year
+++++++++

I probably still don't understand class based views, but that is what I am going to try to use this year. If nothing
else, it should give me an idea of how they work.

.. _trading_post_ideas:

Trading Post Details
--------------------

Here are my current ideas:

Suppose Bill wants gift number 2 but Janet has already selected it. Bill can click on the Trade button that appears for
him next to Janet's gift number 2. This results in Bill opening a page where he can compose an e-mail asking Janet for a
trade. Certain lines in the e-mail are already set. The subject line is "Bill asks for a trade with Janet." The content
will say something along the lines of::

    Bill would like to trade gift number <x> for your gift number <y>. He says: <reason>.

    If you agree to this trade, go to <website> and click on the 'Accept Trade' button that now appears next to gift
    number <x> when you log in and send him your response.

    If you would rather not trade for gift number <y> you can click the 'Decline Trade' button that now appears next to
    gift number <x> when you log in and send him a response.

    These extra buttons only appear if the site recognizes that you are logged in. Each one will send you to a page
    where you can add information to your acceptance or decline. For instance, you might want to thank him for the kind
    offer but you were quite happy with gift number <x>.

If a gift is up to be traded, other people can offer to trade for that same gift.

If an individual offers to trade a gift with another person they can change their mind and take back the offer but,
until they do so, or the offer is declined, they cannot attempt any more trades.

When a trade is accepted the site takes care of switching the gifts.

Note that someone offering a trade must first have selected a gift themselves.

.. _replacement_for_trading_post:

Second Thoughts
---------------

After writing the above description of the "Trading Post" I don't think it's worth the trouble. It adds a lot of
complexity to the programming for something that will probably not engage the interest of family members.

Instead, I thought it might be good to write an ongoing Christmas story: one of those things where one person writes a
sentence of the story, leaving a tantalizing beginning of the next sentence and the next family member that "calls for
it" can write the next sentence. This seems more engaging but the complication here is locking out the possibility of
two people working on the same sentence at the same time. What should it do? Branch into two stories? That might be fun.
Or should the second person be locked out until the first person is finished. That would involve locking out the first
person if he or she has been "hogging" the story for a predetermined amount of time. At the moment, I don't know how to
do any of that. Still, I think it's worth looking into.

Christmas Story
---------------

I will write out here how I imagine it to work and how to handle any problems I foresee.

Near the top of each web page should be a couple of buttons. One for adding memories, the other for adding a line to our
2016 Christmas story. I can start it out with a sentence like "It was the morning before Christmas and he was excited,
the big day was almost here! Yet he felt a bit of anxiety because..."  Whoever clicks on the button first locks down the
story until they have added their contribution or until their time is up and another family member clicks the button to
add a line. This means I will have to have a means of keeping track of whether the story is locked down and who locked
it and when they locked it. This would have to be checked before displaying the page header, which contains the buttons,
so that it knows whether to display the button or a message saying "Jim is adding to the story now. Try again later."
The button would be displayed if no one is working on the story or if someone WAS working on the story but their time
had been exceeded. Here are the global variables needed:

    * locked: boolean
    * user: User who is adding a sentence
    * time: time the story was locked by the user

It seems thin information could be saved in a model that would have only one instance, but I wonder of Django, or
Python, has a better way to do that.

November 11, 2016:

In a conversation with Janet last night, in connection with what she did for Marisa's long-distance wedding shower, I
got the idea that a "Who Am I" game might be a good thing to try. Family members could give clues to their identity and
others could guess who they are. The system would know who entered the clue(s) and could keep track of how many each
family member guessed correctly. No other clues, such as listing who has left clues -- a dead giveaway -- would have to
be given.



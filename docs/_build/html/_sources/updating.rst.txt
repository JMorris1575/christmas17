Updating the Website
====================

This document chronicles the changes I made to Christmas 2017 from Christmas 2016. It may end up containing notes about
sources of files and notes about css and html in general.

Initial Thoughts and Plans
--------------------------

.. index:: Plans; initial

Plans at the Beginning
++++++++++++++++++++++

.. index:: Design; header

Design and Appearance
*********************

I envision a different, more elegant, look than I've had in the past. The old site looks rather garish to me now. I'm
thinking about the header being a red gradient bar with an icon at the left and the title "Christmas 2017" just to the
right of that in golden letters. I've started to create a model in Gimp and I like the looks of it so far.

I don't think I want the login to be part of the header. I'd like a separate page for that so that, when someone logs
in incorrectly it will be more clear what happened instead of just having the username disappear.

Also, I think the design of the header will be nicer, and more elegant, if the current memory displayed under the header
instead of as part of it. Perhaps in a box below the header like the introduction -- which no one would read after the
first time, if that -- does now.

.. index:: Apps; ideas

Apps, New and Old
*****************

I will keep the same elements I got working last year, at least if Janet wants to come up with another set of questions.
But then, perhaps I could follow her style and make them up myself.

I'd like to get the Story app working, something we could use to make a shared story. I still haven't quite figured out
how to handle the case where two people are writing an addition at the same time. Can I branch the story? Can I block
out one person until the other finishes -- or block the first person's entry after a certain time limit? Still to be
worked out.

.. _trivia_desc:

I've also thought of a Christmas Trivia section where family members answer trivia questions about Christmas and get
scored for their attempts. I think that will be easy enough to program, but I need to find a good source of questions.
It would be perfect to find a Christmas Trivia game already out there but then I'd probably be violating the copyright
of whoever produced it. Perhaps I can look online for Christmas Trivia.

Here are some in no particular order:

* http://xmasfun.com/Trivia.aspx
* https://icebreakerideas.com/christmas-trivia/
* http://www.christmastrivia.net/printable-general-trivia
* http://www.christmastrivia.net/
* http://laffgaff.com/christmas-trivia-questions-and-answers/

Some of them may have repeats, especially christmastrivia.net, but they should give me some ideas of questions and
kinds of questions I can ask myself.

Research
--------

.. index:: Fonts; sources

Fonts
+++++

I don't remember the font site or sites I've used before so I will try to search some out. Again, in no particular
order:

* https://fontlibrary.org/
* https://fonts.google.com/
* http://www.fontspace.com/category/open  -- this may be one I've used before
* https://www.fontsquirrel.com/

.. index:: Reference; html, Reference; css

.. _w3schools:

Html and CSS Assistance
+++++++++++++++++++++++

Color Picker: https://www.w3schools.com/colors/colors_picker.asp

Html Reference: https://www.w3schools.com/tags/default.asp

CSS Reference: https://www.w3schools.com/cssref/default.asp

Improving the Header
--------------------

Steps to Improve Header
+++++++++++++++++++++++

#. Improve the appearance of the banner by changing the font and background color.
#. Get the memories to display below the banner and the menu choices.
#. Improve the appearance of the memory section.
#. Develop a new banner image.
#. Separate the login page from the header.

   #. Develop two forms of the header: one for unauthenticated users and one for authenticated users.
   #. Develop a login page and a failed login page


.. index:: Fonts; choices

Choosing Fonts
++++++++++++++

Local Fonts
***********

The header font, the one with the website's title "Christmas 2017" this year is set in the header. Last year it was
Gregorian. This year I might try OldStandard.

I didn't particularly like that, even in its italic form. I'll go to fontspace.com and try some script fonts.

Also, I'm wondering if I should name the fonts something more generic, or more descriptive of their usage, in the css
file so that when I change my mind about a font I only have to change it in one place.

I decided to call it "Banner_Font" and it was easy to test different fonts that way. I've downloaded something called
"HappyFont" which I will try for a while.

.. index:: Fonts; web fonts

Web Fonts
*********

I thought I'd try the font "Great Vibes" for the banner text from fonts.google.com. I could download it but it might be
better to learn how to use it as a web font which the user's browser downloads from the internet. From pages 162-163 in
*The CSS Pocket Guide* and from Google's guide at https://developers.google.com/fonts/docs/getting_started I'm thinking
what I need to do is as follows:

.. index:: Problems; displaying web fonts

In ``christmas17.css`` add::

    @font-face {
        font-family: "Banner_Font";
        src: url("https://fonts.googleapis.com/css?family=Great+Vibes");
        }

then, in the header selector::

    header {
        ...
        font-family: Banner_Font, cursive;
        ...
    }

Let's see if that works...

Hmm... So far, whether I use it as a web font or download it and use it locally, Great Vibes doesn't display. Instead it
shows the backup font, which I have indicated as ``cursive`` but seems to give me something like Comic Sans. Perhaps it
doesn't like the bold or italic settings in the .css file. I will comment them out and see.

No, it wasn't that. The problem with the downloaded local version was that I spelled it wrong, it was supposed to be
called ``GreatVibes-Regular`` but I wrote ``GreatVibes-Reglar``. Meanwhile, when I follow the instructions on google's
site referenced above and include::

    <link href="https://fonts.googleapis.com/css?family=Great+Vibes" rel="stylesheet">

in the <head> section of ``base.html`` and eliminate the @font-face section above and enter::

    font-family: 'Great Fonts', cursive;

into the ``header`` selector it works as it is supposed to. Turn off the bold in the header, change the size to 400%
in the ``.large`` selector and I like the way it looks. I will have to find a better way to do the bold text since
turning if off in the header also affected the "Merry Christmas Jim" at the right.

Speaking of which, the google site suggested "Open Sans" as a font to go with "Great Vibes" so I will try to include
that too by modifying my <link> tag to say::

    <link href="https://fonts.googleapis.com/css?family=Great+Vibes|Open+Sans" rel="stylesheet">

That worked without any problems.

.. index:: Updating; contents

Header Content
++++++++++++++

I had to change ``base.html`` to refer to ``christmas17.css`` and give "Christmas 2017" as the title of the page. So far
I have only changed ``header.html`` to say "Christmas 2017" in the banner rather than "Christmas 2016."

Header Styling
++++++++++++++

Changing the background to what seems to me an elegant red color and the text to a golden yellow was not very
difficult. Under *header* in ``christmas17.css``, I set the background-color to #cc0000 and the color to #ffbb33. I may
want to tweak those colors later.

Moving the Memories Display
+++++++++++++++++++++++++++

This should be a fairly simple change to the ``header.html`` file. My first attempt was to simply take the section
labelled "Memory Block" and move it outside the <header></header> tags. That seemed to work! First time too!

Improving Memory Appearance
+++++++++++++++++++++++++++

The most difficult part here will probably be in deciding how I want it to look. Perhaps a box with a different
background color (pale yellow?) directly below the menu tabs stretching all the way across the screen, but always the
same height. Have the text be left justified but centered in the box vertically. (Is this possible in html?)

:ref:`Later<add_skeleton>` I decided to add skeleton.css to the program since I have been learning to use it in my
Confirmation Website. Now I will try to pretty up the Memory display using Skeleton.

That didn't work, for reasons stated below. I will try to modify the ``.memory-box`` class in ``christmas17.css``

New Banner Image
++++++++++++++++

I've created an image of three Christmas ornaments in Blender. It still needs work but it's a decent start.

Creating a Separate Login Page
++++++++++++++++++++++++++++++

That turned out to be a bit easier than I expected. I just moved the login section out of the header and into the
pre-existing separate login page. It took a while to re-learn how to center the elements by setting their size in css
and then setting margins like this::

    margin: 20px auto 20px auto;

I got this from the css reference pages listed :ref:`above.<w3schools>`

Updating the Gift Pictures
--------------------------

I have simply copied and pasted the new images and their thumbnails to ``gifts\static\gifts\images\``. Now I have to
update the database to indicate that none of the gifts are chosen.

Hmm... either I did that already or the local version of the database didn't have any selected gifts.

Adding Janet's New Questions
----------------------------

The New Questions
+++++++++++++++++

I got an e-mail from Janet today (11-26-2017) with a set of 19 questions -- not all about Christmas. Here is what she
sent::

    Hi Jim
    Here are a bunch of questions to choose from or to reject.  No special order.
    1.  If you could write a letter of gratitude to your ancestors, who would you pick and what would you say?
    2.  What is your earliest childhood memory?
    3.  What is your favorite Christmas tradition?
    4.  What story do you remember being told from the childhood of your mother or father?
    5.  What was your favorite game to play outside when you were a child?
    6.  What was your favorite game to play inside when you were a child?
    7.  Tell something that you remember about a neighbor from your childhood.
    8.  What "saying" or advice do you remember from your childhood.
    9.  What is your favorite Christmas TV program?
    10.When should radio stations start playing Christmas music?
    11.When should Christmas decorations go up?
    12. Real tree or artificial? and why?
    13. If you could be a character in a holiday movie, who would you be and why?
    14. When you close your eyes and think of your "happy place", where is it?
    15. Finish this thought, "It wouldn't be Christmas without ______________".  Please exclude the obvious answer.
    16. What commercial from childhood can you say or sing from memory?
    17. What is your favorite dessert?
    18. Which celebrity would you want to have as a guest?  What would you get him or her for Christmas?
    19. If you could bring any cartoon or animated character to life, who would it be and why?


    Have fun!
    Love,

    Janet

Here are my edited and adapted versions::

    1.  If you could write a letter of gratitude to one of your ancestors, who would you pick and what would you say?
    2.  What is your earliest childhood Christmas memory?
    3.  What is your favorite Christmas tradition?
    4.  What story do you remember being told from the childhood of your mother or father?
    5.  What was your favorite game to play outside when you were a child?
    6.  What was your favorite game to play inside when you were a child?
    7.  Tell something that you remember about a neighbor from your childhood.
    8.  What "saying" or advice do you remember from your childhood.
    9.  What is your favorite Christmas TV program?
    10. When should radio stations start playing Christmas music?
    11. When should Christmas decorations go up?
    12. Real tree or artificial? and why?
    13. If you could be a character in a holiday movie, who would you be and why?
    14. When you close your eyes and think of your "happy place", where is it?
    15. Finish this thought, "It wouldn't be Christmas without ______________".  Please exclude the obvious answer.
    16. What commercial from childhood can you say or sing from memory?
    17. What is your favorite dessert?
    18. Which celebrity would you want to have as a guest, and what would you get him or her for Christmas?
    19. If you could bring any cartoon or animated character to life, who would it be and why?

Here is a list in the order in which the questions will appear::

    What commercial from childhood can you say or sing from memory?
    If you could bring any cartoon or animated character to life, who would it be and why?
    If you could write a letter of gratitude to one of your ancestors, who would you pick and what would you say?
    What story do you remember being told from the childhood of your mother or father?
    What is your favorite dessert?
    Tell something that you remember about a neighbor from your childhood.
    Which celebrity would you want to have as a guest, and what would you get him or her for Christmas?
    If you could be a character in a holiday movie, who would you be and why?
    Finish this thought, "It wouldn't be Christmas without ______________".  Please exclude the obvious answer.
    What was your favorite game to play outside when you were a child?
    What was your favorite game to play inside when you were a child?
    What "saying" or advice do you remember from your childhood.
    What is your favorite Christmas TV program?
    When should radio stations start playing Christmas music?
    When should Christmas decorations go up?
    Real tree or artificial? and why?
    What is your earliest childhood Christmas memory?
    When you close your eyes and think of your "happy place", where is it?
    What is your favorite Christmas tradition?

I will enter them with a start date of December 5, 2017 going up to December 23, 2017.

Modifying the Model
+++++++++++++++++++

To make the list of questions look better in the admin I modified the ``__str__`` function to return a string version of
the date followed by the question. I also changed the Meta class so that they listed in earlier-to-later order. Will
that affect the way they are displayed? First I will study the ``question_list.html`` file...

Nothing in ``question_list.html`` affected the order of the display. The actual determination is in the QuestionList
view. There, the list of questions is obtained as follows::

    Question.objects.filter(date__lte=datetime.date.today()).order_by('-date')

Thus the ordering is handled by the ``.order_by('-date')`` function and I can leave the Meta class in the model alone.

.. _add_skeleton:

Adding the Skeleton CSS Framework
---------------------------------

Since I have been using it in developing my Confirmation Website I find skeleton.css quite easy to work with. To use it
I need to put it, and its partner ``normalize.css`` into ``Christmas2017/static/site/css/`` along side of
``christmas17.css``. I will also have to include the lines::

    <link rel="stylesheet" type="text/css" href="{% static 'css/normalize.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/skeleton.css' %}">

into ``base.html`` just before the line linking in ``christmas17.css``.

Unfortunately, including skeleton.css on top of my existing ``christmas17.css`` created problems with the appearance of
the rest of the website. Most noticable was that the buttons all had the skeleton appearance and didn't fit in their
proper places. Also, the gift list appeared to be twelve columns wide. For now I commented out the links that enabled
the skeleton framework. To use it I would have to revamp the whole website. More than I want to do tonight.

.. index:: Problems; user profile model

Fixing the UserProfile Model
----------------------------

I tried to click the Select button for a gift but got strange errors about UserProfile not existing. It seemed to be
showing in ``/admin`` so I couldn't figure it out. Eventually I investigated by means of
``python manage.py dumpdata user.UserProfile`` and found only one object in the c17Development version of the database
but several elements in the c16Development version's database. I don't think I knew to copy it when I
:ref:`created<copy_database>` the c17Development database. Once I created a ``to_c17_profile.json`` file in c16 I could
use ``loaddata`` in c17 to copy it to the database. Then selecting gifts and adding memories worked again.

.. index:: Problems; git

Problems Understanding Git
--------------------------

The paragraph above had to be recreated from memory because I managed to delete the original. What happened was that I
tried to do a commit and couldn't because of something about the ``docs/_build/doctrees/`` files which I didn't want in
Git anyway. Not knowing how to get them out of Git in PyCharm, and foolishly believing I could just experiment without
harming anything, I tried a VCS.Git.Revert... and somehow included some of the \*.rst files in the revert. I'm guessing
that the revert replaced the selected \*.rst files with earlier versions and, since I hadn't gotten Commit to work, I
lost what I had added here, and probably in other files.

I believe the correct way to remove files from Git without removing them from the file system is::

    git rm --cached <filename>

but I would check this out before using it. For one thing, you may be able to do several files at once -- which I think
I may have done through::

    git rm --cached ../docs/_build/doctrees/*.*

but I'm not sure.

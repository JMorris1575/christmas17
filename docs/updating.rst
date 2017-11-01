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


New Applications
================

This document chronicles my attempts to add new apps to the Christmas 2017 website. I will start with the simpler one,
the Trivia app (:ref:`see initial description <trivia_desc>`), and then perhaps I will know enough to implement the
Story app. If other apps come to mind later I will document them here.

Building the Trivia App
-----------------------

Narrative Desription
++++++++++++++++++++

Bill visits the Christmas 2017 website and clicks on the "Trivia" menu item. He is the first one to do so. The first page
that displays tells him the rules of the game, mostly that he must answer the questions based on his own memory without
looking them up anywhere. Then he clicks the "I will play by the rules." button to see the first question.

The question page gives him the question and a chance to give his answer. Once his answer is given he is told whether
he is right or wrong and, if wrong, what the correct answer is. Once he has submitted his answer he cannot change it. In
this case, Bill is right and he is given a score of 100%. This appears on the same page that tells him he's right or
wrong. Since this is the first day for the trivia questions, and Bill has answered the only one there is, there is a
"Return to Scoreboard" button at the bottom which Bill clicks.  He is returned to the main trivia page and sees the
rules again but, instead of the "I will play by the rules" button there is a message which tells him he has completed
all of the available questions and that he can come back tomorrow for a new one.

But now he notices at the right there is a scoreboard column with his name listed as scoring 100% after answering one
question. Bill also notices a "Start the Conversation" button underneath the scoreboard. He doesn't have anything to
say so he ignores it and clicks on a different menu item and leaves the Trivia app.

Now Janet visits the website and clicks on the "Trivia" menu item. She sees the same page Bill did giving her the rules
and displaying the scoreboard with only Bill's name and score listed. She notices the "Start the Conversation" button
and clicks on it. This sends her to a page where she types "Atta boy Bill!" and clicks the "Submit" button. This sends
her back to the Rules page where she sees her conversation starter in a box under the scoreboard saying:
**Janet says: "Atta boy Bill!"** Now the button says "Add to the Conversation."

But Janet wanted to answer the trivia question and so clicks the "I will play by the rules button." She, too, answers
correctly. (That first question is an easy one!) Since there are still no more questions she also gets the "Return to
Scoreboard" button. When she clicks it she sees that her name and score have been added to the scoreboard under Bill's.
Seeing there are no more questions she clicks on another menu item.

The next day Dave comes to the Trivia page, reads the rules, decides not to add to the conversation, and agrees to play
by the rules. He is presented with the first question, which he answers and gets right. On his answer page he sees a
"Continue" button which sends him to the second question which, alas, he gets wrong. Coming back to the scoreboard he
sees his name in first place in the section of those who have answered two questions.

As each family member visits the Trivia section and answers the questions their score is updated and listed in a section
corresponding to how many questions they have answered. The ones on top are the ones who have answered the most.

Now Bill returns to the Trivia section and can answer the next question. He gets it right and so, when he returns to the
scoreboard his name has moved to the top of the top section, above Dave's.

Information Gleaned from Narrative
++++++++++++++++++++++++++++++++++

Template Pages
**************

I think there will be three basic pages:

* Entry page: tells the rules, displays the scoreboard,the ongoing conversation and the "Play by the Rules" button.

* Question page: presents the questions, supplies radio buttons for the answers and a Submit button.

* Results page: tells the user right or wrong, gives current score and supplies "Continue" or "Return" button.

What Needs to be Remembered
***************************

* the questions
* the possible answers to display
* the correct answer
* each user's answers to each question
* each user's last-answered question (their question count)
* each user's correct answer count
* each conversation entry's text
* each conversation entry's author

URLs
++++

Here are the urls that should work for the Trivia app:

+--------------------------+-------------------------------------------------+
| URL                      | Page(s) Addressed                               |
+==========================+=================================================+
| /trivia/scoreboard/      | scoreboard page (scoreboard.html)               |
+--------------------------+-------------------------------------------------+
| /trivia/question/n/      | question n's page (triv_quest.html)             |
+--------------------------+-------------------------------------------------+
| /trivia/result/n/        | question n's results page (triv_result.html)    |
+--------------------------+-------------------------------------------------+

.. index:: Models; designing

Models
++++++

Initial Thoughts
****************

It has been a while since I have designed a model in Django so it isn't entirely clear to me how to start. I suppose
kind of a top-down approach will be helpful.

What do I need? A set of database models to help manage the Trivia application.

What do they need to contain? At first thought they need to contain and provide access to:

* the questions with their answers and the correct answer and the index number of the question
* a user's answer to each question, which ones they've answered correctly and the number of questions they've answered
* the conversation entries along with the identity of the user making that entry

This suggests to me that three models might be necessary, though I know a couple of them will probably need supporting
models:

* a TriviaQuestion model containing::

    The index number of the question
    The text of the question
    A list of choices for the possible answers
    An indicator as to which answer is the correct one

* a TriviaUserProgress model containing::

    the user's id
    the number of questions they've answered
    a list of their responses and which ones were correct

* a TriviaConversation model containing::

    the text of each entry to the conversation
    the identity of the user making that entry

But each model is only a table and the first two models outlined above require variable length lists which may be best
to include in a different model. Thus there may be two other models necessary:

* a TriviaAnswer model containing::

    a reference to the question to which this selection applies
    the text of the selection
    whether it is the correct selection for this question

* a TriviaUserResponse model containing::

    a reference to the user
    a reference to the question being answered
    a reference to the user's answer
    a reference to whether their answer was correct

So it seems that five models may be necessary.

.. index:: Sphinx; adding empty lines

Models for the Trivia App
*************************

So here is my first attempt to spell out the models needed for the Trivia app:

.. csv-table:: **TriviaQuestion Model**
   :header: "Field Name", "Type", "Parameters", "Notes"
   :widths: auto

   question_number, IntegerField, primary_key=True, so that questions can be moved
   trivia_question_text, CharField,, the question itself
   tried, IntegerField,, the number of users who have responded
   correct, IntegerField,, the number of users getting it right

|

.. csv-table:: **TriviaAnswerChoices Model**
   :header: "Field Name", "Type", "Parameters", "Notes"
   :widths: auto

   choice_number, Integer, primary_key=True, so that responses may be moved
   question, ForeignKey, 'TriviaQuestion', which question this refers to
   choice_text, CharField, , the possible answer
   correct, Boolean, , True if correct False otherwise

|

.. csv-table:: **TriviaUserProgress Model**
   :header: "Field Name", "Type", "Parameters", "Notes"
   :widths: auto

   trivia_user, ForeignKey, settings.AUTH_USER_MODEL, marks which user
   answered_questions, Integer, , tells how many questions they've answered
   questions_correct, Integer, , tells how many questions they've answered correctly

|

.. csv-table:: **TriviaUserResponses Model**
   :header: "Field Name", "Type", "Parameters", "Notes"
   :widths: auto

   responder, ForeignKey, settings.AUTH_USER_MODEL, marks which user
   question, Integer, , tells which question this refers to
   user_response, ForeignKey, 'TriviaAnswerChoices', tells which response they gave
   answer_correct, Boolean, , tells whether this answer was right or wrong

|

.. csv-table:: **TriviaConversation Model**
   :header: "Field Name", "Type", "Parameters", "Notes"
   :widths: auto

   entry, CharField, max_length=256, the user's addition to the conversation
   user, ForeignKey, settings.AUTH_USER_MODEL, gives the author's identity




What the Views Have to Do
+++++++++++++++++++++++++


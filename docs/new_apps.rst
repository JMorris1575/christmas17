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

Models
++++++

URL and Menu Item
+++++++++++++++++

What the Views Have to Do
+++++++++++++++++++++++++


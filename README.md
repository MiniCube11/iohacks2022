# FEMevents

## Inspiration

According to the AAUW, women only make up 28% of the workforce in STEM.

Over the years, people have tried to fix this, by empowering young girls and motivating them to work in STEM fields by making events, like Hackathons and seminars directed towards female and non-binary people, to make it easier to participate in something that is currently so male-dominated

Still, not a lot of people go to these events.

We know it’s not because girls don’t want to participate-- they *do* have an interest in these subjects. But because there’s nowhere to find these events-- no site where they’re all listed, no efficient way to get ahold of them all-- girls are oftentimes pushed away because they don’t see any opportunity where they would thrive and meet peers alike.

In order to fix the STEM gap, we need to solve the *root* of the problem.

Enter FEMevents.

## What it does

**FEMevents** is a website where people who identify as female or non-binary can find events directed towards them quickly. It is intended to be a platform where people can post and find events. This way, it is easy: for students with an interest to find them, educators that want to help, and people who run events.

**FEMevents** also allows users to submit events, which need to be approved by a moderator before going live to the site. Users will receive an email notification once an event is published. This way, it is quick and easy to get information.

## How we built it

The user interface is built with HTML and CSS, using Jinja templating in Flask.

The app is built with a Flask backend, which is responsible for:
 - Handling the routes for the app
 - Storing and retrieving data (user, events) from the PostgreSQL database
 - Connecting to Google OAuth to authenticate the user
 - Sending emails to notify the user of new events
 - Rendering Jinja templates

## Challenges we ran into

It took much longer than expected to implement the add event form-- we realized the form could not validate because the datefield was not returning date objects as expected.

## Accomplishments that we’re proud of

We are proud of creating a functional app in two days, as well as creating a decent interface (while drinking sufficient amounts of water, sleeping a decent amount, and not acquiring too much back pain-- lesson learned from last hackathon).

## What we learned

We learned how to use Figma more efficiently as a team, and learned to use a different, better video editing software.

## What's next

Here are some features that we want to implement in the future:
 - Find new events automatically through web scraping
 - Google map that shows the user the closest events to their location
 - Page for listing useful resources

## Team Members
Acon, Ching Lam - Two grade 10's in Waterloo interested in Computer Science

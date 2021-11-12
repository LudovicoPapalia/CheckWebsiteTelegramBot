# CheckWebsiteTelegramBot
This bot should check if there is a change in a website using an hash. if there is, it notify all users of the bot using telegram

I wanted to create a "private" bot for telegram

what should it do:

it checks a list of websites, it do the hash of the website and if someting is changed
in one of the sites, it sends a message to all users (i know, but for now it's ok) saying
that something change on the website

if you send a normal message it should check if it's a valid url
if it is, it ads the url to the list of urls

every cycle for ever till deactivated
    if the hash exist
        it check the hash.
            if the hash is the same of the previous chek,
                it do nothing
            if the hash it's different,
                it notify all the users
    if the hash doesn't exist
        it saves the new hash in a dictionary using as a key the position of the site in the list and as value the hash

Probably i've done some stupid error, i'm still learning python so i'm not able to fix it
if tou want to use part of this project or fixing this \ giving me some tips to fix this i would be very grateful!
If you create a new project from this please link it in the comments, i would loe to see it to learn!



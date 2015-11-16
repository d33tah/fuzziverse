# fuzziverse

This is an application I created in order to keep track of my experiments with [american fuzzy lop][1].

![screenshot](https://imgur.com/9r5ybCW.jpg)

Note: this screenshot might be out of date.

[1]: http://lcamtuf.coredump.cx/afl/

# Installation and startup

Run the following commands:

```
pip install -r requirements.txt
./manage.py makemigrations fuzziverse
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

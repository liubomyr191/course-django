"""
Using This Code Example
=========================
The code examples provided are provided by Daniel and Audrey Feldroy of
Feldroy to help you reference Django Crash Course. Code samples follow
PEP-0008, with exceptions made for the purposes of improving book
formatting. Example code is provided "as is".

Permissions
============
In general, you may use the code we've provided with this book in your
programs and documentation. You do not need to contact us for permission
unless you're reproducing a significant portion of the code and using it in
commercial educational distributions. Examples:
* Writing an education program or book that uses several chunks of code from
    this course requires permission.
* Selling or distributing a digital package from material taken from this
    book does require permission.
* Answering a question by citing this book and quoting example code does not
    require permission.
* Incorporating a significant amount of example code from this book into your
    product's documentation does require permission.
Attributions usually include the title, author, publisher and an ISBN. For
example, "Django Crash Course, by Daniel and
Audrey Feldroy. Copyright 2020 Feldroy."

If you feel your use of code examples falls outside fair use of the permission
given here, please contact us at hi@feldroy.com.
"""

In [5]: u = User.objects.last()

In [6]: u
Out[6]: <User: user-0>

In [7]: u.delete()
Out[7]: 
(1,
 {'admin.LogEntry': 0,
  'users.User_groups': 0,
  'users.User_user_permissions': 0,
  'users.User': 1})

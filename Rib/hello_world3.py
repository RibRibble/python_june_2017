Last login: Sat Jun  3 19:43:14 on ttys000
ribribble@Ribs-MacBook-Pro ~ $ ls
Applications		Library			Public
Desktop			Movies			iCloud Drive (Archive)
Documents		Music			moveOutForm.pdf
Downloads		Pictures
ribribble@Ribs-MacBook-Pro ~ $ cd 
ribribble@Ribs-MacBook-Pro ~ $ ls
Applications		Library			Public
Desktop			Movies			iCloud Drive (Archive)
Documents		Music			moveOutForm.pdf
Downloads		Pictures
ribribble@Ribs-MacBook-Pro ~ $ ls
Applications		Library			Public
Desktop			Movies			iCloud Drive (Archive)
Documents		Music			moveOutForm.pdf
Downloads		Pictures
ribribble@Ribs-MacBook-Pro ~ $ start-django-env
(djangoEnv) ribribble@Ribs-MacBook-Pro ~ $ alias
alias start-django-env='source /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/bin/activate'
(djangoEnv) ribribble@Ribs-MacBook-Pro ~ $ deactivate
ribribble@Ribs-MacBook-Pro ~ $ start-django-env
(djangoEnv) ribribble@Ribs-MacBook-Pro ~ $ alias
alias start-django-env='source /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/bin/activate'
(djangoEnv) ribribble@Ribs-MacBook-Pro ~ $ ls
Applications		Library			Public
Desktop			Movies			iCloud Drive (Archive)
Documents		Music			moveOutForm.pdf
Downloads		Pictures
(djangoEnv) ribribble@Ribs-MacBook-Pro ~ $ cd desktop
(djangoEnv) ribribble@Ribs-MacBook-Pro desktop $ s
-bash: s: command not found
(djangoEnv) ribribble@Ribs-MacBook-Pro desktop $ ls
CARREER
DojoAssignments
GithubRepos
SKYPE
Screen Shot 2017-04-26 at 1.30.55 PM (2).png
Screen Shot 2017-04-26 at 1.30.55 PM (3).png
Screen Shot 2017-04-26 at 1.30.55 PM.png
Screen Shot 2017-04-26 at 1.31.04 PM (2).png
Screen Shot 2017-04-26 at 1.31.04 PM (3).png
Screen Shot 2017-04-26 at 1.31.04 PM.png
Screen Shot 2017-04-26 at 1.31.32 PM (2).png
Screen Shot 2017-04-26 at 1.31.32 PM (3).png
Screen Shot 2017-04-26 at 1.31.32 PM.png
bin
dojo_arena_photos-master
screen_shots
(djangoEnv) ribribble@Ribs-MacBook-Pro desktop $ cd DojoAssignments
(djangoEnv) ribribble@Ribs-MacBook-Pro DojoAssignments $ ls
Icon?		MySQL		Ruby		deployment
MEAN		Python		WebFundamentals
(djangoEnv) ribribble@Ribs-MacBook-Pro DojoAssignments $ cd Python
(djangoEnv) ribribble@Ribs-MacBook-Pro Python $ ls
Authman			Flask_MySQL		myEnvironments
Django			Python_Fundamentals	surveyFeb_2017
Flask_Fundamentals	Python_OOP
(djangoEnv) ribribble@Ribs-MacBook-Pro Python $ cd Django
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ ls
apps				products.zip
belt2				products2
belt2.zip			products2 2.zip
belt3				products2 3.zip
belt3.zip			products2.zip
beltExam			queries
belt_prep_quotes_delete		ran_word_gen
books				ran_word_gen.zip
books.zip			ran_word_gen2
books2				random_word3
books2.zip			random_word3.zip
courses				real_port
courses.zip			regex_operators.rtf
deployment			secrets
django.pem			settings.py
django_shell			sports_orm
django_tree.jpg			survey2
friends				survey2.zip
full_stack_books		survey3
full_stack_books.zip		survey3.zip
hello_world			survey_form_assignment
hello_world.zip			time_display2
login_registration		time_display_assignment
login_registration 2.zip	user_validation2
login_registration.zip		user_validation2.zip
main				validate
ninja_gold			validate.zip
ninja_gold.zip			vanish_ninja
ninja_gold2			vanish_ninja.zip
notes				wall
notes.docx			wall.zip
portfolio			wall2
portfolio.zip			wall2.zip
products
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ cd friends
(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ ls
apps		db.sqlite3	friends		manage.py
(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 00:50:54
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 00:50:58] "GET / HTTP/1.1" 200 1152
Not Found: /favicon.ico
[04/Jun/2017 00:50:59] "GET /favicon.ico HTTP/1.1" 404 2783
<QueryDict: {u'csrfmiddlewaretoken': [u'uoimGX2um2eQlsv3HptL0ygXJ6rYtuafLeGZO92WJ8VSSXcjmqOxFMUHHRJklBg1'], u'password': [u'password'], u'email': [u'echo@echo.com']}>
***************
<QueryDict: {u'csrfmiddlewaretoken': [u'uoimGX2um2eQlsv3HptL0ygXJ6rYtuafLeGZO92WJ8VSSXcjmqOxFMUHHRJklBg1'], u'password': [u'password'], u'email': [u'echo@echo.com']}>
echo@echo.com
$2b$12$TUuF8C.pvcbhhvsgy/Ro2u.WgqCPy9X.MhHivDe65fHfFJiHTE2ke
[04/Jun/2017 00:51:11] "POST /login HTTP/1.1" 302 0
[04/Jun/2017 00:51:11] "GET /friends HTTP/1.1" 200 499
[04/Jun/2017 00:53:12] "GET /friends HTTP/1.1" 200 583
[04/Jun/2017 00:54:23] "GET /friends HTTP/1.1" 200 489
[04/Jun/2017 00:54:35] "GET / HTTP/1.1" 200 1208
[04/Jun/2017 00:54:38] "GET /friends HTTP/1.1" 200 489
[04/Jun/2017 00:55:18] "GET /friends HTTP/1.1" 200 519
[04/Jun/2017 00:55:22] "GET /friends HTTP/1.1" 200 519
[04/Jun/2017 00:56:17] "GET /friends HTTP/1.1" 200 535
[04/Jun/2017 00:56:20] "GET /friends HTTP/1.1" 200 535
[04/Jun/2017 00:56:22] "GET /friends HTTP/1.1" 200 535
[04/Jun/2017 00:56:52] "GET /friends HTTP/1.1" 200 541
Not Found: /frigfgfgfg
[04/Jun/2017 00:56:53] "GET /frigfgfgfg HTTP/1.1" 404 2780
Not Found: /frigfgfgfg
[04/Jun/2017 00:57:11] "GET /frigfgfgfg HTTP/1.1" 404 2780
[04/Jun/2017 00:57:14] "GET /friends HTTP/1.1" 200 519
[04/Jun/2017 00:57:19] "GET /friends HTTP/1.1" 200 519
[04/Jun/2017 01:00:28] "GET /friends HTTP/1.1" 200 551
[04/Jun/2017 01:00:50] "GET /friends HTTP/1.1" 200 549
[04/Jun/2017 01:00:52] "GET /friends HTTP/1.1" 200 549
[04/Jun/2017 01:00:55] "GET /friends HTTP/1.1" 200 549
[04/Jun/2017 01:02:49] "GET /friends HTTP/1.1" 200 563
1
[04/Jun/2017 01:03:00] "GET /user/1 HTTP/1.1" 200 229
[04/Jun/2017 01:03:07] "GET /friends HTTP/1.1" 200 563
2
[04/Jun/2017 01:03:09] "GET /user/2 HTTP/1.1" 200 226
[04/Jun/2017 01:05:49] "GET /friends HTTP/1.1" 200 563
[04/Jun/2017 01:08:36] "GET /friends HTTP/1.1" 200 595
Not Found: /add_friend/1
[04/Jun/2017 01:08:38] "GET /add_friend/1 HTTP/1.1" 404 2786
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x10b7247d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 12, in <module>
    url(r'^add_friend/(?P<friend_id>\d+)$', views.add_friend)
AttributeError: 'module' object has no attribute 'add_friend'
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x1099dc7d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 12, in <module>
    url(r'^add_friend/(?P<friend_id>\d+)$', views.add_friend)
AttributeError: 'module' object has no attribute 'add_friend'
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x1061227d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 12, in <module>
    url(r'^add_friend/(?P<friend_id>\d+)$', views.add_friend)
AttributeError: 'module' object has no attribute 'add_friend'
^C(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ git checkout master
fatal: Not a git repository (or any of the parent directories): .git
(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ ls
apps		db.sqlite3	friends		manage.py
(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:16:35
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:17:11] "GET /friends HTTP/1.1" 200 595
Internal Server Error: /add_friend/1
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/exception.py", line 42, in inner
    response = get_response(request)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.py", line 187, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.py", line 185, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 34, in add_friend
    print user_id
NameError: global name 'user_id' is not defined
[04/Jun/2017 01:17:16] "GET /add_friend/1 HTTP/1.1" 500 63976
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:18:27
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
1
[04/Jun/2017 01:18:28] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:18:28] "GET /friends HTTP/1.1" 200 595
1
[04/Jun/2017 01:18:30] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:18:30] "GET /friends HTTP/1.1" 200 595
2
[04/Jun/2017 01:18:44] "GET /add_friend/2 HTTP/1.1" 302 0
[04/Jun/2017 01:18:44] "GET /friends HTTP/1.1" 200 595
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x105e1f7d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 2, in <module>
    from . import views
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 34
    print Friend ID: ,friend_id
                  ^
SyntaxError: invalid syntax
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:19:40
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Friend ID: 1
[04/Jun/2017 01:19:41] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:19:41] "GET /friends HTTP/1.1" 200 595
[04/Jun/2017 01:19:42] "GET /friends HTTP/1.1" 200 595
Friend ID: 1
[04/Jun/2017 01:19:44] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:19:44] "GET /friends HTTP/1.1" 200 595
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:20:11
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:20:14] "GET /friends HTTP/1.1" 200 595
User ID:  1
[04/Jun/2017 01:20:17] "GET /user/1 HTTP/1.1" 200 229
[04/Jun/2017 01:20:26] "GET /friends HTTP/1.1" 200 595
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x11133c7d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 2, in <module>
    from . import views
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 36
    print Friend Object: ' ,user'
                      ^
SyntaxError: invalid syntax
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:26:35
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:26:35] "GET /friends HTTP/1.1" 200 595
Friend ID:  1
Friend Object:  1
[04/Jun/2017 01:26:39] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:26:39] "GET /friends HTTP/1.1" 200 595
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:27:27
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:27:29] "GET /friends HTTP/1.1" 200 595
Friend ID:  1
Friend Object:  User object
[04/Jun/2017 01:27:35] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:27:35] "GET /friends HTTP/1.1" 200 595
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:33:39
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:33:52] "GET /friends HTTP/1.1" 200 595
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:33:55
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:34:09] "GET /friends HTTP/1.1" 200 595
[04/Jun/2017 01:34:19] "GET /friends HTTP/1.1" 200 595
Friend ID:  1
Friend Object:  User object
User object
[04/Jun/2017 01:34:26] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:34:26] "GET /friends HTTP/1.1" 200 595
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:36:48
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:36:52] "GET /friends HTTP/1.1" 200 595
Friend ID:  1
Friend Object:  User object
Current User:  User object
[04/Jun/2017 01:36:56] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:36:56] "GET /friends HTTP/1.1" 200 595
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x1093047d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 2, in <module>
    from . import views
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 39
    user.
        ^
SyntaxError: invalid syntax
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x1113447d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 2, in <module>
    from . import views
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 39
    user.
        ^
SyntaxError: invalid syntax
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x10e52b7d0>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 2, in <module>
    from . import views
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 39
    current_user.
                ^
SyntaxError: invalid syntax
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:38:39
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:38:55
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:39:15
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:39:40
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:39:56
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:40:45
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:40:50
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:40:52] "GET /friends HTTP/1.1" 200 595
Friend ID:  1
Friend Object:  User object
Current User:  User object
Internal Server Error: /add_friend/1
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/exception.py", line 42, in inner
    response = get_response(request)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.py", line 187, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.py", line 185, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 39, in add_friend
    current_user.friends.add(friend)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related_descriptors.py", line 881, in add
    self._add_items(self.source_field_name, self.target_field_name, *objs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related_descriptors.py", line 1030, in _add_items
    new_ids = new_ids - set(vals)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/query.py", line 256, in __iter__
    self._fetch_all()
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/query.py", line 1087, in _fetch_all
    self._result_cache = list(self.iterator())
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/query.py", line 155, in __iter__
    for row in compiler.results_iter():
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 789, in results_iter
    results = self.execute_sql(MULTI)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 835, in execute_sql
    cursor.execute(sql, params)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/utils.py", line 79, in execute
    return super(CursorDebugWrapper, self).execute(sql, params)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/utils.py", line 94, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py", line 337, in execute
    return Database.Cursor.execute(self, query, params)
OperationalError: no such table: friends_app_user_friends
[04/Jun/2017 01:40:55] "GET /add_friend/1 HTTP/1.1" 500 116974
^C(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ python manage.py makemigratioMigrations for 'friends_app':
  apps/friends_app/migrations/0002_auto_20170604_0143.py:
    - Remove field fav from quote
    - Remove field user from quote
    - Add field friends to user
    - Delete model Quote
(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, friends_app, sessions
Running migrations:
  Applying friends_app.0002_auto_20170604_0143... OK
The following content types are stale and need to be deleted:

    friends_app | quote

Any objects related to these content types by a foreign key will also
be deleted. Are you sure you want to delete these content types?
If you're unsure, answer 'no'.

    Type 'yes' to continue, or 'no' to cancel: yes
(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 01:43:30
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 01:43:39] "GET /friends HTTP/1.1" 200 595
Friend ID:  1
Friend Object:  User object
Current User:  User object
[04/Jun/2017 01:43:42] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 01:43:42] "GET /friends HTTP/1.1" 200 595
[04/Jun/2017 01:47:29] "GET /friends HTTP/1.1" 200 670
[04/Jun/2017 01:49:33] "GET /friends HTTP/1.1" 200 682
[04/Jun/2017 01:49:57] "GET /friends HTTP/1.1" 200 677
[04/Jun/2017 01:53:16] "GET /friends HTTP/1.1" 200 723
[04/Jun/2017 01:55:14] "GET /friends HTTP/1.1" 200 739
Internal Server Error: /friends
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/exception.py", line 42, in inner
    response = get_response(request)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.py", line 187, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.py", line 185, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 21, in friends
    return render(request, "friends_app/friends.html", context)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/shortcuts.py", line 30, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loader.py", line 67, in render_to_string
    template = get_template(template_name, using=using)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loader.py", line 21, in get_template
    return engine.get_template(template_name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/django.py", line 39, in get_template
    return Template(self.engine.get_template(template_name), self)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/engine.py", line 160, in get_template
    template, origin = self.find_template(template_name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/engine.py", line 134, in find_template
    name, template_dirs=dirs, skip=skip,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/base.py", line 44, in get_template
    contents, origin, origin.template_name, self.engine,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/base.py", line 191, in __init__
    self.nodelist = self.compile_nodelist()
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/base.py", line 233, in compile_nodelist
    return parser.parse()
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/base.py", line 518, in parse
    raise self.error(token, e)
TemplateSyntaxError: Empty variable tag on line 17
[04/Jun/2017 02:00:22] "GET /friends HTTP/1.1" 500 115148
[04/Jun/2017 02:00:33] "GET /friends HTTP/1.1" 200 739
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:02:03
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:02:05
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:02:15
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:02:41
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:02:51
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
User object
[04/Jun/2017 02:02:53] "GET /friends HTTP/1.1" 200 739
User object
[04/Jun/2017 02:02:55] "GET /friends HTTP/1.1" 200 739
Friend ID:  2
Friend Object:  User object
Current User:  User object
[04/Jun/2017 02:03:42] "GET /add_friend/2 HTTP/1.1" 302 0
User object
[04/Jun/2017 02:03:42] "GET /friends HTTP/1.1" 200 739
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x109526de8>
Traceback (most recent call last):
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 374, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py", line 361, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 313, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py", line 306, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/friends/urls.py", line 20, in <module>
    url(r'^', include('apps.friends_app.urls'))
  File "/Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/urls.py", line 2, in <module>
    from . import views
  File "/Users/ribribble/Desktop/DojoAssignments/Python/Django/friends/apps/friends_app/views.py", line 20
    current_user(request).
                         ^
SyntaxError: invalid syntax
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:04:19
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:04:23
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:04:32
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:04:36
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:05:00
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:05:04
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
<QuerySet [<User: User object>, <User: User object>]>
[04/Jun/2017 02:05:07] "GET /friends HTTP/1.1" 200 739
Friend ID:  1
Friend Object:  User object
Current User:  User object
[04/Jun/2017 02:05:18] "GET /add_friend/1 HTTP/1.1" 302 0
<QuerySet [<User: User object>, <User: User object>]>
[04/Jun/2017 02:05:18] "GET /friends HTTP/1.1" 200 739
Friend ID:  1
Friend Object:  User object
Current User:  User object
[04/Jun/2017 02:05:31] "GET /add_friend/1 HTTP/1.1" 302 0
<QuerySet [<User: User object>, <User: User object>]>
[04/Jun/2017 02:05:31] "GET /friends HTTP/1.1" 200 739
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:06:26
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:06:58
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
June 04, 2017 - 02:07:20
Django version 1.10.6, using settings 'friends.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[04/Jun/2017 02:08:04] "GET /friends HTTP/1.1" 200 821
[04/Jun/2017 02:08:35] "GET /logout HTTP/1.1" 302 0
[04/Jun/2017 02:08:35] "GET / HTTP/1.1" 200 1203
('**FORM DATA**', <QueryDict: {u'confirm_password': [u'password'], u'first_name': [u'user1'], u'last_name': [u'user1'], u'alias': [u'user1'], u'date_of_birth': [u'1991-01-01'], u'csrfmiddlewaretoken': [u'o65Nfrce1itjficrMT4r6GrVF0LvPOzUFWtqnDcGooalMNTHrUpdLU5FDL3RHVFG'], u'password': [u'password'], u'email': [u'user1@user1.com']}>)
(u'**postData from views.py***', <QueryDict: {u'confirm_password': [u'password'], u'first_name': [u'user1'], u'last_name': [u'user1'], u'alias': [u'user1'], u'date_of_birth': [u'1991-01-01'], u'csrfmiddlewaretoken': [u'o65Nfrce1itjficrMT4r6GrVF0LvPOzUFWtqnDcGooalMNTHrUpdLU5FDL3RHVFG'], u'password': [u'password'], u'email': [u'user1@user1.com']}>)
[]
('************************************************************', <User: User object>)
[04/Jun/2017 02:09:18] "POST /register HTTP/1.1" 302 0
[04/Jun/2017 02:09:18] "GET /friends HTTP/1.1" 200 912
Friend ID:  1
Friend Object:  User object
Current User:  User object
[04/Jun/2017 02:09:31] "GET /add_friend/1 HTTP/1.1" 302 0
[04/Jun/2017 02:09:31] "GET /friends HTTP/1.1" 200 937
Friend ID:  2
Friend Object:  User object
Current User:  User object
[04/Jun/2017 02:09:39] "GET /add_friend/2 HTTP/1.1" 302 0
[04/Jun/2017 02:09:39] "GET /friends HTTP/1.1" 200 964
Friend ID:  3
Friend Object:  User object
Current User:  User object
[04/Jun/2017 02:09:43] "GET /add_friend/3 HTTP/1.1" 302 0
[04/Jun/2017 02:09:43] "GET /friends HTTP/1.1" 200 991
[04/Jun/2017 02:09:50] "GET /logout HTTP/1.1" 302 0
[04/Jun/2017 02:09:50] "GET / HTTP/1.1" 200 1255
<QueryDict: {u'csrfmiddlewaretoken': [u'RzXnJH1w9ruRnNccqyCu9JlH2dC6MeMT8pl0RT1YwxbTUiTs5zXgOXZr0YUsElSF'], u'password': [u'password'], u'email': [u'echo@echo.com']}>
***************
<QueryDict: {u'csrfmiddlewaretoken': [u'RzXnJH1w9ruRnNccqyCu9JlH2dC6MeMT8pl0RT1YwxbTUiTs5zXgOXZr0YUsElSF'], u'password': [u'password'], u'email': [u'echo@echo.com']}>
echo@echo.com
$2b$12$TUuF8C.pvcbhhvsgy/Ro2u.WgqCPy9X.MhHivDe65fHfFJiHTE2ke
[04/Jun/2017 02:10:14] "POST /login HTTP/1.1" 302 0
[04/Jun/2017 02:10:14] "GET /friends HTTP/1.1" 200 990
[04/Jun/2017 02:12:19] "GET /friends HTTP/1.1" 200 1117
[04/Jun/2017 02:12:30] "GET /friends HTTP/1.1" 200 1128
[04/Jun/2017 02:14:41] "GET /friends HTTP/1.1" 200 1236
[04/Jun/2017 02:14:45] "GET /friends HTTP/1.1" 200 1236
[04/Jun/2017 02:15:06] "GET /friends HTTP/1.1" 200 1272
Not Found: /user/
[04/Jun/2017 02:15:15] "GET /user/ HTTP/1.1" 404 2950
[04/Jun/2017 02:15:42] "GET /friends HTTP/1.1" 200 1275
User ID:  3
[04/Jun/2017 02:15:50] "GET /user/3 HTTP/1.1" 200 229
[04/Jun/2017 02:15:53] "GET /friends HTTP/1.1" 200 1275
User ID:  2
[04/Jun/2017 02:15:55] "GET /user/2 HTTP/1.1" 200 226
[04/Jun/2017 02:15:58] "GET /friends HTTP/1.1" 200 1275
[04/Jun/2017 02:16:21] "GET /friends HTTP/1.1" 200 1374
[04/Jun/2017 02:16:30] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:40] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:41] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:41] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:42] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:42] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:42] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:42] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:43] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:43] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:43] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:43] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:43] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:44] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:44] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:44] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:45] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:45] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:48] "GET /friends HTTP/1.1" 200 1380
[04/Jun/2017 02:16:48] "GET /friends HTTP/1.1" 200 1380
pwd
^C(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ ls
apps		db.sqlite3	friends		manage.py
(djangoEnv) ribribble@Ribs-MacBook-Pro friends $ cd ..
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pip install django
Requirement already satisfied: django in /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pip list
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
appdirs (1.4.3)
bcrypt (3.1.3)
cffi (1.10.0)
Django (1.10.6)
packaging (16.8)
pip (9.0.1)
pycparser (2.17)
pyparsing (2.2.0)
setuptools (34.3.2)
six (1.10.0)
wheel (0.29.0)
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pip freeze
appdirs==1.4.3
bcrypt==3.1.3
cffi==1.10.0
Django==1.10.6
packaging==16.8
pycparser==2.17
pyparsing==2.2.0
six==1.10.0
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pip uninstall django
Uninstalling Django-1.10.6:
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/bin/django-admin
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/bin/django-admin.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/bin/django-admin.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/DESCRIPTION.rst
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/INSTALLER
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/LICENSE.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/METADATA
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/RECORD
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/WHEEL
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/entry_points.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/metadata.json
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/Django-1.10.6.dist-info/top_level.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/__main__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/__main__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/apps/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/apps/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/apps/config.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/apps/config.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/apps/registry.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/apps/registry.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/bin/django-admin.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/bin/django-admin.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/app_template/__init__.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/app_template/admin.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/app_template/apps.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/app_template/migrations/__init__.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/app_template/models.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/app_template/tests.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/app_template/views.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/global_settings.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/global_settings.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ar/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ar/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ar/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ar/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/az/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/az/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/az/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/az/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bg/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bg/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bg/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bg/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bn/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bn/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bn/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bn/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bs/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bs/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bs/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/bs/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ca/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ca/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ca/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ca/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cs/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cs/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cs/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cs/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cy/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cy/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cy/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/cy/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/da/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/da/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/da/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/da/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de_CH/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de_CH/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de_CH/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/de_CH/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/el/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/el/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/el/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/el/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_AU/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_AU/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_AU/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_AU/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_GB/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_GB/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_GB/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/en_GB/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eo/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eo/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eo/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eo/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_AR/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_AR/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_AR/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_AR/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_CO/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_CO/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_CO/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_CO/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_MX/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_MX/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_MX/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_MX/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_NI/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_NI/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_NI/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_NI/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_PR/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_PR/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_PR/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_PR/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/et/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/et/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/et/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/et/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eu/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eu/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eu/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/eu/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fa/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fa/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fa/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fa/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fi/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fi/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fi/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fi/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fr/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fr/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fr/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fr/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fy/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fy/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fy/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/fy/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ga/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ga/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ga/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ga/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gd/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gd/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gd/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gd/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gl/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gl/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gl/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/gl/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/he/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/he/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/he/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/he/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hi/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hi/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hi/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hi/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hr/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hr/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hr/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hr/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hu/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hu/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hu/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/hu/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/id/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/id/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/id/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/id/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/is/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/is/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/is/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/is/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/it/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/it/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/it/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/it/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ja/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ja/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ja/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ja/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ka/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ka/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ka/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ka/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/km/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/km/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/km/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/km/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kn/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kn/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kn/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/kn/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ko/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ko/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ko/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ko/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lt/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lt/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lt/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lt/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lv/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lv/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lv/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/lv/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mk/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mk/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mk/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mk/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ml/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ml/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ml/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ml/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mn/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mn/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mn/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mn/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nb/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nb/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nb/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nb/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nl/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nl/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nl/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nl/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nn/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nn/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nn/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/nn/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pl/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pl/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pl/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pl/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt_BR/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt_BR/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt_BR/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/pt_BR/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ro/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ro/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ro/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ro/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ru/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ru/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ru/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ru/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sk/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sk/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sk/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sk/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sl/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sl/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sl/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sl/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sq/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sq/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sq/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sq/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr_Latn/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr_Latn/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr_Latn/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sr_Latn/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sv/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sv/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sv/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sv/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ta/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ta/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ta/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ta/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/te/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/te/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/te/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/te/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/th/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/th/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/th/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/th/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tr/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tr/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tr/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tr/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/uk/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/uk/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/uk/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/uk/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/vi/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/vi/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/vi/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/vi/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hans/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hans/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hans/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hans/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hant/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hant/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hant/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/locale/zh_Hant/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/project_template/manage.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/project_template/project_name/__init__.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/project_template/project_name/settings.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/project_template/project_name/urls.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/project_template/project_name/wsgi.py-tpl
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/i18n.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/i18n.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/static.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/conf/urls/static.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/actions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/actions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/checks.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/checks.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/decorators.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/decorators.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/exceptions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/exceptions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/filters.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/filters.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/forms.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/forms.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/helpers.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/helpers.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/af/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/af/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/am/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/am/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ar/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ar/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ast/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ast/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/az/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/az/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/be/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/be/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bg/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bg/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bn/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bn/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/br/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/br/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bs/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/bs/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ca/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ca/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cs/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cs/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cy/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/cy/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/da/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/da/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/de/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/de/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/dsb/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/dsb/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/el/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/el/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_AU/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_AU/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_GB/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/en_GB/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eo/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eo/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_AR/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_AR/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_CO/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_CO/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_MX/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_MX/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_VE/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/es_VE/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/et/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/et/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eu/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/eu/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fa/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fa/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fi/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fi/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fr/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fr/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fy/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/fy/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ga/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ga/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gd/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gd/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gl/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/gl/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/he/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/he/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hi/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hi/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hr/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hr/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hsb/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hsb/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hu/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/hu/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ia/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ia/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/id/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/id/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/io/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/io/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/is/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/is/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/it/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/it/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ja/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ja/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ka/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ka/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kk/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kk/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/km/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/km/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kn/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/kn/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ko/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ko/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lb/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lb/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lt/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lt/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lv/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/lv/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mk/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mk/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ml/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ml/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mn/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mn/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mr/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/mr/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/my/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/my/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nb/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nb/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ne/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ne/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nl/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nl/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nn/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/nn/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/os/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/os/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pa/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pa/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pl/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pl/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt_BR/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/pt_BR/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ro/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ro/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ru/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ru/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sk/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sk/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sl/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sl/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sq/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sq/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr_Latn/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sr_Latn/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sv/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sv/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sw/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/sw/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ta/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ta/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/te/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/te/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/th/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/th/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tr/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tr/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tt/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/tt/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/udm/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/udm/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/uk/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/uk/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ur/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/ur/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/vi/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/vi/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hans/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hans/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hant/LC_MESSAGES/djangojs.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/locale/zh_Hant/LC_MESSAGES/djangojs.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/migrations/0001_initial.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/migrations/0001_initial.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/migrations/0002_logentry_remove_auto_add.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/migrations/0002_logentry_remove_auto_add.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/options.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/options.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/sites.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/sites.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/base.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/changelists.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/dashboard.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/fonts.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/forms.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/login.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/rtl.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/css/widgets.css
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/fonts/LICENSE.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/fonts/README.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/fonts/Roboto-Bold-webfont.woff
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/fonts/Roboto-Light-webfont.woff
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/fonts/Roboto-Regular-webfont.woff
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/LICENSE
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/README.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/calendar-icons.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/gis/move_vertex_off.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/gis/move_vertex_on.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-addlink.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-alert.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-calendar.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-changelink.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-clock.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-deletelink.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-no.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-unknown-alt.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-unknown.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/icon-yes.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/inline-delete.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/search.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/selector-icons.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/sorting-icons.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/tooltag-add.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/img/tooltag-arrowright.svg
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/SelectBox.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/SelectFilter2.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/actions.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/actions.min.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/admin/DateTimeShortcuts.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/admin/RelatedObjectLookups.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/calendar.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/cancel.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/change_form.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/collapse.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/collapse.min.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/core.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/inlines.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/inlines.min.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/jquery.init.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/popup_response.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/prepopulate.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/prepopulate.min.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/prepopulate_init.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/timeparse.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/urlify.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/vendor/jquery/LICENSE-JQUERY.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/vendor/jquery/jquery.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/vendor/jquery/jquery.min.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE-XREGEXP.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/vendor/xregexp/xregexp.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/static/admin/js/vendor/xregexp/xregexp.min.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/404.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/500.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/actions.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/app_index.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/auth/user/add_form.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/auth/user/change_password.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/base.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/base_site.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/change_form.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/change_list.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/change_list_results.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/date_hierarchy.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/delete_confirmation.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/delete_selected_confirmation.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/edit_inline/stacked.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/edit_inline/tabular.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/filter.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/includes/fieldset.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/includes/object_delete_summary.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/index.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/invalid_setup.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/login.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/object_history.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/pagination.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/popup_response.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/prepopulated_fields_js.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/related_widget_wrapper.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/search_form.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/submit_line.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/logged_out.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/password_change_done.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/password_change_form.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/password_reset_complete.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/password_reset_confirm.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/password_reset_done.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/password_reset_email.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templates/registration/password_reset_form.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_list.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_list.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_modify.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_modify.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_static.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_static.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_urls.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/admin_urls.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/log.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/templatetags/log.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/tests.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/tests.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/views/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/views/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/views/decorators.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/views/decorators.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/views/main.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/views/main.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/widgets.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admin/widgets.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/middleware.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/middleware.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/bookmarklets.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/index.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/missing_docutils.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/model_detail.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/model_index.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/template_detail.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/template_filter_index.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/template_tag_index.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/view_detail.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/templates/admin_doc/view_index.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/tests/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/tests/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/tests/test_fields.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/tests/test_fields.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/urls.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/urls.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/admindocs/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/admin.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/admin.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/backends.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/backends.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/base_user.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/base_user.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/checks.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/checks.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/common-passwords.txt.gz
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/context_processors.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/context_processors.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/decorators.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/decorators.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/forms.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/forms.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/handlers/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/handlers/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/handlers/modwsgi.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/handlers/modwsgi.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/hashers.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/hashers.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/commands/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/commands/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/commands/changepassword.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/commands/changepassword.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/commands/createsuperuser.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/management/commands/createsuperuser.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/middleware.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/middleware.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0001_initial.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0001_initial.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0002_alter_permission_name_max_length.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0002_alter_permission_name_max_length.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0003_alter_user_email_max_length.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0003_alter_user_email_max_length.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0004_alter_user_username_opts.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0004_alter_user_username_opts.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0005_alter_user_last_login_null.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0005_alter_user_last_login_null.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0006_require_contenttypes_0002.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0006_require_contenttypes_0002.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0007_alter_validators_add_error_messages.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0007_alter_validators_add_error_messages.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0008_alter_user_username_max_length.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/0008_alter_user_username_max_length.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/mixins.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/mixins.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/password_validation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/password_validation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/signals.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/signals.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/templates/registration/password_reset_subject.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/tests/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/tests/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/tests/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/tests/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/tokens.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/tokens.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/urls.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/urls.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/validators.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/validators.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/auth/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/admin.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/admin.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/checks.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/checks.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/fields.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/fields.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/forms.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/forms.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/management.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/management.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/migrations/0001_initial.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/migrations/0001_initial.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/migrations/0002_remove_content_type_name.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/migrations/0002_remove_content_type_name.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/contenttypes/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/admin.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/admin.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/forms.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/forms.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/middleware.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/middleware.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/migrations/0001_initial.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/migrations/0001_initial.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/sitemaps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/sitemaps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/templatetags/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/templatetags/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/templatetags/flatpages.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/templatetags/flatpages.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/urls.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/urls.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/flatpages/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/admin/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/admin/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/admin/options.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/admin/options.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/admin/widgets.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/admin/widgets.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/adapter.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/adapter.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/base/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/mysql/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/adapter.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/adapter.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/oracle/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/adapter.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/adapter.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/const.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/const.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/pgraster.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/pgraster.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/adapter.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/adapter.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/spatialite/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/backends/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/aggregates.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/aggregates.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/fields.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/fields.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/functions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/functions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/lookups.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/lookups.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/manager.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/manager.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/proxy.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/proxy.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/query.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/query.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/sql/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/sql/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/sql/conversion.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/db/models/sql/conversion.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/feeds.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/feeds.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/forms/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/forms/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/forms/fields.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/forms/fields.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/forms/widgets.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/forms/widgets.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/LICENSE
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/datasource.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/datasource.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/driver.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/driver.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/envelope.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/envelope.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/error.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/error.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/feature.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/feature.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/field.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/field.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/geometries.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/geometries.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/geomtype.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/geomtype.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/layer.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/layer.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/libgdal.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/libgdal.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/ds.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/ds.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/errcheck.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/errcheck.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/generation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/generation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/geom.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/geom.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/raster.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/raster.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/srs.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/prototypes/srs.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/band.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/band.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/const.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/const.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/source.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/raster/source.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/srs.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/gdal/srs.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/libgeoip.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/libgeoip.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/prototypes.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip/prototypes.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip2/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip2/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip2/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip2/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip2/resources.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geoip2/resources.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/backend/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/backend/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/backend/geos.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/backend/geos.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/regex.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geometry/regex.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/LICENSE
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/collections.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/collections.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/coordseq.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/coordseq.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/error.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/error.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/factory.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/factory.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/geometry.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/geometry.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/io.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/io.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/libgeos.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/libgeos.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/linestring.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/linestring.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/mutable_list.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/mutable_list.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/point.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/point.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/polygon.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/polygon.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prepared.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prepared.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/coordseq.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/coordseq.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/errcheck.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/errcheck.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/geom.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/geom.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/io.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/io.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/misc.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/misc.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/predicates.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/predicates.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/prepared.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/prepared.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/threadsafe.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/threadsafe.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/topology.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/geos/prototypes/topology.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/commands/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/commands/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/commands/inspectdb.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/commands/inspectdb.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/commands/ogrinspect.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/management/commands/ogrinspect.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/gmap.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/gmap.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/overlays.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/overlays.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/zoom.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/google/zoom.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/openlayers/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/maps/openlayers/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/measure.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/measure.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/serializers/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/serializers/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/serializers/geojson.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/serializers/geojson.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/shortcuts.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/shortcuts.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/sitemaps/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/sitemaps/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/sitemaps/kml.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/sitemaps/kml.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/sitemaps/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/sitemaps/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/static/gis/js/OLMapWidget.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/admin/openlayers.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/admin/openlayers.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/admin/osm.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/admin/osm.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/google/google-map.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/google/google-map.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/google/google-multi.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/google/google-single.js
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/kml/base.kml
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/kml/placemarks.kml
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/openlayers-osm.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/templates/gis/openlayers.html
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/layermapping.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/layermapping.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/ogrinfo.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/ogrinfo.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/ogrinspect.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/ogrinspect.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/srs.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/srs.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/wkt.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/utils/wkt.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/gis/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/hy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/templatetags/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/templatetags/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/templatetags/humanize.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/humanize/templatetags/humanize.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/api.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/api.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/constants.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/constants.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/context_processors.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/context_processors.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/middleware.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/middleware.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/cookie.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/cookie.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/fallback.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/fallback.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/session.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/storage/session.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/messages/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/aggregates/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/aggregates/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/aggregates/general.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/aggregates/general.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/aggregates/statistics.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/aggregates/statistics.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/array.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/array.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/hstore.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/hstore.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/jsonb.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/jsonb.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/ranges.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/ranges.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/fields/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/array.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/array.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/hstore.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/hstore.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/jsonb.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/jsonb.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/ranges.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/forms/ranges.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/functions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/functions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/lookups.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/lookups.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/search.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/search.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/signals.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/signals.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/validators.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/postgres/validators.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/admin.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/admin.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/middleware.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/middleware.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/migrations/0001_initial.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/migrations/0001_initial.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/redirects/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/cache.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/cache.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/cached_db.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/cached_db.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/db.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/db.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/file.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/file.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/signed_cookies.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/backends/signed_cookies.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/base_session.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/base_session.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/exceptions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/exceptions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/management/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/management/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/management/commands/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/management/commands/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/management/commands/clearsessions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/management/commands/clearsessions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/middleware.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/middleware.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/migrations/0001_initial.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/migrations/0001_initial.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/serializers.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sessions/serializers.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/management/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/management/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/management/commands/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/management/commands/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/management/commands/ping_google.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/management/commands/ping_google.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/templates/sitemap.xml
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/templates/sitemap_index.xml
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sitemaps/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/admin.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/admin.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/af/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/af/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ar/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ar/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ast/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ast/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/az/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/az/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/be/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/be/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/bg/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/bg/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/bn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/bn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/br/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/br/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/bs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/bs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ca/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ca/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/cs/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/cs/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/cy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/cy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/da/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/da/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/de/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/de/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/dsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/dsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/el/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/el/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/en/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/en/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/en_AU/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/en_AU/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/en_GB/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/en_GB/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/eo/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/eo/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_AR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_AR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_CO/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_CO/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_MX/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_MX/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_VE/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/es_VE/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/et/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/et/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/eu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/eu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/fy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ga/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ga/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/gd/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/gd/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/gl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/gl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/he/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/he/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hsb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hsb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hu/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hu/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hy/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/hy/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ia/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ia/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/id/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/id/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/io/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/io/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/is/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/is/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/it/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/it/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ja/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ja/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ka/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ka/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/kk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/kk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/km/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/km/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/kn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/kn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ko/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ko/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/lb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/lb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/lt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/lt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/lv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/lv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/mk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/mk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ml/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ml/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/mn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/mn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/mr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/mr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/my/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/my/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/nb/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/nb/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ne/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ne/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/nl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/nl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/nn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/nn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/os/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/os/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pa/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pa/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pt_BR/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/pt_BR/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ro/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ro/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ru/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ru/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sl/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sl/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sq/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sq/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sr_Latn/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sr_Latn/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sv/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sv/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sw/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/sw/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ta/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ta/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/te/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/te/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/th/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/th/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/tr/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/tr/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/tt/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/tt/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/udm/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/udm/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/uk/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/uk/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ur/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/ur/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/vi/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/vi/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/zh_Hans/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/zh_Hans/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/zh_Hant/LC_MESSAGES/django.mo
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/locale/zh_Hant/LC_MESSAGES/django.po
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/management.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/management.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/managers.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/managers.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/middleware.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/middleware.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/migrations/0001_initial.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/migrations/0001_initial.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/migrations/0002_alter_domain_unique.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/migrations/0002_alter_domain_unique.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/requests.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/requests.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/shortcuts.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/sites/shortcuts.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/finders.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/finders.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/handlers.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/handlers.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/collectstatic.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/findstatic.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/findstatic.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/runserver.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/management/commands/runserver.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/storage.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/storage.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/templatetags/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/templatetags/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/templatetags/staticfiles.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/templatetags/staticfiles.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/testing.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/testing.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/urls.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/urls.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/staticfiles/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/syndication/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/syndication/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/syndication/apps.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/syndication/apps.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/syndication/views.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/contrib/syndication/views.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/db.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/db.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/dummy.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/dummy.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/filebased.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/filebased.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/locmem.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/locmem.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/memcached.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/backends/memcached.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/cache/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/caches.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/caches.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/compatibility/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/compatibility/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/compatibility/django_1_10.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/compatibility/django_1_10.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/compatibility/django_1_8_0.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/compatibility/django_1_8_0.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/database.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/database.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/messages.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/messages.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/model_checks.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/model_checks.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/registry.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/csrf.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/csrf.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/sessions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/security/sessions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/templates.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/templates.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/urls.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/checks/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/exceptions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/exceptions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/images.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/images.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/locks.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/locks.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/move.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/move.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/storage.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/storage.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/temp.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/temp.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/uploadedfile.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/uploadedfile.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/uploadhandler.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/uploadhandler.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/files/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/exception.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/exception.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/wsgi.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/handlers/wsgi.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/console.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/console.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/dummy.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/dummy.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/filebased.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/filebased.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/locmem.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/locmem.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/smtp.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/backends/smtp.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/message.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/message.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/mail/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/color.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/color.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/check.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/check.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/compilemessages.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/compilemessages.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/createcachetable.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/createcachetable.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/dbshell.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/dbshell.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/diffsettings.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/diffsettings.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/dumpdata.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/dumpdata.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/flush.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/flush.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/inspectdb.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/inspectdb.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/loaddata.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/loaddata.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/makemessages.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/makemessages.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/makemigrations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/makemigrations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/migrate.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/migrate.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/runserver.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sendtestemail.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sendtestemail.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/shell.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/shell.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/showmigrations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/showmigrations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sqlflush.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sqlflush.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sqlmigrate.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sqlmigrate.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sqlsequencereset.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/sqlsequencereset.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/squashmigrations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/squashmigrations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/startapp.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/startapp.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/startproject.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/startproject.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/test.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/test.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/testserver.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/commands/testserver.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/sql.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/sql.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/templates.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/templates.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/management/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/paginator.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/paginator.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/json.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/json.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/python.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/python.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/pyyaml.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/pyyaml.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/xml_serializer.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/serializers/xml_serializer.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/servers/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/servers/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/servers/basehttp.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/servers/basehttp.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/signals.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/signals.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/signing.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/signing.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/urlresolvers.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/urlresolvers.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/validators.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/validators.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/wsgi.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/core/wsgi.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/creation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/creation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/validation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/base/validation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/dummy/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/dummy/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/dummy/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/dummy/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/dummy/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/dummy/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/compiler.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/compiler.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/creation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/creation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/validation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/mysql/validation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/compiler.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/compiler.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/creation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/creation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/functions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/functions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/oracle/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/creation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/creation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/version.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql/version.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/creation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/creation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/version.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/postgresql_psycopg2/version.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/signals.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/signals.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/creation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/creation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/features.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/features.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/introspection.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/introspection.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/operations.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/operations.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/schema.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/sqlite3/schema.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/backends/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/autodetector.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/autodetector.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/exceptions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/exceptions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/executor.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/executor.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/graph.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/graph.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/loader.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/loader.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/migration.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/migration.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/fields.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/fields.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/special.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/operations/special.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/optimizer.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/optimizer.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/questioner.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/questioner.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/recorder.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/recorder.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/serializer.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/serializer.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/state.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/state.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/topological_sort.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/topological_sort.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/writer.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/migrations/writer.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/aggregates.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/aggregates.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/constants.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/constants.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/deletion.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/deletion.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/expressions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/expressions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/files.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/files.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/proxy.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/proxy.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related_descriptors.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related_descriptors.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related_lookups.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/related_lookups.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/reverse_related.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/fields/reverse_related.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/functions/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/functions/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/functions/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/functions/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/functions/datetime.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/functions/datetime.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/lookups.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/lookups.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/manager.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/manager.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/options.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/options.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/query.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/query.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/query_utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/query_utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/signals.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/signals.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/compiler.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/compiler.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/constants.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/constants.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/datastructures.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/datastructures.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/query.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/query.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/subqueries.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/subqueries.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/where.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/sql/where.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/models/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/transaction.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/transaction.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/db/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/dispatch/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/dispatch/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/dispatch/dispatcher.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/dispatch/dispatcher.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/dispatch/license.txt
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/dispatch/weakref_backports.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/dispatch/weakref_backports.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/boundfield.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/boundfield.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/extras/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/extras/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/extras/widgets.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/extras/widgets.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/fields.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/fields.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/forms.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/forms.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/formsets.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/formsets.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/models.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/models.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/widgets.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/forms/widgets.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/cookie.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/cookie.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/multipartparser.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/multipartparser.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/request.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/request.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/response.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/http/response.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/cache.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/cache.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/clickjacking.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/clickjacking.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/common.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/common.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/csrf.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/csrf.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/gzip.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/gzip.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/http.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/http.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/locale.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/locale.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/security.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/middleware/security.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/shortcuts.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/shortcuts.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/django.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/django.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/dummy.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/dummy.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/jinja2.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/jinja2.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/backends/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/context.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/context.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/context_processors.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/context_processors.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/defaultfilters.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/defaultfilters.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/defaulttags.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/defaulttags.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/engine.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/engine.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/exceptions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/exceptions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/library.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/library.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loader.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loader.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loader_tags.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loader_tags.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/app_directories.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/app_directories.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/cached.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/cached.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/eggs.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/eggs.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/filesystem.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/filesystem.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/locmem.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/loaders/locmem.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/response.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/response.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/smartif.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/smartif.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/template/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/cache.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/cache.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/i18n.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/i18n.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/l10n.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/l10n.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/static.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/static.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/tz.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/templatetags/tz.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/client.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/client.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/html.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/html.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/runner.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/runner.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/selenium.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/selenium.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/signals.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/signals.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/testcases.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/testcases.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/test/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/exceptions.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/exceptions.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/resolvers.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/utils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/urls/utils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/_os.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/_os.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/archive.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/archive.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/autoreload.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/baseconv.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/baseconv.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/cache.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/cache.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/crypto.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/crypto.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/datastructures.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/datastructures.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/dateformat.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/dateformat.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/dateparse.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/dateparse.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/dates.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/dates.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/datetime_safe.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/datetime_safe.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/deconstruct.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/deconstruct.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/decorators.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/decorators.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/deprecation.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/deprecation.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/duration.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/duration.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/encoding.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/encoding.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/feedgenerator.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/feedgenerator.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/formats.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/formats.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/functional.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/glob.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/glob.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/html.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/html.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/html_parser.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/html_parser.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/http.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/http.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/inspect.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/inspect.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/ipv6.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/ipv6.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/itercompat.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/itercompat.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/jslex.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/jslex.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/log.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/log.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/lorem_ipsum.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/lorem_ipsum.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/lru_cache.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/lru_cache.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/module_loading.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/module_loading.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/numberformat.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/numberformat.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/regex_helper.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/regex_helper.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/safestring.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/safestring.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/six.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/six.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/synch.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/synch.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/termcolors.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/termcolors.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/text.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/text.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/timesince.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/timesince.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/timezone.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/timezone.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/translation/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/translation/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/translation/trans_null.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/translation/trans_null.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/translation/trans_real.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/translation/trans_real.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/tree.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/tree.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/version.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/version.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/xmlutils.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/utils/xmlutils.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/csrf.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/csrf.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/debug.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/debug.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/cache.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/cache.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/clickjacking.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/clickjacking.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/csrf.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/csrf.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/debug.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/debug.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/gzip.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/gzip.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/http.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/http.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/vary.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/decorators/vary.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/defaults.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/defaults.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/__init__.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/__init__.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/base.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/base.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/dates.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/dates.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/detail.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/detail.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/edit.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/edit.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/list.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/generic/list.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/i18n.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/i18n.pyc
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/static.py
  /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages/django/views/static.pyc
Proceed (y/n)? n
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pip show django
Name: Django
Version: 1.10.6
Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Home-page: http://www.djangoproject.com/
Author: Django Software Foundation
Author-email: foundation@djangoproject.com
License: BSD
Location: /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages
Requires: 
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pip search flask
Flask-User-05 (0.5)                            - Customizable User Account
                                                 Management for Flask:
                                                 Register, Confirm email,
                                                 Login, Change username,
                                                 Change password, Forgot
                                                 password and more.
flask-restless-swagger-2 (0.0.3)               - Magically create swagger
                                                 documentation as you
                                                 magically create your RESTful
                                                 API
flask-restful-swagger-2 (0.35)                 - Extract swagger specs from
                                                 your flask-restful project.
                                                 Project based on flask-
                                                 restful-swagger by Ran
                                                 Tavory.
3color-Press (0.2.1)                           - A Flask based static site
                                                 generator for comics
flask-ab (0.0.1)                               - 
abilian-core (0.9.2)                           - A framework for enterprise
                                                 applications (CRM, ERP,
                                                 collaboration...), based on
                                                 Flask and SQLAlchemy
AC-Flask-HipChat (0.2.12)                      - Atlassian Connect library
                                                 based on Flask for HipChat
acceptable (0.8)                               - API version negotiation for
                                                 flask-based web services.
Flask-Access (0.1)                             - A Flask extension which
                                                 limits access to views.
Flask-Personal-Access-Token (0.1.2)            - Flask Personal Access Token
                                                 Management Extension
Flask-ACL (0.0.1)                              - Access control lists for
                                                 Flask.
flask-miracle-acl (0.2)                        - The fabric between the Flask
                                                 framework and Miracle ACL
Flask-Actions (0.6.6)                          - custom actions for flask to
                                                 help manage your application
Flask-ActiveRecord (0.2.3)                     - ActiveRecord support for
                                                 Flask-SQLAlchemy models
flask-ad-auth (0.1)                            - Flask Azure Active Directory
                                                 Auth
fab-addon-audit (0.0.1)                        - Audit functionality to flask-
                                                 appbuilder apps.
kore-plugins-flask-admin (0.0.1)               - 
flask-admin-barin (0.0.1)                      - A Barin backend for Flask-
                                                 Admin
flask-admin-lite (0.1.0)                       - Build lightweight admin panel
                                                 for your models
Flask-Admin-Utils (0.0.3)                      - Utils for Flask-Admin
quokka-flask-admin (1.4.2.1)                   - Fork of Flask-Admin for
                                                 QuokkaCMS
flask-admin-s3-upload (0.1.4)                  - Field types for allowing file
                                                 and image uploads to Amazon
                                                 S3 (as well as default local
                                                 storage) in Flask-Admin.
flask-admin-openerp (0.3.3)                    - OpenERP Backend for Flask-
                                                 Admin
Flask-Admin (1.5.0)                            - Simple and extensible admin
                                                 interface framework for Flask
flask-admin.py (0.1.3)                         - copy from djang-admin.py
Flask-Administration (0.1.42)                  - UNKNOWN
afg (0.2)                                      - Alexa Flask Guide for Flask-
                                                 ASK
agaveflask (0.2.0)                             - Common package for authoring
                                                 Agave services in flask
                                                 /Flask-RESTful
kolekti-agent-python-flask (0.0.1)             - Lightweight monitoring system
                                                 agent
burp-ui-agent (0.5.1)                          - Burp-UI is a web-ui for burp
                                                 backup written in python with
                                                 Flask and jQuery/Bootstrap
Flask-Aggregator (0.2.0)                       - Batch the GET requests to
                                                 your REST API into a single
                                                 POST
Flask-Airbrake (0.0.3)                         - Flask extension for Airbrake
airbrake-flask (1.0.7)                         - airbrake-flask - Airbrake
                                                 client for Python Flask
alchemist (0.3.12)                             - A server architecture built
                                                 on top of a solid foundation
                                                 provided by flask,
                                                 sqlalchemy, and various
                                                 extensions.
flask-wtf-alchemy-utils (0.1.0)                - Form and field utility base
                                                 classes for use with Flask,
                                                 Flask-WTF, and wtforms-
                                                 alchemy.
Flask-Alchemy (0.1)                            - The fastest markdown parser
                                                 in pure Python
flask-simple-alchemy (0.3.0)                   - A Simplification of
                                                 SQLAlchemy's declarative
                                                 using Flask-SQLAlchemy
Flask-AlchemyDumps (0.0.10)                    - SQLAlchemy backup/dump tool
                                                 for Flask
Flask-AlchemyView (0.1.4)                      - Simple ModelView for auto-
                                                 generating Flask Views based
                                                 on SQLAlchemy models
Flask-Alchy (0.5.0)                            - Flask extension for alchy
Flask-Alcool (0.3)                             - Implement access control
                                                 lists as decorators for
                                                 flask.
Flask-Alembic (2.0.1)                          - Flask extension to integrate
                                                 Alembic migrations
flask-allows (0.2.0)                           - Impose authorization
                                                 requirements on Flask routes
Flask-Analytics (0.6.0)                        - Analytics snippets generator
                                                 extension for the Flask
                                                 framework
Flask-And-Redis (0.7)                          - Simple as dead support of
                                                 Redis database for Flask
                                                 apps.
Flask-Annex (0.4.0)                            - Efficient integration of
                                                 external storage services for
                                                 Flask
just-another-settings (1.0)                    - Small lib to manage settings
                                                 as object for
                                                 Flask/Bottle/custom apps
Flask-Api-Awesomesauce (0.1)                   - Flask Api Awesomesauce!
rest-api-blueprint (0.1)                       - Pedagogical blueprint of a
                                                 REST API in Flask.
Flask-Debug-API (0.1.0)                        - API Browser for Flask-
                                                 DebugToolbar
Flask-API-Utils (1.0.2)                        - Flask-API-Utils helps you to
                                                 create APIs.
api-star (0.1.4)                               - An API framework for Flask &
                                                 Falcon.
flask-simple-api (1.4.1)                       - Simple API endpoints for
                                                 Flask using Flask-Restful
                                                 reqparse and Python 3
                                                 annotations
Flask-API (0.7.1)                              - Browsable web APIs for Flask.
li-api-flask (0.1.17)                          - Loja Integrada's API Flask
Flask-API.yandex (0.6.2.1)                     - Browsable web APIs for Flask.
Flask-APIBlueprint (1.0.0)                     - Route inheritance for Flask
                                                 Blueprints
flask-apidoc (1.0.0)                           - Adds ApiDoc support to Flask
Flask-APIForm (1.0)                            - A simple form validator for
                                                 REST APIs in Flask
flask-apify (0.7.1)                            - A Flask extension to create
                                                 API to your application as a
                                                 ninja
apikit (0.3.2)                                 - A set of utility functions
                                                 for RESTful Flask
                                                 applications.
flask-apispec (0.3.2)                          - Build and document REST APIs
                                                 with Flask and apispec
flask-app-router (0.0.1)                       - UNKNOWN
social-auth-app-flask-peewee (1.0.0)           - Python Social Authentication,
                                                 peewee Flask models
                                                 integration.
social-auth-app-flask-mongoengine (1.0.0)      - Python Social Authentication,
                                                 Mongoengine Flask models
                                                 integration.
social-auth-app-flask (1.0.0)                  - Python Social Authentication,
                                                 Flask integration.
social-auth-app-flask-sqlalchemy (1.0.1)       - Python Social Authentication,
                                                 SQLAlchemy Flask models
                                                 integration.
create-flask-app (0.2.0)                       - Create flask web apps with
                                                 directory layout
Flask-AppBuilder (1.8.1)                       - Simple and rapid application
                                                 development framework, built
                                                 on top of Flask. includes
                                                 detailed security, auto CRUD
                                                 generation for your models,
                                                 google charts and much more.
Flask-Appcache (0.1.2)                         - Semi-automagically sets up
                                                 appcache for you
flask-appconfig (0.11.1)                       - Configures Flask applications
                                                 in a canonical way. Also
                                                 auto-configures Heroku. Aims
                                                 to standardize configuration.
Flask-AppFactory (0.2.1)                       - Flask-AppFactory is an
                                                 dynamic application loader.
flask-apps (0.0.2)                             - UNKNOWN
Flask-AppUtils (1.2.0)                         - A collection of useful
                                                 patterns and helpers for
                                                 Flask applications
Flask-APScheduler-fork (1.5.4)                 - Test package and a fork of
                                                 flask_apscheduler.
Flask-APScheduler (1.7.0)                      - Adds APScheduler support to
                                                 Flask
apy (0.2.3)                                    - Pythonic API development with
                                                 flask
Flask-Arango (0.1.1)                           - Flask extension providing
                                                 integration with Arango.
Flask-Arangodb (1.0.4)                         - Flask extension for ArangoDB
                                                 using python-arango
archer (0.5)                                   - Thrift app the flask way
Flask-Argon2 (0.1.2.1)                         - Flask-Argon2 provides
                                                 convenient wrappers for
                                                 Argon2 password hashing
flask-args (0.3.0)                             - auto type convertion for flas
                                                 k.request.form/args/values
Flask-arrest (0.5.0)                           - A small Flask extension to
                                                 ease the creation of REST
                                                 apis.
Flask-Ask (0.9.3)                              - Rapid Alexa Skills Kit
                                                 Development for Amazon Echo
                                                 Devices in Python
Flask-Aspen (0.0)                              - UNKNOWN
assentio (0.1)                                 - A minimal, lightweight flask-
                                                 based blog
Flask-AssetRev (1.0.0)                         - UNKNOWN
Flask-Assets (0.12)                            - Asset management for Flask,
                                                 to compress and merge CSS and
                                                 Javascript files.
Flask-Assistant (0.2.9)                        - Framework for Building
                                                 Virtual Assistants with
                                                 API.AI
selenium-astride (0.2.2)                       - Framework to use Selenium
                                                 loud and clear, astride. Use
                                                 it with Django, Flask or your
                                                 favourite web framework.
Flask-Async (0.11-dev-20140215)                - A fork of Flask to support
                                                 asyncio
atilla (1.2.6)                                 - flask API projects helper
Flask-Attest (0.1dev)                          - Test Flask applications with
                                                 Attest
Flask-Augment (0.5)                            - Python decorators
                                                 implementing contracts for
                                                 flask framework
flask-social-auth (0.0)                        - 
flask-wechat-auth (0.0.1)                      - WeChat Flask Blueprint Module
pixelpin-auth-flask (1.0.0)                    - Python Social Authentication,
                                                 Flask integration.
pixelpin-auth-flask-sqlalchemy (1.0.1)         - Python Social Authentication,
                                                 SQLAlchemy Flask models
                                                 integration.
Flask-Auth (0.85)                              - Auth extension for Flask.
Flask-Heroku-Auth (0.0.5)                      - Flask Based Heroku
                                                 Authentication.
Flask-Authbone (0.3)                           - Plugguble Auth framework for
                                                 Flask.
flask-authjwt (0.1.1)                          - Module to secure flask
                                                 endpoints in appengine using
                                                 jwt token.
Flask-Authority (0.0.1)                        - 
Flask-Authorization-Panda (0.3)                - Flask Authorization for
                                                 Pandas!
Flask-Autodoc (0.1.2)                          - Documentation generator for
                                                 flask
Flask-AutoFixture (0.2.3)                      - Flask extension for recording
                                                 JSON fixtures right from your
                                                 test suite
Flask-AutoIndex (0.6)                          - The mod_autoindex for Flask
flask-autorouter (0.2.1)                       - a utility for generating
                                                 flask URL routing
Flask-Avatar (0.1.2)                           - To generate avatar for flask
flask-avro (0.0.1)                             - Simple AVRO IPC endpoint
                                                 registration for Flask
flask-awesomemongokit (0.3.3)                  - Sets up an extremely
                                                 opinionated MongoKit
                                                 environment in Flask, based
                                                 selfishly on my own needs.
Flask-AYAH (0.1)                               - Are you a Human? Flask
                                                 Extension
Flask-Azure-Storage (0.2.1)                    - Flask extension that provides
                                                 integration with Azure
                                                 Storage
Flask-Imagine-AzureAdapter (0.4)               - Microsoft Azure BLOB adapter
                                                 for Flask-Imagine extension.
Flask-B1Connector (0.0.1)                      - Use to connect SAP B1 RESTful
                                                 API.
flask-babel-utclocal-utils (0.1.0)             - UTC to local (and vice versa)
                                                 datetime conversion utilities
                                                 for use with Flask-Babel.
Flask-Babel (0.11.2)                           - Adds i18n/l10n support to
                                                 Flask applications
Flask-Babel2 (0.1)                             - Adds i18n/l10n support to
                                                 Flask applications
Flask-Babeled (0.9.3)                          - Adds i18n/l10n support to
                                                 Flask applications
Flask-BabelEx (0.9.3)                          - Adds i18n/l10n support to
                                                 Flask applications
Flask-BabelPkg (0.9.6)                         - Adds i18n/l10n support to
                                                 Flask applications and
                                                 extensions
Flask-BabelPlus (2.1.0)                        - Adds i18n/l10n support to
                                                 Flask applications
Barista (0.0.22)                               - A Flask application creator
Flask-BasicAuth (0.2.0)                        - HTTP basic access
                                                 authentication for Flask.
Flask-HAL-BBVA (1.0.5)                         - Provides easy integration of
                                                 the HAL specification for
                                                 your REST Flask Applications.
Flask-Bcrypt (0.7.1)                           - Brcrypt hashing for Flask.
Flask-BCS (0.9.1)                              - Baidu Cloud Storage for Flask
Flask-BDEA (0.1.0)                             - Flask-BDEA
Flask-Beaker (0.2.0)                           - Beaker session interface for
                                                 Flask.
flask-beans (1.2)                              - A simple API for counting
                                                 beans with Flask and Redis.
Flask-Beanstalk (0.0.3)                        - Utilities for using Beanstalk
                                                 with Flask
Flask-BearyChat (0.2.0)                        - A Flask extension to help
                                                 interact with BearyChat
behave-models-steps (0.1.6)                    - Provides testing for Flask-
                                                 SQLAlchemy models with Behave
flask-bigtempo (0.8)                           - Flask extension for bigtempo
                                                 features
Flask-bitjws (0.1.1.5)                         - A Flask extension for bitjws
                                                 authentication.
Flask-Bitmapist (0.1.2)                        - Flask extension that creates
                                                 a simple interface to
                                                 Bitmapist analytics library
biweeklybudget (0.1.2)                         - Responsive Flask/SQLAlchemy
                                                 personal finance app,
                                                 specifically for biweekly
                                                 budgeting.
Flask-Bleach (0.0.2)                           - Easy integration of bleach
flask-blitzdb (0.1)                            - Flask extension for blitzdb
flask-block (0.0.1)                            - 
flask-blocks (1.0.4)                           - The common blocks which solve
                                                 common problems encountered
                                                 when creating Flask
                                                 applications.
blocky (0.0.2)                                 - Block rendering for flask and
                                                 django using jinja2.
Blogging-Plugins (0.2.0)                       - A plugin library for Flask-
                                                 Blogging flask extension
                                                 blog.
Flask-Blogging (0.8.0)                         - A flask extension for adding
                                                 Markdown blog support to your
                                                 site
Bluebook (0.0.1)                               - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
blueflask (0.1.4)                              - Flask boilerplate to create
                                                 an application with the idea
                                                 of pluggable blueprints.
flask-bluelogin (0.2.1)                        - Flask BlueLogin module
flask-social-blueprint (0.7.2)                 - An OAuth based authentication
                                                 blueprint for flask. Easy to
                                                 extend and override
flask-boilerplate-utils (0.1.65)               - Additional functionality with
                                                 easy upgrading for the flask-
                                                 boilerplate.
Flask-Turbo-Boost (0.0.10)                     - Forked Flask-Boost - Flask
                                                 application generator for
                                                 boosting your development.
Flask-Boost (0.7.5)                            - Flask application generator
                                                 for boosting your
                                                 development.
Flask-SQLAlchemy-Booster (0.4.96)              - Querying and JSON Response
                                                 generation wrappers for
                                                 Flask-SQLAlchemy
BootFlask (0.1)                                - A simple tool for turn your
                                                 flask projects more quick and
                                                 fun.
Flask-Bootstrap (3.3.7.1)                      - An extension that includes
                                                 Bootstrap in your project,
                                                 without any boilerplate code.
Flask-Bootstrap3 (3.1.1.3)                     - UNKNOWN
Flask-Bootstraps (3.3.7.2.dev1)                - An extension that includes
                                                 Bootstrap in your project,
                                                 without any boilerplate code.
Facebook-Bot-Library (0.1)                     - A facebook messaging SDK for
                                                 Flask
Flask-Boto3 (0.2.2)                            - Flask extension that ties
                                                 boto3 to the application
Flask-BotoSQS (0.2.0)                          - Boto3 SQS integration for
                                                 Flask
flask-bouncer (0.1.13)                         - Flask Simple Declarative
                                                 Authentication based on Ryan
                                                 Bates excellent cancan
                                                 library
Flask-S3-Bower (0.7)                           - Seamlessly serve the static
                                                 files of your Flask app from
                                                 Amazon S3 and also use bower
                                                 for development
Flask-Bower (1.2.1)                            - An extension to manage and
                                                 serve your javascript assets
                                                 with bower
Flask-BowerCDN (0.1.0)                         - Work easily with Bower and
                                                 CDN content.
flask-shell-bpython (0.0.1)                    - Replace the default `flask
                                                 shell` command with a similar
                                                 command running BPython.
flask-braintree (0.01)                         - 
Flask-Breadcrumbs (0.4.0)                      - Flask-Breadcrumbs adds
                                                 support for generating site
                                                 breadcrumb navigation.
Flask-Breathalyzer (0.2.2)                     - Flask module for submitting
                                                 timings and exceptions to
                                                 Datadog
Flask-Breve (0.2)                              - Breve templating with Flask
Flask-Bridgekeeper (0.1.1)                     - Manage the access control of
                                                 a flask application
Flask-outdated-browser (0.1)                   - Easily add outdated-browser
                                                 project to your Flask
                                                 application
Flask-BrowserID (0.0.4)                        - Flask support for BrowserID
                                                 authentication
Flask-BS (0.5.5)                               - Another flask extension that
                                                 provides Bootstrap CSS, JS
                                                 and HTML5 boilerplate.
Flask-BSON (0.1.1)                             - Let your flask endpoints
                                                 handle BSON requests and
                                                 responses
buchner (0.1.dev)                              - Flask project template and
                                                 helper library
flask-buckets (0.1.dev)                        - Simple and easy file storages
                                                 for Flask
bugsnag (3.1.0)                                - Automatic error monitoring
                                                 for django, flask, etc.
buildbot-wsgi-dashboards (0.9.7)               - Buildbot plugin to integrate
                                                 flask or bottle dashboards to
                                                 buildbot UI
Flask-Bulbs (0.1)                              - Flask extension for
                                                 [Bulbs](http://bulbflow.com/)
                                                 supporting the factory
                                                 pattern with the init_app
                                                 method.
flask-bundle-system (0.1)                      - Flask extension for work with
                                                 blueprints as bundles
Flask-Bundle (0.4)                             - Class based tool that behaves
                                                 like blueprints
flask-static-bundle (0.1.3)                    - Flask extension for static-
                                                 bundle
flask-graylog-bundle (0.0.7)                   - Flask Graylog client
Buro (0.1.27)                                  - A very simple Python-powered
                                                 open-source web framework
                                                 inspired by Flask, but
                                                 following different design
                                                 decisions
burp-ui (0.5.1)                                - Burp-UI is a web-ui for burp
                                                 backup written in python with
                                                 Flask and jQuery/Bootstrap
http-butler (0.4.0)                            - Light flask server
Flask-Cache-PyLibMC (0.1)                      - PyLibMC cache for Flask-
                                                 Cache, supports multiple
                                                 operations and other awesome
                                                 things.
Flask-Cache-Latest (0.12)                      - Adds cache support to your
                                                 Flask application
Flask-Cache-Redis-Cluster (0.0.5)              - Adds redis cluster caching
                                                 support to the Flask
                                                 Cache(ing) extension
Flask-SQLAlchemy-Cache (0.1.5)                 - CachingQuery implementation
                                                 to Flask using Flask-
                                                 SQLAlchemy and Flask-Cache
Flask-Cache-Cassandra (0.14.6)                 - Adds cache support to your
                                                 Flask application
Flask-Dogpile-Cache (0.2)                      - Adds dogpile.cache support to
                                                 your Flask application
Flask-Cache (0.13.1)                           - Adds cache support to your
                                                 Flask application
Flask-CacheControl (0.1.2)                     - Set Cache-Control headers on
                                                 the Flask response
Flask-Heroku-Cacheify (1.6.0)                  - Automatic Flask cache
                                                 configuration on Heroku.
Flask-CacheOBJ (0.2.2)                         - Flask-CacheOBJ provides some
                                                 caching decorators
Flask-Caching (1.2.0)                          - Adds caching support to your
                                                 Flask application
Flask-Cachual (0.2.0)                          - Flask extension for the
                                                 Cachual library
Flask-Cake (0.3.1)                             - Flask extension to execute
                                                 Cake on filesystem events.
flask-canvas (0.1)                             - A Flask extension for
                                                 Facebook canvas-based apps
capitains-hook (1.0.0)                         - Hook Flask App for Github/CTS
                                                 repositories
Flask-Captain (0.1.1)                          - Handle webhooks with Flask
Flask-Captcha (0.1.8)                          - A very simple, yet powerful,
                                                 Flask captcha extension
carafe (0.4.7)                                 - Collection of Flask
                                                 extensions geared towards
                                                 JSON APIs
cartographer (0.2.0-alpha5)                    - Python library for using JSON
                                                 API, especially with Flask.
Flask-CAS (1.0.1)                              - Flask extension for CAS
Flask-Cassandra (0.14)                         - Provides a connection to a
                                                 Cassandra cluster in a Flask
                                                 app
cassandra_flask_sessions (0.3)                 - Server side sessions with
                                                 Apache Cassandra
Flask-CassandraDB (0.0.1)                      - connect cassandra to flask
Flask-Caster (0.1.0)                           - A simple Flask extension for
                                                 automatically casting the
                                                 type of query arguments.
castle-flask (0.0.1)                           - A Flask client for Castle.io
Flask-Cavage (0.4.2)                           - Verify cavage-http-signatures
                                                 requests made to Flask
flask-cbv (0.0.1)                              - Class based views for Flask.
Flask-CDN-NG (1.3.0)                           - Serve the static files in
                                                 your Flask app from a CDN.
Flask-CDN (1.5.3)                              - Serve the static files in
                                                 your Flask app from a CDN.
Flask-Celery-Helper (1.1.0)                    - Celery support for Flask
                                                 without breaking PyCharm
                                                 inspections.
Flask-Celery (2.4.3)                           - Celery integration for Flask
Flask-Celery-py3 (0.2.4)                       - Celery 3.0+ integration for
                                                 Flask (Python 3 version)
Flask-Celery3 (0.2)                            - Add Celery3 integration to
                                                 your Flask apps.
Flask-CeleryExt (0.3.0)                        - Flask-CeleryExt is a simple
                                                 integration layer between
                                                 Celery and Flask.
Flask-Cent (0.1.3)                             - centrifugal/cent client for
                                                 flask
centralsession (0.3.0)                         - A redis based session storage
                                                 that works for flask and
                                                 django
Flask-Multipass-LDAP-CERN (1.0.2)              - CERN-specific Flask-Multipass
                                                 providers
python-cfworker (1.6.0)                        - This module makes it easier
                                                 to deploy Python workers by
                                                 wrapping Flask and
                                                 multiprocess functionality
                                                 into a single module. When
                                                 instanced, your app will be
                                                 serving http via Flask, as
                                                 well as performing work.
cheddar (1.4)                                  - PyPI clone with Flask and
                                                 Redis
chiki (1.1.1)                                  - Common libs of flask web
                                                 develop
chill (0.3.1)                                  - Database driven web
                                                 application framework in
                                                 Flask
Flask-Church (0.0.1)                           - Flask-Church is a extension
                                                 for     Flask that help you
                                                 generate fake data for
                                                 testing
Flask-CI (1.2.9.1)                             - Continuous Integration
                                                 support for Flask
Flask-CKEditor (0.1.0)                         - Implementation of CKEditor
                                                 for Flask-WTF.
flask-clacks (1.0.1)                           - A man is not dead while his
                                                 name is still spoken.
Flask-Classful (0.13.1)                        - Class based views for Flask
Flask-Classy (0.6.10)                          - Class based views for Flask
clay-flask (2.1.5)                             - Clay is a framework for
                                                 building RESTful backend
                                                 services using best
                                                 practices.
Flask-Clearbit (0.1.0)                         - Flask-Clearbit
Flask-CLI (0.4.0)                              - Backport of Flask 1.0 new
                                                 click integration.
Flask-Click-Migrate (0.1.0)                    - A library to glue flask +
                                                 alembic + click
platformo-client (0.0.1)                       - 收集Flask的请求响应时间并发送至logstash
Potion-client (2.5.1)                          - A client for APIs written in
                                                 Flask-Potion
klue-client-server (0.0.115)                   - Swagger + Flask + Bravado =
                                                 Client/Server auto-spawning
Flask-Cloudy (1.0.1)                           - Flask-Cloudy is a simple
                                                 flask extension and
                                                 standalone library to upload
                                                 and save files on S3, Google
                                                 storage or other Cloud
                                                 Storages
Flask-CMDB (0.1.4)                             - A cmdb api client for Flask
                                                 applications.
Flask-CMS (0.0.1)                              - Extensible Content Management
                                                 System for Flask: Pages,
                                                 Blogs, Comments and more.
Flask-CMS-Core (0.01)                          - 
coaster (0.5.2)                                - Coaster for Flask
Flask-Swagger-Codegen (0.0.6)                  - Generate Flask code from
                                                 Swagger docs.
swagger-py-codegen (0.2.7)                     - Generate Flask code from
                                                 Swagger docs.
flask-codemirror (1.0)                         - Use CodeMirror Javascript
                                                 library with Flask-WTF
Flask-Coffee (0.3)                             - Fill your flask with coffee.
flask-coffee2js (0.1.2)                        - A small Flask extension that
                                                 adds CoffeScript support to
                                                 Flask.
flask-cognito (0.0.1)                          - AWS Cognito User Auth for
                                                 Flask Applications
Flask-Collect (1.3.2)                          - Flask-Collect -- Collect
                                                 static files in Flask
                                                 application
Flask-Color (0.2.1)                            - flask-color is an extension
                                                 for Flask that improves the
                                                 built-in web server with
                                                 colors when debugging.
                                                 Unnecessary clutter such as
                                                 time or IP are hidden.
flask-command (0.0.3)                          - flask-command - Run you
                                                 flask+gunicorn app as a
                                                 command
Flask-Common (0.2.0)                           - A Flask extension with lots
                                                 of common time-savers (file-
                                                 serving, favicons, etc).
Flask-Compass (0.2)                            - Adds automatic Compass
                                                 compilation to Flask
Flask-Components (0.1.1)                       - A simple flask extension to
                                                 discover files in a declared
                                                 array of components.
Flask-Composer (0.4.1)                         - Composite Web UI extension
                                                 for Flask
Flask-Compress-nondebug (1.0.2)                - Compress responses in your
                                                 Flask app with gzip.
Flask-Static-Compress (1.0.0)                  - Auto-detects your static
                                                 files for minification,
                                                 combination, and versioning.
                                                 Like Django-Compressor for
                                                 Flask.
Flask-Compress (1.4.0)                         - Compress responses in your
                                                 Flask app with gzip.
Flask-Compressor (0.2.0)                       - Compress your CSS and JS
                                                 files.
flask-conditional (0.1)                        - Conditional decorators for
                                                 Flask routes
Flask-Config-Helper (0.1.1)                    - Flask configuration helper
Flask-Config-Override (0.0.2)                  - Override Flask configuration
                                                 via Cookie at runtime.
Flask-Config (0.2.1)                           - Flask configuration class
flask-confighelper (1.0.0)                     - Helper for setting up
                                                 environment configurations
flask-pre-configured-loggers (0.1.1)           - Flask request / script pre-
                                                 configured loggers.
Congo (0.0.1)                                  - Portfolio is a Flask based
                                                 framework that adds structure
                                                 and map your views and
                                                 templates together for rapid
                                                 application development
conmongo (0.0.2)                               - A Flask microplugin based on
                                                 pymongo
connexion (1.1.10)                             - Connexion - API first
                                                 applications with
                                                 OpenAPI/Swagger and Flask
flask-consulate (0.2.0)                        - flask extension that provides
                                                 an interface to consul via a
                                                 flask app
Container-WhooshAlchemyPlus (0.7.5.post3)      - Whoosh extension to
                                                 Flask/SQLAlchemy which used
                                                 in sina container
Flask-REST-Controller (1.0.0)                  - Flask-REST-Controller is
                                                 added Class-Based-
                                                 View(Controller) extension on
                                                 Flask
hepdata-converter-ws (0.1.6)                   - Flask webservices enabling
                                                 usage of hepdata-converter as
                                                 a separate server over the
                                                 network
flask-secure-cookie (0.1.2)                    - Tornado's secure cookie
                                                 support in Flask
flask-extension-cookiecutter (0.1.1)           - Cookiecutter template for a
                                                 Flask Extension
Flask-Copilot (0.2.0)                          - Simple navbar generation for
                                                 Flask applications.
corkscrew (0.18)                               - ooviews, settings, auth &
                                                 more for flask
Sanic-Cors (0.5.4.1)                           - A Sanic extension adding a
                                                 decorator for CORS support.
                                                 Based on flask-cors by Cory
                                                 Dolphin.
Flask-Cors (3.0.2)                             - A Flask extension adding a
                                                 decorator for CORS support
Flask-CORSify (0.1.1)                          - Add CORS support for your
                                                 Flask app.
Flask-CouchDB-Schematics (1.0.0)               - Provides utilities for using
                                                 CouchDB + Schematics with
                                                 Flask
Flask-CouchDB (0.2.1)                          - Provides utilities for using
                                                 CouchDB with Flask
Flask-CouchDBKit (0.3.5)                       - Flask extension that provides
                                                 integration with CouchDBKit.
Flask-CQLAlchemy (1.2.0)                       - Flask-CQLAlchemy handles
                                                 connections to Cassandra
                                                 clusters and provides an
                                                 interface through cqlengine
hero-crawl (0.1.4)                             - Helpers for Scrapy and Flask
                                                 on Heroku
Flask-Creole (0.4.4)                           - Creole parser filters for
                                                 Flask
flask-crossdomain (0.1)                        - HTTP Access Control helper.
Flask-Crossdomain2 (0.1.0)                     - Module for enabling cross-
                                                 site/cross-origin HTTP
                                                 requests on Flask app
                                                 endpoints.
Flask-SQLAlchemy-CRUD-Mixin (0)                - 
Flask-Crud (0.0.2)                             - Quick and Easy CRUD for
                                                 Flask, built on top of Flask-
                                                 Classy
flask-csp (0.9)                                - Flask Content Security Policy
                                                 header support
flask-csrf (0.9.2)                             - A small Flask extension for
                                                 adding CSRF protection.
Flask-CSV (1.0.1)                              - Easily render CSVs within any
                                                 flask application
CTRegisterMicroserviceFlask (0.3.0)            - Library to interact with the
                                                 Control-Tower api-gateway
                                                 (register, do requests to
                                                 other microservices, etc)
flask-ctx (1.0.0)                              - A simple integration of the
                                                 CTX defense against side-
                                                 channel attacks for Flask
                                                 projects.
Flask-CuddlyRest (0.1.15)                      - Flask restful API framework
                                                 for MongoDB/MongoEngine
flask-daapserver (3.0.2)                       - DAAP server framework
                                                 implemented with Flask
Flask-Dance (0.10.1)                           - Doing the OAuth dance with
                                                 style using Flask, requests,
                                                 and oauthlib
Flask-Dashboard (0.0.6a)                       - Yet another admin interface
                                                 for Flask
Flask-Dashed (0.1b2)                           - Adds a way to easily build
                                                 admin apps
Flask-Datadog (0.1.4)                          - Access to dogstatsd in your
                                                 app.
Flask-DB2 (0.0.10)                             - Creates connections for use
                                                 with DB2
Flask-DBConfig (0.3.12)                        - Configure Flask applications
                                                 from a local DB
Flask-DBKit (0.0.1)                            - dbkit integration for Flask.
Flask-DBMigrate (0.1)                          - Database schema change
                                                 management for
                                                 Flask\SQLAlchemy
Flask-DbShell (1.0)                            - Django-like dbshell
Flask-Debug (0.4.3)                            - Shows
                                                 reflection/configuration to
                                                 aid the development of Flask
                                                 applications.
flask-debugtb-elasticsearch (0.1.3)            - Flask debug toolbar panel for
                                                 elasticsearch queries.
Flask-DebugTool (0.1.8)                        - A toolbar overlay for
                                                 debugging Flask applications.
Flask-DebugToolbar-Mongo (0.1)                 - MongoDB panel for the Flask
                                                 Debug Toolbar
Flask-DebugToolbar-LineProfilerPanel (1.0.2)   - Panel for the Flask Debug
                                                 toolbar to capture and view
                                                 line-by-line profiling stats
Flask-DebugToolbar (0.10.1)                    - A toolbar overlay for
                                                 debugging Flask applications.
Flask-Decorators (0.0.1)                       - A list of Flask decorator
                                                 utilitiesnot include in the
                                                 origin flask project.
Flask-Defer (1.1.0)                            - Flask extension to defer task
                                                 execution under after request
                                                 teardown
Flask-Devices (0.0.1)                          - Flask extension for switching
                                                 template folder automatically
                                                 by User Agent
flask-oauth2-devices (0.0.1)                   - OAuth2 for devices flow
                                                 implementation for Flask
Flask-Diamond (0.5.1)                          - Flask-Diamond provides some
                                                 opinions about data-centric
                                                 Internet applications and
                                                 systems. Flask-Diamond is a
                                                 batteries-included Flask
                                                 framework, sortof like Django
                                                 but radically decomposable.
Flask-Diced (0.3)                              - Flask-Diced - CRUD views
                                                 generator for Flask
Flask-Digest (0.2.0)                           - A RESTful authentication
                                                 service for Flask
                                                 applications
flask-discoverer (0.0.2)                       - Flask API autodiscovery
Flask-Disqus (0.0.1)                           - Small extension for Flask to
                                                 make possible using Disqus
                                                 comments
Flask-Dissect (1.0.10)                         - Dissect Distributed Session
                                                 Control
Djam (0.9.8)                                   - Extends Django to work with
                                                 sqlalchemy and make it behave
                                                 like Flask
django-fsu (0.1.2)                             - Flask-Style URL Patterns for
                                                 Django
django-kungfu (0.2)                            - A Flasky approach to
                                                 distributed Django
                                                 configuration
Flask-DjangoQuery (0.2.4)                      - Django like query for Flask-
                                                 SQLAlchemy
flask-djcelery (0.1)                           - An integration of djcelery
                                                 with flask application
djeasyroute (0.0.2)                            - A simple class based route
                                                 system for django similar to
                                                 flask
Flask-Dmango (0.0.7)                           - Contents managements support
                                                 for Flask + MongoDB
                                                 applications
flask-docjson (0.1.7)                          - Validate flask request and
                                                 response json schemas via
                                                 docstring.
Flask-Docker (0.2.0)                           - Using Docker client in your
                                                 Flask application.
doctor (1.1.4)                                 - A module that assists in
                                                 using JSON schemas to
                                                 validate data in Flask APIs
                                                 and generate API
                                                 documentation.
Flask-DogStatsd (0.5.0)                        - A Flask extension for
                                                 dogstatsd-python
pylot-dojo (0.1.0)                             - MVC framework build on top of
                                                 flask
Flask-Sitemap-Domain (0.2.4)                   - Flask extension that helps
                                                 with sitemap generation.
Flask-DotEnv (0.1.0)                           - The .env file support for
                                                 Flask
python-dotenv (0.6.4)                          - Add .env support to your
                                                 django/flask apps in
                                                 development and deployments
webshare-download-manager (0.2.6)              - Download manager for
                                                 webshare.cz site. Flask +
                                                 requests.
Flask-Downloader (0.2)                         - Allow a Flask web app to
                                                 download files on behalf of
                                                 the user.
draftin_a_flask (0.1.5)                        - A simple Flask server that
                                                 allows you to publish Pelican
                                                 blags from http://draftin.com
Flask-Dropbox (0.3)                            - Dropbox Python SDK support
                                                 for Flask applications.
Flask-DropIn (0.0.1)                           - Flask-DropIn let you easily
                                                 organize large flask project.
Flask-Dropzone (1.3)                           - Upload file in Flask with
                                                 Dropzone.js.
Flask-Dry-Transaction (0.1.0)                  - A python package implementing
                                                 the strategy of business
                                                 transaction in flask
                                                 microservices developement
Flask-RESTful-DRY (0.3.1)                      - Flask-RESTful APIs using
                                                 declarations, not code
dscsrf (1.0)                                   - Double-submit CSRF protection
                                                 for Flask applications.
Flask-Should-DSL (0.4)                         - A flask extension for testing
                                                 with should-dsl
Flask-DStore (0.1.2)                           - DStore Web API and JS Client
                                                 using FLask
Flask-DWConnector (0.0.1)                      - Use to connect DataWald
                                                 RESTful API.
flask-dynamo (0.0.7)                           - DynamoDB integration for
                                                 Flask.
flask-east (1.0.0)                             - Flask extension for creating
                                                 REST APIs
Python-EasyConfig (0.1.6)                      - A simple library for loading
                                                 configurations easily in
                                                 Python, inspired by
                                                 `flask.config`.
easyflask (0.0.2)                              - Flask project generator
easyforms (0.0.7)                              - Form processing library for
                                                 Flask and Jinja2
flask-easymode (0.0.17)                        - Make Flask development even
                                                 easier
ecstatic (0.4)                                 - A small flask application to
                                                 serve files.
Flask-Ecstatic (0.3.0)                         - Serves static files with
                                                 optional directory index
Flask-Edits (0.8)                              - Editable Content in Flask
Flask-Elastic (0.2)                            - Integrates official client
                                                 for Elasticsearch into Flask
Flask-Elasticsearch (0.2.5)                    - Flask extension for
                                                 Elasticsearch integration
Flask-ElasticUtils (0.1.7)                     - ElasticUtils for Flask
Eliza (1.0.0)                                  - Library with common features
                                                 for Python (Flask)
                                                 Microservices
elsa (0.1.3)                                   - Helper module for Frozen-
                                                 Flask based websites
Flask-Email (1.4.4)                            - Flask extension for sending
                                                 email
flask-emails (0.4)                             - Elegant and simple email
                                                 library for Flask.
flask-jsonify-emidln (0.1)                     - A small Flask decorator for
                                                 returning json. This is a
                                                 fork pushed to PyPI for easy
                                                 install.
flask-phantom-emoji (0.1.4)                    - Add phantom emoji's to your
                                                 flask application
Empty (0.3.3)                                  - Wrapper which makes Flask
                                                 development easier
Flask-MIME-Encoders (0.1.3)                    - Extensible Flask MIME
                                                 encoders and decoders
flask-endpoint (0.1)                           - 
Flask-Enterprise (1.0)                         - Enterprise capabilities for
                                                 Flask
flask-env-settings (0.1.0)                     - Load application settings
                                                 from env variables
Flask-Env (1.0.1)                              - Easily set Flask settings
                                                 from environment variables
Flask-Heroku-Env (0.0.4)                       - Easily fetch Heroku
                                                 environment variables.
Flask-EnvConfig (0.2.0)                        - Configure Flask from
                                                 environment variables.
Flask-Environ (0)                              - os.environ wrapper for flask
                                                 config
Flask-Environment (0.3.1)                      - Configure a Flask application
                                                 with various file formats.
Flask-Environments (0.1)                       - Environment tools and
                                                 configuration for Flask
                                                 applications
Erlenmeyer (0.2.4)                             - Automatically generate Flask
                                                 servers from Core Data.
Flask-ErrorHandler (0.1.0)                     - Generic error handlers for
                                                 Flask blueprints.
Flask-ErrorMail (0.2.2)                        - Flask extension for sending
                                                 administrators e-mails with
                                                 stacktraces when internal
                                                 server errors occur.
Flask-ESClient (0.1.1)                         - Flask extension for ESClient
                                                 (elasticsearch client)
Flask-Espresso (0.2.0)                         - Adds Coffescript support to
                                                 Flask applications
espressocup (0.0.3)                            - A gevent-intended very very
                                                 basic flask-like WSGI server
Eve-SQLAlchemy (0.4.1)                         - REST API framework powered by
                                                 Flask, SQLAlchemy and good
                                                 intentions.
eventum (0.2.7)                                - A content management system
                                                 for event-driven Flask apps
Flask-Evolution (0.6)                          - Simple migrations for
                                                 Flask/SQLAlchemy projects
Flask-Excel (0.0.5)                            - A flask extension that
                                                 provides one application
                                                 programming interface to read
                                                 and write data in different
                                                 excel file formats
flask-script-exception-handler (0.1.1)         - Exception handler designed
                                                 mainly to handle errors in a
                                                 flask-script custom command.
Flask-Exceptional (0.5.4)                      - Adds Exceptional support to
                                                 Flask applications
Flask-Pypi-Proxy-Ext (0.5.1)                   - A Pypi proxy
tradenity-flask-ext (0.1.0)                    - Flask framework extensions
                                                 for Tradenity Python SDK.
Flask-JSONSchema-Ext (0.1.2)                   - Flask JSONSchema Extended
                                                 Library
Flask-Statsd-Ext (0.0.3)                       - Statsd Extension for Flask
invenio-ext (0.3.2)                            - Invenio module that provides
                                                 integration with Flask
                                                 extensions.
Flask-ExtDirect (0.2)                          - Adds Ext.Direct support to
                                                 Flask.
Flask-RESTful-extend (0.3.7)                   - Improve Flask-RESTFul's
                                                 behavior. Add some new
                                                 features.
Flask-JWT-Extended (2.2.0)                     - Extended JWT integration with
                                                 Flask
Flask-Logging-Extras (0.1.0)                   - Extra logging functionality
                                                 for Flask apps
eyeflask (0.1.3)                               - Flask-based EyeFi Server
Flask-Factory (0.1.0dev)                       - Provide a general-purpose
                                                 application factory of the
                                                 Flask application, and the
                                                 configurator that is
                                                 independent of the app
                                                 object.
fah (0.1.0)                                    - Flask Against Humanity
                                                 (copyright infringement
                                                 pending).
Flask-Failsafe (0.2)                           - A failsafe for the Flask
                                                 reloader
Fakes (0.2.0)                                  - flask-like wrapper around
                                                 asyncio
fannypack (0.0.4)                              - a set of utilities for flask
Flask-Fanstatic (0.2.0)                        - Flask integration for the
                                                 Fanstatic resource publishing
                                                 system.
Flask-FAS (0.1.0)                              - Adds Fedora Account System
                                                 support to Flask
fawn (2.1.1)                                   - flask async uwsgi websocket
                                                 postgresql notify
Flask-FBLogin (0.0.1)                          - Extends Flask-Login to use
                                                 Facebook's OAuth2
                                                 authorization
fbones (0.0.5)                                 - A bootstrap toolkit to
                                                 kickoff a flask project
Flask-FCM (0.1)                                - Flask Extension for using
                                                 Firebase Cloud Messaging
                                                 service
Flask-FDS (0.0.4)                              - Xiaomi File Storage Service
                                                 for Flask
fdt-sqlalchemy (0.0.3)                         - Flask-debugtoolbar
                                                 configurable SQLAlchemy panel
Flask-FeatureFlags (0.6)                       - Enable or disable features in
                                                 Flask apps based on
                                                 configuration
Flask-FedoraCommons (0.0.8)                    - Library for manipulating
                                                 Fedora Commons digitial
                                                 repositories
feiwu (0.0.3)                                  - some useful module on flask
                                                 developer
FejsaFlaskProject (1.0)                        - UNKNOWN
flask-ffs (0.3.0)                              - A Flask library for the
                                                 storage and retrieval of
                                                 images on the file system.
Flask-FIDO-U2F (0.4.4)                         - A Flask plugin that adds FIDO
                                                 U2F support.
Flask-RESTful-Fieldsets (0.1.0)                - Extension to Flask-RESTful to
                                                 create fieldsets
Fifty-Flask (1.2.0)                            - Flask enhancements.
fighting (0.1.0)                               - A simple JSON API web
                                                 framework based on Flask
Flask-FileRev (0.1.0)                          - Flask-FileRev
Flask-FileUpload (0.4.2)                       - Flask-FileUpload is a Flask
                                                 extension for easy file
                                                 upload and management
Flask-fillin (0.2)                             - A flask extension that
                                                 provides utilities to test
                                                 forms.
Flask-Filtered-Response (1.0.2)                - Add filter capability to JSON
                                                 responses
flask-filters (0.3)                            - The Flask Filter to use with
                                                 flask-restful and Relational
                                                 DB
finny (0.3.10)                                 - Finny is the act of being
                                                 skinny and fat at the same
                                                 time.
                                                 Basic structure for an api-
                                                 centry approach to Flask -
                                                 that is both fat in skinny,
                                                 with basic and augmented
                                                 support over some popular
                                                 Flask libs
fireflask (0.2.0)                              - Simple, beautiful logging
                                                 from Flask web apps to
                                                 FireBug console
fis3 (0.0.2)                                   - 扩展flask,支持fis3
Flask-Fixtures (0.3.7)                         - A simple library for adding
                                                 database fixtures for unit
                                                 tests using nothing but JSON
                                                 or YAML.
fl-static (0.0.2)                              - Serve production static files
                                                 with Flask.
Flask-Flacro (0.0.8)                           - flask/jinja2 templating tools
flactory (0.2.0)                               - A handy tool for creating and
                                                 initializing flask
                                                 applications
flagen (0.1)                                   - A flask static site generator
                                                 that uses markdown and jinja2
                                                 templates.
flamyngo (0.9.2)                               - Flamyngo is a customizable
                                                 Flask frontend for MongoDB.
flango (0.0.1)                                 - Flask-like interface for
                                                 Django
Flask-Flarf (0.0.5)                            - Flask request filtering
flasgger (0.6.4)                               - Extract swagger specs from
                                                 your flask project
Flask-Forward (0.1.0)                          - Flask-Forward extension
                                                 provides auto discovery,
                                                 prioritization and rendering
                                                 of template for Flask based
                                                 on endpoint
Flask-GripControl (0.0.1)                      - Flask GripControl
Flask-Humanoid (1.0)                           - Common humanization utilities
                                                 for Flask applications.
flask-iMail (0.1)                              - Mailgun integration for
                                                 Flask.
Flask-Imgur (0.1)                              - Upload images straight to
                                                 Imgur in your Flask app
Flask-kale (0.1)                               - Use kale models on a flask
                                                 project
Flask-Librato (0.0.1)                          - 
Flask-Lock (0.0.1)                             - 
flask-logsocketio (0.1.0)                      - Flask LogSocketIo module
Flask-Mage2Connector (0.0.1)                   - Use to connect Magento 2.
flask-manager (0.0.1a0)                        - A CRUD manager for Flask
flask-metrics (0)                              - 
Flask-MongoMyAdmin (0.1)                       - Simple MongoDB Administrative
                                                 Interface for Flask
flask-multistatic (1.0)                        - Simple flask plugin to allow
                                                 overriding static files
Flask-OmMongo (1.0)                            - Add Flask support for MongoDB
                                                 using OmMongo.
Flask-Pika-NG (0.3.3)                          - Pika amqp flask extension
flask-ratelimit (0.0.1)                        - 
Flask-ResponseFactory (0.1)                    - Create Flask response objects
                                                 in a declarative way
Flask-Search (0.01)                            - 
Flask-Sendmail (0.1)                           - Flask extension for sendmail
flask-sleep (0)                                - 
Flask-SQLAlchemy-Meiqia (2016.8.1)             - Adds SQLAlchemy support to
                                                 your Flask application
Flask-Static (0.1)                             - Generates a static website
                                                 from a Flask application
Flask-Stripe (0.1.0)                           - Flask-Stripe
Flask-TaskTiger (0.0.1)                        - Flask TaskTiger
Flask-Theme (0.1.0)                            - Provides infrastructure for
                                                 theming Flask applications
flask-urls (0.9.2)                             - A collection of URL-related
                                                 functions for Flask
                                                 applications.
Flask-User-Social (0.0.1)                      - Role based user
                                                 authentication for Flask.
                                                 Extends Flask-User.
Flask-Watson (0.1.0)                           - Flask-Watson
Flask-WebSocket (1.0)                          - simple websocket for Flask
flask-xuacompatible (0.1.0)                    - Sets X-UA-Compatible HTTP
                                                 header in your Flask
                                                 application.
Flask-YunPian (0.0.1)                          - Flask extension for YunPian
                                                 API
quokka-flask-login (0.3.0)                     - User session management for
                                                 Flask
flask-funktional-gae (0.0.1)                   - flask-funktional-gae
                                                 ~~~~~~~~~~~~~~~~~~~~  flask
                                                 extension to make functional
                                                 testing of flask applications
                                                 with the app engine sdk
                                                 easier.  used on top of the
                                                 `flask-funktional <http://git
                                                 hub.com/gregorynicholas
                                                 /flask-funktional>`_
                                                 extension, it provides setup
                                                 of app engine sdk stubs with
                                                 a focus on being transparent
                                                 and minimally invasive.
                                                 links `````  * `docs <http://
                                                 gregorynicholas.github.io
                                                 /flask-funktional-gae>`_ *
                                                 `source <http://github.com/gr
                                                 egorynicholas/flask-
                                                 funktional-gae>`_ * `package
                                                 <http://packages.python.org
                                                 /flask-funktional-gae>`_ *
                                                 `travis-ci <http://travis-
                                                 ci.org/gregorynicholas/flask-
                                                 funktional-gae>`_
Flask-Gladiator (0.1)                          - Gladiator is a Data
                                                 Validation Framework for
                                                 Python3 (Flask Plugin)
Flask-GoogleFed (0.1)                          - Google Federated Logins for
                                                 Flask.
Flask-gzip (0.1)                               - Compress responses in your
                                                 Flask app with gzip.
Flask-Habitat (0.1)                            - Selectively load Flask
                                                 configuration values from
                                                 environment variables at
                                                 runtime.
flask-handlers (0.0.1)                         - Handlers for Flask
                                                 applications
flask-inliner (1.0.0)                          - Flask-Inliner converts CSS
                                                 <style> blocks to inline
                                                 style attributes
Flask-Intercom (0.1.0)                         - Flask-Intercom
flask-jsonapi (0.1.0)                          - JSONAPI 1.0 implementation
                                                 for Flask.
Flask-JsonSchemer (0.0.1)                      - Flask extension for
                                                 validating JSON requets
Flask-JSON-Validation (0)                      - 
Flask-Kadabra (0.1.0)                          - Flask extension for the
                                                 Kadabra metrics framework
flask-keystone (0.2)                           - This project wraps the
                                                 existing keystone middleware
                                                 to provide courtesy user
                                                 functions within an API.
Flask-Landing (0.1.0)                          - Landing page for collecting
                                                 emails.
Flask-Latch (0.1.0)                            - Latch extension for Flask
Flask-LiveScript (0.1)                         - implements the webassets
                                                 filter for livescript
Flask-MenuBuilder (0.9.2)                      - An easy way to create menus
                                                 to use with flask.
Flask-MongoObject (0.1)                        - Access MongoDB from your
                                                 Flask application
Flask-MultipleBlueprint (0.1)                  - Decorate function using
                                                 multiple blueprints at once.
Flask-OldSessions (0.10)                       - Provides a session class that
                                                 works like the one in Flask
                                                 before 0.10.
Flask-Postmark (0.1.0)                         - Postmark Flask extension
Flask-Prometheus (0.0.1)                       - Prometheus client
                                                 instrumentation for flask.
                                                 See
                                                 http://github.com/sbarratt
                                                 /flask-prometheus
Flask-PyMssql (0.1.0)                          - PyMssql support for Flask
                                                 applications
Flask-Raptor (0.1)                             - Raptor support for Flask
Flask-Registry (0.2.0)                         - Flask-Registry is an
                                                 extension for Flask that
                                                 allow frameworks to
                                                 dynamically assemble your
                                                 Flask application from
                                                 reusable packages consisting
                                                 of blueprints, extensions,
                                                 and configurations.
flask-reveal (0.3)                             - Make reveal.js presentations
                                                 with Flask
flask-revise (0)                               - 
Flask-RIP (0.1)                                - 
Flask-Roughage (0.1)                           - Very short description
Flask-RouteLogger (0.1)                        - Logging the meta route level
                                                 request- response information
                                                 in the structured manner for
                                                 your flask web application
flask-secretbox-session (0.1.0)                - Flask client side session
                                                 serializer, using Sodium
                                                 SecretBox authenticated
                                                 encryption
flask-send-mail-util (0.1.0)                   - Send an email via the Flask-
                                                 Mail extension, using text
                                                 and HTML templates.
Flask-SimpleSQLA (1.0)                         - Extension providing basic
                                                 support of SQLAlchemy in
                                                 Flask applications
Flask-SocketAPI (0.2)                          - Lightweight library to create
                                                 streaming APIs over Flask-
                                                 SocketIO
Flask-SockJS (0.1.0)                           - Simple integration of Flask
                                                 and SockJS
Flask-Token (1.0)                              - 快速生成API认证令牌
Flask-Twilio (0.0.1)                           - Make Twilio voice/SMS calls
                                                 with Flask
Flask-UltraJSON (0.0.1)                        - Integrates UltraJSON with
                                                 your Flask application.
flask-uuid-utils (0.1.0)                       - Utilities for working with
                                                 UUID fields in Flask.
Flask-WebGlEarth (0.1.3)                       - Simple extension for Flask to
                                                 use WebGl Earth
Flask-Whiteprint (0.0.1)                       - An enhancement of flask
                                                 blueprint.
flask-wikimediaui (0.0.1)                      - This library provides python
                                                 Flask utilities and static
                                                 assets for rendering
                                                 Wikimedia UI elements
Flask-WX-OAuth (0.1.1)                         - Flask Extension for wechat
                                                 oauth2.0.
google-oauth-flask (0.0.1)                     - UNKNOWN
flask-funktional (0.0.1)                       - flask-funktional
                                                 ~~~~~~~~~~~~~~~~  flask
                                                 extension which hopes to make
                                                 functional testing easier.
                                                 links `````  * `documentation
                                                 <http://gregorynicholas.githu
                                                 b.io/flask-funktional>`_ *
                                                 `package
                                                 <http://packages.python.org
                                                 /flask-funktional>`_ *
                                                 `source <http://github.com/gr
                                                 egorynicholas/flask-
                                                 funktional>`_ * `development
                                                 version   <http://github.com/
                                                 gregorynicholas/flask-
                                                 funktional>`_
Flask-GSSAPI (1.0)                             - HTTP Negotiate (GSSAPI)
                                                 authentication support for
                                                 Flask applications.
Flask-Headers (1.0)                            - A Flask extension making
                                                 adding headers one decorator
                                                 away
Flask-ICU (0.9.1)                              - Adds i18n/l10n support to
                                                 Flask applications
flask-id (0.0.1)                               - 
Flask-InfluxDB (0.1)                           - Flask bindings for the
                                                 InfluxDB time series database
Flask-JIRA (0.0.2)                             - Flask extension that provides
                                                 simple integration with JIRA
                                                 REST API
Flask-JSUtils (0.1)                            - Flask utilities in your
                                                 javascript
Flask-MakoTemplates (0.2)                      - All future development will
                                                 be done under the name Flask-
                                                 Mako at
                                                 <http://pypi.python.org/pypi
                                                 /Flask-Mako>
flask-multiconfig (0.1)                        - A simple extension to add
                                                 advanced configuration source
                                                 support.
flask-myapi (0.1)                              - Flask-MyAPI - RESTful support
                                                 library for Flask
Flask-Negotiate (0.1.0)                        - Content negotiation utility
                                                 for Flask apps
Flask-NextCaller (0.1.0)                       - Flask-NextCaller
Flask-NoExtRef (0.1)                           - Support for hiding external
                                                 URL
Flask-Notifications (v0.1.0.dev20150000)       - 
Flask-oDesk (0.4.1.1)                          - Adds oDesk API support to
                                                 Flask
Flask-OrientDB (0.1)                           - A Flask extension for using
                                                 OrientDB with Flask
Flask-OtpAuth (0.0.1)                          - One Time Password
                                                 Authentication for Flask
Flask-Passlib (0.1)                            - Flask extension for passlib
flask-paypal (0.1.0)                           - Flask integration with
                                                 PayPal, mainly focused on
                                                 subscriptions.
Flask-Quik (0.1.1)                             - Quik for Flask
Flask-RequestID (0)                            - 
flask-request-id-middleware (1.0)              - Adds Request ID inside your
                                                 http requests to better
                                                 identify what's happening on
                                                 your app
Flask-Roots (0.0.1)                            - Lightweight personal git
                                                 server.
flask-rst (0.1)                                - Create a static website from
                                                 simple reStructuredText files
Flask-SaeStorage (0.9.0)                       - SAE Storage for Flask
flask-samurai (0.1)                            - Easily create Heroku addons
                                                 in Flask.
flask-schematics (0)                           - 
flask-segmentio (0.1.0)                        - Adds SegmentIO support to
                                                 your Flask application
flask-shell-ptpython (0.0.1)                   - Replace the default `flask
                                                 shell` command with a similar
                                                 command running Ptpython.
flask-simple (0.0.1)                           - SimpleDB integration for
                                                 Flask.
Flask-Sixpack (0.0.1)                          - Flask wrapper for Sixpack
Flask-SPF (0.0.0)                              - Flask-SPF
Flask-SSLify-flexme (0.1.6)                    - Force SSL on your Flask app.
Flask-WeChat (0.1.0)                           - a simple flask extension for
                                                 setup wechat service.
flask-wechat-kit (0.0.1)                       - flask blueprint for wechat
Flask-WTF-Polyglot (0.1)                       - Flask-WTF companion library
                                                 providing `PolyglotForm` for
                                                 polyglot HTML output
flask-yeoman (0.1.0)                           - UNKNOWN
flask-zabbix (0.1.1)                           - Zabbix API wrapper
Flask-ZODB (0.1)                               - Use the ZODB with Flask
Thread-Flask-Prometheus (0.0.2)                - Prometheus client
                                                 instrumentation for flask.
tdewitt_AC-Flask-HipChat (0.2.9.dev0)          - Atlassian Connect library
                                                 based on Flask for HipChat
hyperdns-flask (0.9.4)                         - HyperDNS Flask Utilities
Flask-FluidDB (0.1)                            - Fluiddb access for flask
Flask-FontAwesome-Headers (0.1.0)              - Sets CORS HTTP response
                                                 headers for Font-Awesome
                                                 files served by Flask's
                                                 send_file().
flask-gae (0.1.0-20140530)                     - Commons for Flask running on
                                                 Google App Engine
Flask-HipPocket (0.2.0b1)                      - A wrapper around Flask to
                                                 ease the development of
                                                 larger applications
Flask-HttpCaching (0.01)                       - flask http caching
Flask-HTTPS (0.1.0)                            - Make HTTPS required on any
                                                 Flask app
Flask-Imagine-GoogleAdapter (0.4)              - Google Cloud Storage adapter
                                                 for Flask-Imagine extension.
Flask-Imagine-S3Adapter (0.4)                  - Amazon AWS S3 adapter for
                                                 Flask-Imagine extension.
Flask-Ink (2.2.1)                              - Easily integrate Sapo Ink's
                                                 framework in your Flask
                                                 project.
flask-jade2underscore (0.1)                    - A small Flask extension adds
                                                 suppot to Jade2Underscore
                                                 templates compiler (used in
                                                 Backbone) to Flask.
Flask-Kits (0.0.1)                             - A simple and brief utility
                                                 tools framework
Flask-Maoko (0.1.1)                            - Mako templating support for
                                                 Flask applications.
Flask-Material-Lite (0.0.1)                    - An easy way to get started
                                                 with Google's Material Lite
                                                 in your next Flask project,
                                                 without any boilerplate code.
flask-memcache-session (2.0)                   - Use memcache for store
                                                 session data
Flask-Mime (0.1.0)                             - Provides MIME type based
                                                 request dispatching
                                                 mechanism.
Flask-Modus (0.0.1)                            - Flask Method Overriding
                                                 Middleware.
Flask-mongobit (0.1.2)                         - MongoBit support in Flask
flask-morepath (0.1)                           - UNKNOWN
flask-nap (0.0.1)                              - Flask REST Framework
Flask-OAuth2Server (0.1)                       - Flask-OAuth2Server allows you
                                                 to quickly add an OAuth2
                                                 provider to your Flask
                                                 application.
Flask-PluginEngine (0.2.2.dev0)                - 
Flask-PubSub (0.1.0)                           - Flask-PubSub
Flask-QSSession (0.3.0)                        - Add server-side session
                                                 support for Flask application
Flask-Resource (0.0.1)                         - Build resource-oriented Web
                                                 apps with Flask.
Flask-RethinkDB (0.2)                          - Adds RethinkDB support to
                                                 Flask
Flask-Sandbox (0.1.0)                          - ACL Route controls for Flask
flask-schema (0.1a)                            - Schema Validation for your
                                                 JSON APIs
Flask-SQLAlchemy-tw (3.0-dev-20160331)         - Adds SQLAlchemy support to
                                                 your Flask application
Flask-SRI (0.1.0)                              - Flask-SRI
flask-stacksentinel (1.2.1)                    - Stack Sentinel error tracking
                                                 integration with Flask
flask-stylus2css (0.1)                         - A small Flask extension that
                                                 adds Stylus support to Flask.
flask-swaggerui (0.0.1)                        - This library provides python
                                                 Flask utilities and static
                                                 assets for rendering Swagger
                                                 UI
flask-thumbor (0.1.0)                          - Flask utilities to use
                                                 thumbor images.
Flask-Transit (0.1.0-pre)                      - A flask extension for working
                                                 with transit data.
Flask-Tweepy (0.1)                             - Tweet easily from Flask
                                                 applications
Flask-Webhook (0.1.0)                          - Create Flask application
                                                 webhooks with attached
                                                 handlers
flask-webpackext (0.1.0)                       - Webpack integration for
                                                 Flask.
Flask-WkHTMLtoPDF (0.1.0)                      - Convert JavaScript dependent
                                                 Flask templates into PDFs
                                                 with wkhtmltopdf.
flask-ws (0.0.1.0)                             - Websocket for flask.
flask-wysiwyg (0.1)                            - flask-wysiwyg provides custom
                                                 form fields to render wysiwyg
                                                 editor instead of regular
                                                 textareas. It takes care of
                                                 cleaning html for you too.
                                                 With its super secure
                                                 defaults you do not want to
                                                 modified it's whitelisting
                                                 rules.
Flask-XStatic (0.0.1)                          - Flask support for XStatic
                                                 assets
launchkey-flask (0.1.0)                        - LaunchKey authentication
                                                 extension for Flask
flask-flywheel (0.1.0)                         - Adds Flywheel support to your
                                                 Flask application
Flask-Generator (0.1)                          - Generator tool to quickly
                                                 create flask application
                                                 skeleton.
Flask-Imagine-RackspaceAdapter (0.4)           - Rackspace Files adapter for
                                                 Flask-Imagine extension.
flask-ipblock (0.2)                            - Block certain IP addresses
                                                 from accessing your Flask app
Flask-Keen (0.1.0)                             - Flask-Keen
Flask-Leancloud-Sms (0.1)                      - Leancloud SMS Service for
                                                 Flask
flask-letsencrypt (0.1)                        - UNKNOWN
flask-log (0.1.0)                              - Configure logging in flask
                                                 applications
Flask-MongoRest-Swagger (0.1)                  - Swagger API generation for
                                                 Flask-MongoRest
Flask-MoSession (0.2)                          - Mongodb based server side
                                                 session management system for
                                                 Flask
flask-negotiate2 (0.2.0)                       - Content negotiation utility
                                                 for Flask apps
Flask-NIH (0.1.0.dev1)                         - A toolkit to write static
                                                 site generators using Flask
                                                 as a basis.
Flask-NSQ (0.1.0)                              - Adds NSQ support for your
                                                 Flask application
Flask-OAuth2 (0.01)                            - 
Flask-OAuthRes (0.1.0)                         - OAuth Resource for Flask
Flask-Obscure (1.0)                            - Obscure numerical IDs in URLs
flask-oslolog (0.1)                            - This project wraps the
                                                 existing oslo.log library to
                                                 providerequest logging and
                                                 logger access within flask..
Flask-PAM (0.1rc1)                             - Flask authentication using
                                                 PAM
Flask-PJAX (0.0.1)                             - PJAX Templating for Flask
                                                 Applications
Flask-Pony (1.0.1)                             - PonyORM for your Flask
                                                 application
Flask-Register (0.1.0)                         - A extension of Flask to
                                                 control Register view.
Flask-RegisterBlueprints (0.1.0)               - Dynamically register Flask
                                                 blueprints on application
                                                 object
Flask-ResponseExt (0.2.0)                      - An extension of the Flask
                                                 Response class.
Flask-RESTbolt (0.1.0)                         - Powerful and fast framework
                                                 for creating REST APIs with
                                                 Flask
flask-restful-swagger-flexme (0.20)            - Extract swagger specs from
                                                 your flast-restful project
flask-r-login (0.0.1)                          - 
Flask-Scaffold (0.5.1)                         - Scaffold Database
                                                 Applications in MySQL or
                                                 PostgreSQL with Flask
flask-simple-login (0.0.1)                     - Easily turn your python data
                                                 into a flot graph in a static
                                                 html file.
Flask-SocialShare (0.0.1)                      - Flask social sharing helpers
flask-spring (0.1.0)                           - Adds the Spring framework
                                                 support to your Flask
                                                 application
Flask-SQLService (0.1.0)                       - Flask extension for
                                                 sqlservice
Flask-SSDB (0.0.1)                             - Flask simple ssdb client
Flask-Storm (0.1.0)                            - Storm integration for Flask.
flask-structlog (0)                            - 
flask-toolbox (0.0.2)                          - A flask toolbox.
Flask-Upload (0.0.1)                           - A simple and brief utility
                                                 tools framework
Flask-UserEnvConfig (0.1.12)                   - Configure a flask app with
                                                 environment variables or a
                                                 file.
Flask-Validictory (0.1.0)                      - Simple integration between
                                                 Flask and Validictory.
flask-zappa (0.0.1)                            - Serverless Flask With AWS
                                                 Lambda + API Gateway
toga-flask (0.0.0)                             - A Flask backend for the Toga
                                                 widget toolkit.
Flask-Fleem (0.0.5)                            - Theming for Flask
                                                 applications
Flask-Gist (0.1.1)                             - A simple flask extension to
                                                 render Github Gists on
                                                 template
Flask-Graylog (1.1.0)                          - Configure Graylog logging
                                                 handlers and middleware for
                                                 your Flask app
flask-itemshop (0.2)                           - Simple flask blueprint
                                                 (ItemBP) that you can mount
                                                 in your app to get a basic
                                                 purchase flow for a single
                                                 item. Credit card processing
                                                 is done with stripe.js and
                                                 the stripe python API.
Flask-JsonSchemaValidator (0.2)                - Basic JSON Schema Validator
                                                 for the Flask web framework.
flask-jsontools-slippers (0.1.6)               - JSON API tools for Flask
Flask-Kerberos (1.0.4)                         - Kerberos authentication
                                                 support for Flask
flask-konch (1.1.0)                            - An improved shell command for
                                                 the Flask CLI
Flask-Manifest (0.2.0)                         - Asset manifest integration
                                                 with Flask.
Flask-MarrowMailer (0.2.0)                     - Marrow Mailer integration for
                                                 Flask.
flask-MenuManager (1.0a2)                      - An easy way to build and
                                                 manage menus in Flask
flask-praetorian (0.2.1rc1)                    - Strong, Simple, and Precise
                                                 security for Flask APIs
Flask-Project (0.1.1)                          - Flask project template
                                                 generator.
Flask-RateLimiter (0.2.0)                      - Flask-RateLimiter is an
                                                 extension for Flask that adds
                                                 support for rate limiting.
Flask-Redistore (1.0.1)                        - Adds Redis support to your
                                                 Flask applications
Flask-ReqArg (0.1.5)                           - The decorator that maps
                                                 request arguments into
                                                 function arguments.
flask-request-id (0.1)                         - Extract yourself some Request
                                                 IDs.
Flask-SSE (0.2.1)                              - Server-Sent Events for Flask
Flask-StatsD (0.1.1)                           - Access to statsd in your app.
Flask-WAT (0.0.2)                              - 
Flask-Webhelpers (0.1)                         - Simple integration of Flask
                                                 and Webhelpers
Flask-Zipkin (0.0.2)                           - An zipkin extension for Flask
                                                 based on py_zipkin.
quokka-flask-security (1.7.4dev2)              - Fork of Simple security for
                                                 Flask apps
thunderdome-flask (1.0.2)                      - Thunderdome Flask integration
graphql-flask (1.1.0)                          - Adds GraphQL support to your
                                                 Flask application
Flask-FlatPagesCut (0.5.1)                     - Flask-FlatPagesCut is fork
                                                 Flask-FlatPages (Provides
                                                 flat static pages to a Flask
                                                 application)
Flask-fluentd (0.2)                            - Log fluentd events from Flask
Flask-Fundatio (0.1)                           - Flask extension to integrate
                                                 the Foundation front-end
                                                 framework
flask-gae_messages (1.0.1)                     - Flask extension for working
                                                 with messages using the mail
                                                 & xmpp apis on App Engine.
flask-gemoji (0.2.0)                           - Add gemojis to your Flask
                                                 apps
Flask-Heroku-Helpers (0.0.2)                   - Flask helpers for Heroku Apps
Flask-Heroku-Runner (2)                        - Minimalist Heroku bootstrap
                                                 for Flask
flask-http2-push (0.0.3)                       - A Flask extension to add
                                                 http2 server push to your
                                                 application.
Flask-JsonSchema (0.1.1)                       - Flask extension for
                                                 validating JSON requets
flask-login-openerp (0.2.0)                    - OpenERP Login for Flask using
                                                 Flask-Login
Flask-OpenAPI (0.1.0a1)                        - Generate a swagger.json
                                                 handler from a Flask app
Flask-Paginated-Response (1.0.1)               - Response maker for Flask with
                                                 RFC Standards such as Link
                                                 Headers
Flask-Restdoc (0.0.2)                          - Flask-Restdoc is a simple
                                                 tool that generates RESTful
                                                 API documentation
                                                 automatically from python
                                                 files.
flask-restless-swagger (0.2.1)                 - Magically create swagger
                                                 documentation as you
                                                 magically create your RESTful
                                                 API
Flask-SAPB1 (0.0.2)                            - Use to connect SAP B1 DI API.
Flask-SL (0.0.4)                               - Basic recognition of Second
                                                 Life® requests.
Flask-Stache (0.1.1)                           - Simple mustache templating
                                                 for Flask applications
flask-thumbs (1.2)                             - An extension managing
                                                 thumbnail based on flask-
                                                 thumbnails
flask-tml (0.3.1)                              - Flask SDK for
                                                 tranlationexchange.com API
Flask-Wdb (0.0.2)                              - Integrate Wdb instead of
                                                 Werkzeug debugger for Flask
                                                 applications
labirinto-flask (0.1.1)                        - Joguinho de labirinto usando
                                                 Flask + GTM
flask-graphql-subscriptions-transport (0.1.4)  - Adds subscription transport
                                                 layer for Flask applications
                                                 using GraphQL
Flask-GSA (0.1.1)                              - A simple wrapper for the
                                                 Google OAuth2 client library
Flask-Gunicorn (0.1.1)                         - 
Flask-Hashing (1.1)                            - Easy hashing of data in Flask
Flask-Inject (1.1.0)                           - A micro dependency injection
                                                 framework for Flask micro web
                                                 framework :)
Flask-Jigger (0.0.2)                           - Web APIs for Flask,
                                                 unintrusive.
Flask-JWTAuthorization (0.0.5)                 - Authorization framework based
                                                 on JWT for Flask applications
Flask-Migrate-tw (1.8.1)                       - A custom version of Flask-
                                                 Migrate, which depends on
                                                 Flask-SQLAlchemy-
                                                 tw(v3.0)using Alembic
Flask-MongoSet (0.1.8)                         - Access MongoDB from your
                                                 Flask application
Flask-Multi-Session (0.1.7)                    - Redis multi-sessions for
                                                 Flask apps
Flask-NYC (0.1.1)                              - New York Flask Meetup
Flask-Pagination (0.0.1)                       - Pagination Helpers for Flask
                                                 Apps
flask-passwordless (0.1.1)                     - Flask extension for
                                                 passwordless login
Flask-Phrase (1.0.0)                           - Connect your Flask apps to
                                                 PhraseApp, the powerful in-
                                                 context-translation solution.
Flask-SACore (0.0.3)                           - SQLAlchemy Core extension for
                                                 Flask
Flask-SES (0.1.1)                              - Flask extension for
                                                 interfacing with AWS' SES
                                                 service
flask-sqlalchemy-rls (0.0.2)                   - Flask-SQLAlchemy with row-
                                                 level security
Flask-Storage (0.1.1)                          - Flask upload and storage
                                                 extensions.
Flask-Storage-Helpers (0.1.5)                  - Various file storage backends
                                                 for Flask apps.
flask-template-loader (0.0.3)                  - UNKNOWN
Flask-Triangle-joeflack4 (0.5.6)               - Integration of AngularJS and
                                                 Flask, originally created by
                                                 Morgan Delahaye-Prat
                                                 (mdp@m-del.fr).
flask-yamli18n (0.1.4)                         - Use yaml files as translation
                                                 files in flask
Flask-FormEncode (0.10.1)                      - A form validation extension
                                                 for Flask using the
                                                 FormEncode package.
flask-go (0.1.1)                               - Let you create flask project
                                                 like use django-admin
flask-heroku-mongoengine (0.1.5)               - Heroku environment variable
                                                 configurations for Flask
Flask-Heroku-RQify (0.2)                       - Automatic RQ configuration
                                                 for your Heroku Flask
                                                 applications.
Flask-libsass (1.1.0)                          - Flask extension for building
                                                 css from sass or scss
Flask-Mobility (0.1.1)                         - A Flask extension to simplify
                                                 building mobile-friendly
                                                 sites.
Flask-MySQLdb (0.2.0)                          - MySQLdb extension for Flask
Flask-PaperTrail (0.0.2)                       - Adds PaperTrail logging to
                                                 your Flask application
Flask-Pigeon (0.11.0)                          - Flask messages extension.
Flask-PyFCM (0.1.1)                            - Flask extension for PyFCM
Flask-PyQuery (0.1)                            - PyQuery templating support
                                                 for Flask applications.
Flask-QiniuStorage (0.9.4)                     - Qiniu Storage for Flask
flask-rollbar (1.0.1)                          - A sane configuration for
                                                 Rollbar for Flask selfishly
                                                 based on my own needs
Flask-Router (0.1.1)                           - Tuned flask's URL routing
                                                 library
Flask-RQ (0.2)                                 - RQ (Redis Queue) integration
                                                 for Flask applications
Flask-Sass (0.9)                               - A small Flask extension that
                                                 makes it easy to use Sass
                                                 with your Flask application.
Flask-Shelve (0.1.1)                           - Shelve support for Flask
Flask-Sockets-Tornado (0.1.1)                  - Elegant WebSockets for your
                                                 Flask apps.Tornado style app
                                                 included
Flask-Sphinx-Themes (1.0.1)                    - Sphinx themes for Flask and
                                                 related projects.
flask-tmpl (0.2.0)                             - PasteScript templates for the
                                                 Flask+Celery+SQLAlchemy
Flask-Travis (0.0.2)                           - Easily fetch Travis CI
                                                 environment variables when
                                                 testing.
Flask-UUID (0.2)                               - UUID url converter for Flask
                                                 routes
Flask-WatQY (0.0.3)                            - 
Flask-Zurb-Foundation (0.2.1)                  - A Foundation Wrapper for
                                                 Flask
Flask-FlatPages-Pandoc (0.2)                   - Pandoc rendering for Flask-
                                                 FlatPages
Flask-Gfwlist2Pac (0.0.2)                      - Flask application to generate
                                                 PAC file based on gfwlist
Flask-httpretty (1.3.0)                        - flask-httpretty help you to
                                                 mock http requests via flask.
flask-lesscss (0.9.1)                          - A small Flask extension that
                                                 adds LessCSS support to
                                                 Flask.
Flask-Mistune (0.1.1)                          - A interface between the Flask
                                                 web framework and the Mistune
                                                 Markdown parser.
Flask-OlinAuth (1.0.1)                         - A simple Flask extension
                                                 implementing Olin's
                                                 authentication
flask-optimize (0.2.6)                         - Flask optimization: cache,
                                                 minify html and gzip response
flask-otp (1.2)                                - One-Time Password extension
                                                 to Flask
flask-ponywhoosh (1.0.1)                       - A search engine for flask
                                                 framework using pony orm.
Flask-Profile (0.2)                            - Flask Application Profiler
flask-project-templates (0.2)                  - Paster templates for creating
                                                 Flask projects
Flask-Prose (0.1.49)                           - A flask extension for
                                                 generating markov prose
Flask-Pyco (0.2)                               - Simple flat file CMS inspired
                                                 by Pico and Jekyll
Flask-Reggie (0.0.2)                           - Flask Regex Routes.
Flask-Responses (0.2)                          - Simple response utility for
                                                 Flask
Flask-REST (1.1)                               - A simple REST toolkit for
                                                 Flask
flask-robohash (1.0.1)                         - robohash.org avatars that you
                                                 can use with the
                                                 microframework Flask.
Flask-SAResource (0.1.1)                       - Flask extension for building
                                                 routes from SQLAlchemy models
flask-sqlacodegen (1.1.6.1)                    - Automatic model code
                                                 generator for SQLAlchemy with
                                                 Flask support
Flask-SQLAlchemy-Session (1.1)                 - SQL Alchemy session scoped on
                                                 Flask requests.
flask-swagger-plus (0.0.3)                     - extract swagger spec from
                                                 source code and docstring for
                                                 a flask app
flask-telegram (0.0.2)                         - flask-telegram  flask
                                                 extension for delivering
                                                 messages. send via the app
                                                 engine mail or xmpp apis,
                                                 and/or other third party
                                                 providers such as sendgrid.
                                                 links:  * docs: http://gregor
                                                 ynicholas.github.io/flask-
                                                 telegram * source: http://git
                                                 hub.com/gregorynicholas
                                                 /flask-telegram * package:
                                                 http://packages.python.org
                                                 /flask-telegram * travis-ci:
                                                 http://travis-
                                                 ci.org/gregorynicholas/flask-
                                                 telegram
flask-transfer (0.1.0)                         - Validate and process file
                                                 uploads in Flask easily
flask-utils (0.1.1)                            - Various Flask utilities.
Flask-WXApp (0.1.2)                            - Flask Extension for WeChat
                                                 App.
Flask-Zen (0.2)                                - Flask-Script commands to
                                                 integrate with PyZen.
flask-gae_blobstore (1.0.2)                    - Flask extension module for
                                                 working with the blobstore &
                                                 files apis on App Engine.
Flask-HAL (1.0.4)                              - Provides easy integration of
                                                 the HAL specification for
                                                 your REST Flask Applications.
Flask-Hopak (0.1.0)                            - Admin interface for Flask
                                                 that uses Hopak models
flask-lazyapi (0.4.8)                          - A Simple, Restful MongoDB
                                                 Server built on Flask and
                                                 Flask-Classy
Flask-MicroServices (0.34.5)                   - Self contained modules and
                                                 Django style URL routing for
                                                 Flask.
Flask-PagedList (0.2.1)                        - Add pypagedlist support for
                                                 Flask
Flask-Pushjack (1.0.0)                         - Flask extension for push
                                                 notifications on APNS (iOS)
                                                 and GCM (Android).
flask-rethinkview (0.1.2)                      - RESTful Flask View with
                                                 RethinkDB
Flask-ShellPlus (0.0.3)                        - UNKNOWN
Flask-Simple-Serializer (1.1.3)                - Simple Serializers for API
                                                 validations
Flask-Sockets (0.2.1)                          - Elegant WebSockets for your
                                                 Flask apps.
Flask-Soy (0.3)                                - Provides support for Closure
                                                 Templates (Soy) in Flask.
Flask-Twisted (0.1.2)                          - Simple integration of Flask
                                                 and Twisted
Flask-WeRoBot (0.1.2)                          - Writing WeChat Robot by
                                                 WeRoBot in Flask.
Flask-Zero (0.9.6)                             - Qiniu Storage for Flask
Flask-Fulfil (0.1.2)                           - Fulfil.IO for Flask Apps
Flask-HashFS (0.3.0)                           - Flask extension for HashFS, a
                                                 content-addressable file
                                                 management system.
Flask-HMAC (0.1.3)                             - Flask HMAC generator,
                                                 checker, and route decorator
Flask-Kaccel (1.0.1)                           - Add Flask support for Nginx
                                                 X-Accel
Flask-MongoNorm (0.2.0)                        - MongoNorm support for Flask
                                                 applications
Flask-naver (1.2)                              - Oauth2 wraper for Naver login
Flask-Navigation (0.2.0)                       - The navigation of Flask
                                                 application.
Flask-Pilot (0.5.0)                            - Flask-Pilot is a Flask
                                                 extension that adds structure
                                                 and map your views and
                                                 templates together for rapid
                                                 application development
Flask-Redis-Sentinel (1.0.0)                   - Redis-Sentinel integration
                                                 for Flask
Flask-Simon (0.3.0)                            - Simple MongoDB Models for
                                                 Flask
flask-sparkle (0.2.1)                          - Flask app that publishes
                                                 Sparkle update feeds
flask-sqlite_admin (0.3)                       - SQLite DB Management
                                                 Blueprint for Flask
                                                 Applications
Flask-Thunderargs (0.3.1)                      - Implements thunderargs to
                                                 flask framework.
Flask-Views (0.2.1)                            - Class based views for Flask
Flask-XML-RPC (0.1.2)                          - Adds support for creating
                                                 XML-RPC APIs to Flask
Humanize-Flask (0.2.0)                         - Common humanization utilities
                                                 for Flask applications.
sa-flask-restful-resource (0.0.3)              - base class for sqlalchemy and
                                                 flask-restless
Flask-Healthcheck (0.1.2)                      - Healthchecks for flask
                                                 applications made easy
flask-hmacauth (0.3.9)                         - A module to simplify working
                                                 with HMAC auth in Flask apps
Flask-IIIF (0.2.1)                             - Flask-IIIF extension provides
                                                 easy IIIF API standard
                                                 integration.
Flask-ini (0.2.1)                              - Allow Flask to be configured
                                                 with configparser ini files
Flask-Inputs (0.2.0)                           - Flask request data validation
flask-ldap-login (0.3.0)                       - UNKNOWN
Flask-Mitten (0.2.1)                           - Adds security functions to
                                                 Flask applications for
                                                 preventing some of the basic
                                                 threats.
flask-mongo-model (0.0.3a4)                    - A module provides basic ORM
                                                 feature for MongoDB to Flask
                                                 applications.
Flask-MQTT (0.0.3)                             - Flask extension for the MQTT
                                                 protocol
Flask-Obscurity (0.4)                          - Security-by-obscurity. Move
                                                 along, nothing to see here.
flask-oojsui (0.0.3)                           - This library provides python
                                                 Flask utilities and static
                                                 assets for rendering
                                                 Wikimedia UI elements
Flask-Pystmark (0.11.1)                        - A Flask extension for
                                                 Postmark API library Pystmark
Flask-QueryInspect (0.1.2)                     - Flask extension to provide
                                                 metrics on SQL queries per
                                                 request.
Flask-reStructuredText (1.2)                   - Small extension to make using
                                                 rst easy
Flask-Rev (0.1.2)                              - Easily integrate flask with
                                                 revisioned static files
Flask-Routing (0.0.21)                         - Alternative web.py style
                                                 routing for Flask
Flask-Sendwithus (1.0.2)                       - Forwards-compatible Flask
                                                 extension to interact with
                                                 the sendwithus API
Flask-SimpleMDE (0.3.0)                        - Flask-SimpleMDE - a Flask
                                                 extension for SimpleMDE
Flask-Sitemap (0.2.0)                          - Flask extension that helps
                                                 with sitemap generation.
Flask-Split-JS (0.2.1)                         - A JavaScript library for
                                                 Flask-Split.
Flask-Spyne (0.3)                              - A Flask extension, provides
                                                 support for Spyne.
Flask-TokenAuth (0.1.0)                        - Token-based authentication
                                                 for Flask routes
flask-wdb-hook (0.1.2)                         - Hook to replace flask
                                                 werkzeug debugger with wdb.
Flask-YAMLConfig (0.0.3)                       - YAML configurator for Flask
                                                 app.
Flask-GCM (0.2.0)                              - Flask-GCM is a simple wrapper
                                                 for the python-gcm library to
                                                 be used with Flask
                                                 applications.
Flask-HTAuth (0.1.2)                           - Easy to integrate basic HTTP
                                                 authentication for Flask apps
Flask-HTMLmin (1.2)                            - Minimize rendered templates
                                                 html
Flask-JSONPages (0.2)                          - Provides static pages to a
                                                 Flask application based on
                                                 JSON
Flask-Meter (0.1.2)                            - Flask-Meter adds a monitoring
                                                 endpoint for consuming
                                                 application host metrics.
flask-pundit (1.0.2)                           - Simple library to manage
                                                 resource authorization and
                                                 scoping
flask-restful-routing (1.0.3)                  - An easier way to register
                                                 flask-restful routes
Flask-RSTPages (0.3)                           - Adds support for
                                                 reStructuredText to a Flask
                                                 application
Flask-Runner (2.1.1)                           - A set of standard command
                                                 line arguments for Flask
                                                 applications built on top of
                                                 Flask-Script
Flask-ServerInfo (0.1.2)                       - Flask server info view for
                                                 inspecting server app and
                                                 user requests
Flask-Sillywalk (2.1)                          - So you want to implement an
                                                 auto-documenting API?
Flask-SimpleACL (1.2)                          - Simple ACL extension
Flask-ThriftClient (0.2.0)                     - Adds thrift client support to
                                                 your Flask application
Flask-Upwork (1.0-pre2)                        - Upwork API support to Flask
flask-ypaginate (0.1.3)                        - Pagination for Flask
Webstack-Flask-JWT (0.4)                       - JWT token authentication for
                                                 Flask apps
Flask-GAE-Mini-Profiler (0.1.2)                - Flask integration of
                                                 gae_mini_profiler
flask-gae_tests (1.0.2)                        - Flask Extension with base
                                                 test cases to simplify
                                                 testing Flask applications on
                                                 App Engine.
Flask-Geckoboard (0.2.1)                       - Geckoboard custom widgets for
                                                 Flask projects
Flask-GoogleCharts (0.0.3)                     - Google Charts API support for
                                                 Flask
Flask-Humanize (0.3.0)                         - Common humanization utilities
                                                 for Flask applications.
Flask-Hypertable (0.3.0)                       - A Flask extension for
                                                 Hypertable over Thrift.
Flask-MimeRender (0.1.3)                       - RESTful resource variant
                                                 rendering using MIME Media-
                                                 Types, for the Flask Micro
                                                 Web Framework
flask-mongo-sessions (0.2.1)                   - Server-side sessions for
                                                 Flask with MongoDB
Flask-ObjectRocket (0.2.1)                     - User authentication with the
                                                 ObjectRocket API.
flask-orator (0.2.0)                           - Adds Orator support to your
                                                 Flask application
Flask-RedisSession (0.1.2.0)                   - add server-side session,
                                                 stored by Redis
flask-resty-shared-session (0.1.2)             - An adapted flask-session
                                                 module and corresponding
                                                 OpenResty package, so flask
                                                 and Nginx can share session
                                                 information.
Flask-SSO (0.4.0)                              - Flask-SSO extension that
                                                 eases Shibboleth
                                                 authentication.
Flask-Stats (1.0.1)                            - A flask plugin to keep stats
                                                 about your application
Flask-Swag (0.1.2)                             - Build swagger spec with
                                                 Flask.
quokka-flask-mongoengine (0.7.4)               - Fork of Flask support for
                                                 MongoDB and with WTF model
                                                 forms
kore-plugins-flask (0.0.4)                     - 
Flask-Gulp (0.3.0)                             - Task executioner similar to
                                                 gulp for Python
Flask-Hooker (1.0.3)                           - Receive and manage webhooks
                                                 of several services at the
                                                 same time
Flask-Jsonpify (1.5.0)                         - A Flask extension adding a
                                                 decorator for JSONP support
Flask-Mandrill (0.3)                           - Adds Mandrill support to
                                                 Flask applications
Flask-Multipass (0.0.dev4)                     - 
Flask-Psycopg2 (1.3)                           - postgresql adapter for Flask
Flask-RBAC (0.3.0)                             - RBAC support for Flask
flask-reverse-proxy (0.2.0.2)                  - A Flask extension for
                                                 applications in a reverse
                                                 proxy not at the root
Flask-SQLAlchemySession (0.0.4)                - UNKNOWN
Flask-Themes (0.1.3)                           - Provides infrastructure for
                                                 theming Flask applications
Flask-URS (0.1.3)                              - JWT token authentication
                                                 using NASA URS Oauth2 for
                                                 Flask apps
Flask-Venom (1.0.2)                            - Flask extension for the Venom
                                                 RPC framework
Flask-Widgets (0.4)                            - This extension provides basic
                                                 template widget feature for
                                                 Flask
Flask-FlatPages-Knitr (0.3.1)                  - Knitr preprocessing for
                                                 Flask-FlatPages
Flask-GeoIP (0.1.3)                            - Flask-GeoIP -------------
                                                 Simple Flask extension for
                                                 pygeoip.
Flask-JSONRPC (0.3.1)                          - Adds JSONRPC support to
                                                 Flask.
flask-lambda (0.0.4)                           - Python module to make Flask
                                                 compatible with AWS Lambda
                                                 for creating RESTful
                                                 applications
Flask-Mailer (0.4.0)                           - A Flask extension for sending
                                                 emails with pluggable
                                                 backends.
Flask-MAuth (1.1)                              - MAuth Client and Server
                                                 Library for MAuth
flask-media (0.4.6)                            - Flask extestion helper
                                                 uploads files
Flask-MetaRoute (1.3.0)                        - Extra routing capabilities
                                                 for Flask
Flask-NewProject (0.2.1)                       - Create new Flask project.
Flask-Pages (0.1.4)                            - Another? flask extension that
                                                 provides dynamic pages.
Flask-WaffleConf (0.3.1)                       - Store variables in database
                                                 and update them at runtime
Flask-wechatpy (0.1.3)                         - wechatpy for flask extension
py-jsonapi-flask (1.0.3b0)                     - The Flask extension for py-
                                                 jsonapi
Flask-OAuth (0.12)                             - Adds OAuth support to Flask
Flask-QR (0.1.3)                               - Flask extension for
                                                 generating qr codes
Flask-ServiceLayer (0.0.4)                     - Base classes to create a
                                                 Service Layer in Flask.
flask-skel (0.4)                               - Basic Flask paster skeleton
                                                 template
Flask-thumbnails (1.0.0)                       - A simple extension to create
                                                 a thumbs for the Flask
Flask-Gears (0.2)                              - Gears for Flask
Flask-Github (0.1.3)                           - Adds support for authorizing
                                                 users with Github to Flask
Flask-Goat (0.2.1)                             - Flask plugin for security and
                                                 user administration via
                                                 GitHub OAuth & organization
Flask-Logging (0.1.3)                          - UNKNOWN
flask-macros (0.1.5)                           - macros for flask projects
Flask-Mailgun (0.4)                            - Adds Mailgun support to Flask
                                                 applications
Flask-Mako (0.4)                               - Mako templating support for
                                                 Flask applications.
Flask-MoreSQL (0.4)                            - Call PostgreSQL stored
                                                 procedures from Flask
Flask-SendGrid (0.5.2)                         - Adds SendGrid support to
                                                 Flask applications
flask-sqlalchemy-plus (0.1.3)                  - 
Flask-TwitterBootstrap (0.0.4)                 - UNKNOWN
kt-flask-sessions (0.1.3)                      - Kyoto Tycoon backed sessions
                                                 for Flask
Flask-JIRA-Helper (0.2.0)                      - JIRA support for Flask
                                                 without breaking PyCharm
                                                 inspections.
Flask-JSGlue (0.3.1)                           - Flask-JSGlue helps hook up
                                                 your Flask application nicely
                                                 with the front end.
Flask-JSONPlus (0.0.4)                         - Flask extension for non-basic
                                                 types' serialization to JSON
                                                 via jsonplus lib.
flask-msearch (0.1.3)                          - full text search with whoosh
                                                 for flask
Flask-Nicely (0.2.0)                           - Pretty Flask JSON responses
                                                 for API building.
flask-nidhogg (1.1.1)                          - OpenSource Yggdrasil protocol
                                                 implementation
flask-oauthprovider (0.1.3)                    - A full featured and secure
                                                 OAuth provider base
Flask-OpenERP (0.3.1)                          - OpenERP Connector for Flask
Flask-ReportableError (0.4.3)                  - handle errors that can be
                                                 reported to the web client
Flask-RESTify (0.1.3)                          - Flask REST framework
Flask-Run (0.1.3)                              - Flask-based web application
                                                 runner
Flask-Sessions (0.1.5)                         - Adds server-side session
                                                 support to your Flask
                                                 application
flask-shell (0.1.3)                            - Flask extension to improve
                                                 shell command for the Flask
                                                 CLI.
Flask-Shield (0.2.2)                           - Flask-Shield is an extension
                                                 of Flask for permission
                                                 management based on RBAC.
Flask-ShortUrl (0.2.0)                         - Short URL generaotr for Flask
Flask-Silk (0.2)                               - Adds silk icons to your Flask
                                                 application or blueprint, or
                                                 extension.
Flask-Stormpath-test (0.4.7)                   - Simple and secure user
                                                 authentication for Flask via
                                                 Stormpath.
Flask-Velox (2014.04.25)                       - Velox is a set of classes &
                                                 mixins to help rapidly build
                                                 Flask applications.
Flask-Weixin-Login (0.2.1)                     - Weixin Login from Flask
pylint-flask (0.5)                             - pylint-flask is a Pylint
                                                 plugin to aid Pylint in
                                                 recognizing and understanding
                                                 errors caused when using
                                                 Flask
quokka-flask-htmlbuilder (0.13)                - Fork of Flexible Python-only
                                                 HTML generation for Flask
Flask-Jasmine (1.4)                            - Execution of Jasmine
                                                 JavaScript tests within Flask
Flask-JqueryUiBootstrap (0.5.0.4)              - Flask jQuery UI Bootstrap
                                                 minimalistic fork of Flask-
                                                 Bootsrap extension
Flask-Pure (0.5)                               - Flask-Pure - a Flask
                                                 extension for Pure.css
Flask-StatsdTagged (0.9)                       - Flask extension for sending
                                                 statsd data with tags, for
                                                 use with telegraf statsd
                                                 plugin
Flask-Test (0.1.5)                             - Various unit testing helpers
                                                 for Flask applications.
Flask-Triangle (0.5.4)                         - Integration of AngularJS and
                                                 Flask.
Flask-Twip (0.0.5)                             - twitter API proxy extension
                                                 for Flask microframework
Flask-Versioned (0.9.4-20101221)               - Add version info to file
                                                 paths.
flask-hype (0.1.4)                             - Flask extension for hype
Flask-IndieAuth (0.0.3.2)                      - Allow requests to be
                                                 authenticated with
                                                 https://indieauth.com/
Flask-JSON (0.3.0)                             - Better JSON support for Flask
Flask-Menu (0.5.0)                             - Flask-Menu is a Flask
                                                 extension that adds support
                                                 for generating menus.
Flask-Nytro (1.2)                              - Nytro is an extension to help
                                                 the developers providing a
                                                 set of useful tools giving
                                                 even more facility to
                                                 development apps with Flask.
Flask-Pika (0.3.8)                             - Pika amqp flask extension
Flask-RestPoints (0.0.8)                       - Adds some common health check
                                                 endpoints (ping, time,
                                                 status)
flask-talisman (0.3.2)                         - HTTP security headers for
                                                 Flask.
Flask-WhooshAlchemy-Redux (0.7.1)              - Whoosh extension to
                                                 Flask/SQLAlchemy
flask-htpasswd (0.3.1)                         - Basic authentication support
                                                 via htpasswd files in flask
                                                 applications
Flask-Idempotent (0.1.0)                       - Idempotent requests for Flask
                                                 applications
Flask-JWT (0.3.2)                              - JWT token authentication for
                                                 Flask apps
Flask-MongoKit (0.6)                           - A Flask extension simplifies
                                                 to use MongoKit
Flask-MongoRest (0.2.2)                        - Flask restful API framework
                                                 for MongoDB/MongoEngine
flask-nav (0.6)                                - Easily create navigation for
                                                 Flask applications.
Flask-Redis-Helper (1.0.0)                     - Redis support for Flask
                                                 without breaking PyCharm
                                                 inspections.
Flask-Redtask (0.3.1)                          - Redqueue integration for
                                                 flask
Flask-SocialAPI (1.0.5)                        - Simple api for controlling
                                                 and login to provider
Flask-Statics-Helper (1.0.0)                   - Provides Bootstrap3 and other
                                                 static resources in a modular
                                                 fashion.
Flask-WeasyPrint (0.5)                         - Make PDF in your Flask app
                                                 with WeasyPrint.
flask-fs (0.3.0)                               - Simple and easy file storages
                                                 for Flask
flask-geokit (0.1.7)                           - Geocoding toolkit
Flask-JWE (0.0.5)                              - Add Flask Support for JWE
                                                 Requests
flask-pytest (0.0.5)                           - Runs pytest in a background
                                                 process when DEBUG is True.
Flask-Rauth (0.3.2)                            - Adds OAuth 1.0/a, 2.0, and
                                                 Ofly consumer support for
                                                 Flask.
Flask-RedisConfig (0.3.0)                      - Redis-backed config for Flask
                                                 applications
flask-request-validator (1.1.0)                - Flask request data validation
Flask-Sessionstore (0.4.3.1)                   - Adds session support to your
                                                 Flask application
Flask-Themes2 (0.1.4)                          - Provides infrastructure for
                                                 theming Flask applications
                                                 (and supports Flask>=0.6!)
Flask-Tracy (0.1.3)                            - Logs tracing information on a
                                                 per-request basis
Flask-Turbolinks (0.2.0)                       - Turbolinks for Flask.
li-flask-validation (1.0.4)                    - Flask Validation.
Flask-GoogleAuth (0.4.2)                       - Super simple OpenID and
                                                 Google Federated Auth for
                                                 Flask apps.
Flask-kinesis (0.1.8)                          - Flask plugin for aws kinesis
                                                 stream
Flask-MakeStatic (0.3.0)                       - Make for your flask app
                                                 assets
Flask-OAuth2-Provider (0.2.1)                  - A simple flask oauth2
                                                 provider
Flask-PyMemcache (0.0.5)                       - pymemcache integration for
                                                 Flask
flask-rest4 (0.1.8)                            - Elegant RESTful API for your
                                                 Flask apps.
Flask-Scss (0.5)                               - Adds support for scss files
                                                 to Flask applications
Flask-SERVICE (0.1.4)                          - A service api client for
                                                 Flask applications.
flask-swagger-ui (3.0.12a0)                    - Swagger UI blueprint for
                                                 Flask
Flask-Uploads (0.2.1)                          - Flexible and efficient upload
                                                 handling for Flask
Flask-WhooshAlchemyPlus (0.7.5)                - Whoosh extension to
                                                 Flask/SQLAlchemy
Flask-Redislite (0.1.0rc0)                     - Using Flask with Redislite
flask-secure-headers (0.6)                     - Secure Header Wrapper for
                                                 Flask Applications
Flask-Slack (0.1.5)                            - Slack extension for Flask.
flask-keyauth (0.1.5)                          - A module to simplify working
                                                 with KEY auth in Flask apps
Flask-MySQL (1.4.0)                            - Flask simple mysql client
Flask-reCaptcha (0.4.2)                        - The new Google ReCaptcha
                                                 implementation for Flask
                                                 without Flask-WTF
Flask-request-params (0.3.0)                   - Flask-request-params provides
                                                 Rails-like interface to HTTP
                                                 Request Parameters for Flask.
Flask-RQ2 (17.0)                               - A Flask extension for RQ.
Flask-Scrypt (0.1.3.6)                         - Flask-Scrypt provides
                                                 convenient wrappers forscrypt
                                                 password hashing and random
                                                 salt generation.
Flask-Sentinel (0.0.6)                         - OAuth2 Provider for Flask
                                                 applications.
flask-shell-ipython (0.2.2)                    - Replace default `flask shell`
                                                 command by similar command
                                                 running IPython.
Flask-Split (0.3.0)                            - A/B testing for your Flask
                                                 application
Flask-StatHat (0.1.2)                          - StatHat extension for Flask
Flask-Weixin (0.5.0)                           - Weixin for Flask.
flask-idempotent2 (0.0.6)                      - Redis based idempotent
                                                 support for sqlalchemy based
                                                 flaskapplications.
Flask-MAB (1.1.1)                              - Multi-armed bandits for flask
Flask-OFAUTH (0.1.7)                           - passport api client for Flask
                                                 applications.
Flask-Sleepy (0.3.0)                           - REST is hard. Let's go
                                                 shopping
Flask-SSLify (0.1.5)                           - Force SSL on your Flask app.
Flask-PRISM (0.3.2)                            - Simple APIs with Flask PRISM
Flask-Pushrod (0.3)                            - Views for your API
Flask-Security-Fork (2.0.1)                    - Simple security for Flask
                                                 apps.
Flask-Staticify (0.2.2)                        - Looks for static files in the
                                                 additional locations as a
                                                 fallback
flask-thumbnails-s3 (0.1.5)                    - An extension to create image
                                                 thumbnails on Amazon S3 (or
                                                 on local storage) with the
                                                 Flask framework, based on
                                                 flask-thumbnails.
flask-xadmin (0.1.2)                           - eXtended Flask-Admin
Flask-GraphQL (1.4.1)                          - Adds GraphQL support to your
                                                 Flask application
Flask-LogConfig (0.4.2)                        - Flask extension for
                                                 configuring Python logging
                                                 module
Flask-Misaka (0.4.1)                           - A pleasant interface between
                                                 the Flask web framework and
                                                 the Misaka Markdown parser.
Flask-PyBankID (0.3.1)                         - Flask Extension for PyBankID
                                                 client
Flask-qiniu (1.1.4)                            - Flask Qiniu extension
Flask-S3-gzip (0.1.8)                          - Seamlessly serve the static
                                                 files of your Flask app from
                                                 Amazon S3 (forked from
                                                 original flask-s3)
Flask-Track-Usage (1.1.0)                      - Basic metrics tracking for
                                                 the Flask framework.
Flask-Upstatic (0.0.6)                         - Opinionated library for
                                                 working with CDNs in Flask.
Flask-Via (2015.1.1)                           - Provides a clean, simple URL
                                                 routing framework for growing
                                                 Flask Applications.
flask-monitor (0.2.2)                          - Flask Monitor module
flask-openldap (0.0.8)                         - Flask extension to query an
                                                 openLDAP server
flask-zookeeper (0.0.8)                        - Flask Zookeeper client
Flask-Genshi (0.5.1)                           - An extension to Flask for
                                                 easy Genshi templating.
Flask-Snooze (0.1.6)                           - Backend agnostic REST API
                                                 provider for Flask
flask-uiface (0.7)                             - Random user avatars for the
                                                 rest of us!
Flask-Webpack (0.1.0)                          - Flask extension for managing
                                                 assets with Webpack.
Flask-IdentityClient (0.5.2)                   - PassaporteWeb connection for
                                                 Flask applications
Flask-WePay (0.0.7)                            - WePay API support
flask-init (0.2.3)                             - Generate Flask project
Flask-FlatPages (0.6)                          - Provides flat static pages to
                                                 a Flask application
Flask-ImageAlchemy (0.0.7)                     - SQLAlchemy Standarized Image
                                                 Field for Flask
Flask-IPInfo (0.0.10)                          - Get IP, ISP, Location, OS
                                                 from flask request
Flask-LazyViews (0.6)                          - Registers URL routes for
                                                 Flask application or
                                                 blueprint in lazy way.
Flask-LDAP (0.1.6)                             - Flask extension for LDAP auth
                                                 and profile user
Flask-LinkTester (0.3.0)                       - Link tester for Flask
                                                 applications
flask-logmanager (0.2.6)                       - Flask LogManager module
Flask-Marcos (0.0.7dev)                        - ERP apps Flask container
flask-statsd-tags (0.1.6)                      - Flask extention for sending
                                                 statsd data
Flask-Markdown (0.3)                           - Small extension to make using
                                                 markdown easy
Flask-Session (0.3.1)                          - Adds server-side session
                                                 support to your Flask
                                                 application
Flask-Styleguide (0.4.0)                       - A living Styleguide for your
                                                 Flask application.
Flask-Locale (1.0.2)                           - Adds i18n/l10n support to
                                                 Flask applications easily.
                                                 Uses CSV files(or database)
                                                 to load translations.
oleg-flask-sessions (0.2.5)                    - Oleg DB backed sessions for
                                                 Flask
Flask-Foundation (2.1)                         - An extension that includes
                                                 the Foundation css framework
                                                 in your project, without any
                                                 boilerplate code.
Flask-SuperAdmin (1.7.1)                       - The best admin interface
                                                 framework for Python. With
                                                 scaffolding for MongoEngine,
                                                 Django and SQLAlchemy.
Flask-WhooshAlchemy (0.8)                      - Whoosh extension to
                                                 Flask/SQLAlchemy
Flask-Mustache (0.4.1)                         - Mustache for Flask
Flask-OpenTracing (0.1.7)                      - OpenTracing support for Flask
                                                 applications
Flask-Vue (0.3.5)                              - Vue.js 1.0+ integration for
                                                 Flask (Python 3 version)
Flask-Redis (0.3.0)                            - Redis Extension for Flask
                                                 Applications
Flask-Stormpath-Plus (0.2.4)                   - Simple and more secure user
                                                 authentication for Flask via
                                                 Stormpath.
flask-tat (0.0.9)                              - Flask TAT client
Flask-Principal (0.4.0)                        - Identity management for flask
Flask-SimpleLDAP (1.1.1)                       - LDAP authentication extension
                                                 for Flask
Flask-WebTest (0.0.9)                          - Utilities for testing Flask
                                                 applications with WebTest.
Flask-OAuth2-Login (0.0.9)                     - Simple OAuth2 login
Flask-INIConfig (0.1.0)                        - A flask extension to load ini
                                                 files via config
Flask-RESTeasy (0.0.8)                         - Create easy REST APIs with
                                                 Flask
Flask-Store (0.0.4.4)                          - Provides Django-Storages like
                                                 file storage backends for
                                                 Flask Applications.
Flask-Gravatar (0.4.2)                         - Small extension for Flask to
                                                 make usage of Gravatar
                                                 service easy.
Flask-Multi-Redis (0.1.5)                      - MultiThreaded MultiServers
                                                 Redis Extension for Flask
                                                 Applications
Flask-PageDown (0.2.2)                         - Implementation of
                                                 StackOverflow's "PageDown"
                                                 markdown editor for Flask-
                                                 WTF.
Flask-Twitter-OEmbedder (0.1.8)                - Embedded tweets in Flask
                                                 Jinja2 Templates with only
                                                 the Tweet_ID
Flask-Json-Syslog (0.1.28)                     - Output syslog of the json
                                                 format.
Flask-Social (1.6.2)                           - Simple OAuth provider
                                                 integration for Flask-
                                                 Security
Flask-Z3950 (0.3.2)                            - Z39.50 integration for Flask
                                                 applications.
Flask-MxitGA (0.10)                            - Google analytics for flask
                                                 and mxit.
Flask-KVSession (0.6.2)                        - Transparent server-side
                                                 session support for flask
Flask-Lastuser (0.3.12)                        - Flask extension for Lastuser
Flask-Moment (0.5.1)                           - Formatting of dates and times
                                                 in Flask templates using
                                                 moment.js.
Flask-Negotiation (0.1.9)                      - Better content negotiation
                                                 for flask
flask-oidc (1.1.1)                             - OpenID Connect extension for
                                                 Flask
Flask-Permissions (0.2.3)                      - Simple user permissions for
                                                 Flask
Flask-Weixin-Pay (0.3.4)                       - Weixin Pay from Flask
flask-ptrans (1.4)                             - Flask extension for
                                                 localisation of templates
                                                 from JSON files
Flask-NSFW (6)                                 - Flask-NSFW blocks all the
                                                 requests that contains images
                                                 with nudity.
Flask-Funnel (0.1.10)                          - Asset management for Flask.
Flask-Plugins (1.6.1)                          - Create plugins for your Flask
                                                 application
Flask-pyoidc (1.1.0)                           - Flask extension for OpenID
                                                 Connect authentication.
flask-heroku (0.1.9)                           - Heroku environment variable
                                                 configurations for Flask
Flask-Loopback (1.4.5)                         - Library for faking HTTP
                                                 requests using flask
                                                 applications without actual
                                                 network operations
flask-marshmallow (0.8.0)                      - Flask + marshmallow for
                                                 beautiful APIs
Flask-Pusher (1.2.1)                           - Flask extension for Pusher
Flask-RAML (0.2.2)                             - Flask-RAML (REST API Markup
                                                 Language) API server with
                                                 parameter conversion,
                                                 response encoding, and
                                                 examples
Flask-Neo4j (0.5.1)                            - Flask extension providing
                                                 integration with Neo4j.
Flask-WebCache (0.9.1)                         - A Flask extension that adds
                                                 HTTP based caching to Flask
                                                 apps
Flask-Images (2.1.2)                           - Dynamic image resizing for
                                                 Flask.
flask-ldap3-login (0.9.12)                     - LDAP Support for Flask in
                                                 Python3/2
Flask-Tus (0.7.1)                              - TUS protocol implementation
Flask-GoogleMaps (0.2.4)                       - Small extension for Flask to
                                                 make using Google Maps easy
Flask-MailGun3 (0.1.5)                         - Flask extension to use the
                                                 Mailgun email parsing service
flask-hookserver (1.1.0)                       - Server for GitHub webhooks
                                                 using Flask
Flask-OpenID (1.2.5)                           - OpenID support for Flask
Flask-QRcode (0.10.0)                          - An elegant flask extension to
                                                 render QR codes
flask-spawn (0.1.11)                           - Generate new flask projects
                                                 quickly and easily, in a
                                                 variety of customisable
                                                 structures.
Flask-Micropub (0.2.6)                         - Adds support for Micropub
                                                 clients.
flask-ripozo (1.0.4)                           - An extension for ripozo and
                                                 that brings
                                                 HATEOAS/REST/Hypermedia apis
                                                 to flask
flask-resty-tenants (0.5.3)                    - Flask Resty Authorization
                                                 module for multitenancy
Flask-JinjaHelpers (0.3.7)                     - Various helpers for Flask
                                                 based Jinja2 templates.
Flask-PyMongo (0.5.1)                          - PyMongo support for Flask
                                                 applications
Flask-Sijax (0.4.1)                            - An extension for the Flask
                                                 microframework that adds
                                                 Sijax support.
Flask-WXPay (0.1.12)                           - Flask Extension for WeChat
                                                 Pay.
Flask-Navigate (0.2.2)                         - Another flask extension that
                                                 provides Navigation menus.
twopi-flask-utils (1.1.5)                      - A set of utilities to make
                                                 working with flask web
                                                 applications easier.
Flask-Holster (0.3.4)                          - Rigid MVC content negotiation
                                                 for Flask
Flask-Testing (0.6.2)                          - Unit testing for Flask
Frozen-Flask (0.14)                            - Freezes a Flask application
                                                 into a set of static files.
Flask-Material (0.1.1)                         - An extension that includes
                                                 Materialize CSS
                                                 (http://materializecss.com/)
                                                 in your project, without any
                                                 boilerplate code.
flask-mwoauth (0.3.61)                         - Flask blueprint to connect to
                                                 a MediaWiki OAuth server
Flask-MustacheJS (0.6.0)                       - Mustache integration in
                                                 Flask, with Jinja and client-
                                                 side libraries.
flask-swagger (0.2.13)                         - Extract swagger specs from
                                                 your flask project
Flask-Imagine (0.5)                            - Extension which provides easy
                                                 image manipulation support in
                                                 Flask applications.
Flask-SQLAlchemy (2.2)                         - Adds SQLAlchemy support to
                                                 your Flask application
Flask-PW (1.0.3)                               - Peewee ORM integration for
                                                 Flask framework
flask-musers (0.5.4)                           - Flask app for store user in
                                                 MongoDB and simple views for
                                                 login, logout and
                                                 registration.
Flask-Pypi-Proxy (0.5.1)                       - A Pypi proxy
Flask-JSONAPIView (0.1.0)                      - DEPRECATED: This library has
                                                 been renamed to Flask-RESTy
Flask-Validator (1.2.3)                        - Data validator for Flask and
                                                 SQL-Alchemy, working at Model
                                                 component with events
flask-whooshee (0.4.1)                         - Flask-SQLAlchemy - Whoosh
                                                 Integration
Flask-LwAdmin (0.6.3)                          - Flask-LwAdmin is minimalistic
                                                 administrative interface
                                                 building extension for the
                                                 Flask framework
Flask-Injector (0.9.0)                         - Adds Injector, a Dependency
                                                 Injection framework, support
                                                 to Flask.
flask-restful-swagger (0.19)                   - Extrarct swagger specs from
                                                 your flast-restful project
Flask-Login (0.4.0)                            - User session management for
                                                 Flask
Flask-MongoAlchemy (0.7.2)                     - Add Flask support for MongoDB
                                                 using MongoAlchemy.
Flask-GoogleLogin (0.3.1)                      - Extends Flask-Login to use
                                                 Google's OAuth2 authorization
flask-mongoengine (0.9.3)                      - Flask-MongoEngine is a Flask
                                                 extension that provides
                                                 integration with MongoEngine
                                                 and WTF model forms.
Flask-paginate (0.4.6)                         - Simple paginate support for
                                                 flask
Flask-Perm (0.2.8)                             - Flask Permission Management
                                                 Extension
flask-zeus (0.2.1)                             - UNKNOWN
Flask-MarcoPolo (0.6.3)                        - Flask-MarcoPolo  Flask-
                                                 MarcoPolo is a Flask
                                                 extension that adds structure
                                                 to both your views and
                                                 templates, by mapping them to
                                                 each other to provide a rapid
                                                 application development
                                                 framework. The extension also
                                                 comes with Flask-Classy,
                                                 Flask-Assets, Flask-Mail,
                                                 JQuery 2.x, Bootstrap 3.x,
                                                 Font-Awesome, Bootswatch
                                                 templates. The extension also
                                                 provides pre-made templates
                                                 for error pages and macros.
                                                 https://github.com/mardix
                                                 /flask-marcopolo
pytest-flask (0.10.0)                          - A set of py.test fixtures to
                                                 test Flask applications.
Flask-OAuthlib (0.9.3)                         - OAuthlib for Flask
Flask-Maple (0.4.8)                            - captcha ,bootstrap,easy login
                                                 and more flask tips.
Flask-LoginManager (1.1.6)                     - Flask-Loginmanager supports
                                                 multiple roles and
                                                 permissions for Flask,
                                                 inspired by Flask-Login
Flask-REST-JSONAPI (0.12.5)                    - Flask extension to create
                                                 REST web api according to
                                                 JSONAPI 1.0 specification
                                                 with Flask, Marshmallow
                                                 and data provider of your
                                                 choice (SQLAlchemy, MongoDB,
                                                 ...)
Flask-Script (2.0.5)                           - Scripting support for Flask
Flask-HTTPAuth (3.2.3)                         - Basic and Digest HTTP
                                                 authentication for Flask
                                                 routes
Flask-Migrate (2.0.4)                          - SQLAlchemy database
                                                 migrations for Flask
                                                 applications using Alembic
Flask-Slither (1.1.7)                          - A small library between
                                                 MongoDB and JSON API
                                                 endpoints
Flask (0.12.2)                                 - A microframework based on
                                                 Werkzeug, Jinja2 and good
                                                 intentions
GitHub-Flask (3.1.7)                           - GitHub extension for Flask
                                                 microframework
Flask-SeaSurf (0.2.2)                          - An updated CSRF extension for
                                                 Flask.
Flask-Restless (1.0.0b1)                       - A Flask extension for easy
                                                 ReSTful API generation
Flask-LDAPConn (0.6.13)                        - Pure python, LDAP connection
                                                 and ORM for Flask
                                                 Applications
Flask-Resize (2.0.3)                           - Flask extension for resizing
                                                 images in code and templates
Flask-Security (1.7.5)                         - Simple security for Flask
                                                 apps
Flask-WTF-FlexWidgets (0.1.25)                 - A flask extension that
                                                 provides customizable WTF
                                                 widgets and macros.
flask-peewee (0.6.7)                           - Peewee integration for flask
Flask-Mail (0.9.1)                             - Flask extension for sending
                                                 email
Flask-RESTful (0.3.6)                          - Simple framework for creating
                                                 REST APIs
Flask-Table (0.4.1)                            - HTML tables for use with the
                                                 Flask micro-framework
flask-restplus (0.10.1)                        - Fully featured framework for
                                                 fast, easy and documented API
                                                 development with Flask
Flask-S3 (0.3.3)                               - Seamlessly serve the static
                                                 files of your Flask app from
                                                 Amazon S3
flask-transmute (1.3.0)                        - a flask plugin to generate
                                                 routes from objects.
Flask-uWSGI-WebSocket (0.6.0)                  - High-performance WebSockets
                                                 for your Flask apps powered
                                                 by uWSGI.
Flask-Stormpath (0.4.8)                        - Simple and secure user
                                                 authentication for Flask via
                                                 Stormpath.
flask-magic (0.0.53)                           - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
Flask-Wizard (0.4.13)                          - Rapid and easy bot
                                                 development in Python
flask-io (1.12.0)                              - Flask-IO is a library for
                                                 parsing Flask request
                                                 arguments into parameters and
                                                 for serialization of complex
                                                 objects into Flask response.
Flask-RESTy (0.11.4)                           - Building blocks for REST APIs
                                                 for Flask
Flask-User (0.6.11)                            - Customizable User Account
                                                 Management for Flask:
                                                 Register, Confirm email,
                                                 Login, Change username,
                                                 Change password, Forgot
                                                 password and more.
Flask-WTF (0.14.2)                             - Simple integration of Flask
                                                 and WTForms.
Flask-Limiter (0.9.4)                          - Rate limiting for flask
                                                 applications
Flask-SocketIO (2.8.6)                         - Socket.IO integration for
                                                 Flask applications
flask-restaction (0.25.3)                      - A web framwork born to create
                                                 RESTful API
Flask-Potion (0.14.1)                          - Powerful REST API framework
                                                 for Flask and SQLAlchemy
Flask-Restler (1.7.5)                          - Build REST API for Flask
                                                 using Marshmallow.
flask-xxl (0.9.20)                             - quick way to design large
                                                 flask projects
microcosm-flask (0.72.0)                       - Opinionated persistence with
                                                 FlaskQL
flask2postman (1.4.2)                          - Generate a Postman collection
                                                 from your Flask application
flask_accept (0.0.3)                           - Custom Accept header routing
                                                 support for Flask
flask_aide (0.0.1)                             - demo
flask_alcohol (0.1)                            - Automatically generate API
                                                 routes from Flask-SQLAlchemy
                                                 models
flask_ample (0.0.1)                            - basic setup of ample for
                                                 flask
flask_api_builder (0.2.0)                      - A shortcut for stubbing out
                                                 your RESTful Flask APIs
flask_app_generator (0.1.0)                    - Flask Project Generator
flask_autorest (0.1.5)                         - auto create restful apis for
                                                 database, with the help of
                                                 dataset.
flask_backstage (0.2.1)                        - A backstage framework with
                                                 very few code.
flask_base64_msm_session (1.0.2)               - Use base64 encoder on
                                                 memcached server. And it will
                                                 use memcached on session
flask_basic_roles (0.1.post4)                  - A plugin for adding very
                                                 simple users + roles to a
                                                 flask app
flask_bootstrap_forms (0.4)                    - A set of tools that makes it
                                                 easy to draw HTML forms in
                                                 Flask in the style of
                                                 Boostrap.
flask_cache_external_assets (0.2.0)            - Flask extension for caching
                                                 external assets
flask_checkargs (0.1.2)                        - A module to simplify checking
                                                 arguments in Flask apps
flask_chip (0.1.2)                             - A token generator for Flask
                                                 apps.
flask_clapi (0.2.0)                            - CLAPI wrapper
flask_cm (0.8.1)                               - Cloud Mesh: managing multiple
                                                 virtual machines in Clouds
flask_datatables (0.6.17)                      - Integrates SQLAlchemy with
                                                 DataTables (framework Flask)
flask_doc (0.2.5)                              - Write API document when you
                                                 coding, Test your API when
                                                 you press last word
                                                 immediately
flask_error (0.1)                              - A simple and extensible way
                                                 of displaying error messages.
flask_ext_migrate (1.0.0)                      - A sourcecode manipulation
                                                 tool for converting imports.
flask_extras (4.0.3)                           - Assorted useful flask views,
                                                 blueprints, Jinja2 template
                                                 filters, and templates/macros
flask_flaskwork (0.1.10)                       - A Flask plugin to talk with
                                                 the Flaskwork Chrome
                                                 extension.
flask_frink (0.0.1)                            - Add Flask-Security datastore
                                                 functionality to Frink.
flask_github_proxy (0.0.2)                     - Plugin to build services to
                                                 push data from a website to
                                                 github with PullRequests
                                                 confirmation
flask_helpers (0.1)                            - Useful stuff for Flask
                                                 application
flask_introspect (0.0.1)                       - basic setup of ample for
                                                 flask
flask_json_multidict (1.0.0)                   - Convert Flask's
                                                 `request.get_json` dict into
                                                 a MultiDict like
                                                 `request.form`
flask_json_resource (0.2.18)                   - UNKNOWN
flask_jsondash (5.2.3)                         - Easily configurable, chart
                                                 dashboards from any arbitrary
                                                 API endpoint. JSON config
                                                 only. Ready to go.
flask_jsontools (0.1.1-0)                      - JSON API tools for Flask
Flask_LDAP_View (0.3)                          - A library to restrict your
                                                 flask pages by LDAP groups
flask_locust (0.0.2-alpha)                     - SQL-Migrations for your
                                                 Application
flask_markdown2 (0.0.3)                        - A flask extension that adds a
                                                 {% markdown %} tag to
                                                 templates.
flask_nameko (1.3.0)                           - A wrapper for using nameko
                                                 services with Flask
flask_neglog (0.0.2)                           - demo
flask_nemo (1.0.0)                             - Flask Extension to browse CTS
                                                 Repository
flask_open_directory (0.1.1)                   - MacOS OpenDirectory
                                                 Authorization Middleware for
                                                 Flask
flask_params (1.0.1)                           - Processes the Request params
                                                 for Flask served as a Python
                                                 library
flask_profiler (1.4)                           - API endpoint profiler for
                                                 Flask framework
flask_raven (0.0.4)                            - A flask extension for the
                                                 University of Cambridge's
                                                 authentication system
flask_rdf (0.2.0)                              - Flask decorator to output RDF
                                                 using content negotiation
flask_react (0.0.5)                            - Auto setup tool for flask and
                                                 react project
flask_replicated (1.2)                         - Flask SqlAlchemy router for
                                                 stateful master-slave
                                                 replication
flask_reqparse (2.2.1)                         - flask_reqparse is a simple
                                                 wrapper around flask request
                                                 module that helps to parse
                                                 args efficently.
flask_rest_toolkit (0.0.1)                     - A set of tools to create
                                                 simple Flask REST web
                                                 services and APIs
flask_restframework (0.0.21)                   - Web APIs for Flask, made
                                                 easy, inspired from Django
                                                 DRF.
flask_restful_jsonschema (0.1.1)               - Provides a wrapper which
                                                 provides valid json to
                                                 Resource methods.
flask_restful_url_generator (0.0.4)            - flask-restful URLs list
flask_resty_swagger (0.1.3)                    - Generate swagger
                                                 documentation from flask-
                                                 resty service
flask_sandboy (0.0.3)                          - Automated REST APIs for
                                                 SQLAlchemy models
flask_script_extras (0.1.4)                    - extras commands to Flask-
                                                 Script.
flask_servatus (0.1.3)                         - A port of djangos storages
                                                 framework for use with flask
                                                 applications
flask_servicenow (0.1.1)                       - ServiceNow REST API Flask
                                                 extension
flask_siilo (0.1.2)                            - A simple storage for Flask
                                                 based on siilo.
flask_simple_sitemap (0.0.3)                   - 
flask_simplerest (1.0.3)                       - A Flask extension for easy
                                                 ReSTful API generation
flask_singleview (0.2.1)                       - A flask micro extension for
                                                 building single-view web
                                                 apps.
flask_slackbot (0.2.1)                         - Deal with slack outgoing
                                                 webhook
flask_sqla_debug (0.2)                         - Helpers for debugging flask
                                                 and sqlalchemy performance
flask_tlsauth (0.1.3)                          - Flask extension implementing
                                                 TLS Authentication - simple
                                                 client certificate CA
                                                 inclusive
flask_trace (0.0.4)                            - Log trace decorator function
                                                 for Flask
flask_tryton (0.6)                             - Adds Tryton support to Flask
                                                 application
flask_util_js (0.2.25)                         - flask's util in javascript.
                                                 such as url_for etc.
flask_web_args (0.1.2)                         - A library to help easily
                                                 parse/validate web arguments
                                                 with Flask
flask_yamlpage (0.0.6)                         - Flatpages in yaml syntax
flaskcbv (1.4.11)                              - FlaskCBV is Alternative
                                                 Framework for working with
                                                 flask with the class Based
                                                 Views approach (CBV)
flaskchatterbot (0.1.0)                        - An open-source web based
                                                 Python chat bot in Flask.
flaskckeditor (1.6)                            - flask后台快速集成ckeditor编辑器
FlaskCms (0.0.4)                               - UNKNOWN
FlaskDeferredHandler (0.1)                     - A Flask handler for the
                                                 Google Appengine's deferred
                                                 library
flasker (0.1.45)                               - Flask, SQLAlchemy, and Celery
                                                 integration
FlaskEx (0.0.66)                               - UNKNOWN
flaskhmac (1.2.1)                              - Provides easy integration of
                                                 the HMAC signatures for your
                                                 REST Flask Applications.
flaskinit (0.0.1)                              - Bootstraps Flask projects
flaskit (0.1.0)                                - Utilies for Flask
                                                 application.
flaskJSONRPCServer (0.9.3)                     - A Python JSON-RPC over HTTP
                                                 with flask and gevent
flaskle (0.4)                                  - bottle-like utility
                                                 decorators for flask
FlaskPusher (1.0.1)                            - Adds Pusher support for your
                                                 Flask application.
flaskrestframework (0.1.4)                     - Web APIs for Flask, made
                                                 easy.
FlaskSearch (0.1)                              - Powerful search functionality
                                                 for Flask apps via
                                                 ElasticSearch
flaskserver (0.1.1)                            - simple web server with Flask
flasksr (0.6)                                  - Start streaming HTTP
                                                 Responses based on your page
                                                 layout for Flask and improve
                                                 Time for First Paint.
flaskstrap (0.3.6)                             - Easily create a flask, nginx,
                                                 uwsgi and bootstrap project
                                                 ready for deployment
flaskup (0.3.2)                                - A simple Flask application to
                                                 share files.
FlaskWarts (0.1a8)                             - Assortment of various
                                                 utilities for Flask
                                                 applications
flaskwork (0.1.1)                              - UNKNOWN
Flasky (0.1.0)                                 - Lazy man's Flask Application
FlaskyTornado (0.0.35)                         - A microframework based on
                                                 Tornado and Flask and good
                                                 intentions
flatly (0.3)                                   - Pyramid scaffold that is
                                                 flat.  Kind of like Flask.
fleaker (0.4.0)                                - Tools and extensions to make
                                                 Flask development easier.
flekky (0.4.1)                                 - Static website generator
                                                 inspired by jekyll based on
                                                 flask.
flexrest (0.1.9)                               - Flexible Flask Rest Api
FliKISS (0.1)                                  - Wiki engine based on Markdown
                                                 flat files powered by Flask
flump (0.10.1)                                 - REST API builder using Flask
                                                 routing and Marshmallow
                                                 schemas.
flymph (0.1.3)                                 - Flask as Lymph Web API
gitlab-freak (1.0.0a1)                         - A Flask server that allows
                                                 you to interact with Trello
                                                 from your own Gitlab, and
                                                 keep track of your projects
                                                 dependencies.
Fregger (0.10.6)                               - Automatically generate
                                                 Swagger docs for Flask-
                                                 Restful.
frl (0.0.4)                                    - flask/requests logging
froth (0.0.1)                                  - Data Visualization Template
                                                 Engine for Django/Flask=
frs (0.0.0.dev7)                               - Flask-RESTful
                                                 Swagger(-driven) Validation
fss (0.2.1)                                    - Compile Flask/Jinja2 site
                                                 into static html content
funkyserver (0.1)                              - FunkyServer is simple package
                                                 to create Flask servers in
                                                 background processes.
Funnel (0.1)                                   - Flask extension for Beaker
gdbgui (0.7.7.0)                               - browser-based gdb frontend
                                                 using Flask and JavaScript to
                                                 visually debug C, C++, Go, or
                                                 Rust
getolaf (1.0.2)                                - A static site generator based
                                                 on flask and markdown
git-golem (0.1)                                - Git web interface using
                                                 libgit2 and flask
git-webhook (0.0.6)                            - 使用 Python Flask + SQLAchemy +
                                                 Celery + Redis + React
                                                 开发的用于迅速搭建并使用 WebHook
                                                 进行自动化部署和运维，支持 Github / GitLab
                                                 / Gogs / GitOsc。
Glask (0.0.23)                                 - An extension for flask
                                                 applications with best
                                                 practices.
glassblower (0.2.5)                            - The Best Flask Boilerplate
                                                 Framework
Gluino (0.4)                                   - port of web2py libs to
                                                 bottle, flask, pyramid,
                                                 tornado (includes copy of
                                                 modules from the web2py
                                                 framework)
goblet (0.3.5)                                 - Git web interface using
                                                 libgit2 and flask
google_forms (0.3)                             - Flask web proxy for Google
                                                 forms
halef-SETU (0.0.5)                             - halef-SETU provides an easy
                                                 wrapper around SKLL models
                                                 for statistical language
                                                 understanding as well as an
                                                 easy to API based on Flask
happymongo (0.1.1)                             - Python module for making it
                                                 easy and consistent to
                                                 connect to MongoDB via
                                                 PyMongo either in Flask or in
                                                 a non-flask application
Harambe (0.10.0)                               - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
haven (1.1.105)                                - flask's style binary server
                                                 framework
py-healthcheck (1.6.1)                         - Adds healthcheck endpoints to
                                                 Flask or Tornado apps
healthcheck (1.3.2)                            - Adds healthcheck endpoints to
                                                 Flask apps
hflossk (0.5.10)                               - HFOSS course materials via
                                                 flask
highfield (1.0.21)                             - Structured flask with mongo
HipPocket (0.1.2a)                             - A wrapper around Flask to
                                                 ease the development of
                                                 larger applications
horn ((latest release))                        - Hy Macros for Flask
http-server-livereload (1.1.0)                 - A monkey patch of http.server
                                                 to call livereload when
                                                 server_forever is called.
                                                 This is compatible with flask
                                                 reload and tiny-lr (grunt
                                                 watch).
hxl-proxy (1.0)                                - Flask-based web proxy for HXL
jac (0.16.1)                                   - A Jinja extension (compatible
                                                 with Flask and other
                                                 frameworks) to compile and/or
                                                 compress your assets.
Jalapeno (0.1.4)                               - Static Site Generator based
                                                 on Flask
jiac (0.2.1)                                   - A Jinja extension (compatible
                                                 with Flask) to compile and/or
                                                 compress your assets inline.
jobmonitor (0.0.5)                             - Physics-orientated job
                                                 monitoring over HTTP with
                                                 Flask.
json-validator (1.0)                           - Provide decorator for
                                                 validating json parameters
                                                 passed to function. Can be
                                                 used for validation of json
                                                 parameters sent to Flask.
py-json-rpc (0.0.3)                            - Decorator based toolkit to
                                                 use JSONRPC easy like Flask
Juice (0.0.23)                                 - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
Keg (0.4.1)                                    - A web framework built on
                                                 Flask & SQLAlchemy.
                                                 Somewhere North of Flask but
                                                 South of Django.
KegBouncer (2.2.3)                             - A three-tiered permissions
                                                 model for KegElements built
                                                 atop Flask-User
kipavois (0.1.2)                               - Flask proxy over Kibana with
                                                 KiPavois
kit (0.2.15)                                   - Flask, Celery, SQLAlchemy
                                                 integration framework.
kola (1.5.6)                                   - flask's style json server
                                                 framework
kube_shields (0.0.6)                           - kube shields flask frontend.
zeus-lab804 (0.1.2)                            - Fast create scaffold of
                                                 flask.
Lagring (0.2.7.1)                              - Asset storage for Flask
Lapin (0.01a1)                                 - A flask-based web framework
latexrender (0.3.6)                            - A simple Flask app for
                                                 rendering latex snippets into
                                                 images.
lever (0.2.6)                                  - A tool for exposing
                                                 SQLAlchemy models in Flask
                                                 via REST
littlefish (0.0.4)                             - Flask webapp utility
                                                 functions by Little Fish
                                                 Solutions LTD
logy (0.1)                                     - A flask based web application
                                                 for central logging
lraudit (0.1.1)                                - Adds auditing to LR Flask
                                                 apps
lrutilities (0.1.2)                            - Utilities for LR Flask apps
lrutils (0.1.4)                                - Utilities for LR Flask apps
madame (0.1.2.a)                               - RESTful API for MongoDB built
                                                 on Flask
magic-xxl (0.6.1)                              - A collection librairies to
                                                 work with Flask-Magic
tornado-mail (0.4.0)                           - A email plugin for tornado.
                                                 It is a fake Flask_mail.
Mambo (1.0.0b21)                               - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
mana (4.8)                                     - the missing startproject
                                                 command for Flask
mana0 (0.10)                                   - my flask toolkit
mana2 (0.15)                                   - my flask toolkit
mana3 (0.15)                                   - my flask toolkit
mana4 (0.15)                                   - my flask toolkit
simple-site-manager (0.1.7)                    - Manage multiple lighttpd and
                                                 Django or Flask websites on a
                                                 single machine.
script-manager (0.1.0)                         - A command-line interface.
                                                 Just a simple and crude
                                                 implementation of Flask-
                                                 Script.
mandrill_webhooks (0.1.0)                      - Flask Webhooks
manhattan_dispatch (0.0.2)                     - A middleware dispatcher for
                                                 Flask based on             we
                                                 rkzeug.wsgi.DispatcherMiddlew
                                                 are.
markov_autocomplete (1.0.1)                    - Autocomplete model easy to
                                                 integrate with Flask apps
mediaflask (0.2.1)                             - Download audio from online
                                                 videos.
mediatumbabel (0.1.1)                          - flask-babel port to provide
                                                 i18n for mediaTUM (+jinja2)
                                                 with some improvements
meteorpi_server (0.1.5)                        - HTTP server based on Flask
                                                 providing a remote API
Microbe (1.2)                                  - Micro Blog Engine inspired by
                                                 Pelican and powered by Flask
oauth-middleware (0.3.3)                       - Simple flask_oauthlib based
                                                 middleware for WSGI app to
                                                 preform oauth
simple-migrate (0.0.3)                         - A simple database migrate
                                                 tool for flask
mimerender (0.6.0)                             - RESTful HTTP Content
                                                 Negotiation for Flask,
                                                 Bottle, web.py and webapp2
                                                 (Google App Engine)
mkflask_module (0.1.1)                         - Python module
Mlask (0.2)                                    - manage.py for Flask
Mocha (0.8.0)                                  - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
moesifwsgi (1.0.0)                             - Moesif Middleware for Python
                                                 WSGI based flatforms (Flask,
                                                 Bottle & Others)
moflask (0.1)                                  - Re-usable flask utilities.
pyramid-mongoengine (0.0.4)                    - Mongoengine Pyramid extension
                                                 based in flask-mongoengine
redis-monitor (1.0.3)                          - 使用Flask开发的一个 web 可视化的 redis
                                                 监控程序，可以查看 redis 的服务器信息、实时监控
                                                 redis 的消息处理 ops、内存占用、cpu
                                                 消耗，以及 redis 联通时间。 A web
                                                 visualization redis
                                                 monitoring program.
                                                 Performance optimized and
                                                 very easy to install and
                                                 deploy. the monitor data come
                                                 from redis.info().
myflaskr (0.0.1)                               - A test upload for PyPI
NCTU-Oauth (0.1.0)                             - adds NCTU-Oauth support to
                                                 flask
notes-pico (0.7)                               - A note-taking example web
                                                 application for Picoweb web
                                                 pico-framework. (Ported from
                                                 Flask original)
nyt-pyiap (0.0.6)                              - Python utility functions and
                                                 Django/Flask middlewares for
                                                 validating JWT tokens from
                                                 Google's Identity-Aware Proxy
ofcourse (0.2.5)                               - Python courseware with Flask
                                                 on OpenShift
onyx_sqlalchemy (3.2)                          - flask_sqlalchemy for Onyx
onyxbabel (0.0.3)                              - Ramake of the Flask_BabelEX
                                                 for Onyx
Openedoo-Script-Test (0.1.2)                   - Scripting support for Flask
openedoo (1.1.0.19)                            - openedoo is backend service
                                                 for education base on flask
palmer (0.0.4)                                 - Redice Flask Boost Library.
                                                 Inspired by flask-api.
paqmind.flask-paqforms (1.0.0)                 - UNKNOWN
paqmind.flask-routes (0.2.4)                   - Class-based routes for Flask
paqmind.flask-views (0.5.1)                    - Class-based views for Flask
sanic-patched (0.4.1)                          - A microframework based on
                                                 uvloop, httptools, and
                                                 learnings of flask
perfume (0.2)                                  - Simple Object Oriented layer
                                                 for Flask.
permission (0.4.1)                             - Simple and flexible
                                                 permission control for Flask
                                                 app.
phial (0.2.0)                                  - A static website generator
                                                 that takes motivation from
                                                 Flask and Jekyll.
Phial-Toolset (1.0.2)                          - Non-intrusive toolset to
                                                 easily use
                                                 Flask/Peewee/Celery
phovea_security_flask (0.1.0)                  - UNKNOWN
PlatformoClient (0.0.7)                        - 收集Flask的请求响应时间并发送至logstash
plush_web (0.1.0)                              - Micro framework inspirated by
                                                 Sinatra, Express and Flask.
podhub.meh (0.1.12)                            - Flask framework with
                                                 defaults.
Pontus (0.2.1)                                 - Flask utility for Amazon S3.
ponywhoosh (1.7.5)                             - Your database now searchable.
                                                 The backend behind the Flask-
                                                 PonyWhoosh.
Portfolio-py (0.0.1)                           - Portfolio is a Flask based
                                                 framework that adds structure
                                                 and map your views and
                                                 templates together for rapid
                                                 application development
pour (0.2.1)                                   - A lightweight Flask app
                                                 generator.
preflask (0.2)                                 - flask & preprocessors,
                                                 together, forever <3
Prestige (0.0.1)                               - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
proxapy (0.1.5)                                - Simple API proxy that uses
                                                 Flask/requests/gunicorn.
py3web (0.3.14)                                - Django lets you write web
                                                 apps in Django. Flask lets
                                                 you write web apps in Flask.
                                                 Py3web lets you write web
                                                 apps in Python.
pygrest (0.3)                                  - Build REST APIs with Neo4j
                                                 and Flask, as quickly as
                                                 possible!
Pylot (0.0.4)                                  - Pylot is a Flask extension
                                                 that adds structure and map
                                                 your views and templates
                                                 together for rapid
                                                 application development
pyros_config (0.2.0)                           - Classes to manage a server
                                                 configuration. Heavily
                                                 inspired by flask
python-thumbnails (0.5.1)                      - Thumbnails for Django, Flask
                                                 and other Python projects.
PyTyrion (1.0.1)                               - 支持Tornado、Django、Bottle、Flask
                                                 的Web表单验证
pyxley (0.1.0)                                 - Python tools for building
                                                 Flask-based web applications
qiniufs (1.0.1)                                - qiniu file uploader for
                                                 flask!
Quart (0.1.0)                                  - An asyncio web microframework
                                                 with Flask's API
quokka (0.2.0)                                 - Flexible & modular CMS
                                                 powered by Flask and MongoDB
quorum (0.5.8)                                 - Quorum Extensions for Flask
Redberry (0.0.7.5)                             - Flask Blueprint for adding
                                                 simple CMS functionality
relask (0.1.0)                                 - A Relay-based web development
                                                 kit on Flask
reportexport (0.0.3)                           - A Flask microservice that
                                                 produces reports out of a
                                                 database in xml and pdf
                                                 format.
RESTfulEf (0.1.1)                              - A generic restful api
                                                 generator based on elixir and
                                                 flask
Tornado-Restless (0.4.5)                       - flask-restless adopted for
                                                 tornado
restpager (0.1)                                - A RESTful pager class for
                                                 Flask
revise (0.0.3)                                 - Simple Schemas for Flask JSON
                                                 Validation
ripozo (1.3.0)                                 - ReSTful API framework with
                                                 HATEOAS support and
                                                 compatibility with Flask,
                                                 Django, SQLAlchemy and more.
rororo (1.0.0)                                 - Collection of utilities,
                                                 helpers, and principles for
                                                 building Python backend
                                                 applications. Supports
                                                 aiohttp.web, Flask, and your
                                                 web-framework
serverless-runlocal (0.1.2)                    - Serverless configuration
                                                 parser to run your serverless
                                                 function as Flask.
s_sqlachemy (0.1.1)                            - 不依赖app的flask-
                                                 sqlachemy，更好用的sqlachemy
Sanic (0.5.4)                                  - A microframework based on
                                                 uvloop, httptools, and
                                                 learnings of flask
sbswebsite (0.0.23)                            - Flask based project to create
                                                 a personal site
sga (0.1.39)                                   - make it easier to use pyga
                                                 for web develop. and make
                                                 pyga compatible with flask
                                                 and django.
Shaft (0.0.8)                                  - A mid stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha, Cors.
                                                 Supports HTML, Markdown and
                                                 Jade and more
Shake (1.6.4)                                  - A lightweight web framework
                                                 based on Werkzeug and Jinja2
                                                 as an alternative to Flask
ShelfCMS (0.12.25)                             - Enhancing flask
                                                 microframework with beautiful
                                                 admin and cms-like features
shiftboiler (0.1.6)                            - Best practices setup for
                                                 webapps, apis and cli
                                                 applications with flask
simple_flask_server (0.0.1)                    - Flask equivalent of python -m
                                                 SimpleHTTPServer.
simple_openid (1.0.6)                          - Simple OpenID. One-line setup
                                                 for OpenID login for Flask.
simpleapi (0.0.9)                              - A simple API-framework to
                                                 provide an easy to use,
                                                 consistent and portable
                                                 client/server-architecture
                                                 (for django, flask and a lot
                                                 more).
SimpleFlask (0.1.0)                            - Simple Flask application.
SimpleFlaskBlueprint (0.1.1)                   - Simple Flask blueprint.
SimpleSQLProxy (1.0)                           - A simple sqlproxy for SQL
                                                 LITE databases based on flask
SinglePage (0.1.0)                             - A RESTful framework based on
                                                 Flask and SQLAlchemy and
                                                 Redis
skaffold (0.1)                                 - Flask/SQLAlchemy Admin
                                                 Scaffold
slask (0.1.1)                                  - A Flask app to republish to
                                                 Slack
Slingr (0.0.13)                                - Web development framework
                                                 that builds and serves Cobs
                                                 (deployable web
                                                 applications), running on top
                                                 of Flask
SmallScrewdriver (1.0.2)                       - SmallScrewdriver is python
                                                 texture packer library, with
                                                 frontend's on PySide GUI,
                                                 Flask/React.js, and console
solidwebpush (1.2.1)                           - This package lets your server
                                                 send Web Push Notifications
                                                 to your clients. NOTE: No
                                                 particular web framework are
                                                 required (e.g. Django, Flask,
                                                 Pyramid, etc.), since it was
                                                 originally designed to run on
                                                 a Raspberry Pi with no web
                                                 server installed (only a bare
                                                 Python program listening on a
                                                 port for HTTP requests).
spill (0.0.1a0)                                - A utility for generating
                                                 Flask scaffolding and
                                                 boilerplate.
spouk_utils (0.1)                              - some utils for flask
                                                 distributions
StasFliKISS (0.1.2)                            - Wiki engine based on Markdown
                                                 flat files powered by Flask.
                                                 Fork from StasEvseev.
StatesofUSA (0.1)                              - An API built on  Flask-
                                                 RESTful that returns with the
                                                 names of all the states in
                                                 USA.
sucrose (0.1)                                  - mircroservice library using
                                                 flask and rabbitmq
tahoe (1.0.3.1)                                - A Flask-based framework that
                                                 handles the tedious things
talisman (0.1.0)                               - HTTP security headers for
                                                 Flask.
teleflask (0.0.8)                              - Easily create Telegram bots
                                                 with pytgbot and flask.
                                                 Webhooks made easy.
testflask (0.5)                                - Test flask applications
                                                 easily.
Thorium (0.2.16)                               - A Python framework for
                                                 RESTful API interfaces in
                                                 Flask
tinflask (0.0.2)                               - Simple wrapper around flask
                                                 that uses environment
                                                 variables for host, port,
                                                 endpoint prefix. Also uses
                                                 the py-hancock library for
                                                 the ability to sign
                                                 endpoints. Endpoints for
                                                 `time`, `ping`, and `status`
                                                 are automatically added as
                                                 well.
tinysmtp (0.1.2)                               - Basically Flask-Mail without
                                                 the Flask part
Toucan (0.0.0)                                 - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
trappist (0.2.0)                               - Mount your Flask or WSGI app
                                                 in your Django app.
tumbler (0.0.23)                               - Tumbler is a simple layer
                                                 that leverage flask with nice
                                                 logs and automated settings
                                                 management
txflask (0.1)                                  - txflask makes working with
                                                 Twisted Web as easy as
                                                 working with flask
tyron (0.2.4)                                  - Gevent redis/pubsub event
                                                 notifier written in flask and
                                                 gevent
update_checker_app (0.6)                       - Flask Application that
                                                 provides the interface to the
                                                 update_checker package.
uppsell (0.1)                                  - A Flask-based e-commerce API
                                                 and a django-backed admin for
                                                 managing them.
vassal_deployer (0.0.2)                        - uwsgi and nginx flask app
                                                 vassal manager for containers
vuuvv (0.0.1)                                  - A web framework using flask,
                                                 like ror.
webargs (1.7.0)                                - A friendly library for
                                                 parsing and validating HTTP
                                                 request arguments, with
                                                 built-in support for popular
                                                 web frameworks, including
                                                 Flask, Django, Bottle,
                                                 Tornado, Pyramid, webapp2,
                                                 Falcon, and aiohttp.
webdeployer (0.0.4)                            - Personal Deployer for site
                                                 created with Flask and Django
weber_utils (1.2.2)                            - Utilities for the Weber flask
                                                 template
Webmaster (0.0.2)                              - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
WebPortfolio (0.2.6)                           - A full stack Flask based
                                                 framework that put structure
                                                 in the file system. Features:
                                                 Caching, Mailing, Storage,
                                                 CSRF, recaptcha and more
webspanner (0.1.0)                             - Spanner is a micro web
                                                 framework based on asyncio
                                                 inspired by Flask &
                                                 Express.js.
wfgfw (0.0.6)                                  - word filter for gfw, include
                                                 plugin for flask. download
                                                 keywords: https://github.com/
                                                 observerss/textfilter
wheelshop (0.1)                                - your python wheels on a PyPI
                                                 compatible server using flask
                                                 and S3
whs.utils.flask (0.2.0)                        - Some Flask utils, targeting
                                                 REST services
WTCrud (0.1dev)                                - CRUD forms for WTForms using
                                                 Flask, Jinja2, SQLAlchemy
xstat (0.1.9)                                  - make statsd work with flask,
                                                 django, maple or other server
yell (0.3.2)                                   - User notification library
                                                 with pluggable backends.
                                                 Compatible with popular
                                                 frameworks such as Django,
                                                 Flask, Celery.
Zask (1.9.4)                                   - Basic framework to use with
                                                 ZeroRPC inspired by Flask
zforms (1.8)                                   - Tiny Flask form validation
                                                 library.
Zolenmeyer (0.1)                               - Stupid personally customized
                                                 Flask
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ git checkout branch
fatal: Not a git repository (or any of the parent directories): .git
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ hist
-bash: hist: command not found
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pip install django
Requirement already satisfied: django in /Users/ribribble/Desktop/DojoAssignments/Python/myEnvironments/djangoEnv/lib/python2.7/site-packages
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ pyhton
-bash: pyhton: command not found
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ ls
apps				products.zip
belt2				products2
belt2.zip			products2 2.zip
belt3				products2 3.zip
belt3.zip			products2.zip
beltExam			queries
belt_prep_quotes_delete		ran_word_gen
books				ran_word_gen.zip
books.zip			ran_word_gen2
books2				random_word3
books2.zip			random_word3.zip
courses				real_port
courses.zip			regex_operators.rtf
deployment			secrets
django.pem			settings.py
django_shell			sports_orm
django_tree.jpg			survey2
friends				survey2.zip
full_stack_books		survey3
full_stack_books.zip		survey3.zip
hello_world			survey_form_assignment
hello_world.zip			time_display2
login_registration		time_display_assignment
login_registration 2.zip	user_validation2
login_registration.zip		user_validation2.zip
main				validate
ninja_gold			validate.zip
ninja_gold.zip			vanish_ninja
ninja_gold2			vanish_ninja.zip
notes				wall
notes.docx			wall.zip
portfolio			wall2
portfolio.zip			wall2.zip
products
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ cd GithubRepos
-bash: cd: GithubRepos: No such file or directory
(djangoEnv) ribribble@Ribs-MacBook-Pro Django $ cd ..
(djangoEnv) ribribble@Ribs-MacBook-Pro Python $ ls
Authman			Flask_MySQL		myEnvironments
Django			Python_Fundamentals	surveyFeb_2017
Flask_Fundamentals	Python_OOP
(djangoEnv) ribribble@Ribs-MacBook-Pro Python $ cd ..
(djangoEnv) ribribble@Ribs-MacBook-Pro DojoAssignments $ ls
Icon?		MySQL		Ruby		deployment
MEAN		Python		WebFundamentals
(djangoEnv) ribribble@Ribs-MacBook-Pro DojoAssignments $ cd ..
(djangoEnv) ribribble@Ribs-MacBook-Pro desktop $ ls
CARREER
DojoAssignments
GithubRepos
SKYPE
Screen Shot 2017-04-26 at 1.30.55 PM (2).png
Screen Shot 2017-04-26 at 1.30.55 PM (3).png
Screen Shot 2017-04-26 at 1.30.55 PM.png
Screen Shot 2017-04-26 at 1.31.04 PM (2).png
Screen Shot 2017-04-26 at 1.31.04 PM (3).png
Screen Shot 2017-04-26 at 1.31.04 PM.png
Screen Shot 2017-04-26 at 1.31.32 PM (2).png
Screen Shot 2017-04-26 at 1.31.32 PM (3).png
Screen Shot 2017-04-26 at 1.31.32 PM.png
bin
dojo_arena_photos-master
screen_shots
(djangoEnv) ribribble@Ribs-MacBook-Pro desktop $ cd GithubRepos
(djangoEnv) ribribble@Ribs-MacBook-Pro GithubRepos $ git checkout master
fatal: Not a git repository (or any of the parent directories): .git
(djangoEnv) ribribble@Ribs-MacBook-Pro GithubRepos $ python
Python 2.7.13 (default, Dec 18 2016, 07:03:39) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + 5
9
>>> 18 - 5
13
>>> 4 * 7
28
>>> 31/2
15
>>> 9.04/4
2.26
>>> 9.04/4.0
2.26
>>> str = "This is a string stored in str variable"
>>> num = 5
>>> str = " I can change my value whenever I like"
>>> list =[4,2,9,7]]
  File "<stdin>", line 1
    list =[4,2,9,7]]
                   ^
SyntaxError: invalid syntax
>>> list = [4,2,9,1]
>>> exit()
(djangoEnv) ribribble@Ribs-MacBook-Pro GithubRepos $ ls
python_april_2017			submitt_assignment_to_github.rtf
python_may_2017
(djangoEnv) ribribble@Ribs-MacBook-Pro GithubRepos $ cd ..
(djangoEnv) ribribble@Ribs-MacBook-Pro desktop $ touch hello_world.py
(djangoEnv) ribribble@Ribs-MacBook-Pro desktop $ cd ..
(djangoEnv) ribribble@Ribs-MacBook-Pro ~ $ ls
Applications		Library			Public
Desktop			Movies			iCloud Drive (Archive)
Documents		Music			moveOutForm.pdf
Downloads		Pictures
(djangoEnv) ribribble@Ribs-MacBook-Pro ~ $ cd Desktop
(djangoEnv) ribribble@Ribs-MacBook-Pro Desktop $ ls
CARREER
DojoAssignments
GithubRepos
SKYPE
Screen Shot 2017-04-26 at 1.30.55 PM (2).png
Screen Shot 2017-04-26 at 1.30.55 PM (3).png
Screen Shot 2017-04-26 at 1.30.55 PM.png
Screen Shot 2017-04-26 at 1.31.04 PM (2).png
Screen Shot 2017-04-26 at 1.31.04 PM (3).png
Screen Shot 2017-04-26 at 1.31.04 PM.png
Screen Shot 2017-04-26 at 1.31.32 PM (2).png
Screen Shot 2017-04-26 at 1.31.32 PM (3).png
Screen Shot 2017-04-26 at 1.31.32 PM.png
bin
dojo_arena_photos-master
screen_shots
(djangoEnv) ribribble@Ribs-MacBook-Pro Desktop $ cd DojoAssignments
(djangoEnv) ribribble@Ribs-MacBook-Pro DojoAssignments $ ls
Icon?		MySQL		Ruby		deployment
MEAN		Python		WebFundamentals
(djangoEnv) ribribble@Ribs-MacBook-Pro DojoAssignments $ cd Python
(djangoEnv) ribribble@Ribs-MacBook-Pro Python $ ls
Authman			Flask_MySQL		myEnvironments
Django			Python_Fundamentals	surveyFeb_2017
Flask_Fundamentals	Python_OOP
(djangoEnv) ribribble@Ribs-MacBook-Pro Python $ cd Python_Fundamentals
(djangoEnv) ribribble@Ribs-MacBook-Pro Python_Fundamentals $ ls
ave_list.py			min_max.py
checkerboard.py			multiple_part1.py
coin_toss.py			multiple_part2.py
compare_arrays.py		names.py
debugging_practice.py		nesteddictionaries_practice.py
dictionaries_practice.py	pipPractice.txt
dictionary_basics.py		requirements.txt
find_chr.py			scores_grades.py
find_replace.py			stars.py
first_last.py			string_list_practice.py
funwfunc_multi.py		sum_list.py
funwfunc_odd_even.py		tuple_Practice.py
hello_world2.py			type_list.py
int_filter.py
(djangoEnv) ribribble@Ribs-MacBook-Pro Python_Fundamentals $ print "Hello World!"



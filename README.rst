.. role:: python(code)
    :language: python

Django Logging DLP Fork
=======================

A Django library that logs request, response and exception details in a JSON document.
It uses the python rotation mechanism to rotate the file logs, but the rotation files will be gziped and it has support for sending the log messages to Elasticsearch.

This fork adds more user control of the configuration of handlers and supports custom handlers. 

There is a test django project companion repo at https://github.com/dlparker/test_project_django_logging_dlp. If you take a look at that project, in the utils/handler.py file you will see a custom handler. You can see the configuration of that handler as an extra in the project settings.py file. You can see the configuration of the same handler as the only handler in the replace_settings.py file.



Installation
============

.. code-block:: python

    pip install git+https://github.com/dlparker/django-logging.git


Quick start
===========
1. Add "django_logging" to your INSTALLED_APPS settings like this:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_logging_dlp',
    )


2. Include the DjangoLoggingMiddleware middleware in your MIDDLEWARE_CLASSES like this:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'django_logging_dlp.middleware.DjangoLoggingMiddleware',
        ...
    )

Handlers
========

AppFileHandler
--------------

This handle will log request/response info to ``LOG_PATH/app.log``. It will also log request/exception, for unhandled exceptions, in the same file.
Log format:

Request and Response

.. code-block:: javascript

    {
        "INFO":
        {
            "timestamp":
            {
                "request": {
                ... request info ...
                },
                "response": {
                ... response info ...
                }
            }
        }
    }

Request and Exception

.. code-block:: javascript

    {
        "ERROR":
        {
            "timestamp":
            {
                "request": {
                ... request info ...
                },
                "exception": {
                    "message": "Exception message",
                    "traceback": [
                        ...
                    ]
                }
            }
        }
    }

SQLFileHandler
--------------

This handler will log all queries to ``LOG_PATH/sql.log``.
In a production environment you should set ``LOG_LEVEL = Error`` or ``SQL_LOG = False`` to avoid performance issues.
The queries will also be logged to the console if ``CONSOLE_LOG`` is set to ``True``

DebugFileHandler
----------------

This handler will log debug messages to ``LOG_PATH/debug.log``. This handler is only used when ``settings.DEBUG`` is set to ``True``.

Log format:

.. code-block:: python

    [%(levelname)s - %(created)s], file:%(module)s.py, func:%(funcName)s, ln:%(lineno)s: %(message)s


Custom Use
==========


To log debug messages:

.. code-block:: python

    from django_logging_dlp import log

    log.debug('debug message')

To log handled exceptions:

.. code-block:: python

    from django_logging_dlp import log, ErrorLogObject

    log.error(ErrorLogObject(request, exception))


Settings
========
Inspired by Django Rest Framework, Django Logging settings are grouped in a single dictionary.

To override Django Logging settings, add a dictionary in your project's settings file

.. code-block:: python

    DJANGO_LOGGING = {
        "CONSOLE_LOG": False
    }

Default Settings
----------------

:python:`CONSOLE_LOG = True` - Log to console.

:python:`SQL_LOG = True` - Log SQL queries.

:python:`LOG_LEVEL = 'debug'` - If settings.DEBUG is set to True, otherwise LOG_LEVEL is set to 'info'

:python:`DISABLE_EXISTING_LOGGERS = True` - Set this to False if you want to combine with multiple loggers.

:python:`LOG_PATH = '{}/logs'.format(settings.BASE_DIR)` - If the logs folder does not exist, it will be created.

:python:`IGNORED_PATHS = ['/admin', '/static', '/favicon.ico']` - List of URL endpoints to ignore.

:python:`RESPONSE_FIELDS = ('status', 'reason', 'charset', 'headers', 'content')` - List of response fields to log.

:python:`CONTENT_JSON_ONLY = True` - Log response content only if its a JSON document.

:python:`ROTATE_MB = 100` - Maximum size in MB that the log file can have before it gets rotated.

:python:`ROTATE_COUNT = 10` - Maximum number of rotated log files.

:python:`INDENT_CONSOLE_LOG = 2` - Indent console log by "n" spaces.

:python:`ELASTICSEARCH_ENABLED = False` - Set to yes to enable elasticsearch support.

:python:`ELASTICSEARCH_HOSTS = ["localhost"]` - Elasticsearch hosts

:python:`EXTRA_HANDLERS = []` - List of handlers to be added to default set (this fork, not in original)

:python:`OVERRIDE_HANDLERS = []` - List of handlers to be used to completely replace default set (this fork, not in original)


Fork Change Log
===============
[2017-1-18] 15:30 CDT

- Changed behavior of settings so that it honors LOG_PATH if it present, then uses django.conf.settings.BASE_DIR + '/logs', unless that setting is missing in which case it uses  pwd + "/logs";
- Added EXTRA_HANDLERS to settings to allow you to create your own handler class and add it to the set of pre-defined handlers.
- Added OVERRIDE_HANDLERS to settiongs to allow you to completely replace the pre-defined handlers with your own set.



[2017-1-18] 11:00 CDT
Fork and update of this file



Original Change Log
===================

1.5.3 [2016-06-26]
------------------
- bug fixing

1.5 [2016-06-04]
----------------
 - do not return a response in process_exception. Give other middlewares a chance to process the exception.
 - console log indentation
 - elastic search support. below a sample chart using kibana with elasticsearch and django-logging

.. image:: kibana_sample.png


1.4 [2016-02-19]
----------------

 - bug fixing
 - added support for query logging when using multiple database
 - added database alias for sql logs if multiple databases are used
 - added plain dict logging support

1.3 [2015-12-13]
----------------

 - added support for Python 2.7
 - added support for Django >= 1.4

1.2 [2015-11-22]
----------------
 - added sql logging support
 - log entries are now sorted by keys
 - console handler now indents the log entries by 4 spaces
 - log response content if it's JSON (bug)

1.1 [2015-11-17]
----------------
 - added exception "type" for exception log entries

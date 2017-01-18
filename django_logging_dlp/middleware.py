import datetime
import threading
from django.db import connections
from . import log
from . import settings
from .log_object import LogObject, ErrorLogObject, SqlLogObject


class DjangoLoggingMiddleware(object):
    def process_exception(self, request, exception):
        error = ErrorLogObject(request, exception)
        log.error(error)

    def process_request(self, request):
        self.tdata = threading.local()
        self.tdata.start = datetime.datetime.now()

    def process_response(self, request, response):
        done = datetime.datetime.now()
        delta = (done - self.tdata.start).total_seconds()
        for connection in connections.all():
            self.log_connection_queries(connection)

        if request.path_info.startswith(tuple(settings.IGNORED_PATHS)):
            return response

        if response.status_code == 500:
            return response
        elif 400 <= response.status_code < 500:
            log.warning(LogObject(request, response, delta))
        else:
            log.info(LogObject(request, response, delta))
        return response

    def log_connection_queries(self, connection):
        for query in connection.queries:
            log.debug(SqlLogObject(query, connection.alias))

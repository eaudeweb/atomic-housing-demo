from threading import local


_thread_locals = local()


def get_current_request():
    return getattr(_thread_locals, 'request', None)


class RequestMiddleware(object):
    """
    Middleware that gets various objects from the
    request object and saves them in thread local storage.
    """

    def process_request(self, request):
        _thread_locals.request = request

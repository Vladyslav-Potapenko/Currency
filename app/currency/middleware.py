from time import time

from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        end = time()

        log = RequestResponseLog(
            time=end - start,
            path=request.path,
            request_method=request.method,
        )
        log.save()

        return response

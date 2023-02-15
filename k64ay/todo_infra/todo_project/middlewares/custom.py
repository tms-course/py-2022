def custom_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        return response

    return middleware


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.custom = 'hello world'

        response = self.get_response(request)

        

        return response
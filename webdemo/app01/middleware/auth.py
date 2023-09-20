from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info == "/login/":
            return

        info = request.session.get("info")
        if info:

            return
        else:
            return redirect('/login/')


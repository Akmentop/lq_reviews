

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm

USER_LIST = dict()


@method_decorator(csrf_exempt, name='dispatch')
class UserSignupView(View):

    form_class = UserForm
    user_model = User

    def post(self, request: HttpRequest) -> JsonResponse:

        f = self.form_class(request.POST)

        if not f.is_valid():
            return JsonResponse(
                {'success': False, 'message': 'invalid username/password'},
                status=400
            )

        # if f.cleaned_data['username'] in USER_LIST:
        #     return JsonResponse(
        #         {'success': False, 'message': 'username exists'},
        #         status=400
        #     )
        #
        # USER_LIST.update(
        #     {f.cleaned_data['username']: f.cleaned_data['password']}
        # )

        try:
            user = self.user_model.objects.create_user(
                username=f.cleaned_data['username'],
                password=f.cleaned_data['password']
            )
        except IntegrityError:
            return JsonResponse(
                {'success': False, 'message': 'duplicate username'},
                status=400)

        return JsonResponse(
            {'success': True, 'username': user.username}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(View):

    form_class = UserForm

    def post(self, request: HttpRequest) -> JsonResponse:
        f = self.form_class(request.POST)

        if not f.is_valid():
            return JsonResponse(
                {'success': False, 'message': 'invalid username/password'},
                status=400
            )

        user = authenticate(request,
                            username=f.cleaned_data['username'],
                            password=f.cleaned_data['password'])

        if user:
            login(request, user)
            return JsonResponse({'success': True}, status=200)
        else:
            return JsonResponse(
                {'success': False,
                 'message': 'incorrect username/password'},
                status=400)


class UserLogoutView(View):

    redirect_url = '/'

    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect(self.redirect_url)

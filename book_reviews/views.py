

from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .utils import get_summary_list, get_review_detail
from .models import ReviewModel
from .forms import ReviewForm, RegisterForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> dict:
        # TODO(leonqu): need to add recent review list
        return {'change_form': ReviewForm()}

    # def get(self, request) -> HttpResponse:
    #     return render(request, self.template_name, context={'change_form': ReviewForm(), 'register_form': RegisterForm()})
    
    def post(self, request) -> HttpResponse:

        form = ReviewForm(request.POST, request.FILES)
        
        if form.is_valid():
            rev = form.save(commit=False)
            # rev.submitted_by = User.objects.get(username=request.user)
            rev.submitted_by = request.user
            rev.save()
        else:
            print(form.errors)

        return redirect('/')
        # return render(request, self.template_name, context={'change_form': ReviewForm(), 'register_form': RegisterForm()})


def dt_data(request) -> JsonResponse:
    """Returns the full data set to data table front end.

    TODO(leonqu): Implement server-side processing with search/pagination.
    """

    # print(ReviewModel.objects.all())

    return JsonResponse(get_summary_list(), safe=False)


def detail(request, review_id) -> JsonResponse:
    review_detail = get_review_detail(review_id)
    print(review_detail)
    return JsonResponse(review_detail, safe=False)
    

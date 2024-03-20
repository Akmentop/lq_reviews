

from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect

from .models import Review
from .forms import ReviewForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> dict:
        # TODO(leonqu): need to add recent review list
        recent_list = [i.get_as_recent() for i in Review.objects.all()[:3]]
        print(recent_list)
        return {'user': None, 'recent_list': recent_list, 'change_form': ReviewForm()}
    
    def post(self, request) -> HttpResponse:
        _ = self

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



class DataTableSourceView(View):

    review_model = Review

    def get(self, request: HttpRequest) -> JsonResponse:
        """Returns the full data set to data table front end.
        """

        if (request.GET.get('self') == 'true' and
                request.user.is_authenticated):
            results = self.review_model.objects.filter(
                submitted_by=request.user)
        else:
            results = self.review_model.objects.all()

        summ_list = [ i.get_info_as_list() for i in results]

        return JsonResponse(summ_list, safe=False)


class ReviewDetailView(View):

    review_model = Review

    def get(self, request: HttpRequest) -> JsonResponse:
        review_id = request.GET.get('id', 0)
        try:
            review = self.review_model.objects.get(id=review_id)
        except self.review_model.DoesNotExist:
            return JsonResponse(
                {'message': 'Review does not exist.'}, status=404)

        return JsonResponse(review.get_info_as_list(summary=False), safe=False)


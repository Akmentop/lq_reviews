

from django.http import JsonResponse
from django.views.generic import TemplateView

from .utils import get_summary_list, get_review_detail


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> dict:
        # TODO(leonqu): need to add recent review list
        return {'user': None}


def dt_data(request) -> JsonResponse:
    """Returns the full data set to data table front end.

    TODO(leonqu): Implement server-side processing with search/pagination.
    """
    return JsonResponse(get_summary_list(), safe=False)


def detail(request, review_id) -> JsonResponse:
    review_detail = get_review_detail(review_id)
    print(review_detail)
    return JsonResponse(review_detail, safe=False)

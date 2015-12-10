from django.views.generic import View

class SearchView(View):
    template_name = 'search/search_page.html'

    def get(self, request):
        pass

    def perform_search(self, request):
        pass

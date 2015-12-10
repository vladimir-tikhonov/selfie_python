from django.views.generic import View

class HelpTourView(View):
    template_name = 'help_tour/help_tour_page.html'

    def get(self, request):
        pass

    def show_help_tour(self, request):
        pass

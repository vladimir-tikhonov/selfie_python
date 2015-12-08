from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from plan.models.plan import Plan

class PlanListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'plan/choose_plan.html'
    context_object_name = 'plans'

    def get_queryset(self):
        all_plans = Plan.objects.all()
        queryset = []
        for plan in all_plans:
            plan_data = {
                'description': plan.plan_description.description,
                'price': plan.price,
                'duration': plan.duration
            }
            queryset.append(plan_data)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(PlanListView, self).get_context_data(**kwargs)
        context['username'] = self.kwargs['username']
        return context

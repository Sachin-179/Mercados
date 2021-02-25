import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import sales


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "application/dashboard.html"

    def get_context_data(self):
        context = super(DashboardView, self).get_context_data()
        sales_obj = sales.objects.all().values('order_number', 'quantity', 'price', 'sales', 'month', 'year', 'productline', 'dealsize')
        context['sales_obj'] = json.dumps({'sales_obj': list(sales_obj)})
        return context

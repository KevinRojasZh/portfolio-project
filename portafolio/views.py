from django.views.generic import TemplateView
from .models import Developer


class HomeView(TemplateView):
    model = Developer
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["developer"] = Developer.objects.get(id=1)  # Obtiene el objeto con id=1
        return context


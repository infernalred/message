from django.contrib.auth.decorators import login_required
from django.utils import decorators
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from postman.forms import PostmanForm
from postman.models import Postman


@method_decorator(login_required, name='dispatch')
class PostmanView(CreateView):
    model = Postman
    form_class = PostmanForm
    success_url = "/"
    template_name = "postman.html"

    # @method_decorator(login_required)
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

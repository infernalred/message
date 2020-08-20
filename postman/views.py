from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from postman.forms import PostmanForm
from postman.models import Postman
from postman.tasks import check_send_email


@method_decorator(login_required, name='dispatch')
class PostmanView(CreateView):
    model = Postman
    form_class = PostmanForm
    success_url = ""
    template_name = "postman.html"

    def form_valid(self, form):
        form.save()
        # check_email(form.instance.text, form.instance.email, form.instance.id)
        check_send_email.delay(form.instance.text, form.instance.email,
                               form.instance.id)
        return HttpResponseRedirect("/")

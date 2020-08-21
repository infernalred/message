from postman.models import Postman


def total_postman(request):
    postmans = Postman.objects.all()
    filed = len({post for post in postmans if not post.sent})
    return {"postman_total": postmans.count, "postman_filed": filed}

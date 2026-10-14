from django.http import HttpResponse


def health(request):
    """Railway healthcheck. Returns 200 once the app is serving requests."""
    return HttpResponse("ok", content_type="text/plain")

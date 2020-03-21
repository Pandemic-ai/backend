from .from django.urls import path, re_path, include
from . import views as v


urlpatterns = [
    # Catch-all stub view which just tries to read stuff from files.
    re_path('^.*/$', v.StubView.as_view()),
]

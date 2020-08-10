from django.urls import path

from what_can_i_cook.views import WCICFilterView, WCICResultView

app_name = "wcic"


urlpatterns = [
    path("", WCICFilterView.as_view(), name="wcic-start"),
    path("results/", WCICResultView.as_view(), name="wcic-results"),
]


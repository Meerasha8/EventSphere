from django.urls import path
from .views import (dashboard_home,profile_page,profile_view,events_page,event_page,create_event,my_events)

urlpatterns = [
    path("",dashboard_home,name="dashboard"),

    # profile pages
    path("profile/",profile_page,name="profile_page"),
    path("profile/<str:username>/",profile_view,name="profile_view"),

    # events pages
    path("events/",events_page,name="events_page"),
    path("events/<int:event_id>/",event_page,name="event_page"),
    path("create-event/",create_event,name="create_event"),
    path("my-events/",my_events,name="my_events"),

]
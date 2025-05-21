from django.urls import path
from bands import views

urlpatterns = [
    path("musician/<int:musician_id>", views.musician, name="musician"),
    path("musicians/", views.musicians, name="musicians"),
    path('bands/', views.bands_list, name='bands'),
    path('bands/<int:musician_id>', views.band_detail, name='band'),
]

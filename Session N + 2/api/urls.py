from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import FilmViewSet, FilmGeneric, FilmGenericDetail
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()

router.register(r'film', FilmViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('films/generics/', FilmGeneric.as_view()),
    path('films/generics/<int:pk>/', FilmGenericDetail.as_view()),
    path('docs/', include_docs_urls(title='My DVD documentation'))
]
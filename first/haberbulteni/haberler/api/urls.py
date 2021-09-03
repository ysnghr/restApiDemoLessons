from django.urls import path
from haberler.api import views as api_views


urlpatterns = [
    path('makalaler/', api_views.MakaleListCreateAPIView.as_view(), name='makale-listesi'),
    path('yazarlar/', api_views.GazeteciListCreateAPIView.as_view(), name='yazar-listesi'),
    path('makalaler/<int:pk>', api_views.MakaleDetailAPIView.as_view(), name='makale-detay'),
]


## FUNCTION BASED VIEWS ## 
# urlpatterns = [
#     path('makalaler/', api_views.makale_list_create_api_view, name='makale-listesi'),
#     path('makalaler/<int:pk>', api_views.makale_detail_api_view, name='makale-detay'),
# ]
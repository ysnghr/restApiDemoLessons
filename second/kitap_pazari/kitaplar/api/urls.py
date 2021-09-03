from django.urls import path
from kitaplar.api import views as apiviews

urlpatterns = [
    path('kitaplar/', apiviews.KitapListCreateAPIView.as_view(), name="kitap-listesi"),
    path('kitaplar/<int:pk>', apiviews.KitapDetailAPIView.as_view(), name="kitap-bilgileri"),
    path('kitaplar/<int:kitap_pk>/yorum_yap', apiviews.YorumCreateAPIView.as_view(), name="yorum-yap"),
    path('yorumlar/<int:pk>/', apiviews.YorumDetailAPIView.as_view(), name="yorumlar"),
]
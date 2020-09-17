from django.urls import path
from listings.api.views import (
    ListingListApiView,
    ListingPostApiView,
    ListingGetApiView,
    ListingPutApiView,
    ListingDeleteApiView,
    )

urlpatterns = [
    path('', ListingListApiView.as_view()),
    path('create/', ListingPostApiView.as_view()),
    path('<id>/', ListingGetApiView.as_view()),
    path('<id>/update', ListingPutApiView.as_view()),
    path('<id>/delete', ListingDeleteApiView.as_view()),
]

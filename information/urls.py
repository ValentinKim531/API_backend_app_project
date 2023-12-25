from django.urls import path

from .views import AboutViewSet, EventViewSet, RoomViewSet, AdvantageMainViewSet, AdvantageViewSet, BookingEventViewSet, \
    GalleryViewSet, ContactViewSet, CallbackRequestViewSet

urlpatterns = [
    path('about/', AboutViewSet.as_view({'get': 'get_about'}), name='about'),
    path('events/', EventViewSet.as_view({'get': 'list'}), name='event_list'),
    path('event/<int:pk>/', EventViewSet.as_view({'get': 'retrieve'}), name='event_detail'),
    path('rooms/', RoomViewSet.as_view({'get': 'list'}), name='room_list'),
    path('rooms/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve'}), name='room_detail'),
    path('advantage-main/', AdvantageMainViewSet.as_view({'get': 'get_about'}), name='advantage_main'),
    path('advantages/', AdvantageViewSet.as_view({'get': 'list'}), name='advantage_list'),
    path('advantage/<int:pk>/', AdvantageViewSet.as_view({'get': 'retrieve'}), name='advantage_detail'),
    path('booking-event-create/', BookingEventViewSet.as_view({'post': 'create'}), name='booking_event_create'),
    path('gallery/', GalleryViewSet.as_view({'get': 'get_gallery'}), name='gallery'),
    path('contacts/', ContactViewSet.as_view({'get': 'get_contacts'}), name='contacts'),
    path('callback-create/', CallbackRequestViewSet.as_view({'post': 'create'}), name='callback_request_create'),

]


from django.urls import path, include

from commons import views, date_views, time_views, timestamp_views

date_urlpatterns = [
    path('tostring/', date_views.to_string, name='date_tostring'),
    path('compare/', date_views.compare, name='date_compare'),
    path('add_days/', date_views.add_days, name='date_add_days'),
    path('diff/', date_views.diff, name='date_diff'),
    path('is_leap_year/', date_views.is_leap_year, name='date_is_leap_year'),
    path('max_days_in_this_month/', date_views.max_days_in_this_month, name='date_max_days_in_this_month'),
    path('next_month/', date_views.next_month, name='date_next_month'),
    path('previous_month/', date_views.previous_month, name='date_previous_month'),
    path('days_from_year_start/', date_views.days_from_year_start, name='date_days_from_year_start'),
    path('days_in_this_year/', date_views.days_in_this_year, name='date_days_in_this_year'),
    path('days_remaining_in_this_year/', date_views.days_remaining_in_this_year, name='date_days_remaining_in_this_year'),
]

time_urlpatterns = [
    path('tostring/', time_views.to_string, name='time_tostring'),
    path('compare/', time_views.compare, name='time_compare'),
    path('add_minutes/', time_views.add_minutes, name='time_add_minutes'),
    path('diff/', time_views.diff, name='time_diff'),
]

timestamp_urlpatterns = [
    path('tostring/', timestamp_views.to_string, name='timestamp_tostring'),
    path('compare/', timestamp_views.compare, name='timestamp_compare'),
]

urlpatterns = [
    path('date/', include(date_urlpatterns)),
    path('time/', include(time_urlpatterns)),
    path('timestamp/', include(timestamp_urlpatterns))
]

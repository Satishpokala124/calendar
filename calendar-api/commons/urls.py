from django.urls import path

from commons import views
from commons import date_views

urlpatterns = [
    path('date/tostring/', date_views.to_string, name='date_tostring'),
    path('date/compare/', date_views.compare, name='date_compare'),
    path('date/add_days/', date_views.add_days, name='date_add_days'),
    path('date/diff/', date_views.diff, name='date_diff'),
    path('date/is_leap_year/', date_views.is_leap_year, name='date_is_leap_year'),
    path('date/max_days_in_this_month/', date_views.max_days_in_this_month, name='date_max_days_in_this_month'),
    path('date/next_month/', date_views.next_month, name='date_next_month'),
    path('date/previous_month/', date_views.previous_month, name='date_previous_month'),
    path('date/days_from_year_start/', date_views.days_from_year_start, name='date_days_from_year_start'),
    path('date/days_in_this_year/', date_views.days_in_this_year, name='date_days_in_this_year'),
    path('date/days_remaining_in_this_year/', date_views.days_remaining_in_this_year, name='date_days_remaining_in_this_year'),
]

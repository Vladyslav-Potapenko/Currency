from django.urls import path


from currency.views import(
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDetailView,
    RateDeleteView,
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDetailView,
    SourceDeleteView,
    ContactusListView,
    ContactusCreateView,
    ContactusUpdateView,
    ContactusDetailView,
    ContactusDeleteView,
)

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

    path('contactus/list/', ContactusListView.as_view(), name='contactus'),
    path('contactus/create/', ContactusCreateView.as_view(), name='contactus-create'),
    path('contactus/update/<int:pk>/', ContactusUpdateView.as_view(), name='contactus-update'),
    path('contactus/details/<int:pk>/', ContactusDetailView.as_view(), name='contactus-details'),
    path('contactus/delete/<int:pk>/', ContactusDeleteView.as_view(), name='contactus-delete'),


]

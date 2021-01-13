from django.urls import include, path

app_name = 'api'
urlpatterns = [
    path('v1/', include('api.v1.urls', namespace='v1')),
    path('v2/', include('api.v2.urls', namespace='v2')),
    path('v3/', include('api.v3.urls', namespace='v3')),
]

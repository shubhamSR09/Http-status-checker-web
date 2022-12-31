from django.urls import re_path as url,include
from django.contrib import admin


urlpatterns = [
	url(r'', include('status.urls'), name='status'),
    url(r'^admin/', admin.site.urls),
	
]

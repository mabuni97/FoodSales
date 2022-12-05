from django.urls import path
from . import views  
from exportdata import settings
from django.conf.urls.static import static
urlpatterns =[
path("",views.Import_Excel_pandas,name="Import_Excel_pandas"),
path('Import_Excel_pandas/', views.Import_Excel_pandas,name="Import_Excel_pandas"), 
path('Import_excel',views.Import_excel,name="Import_excel"),
path('Food', views.Foodlist.as_view()),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
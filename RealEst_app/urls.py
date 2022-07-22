from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin




urlpatterns =[  path('load_index',views.load_index,name='load_index'),

                #Admin

                path('admin_staf',views.admin_staf,name='admin_staf'),
                path('admin_propertylist',views.admin_propertylist,name='admin_propertylist'),
                path('admin_propertyview',views.admin_propertyview,name='admin_propertyview'),
                path('admin_agent',views.admin_agent,name='admin_agent'),
                path('admin_agentadd',views.admin_agentadd,name='admin_agentadd'),
                path('admin_propertyadd',views.admin_propertyadd,name='admin_propertyadd'), 
                path('admin_telecaller',views.admin_telecaller,name='admin_telecaller'),
                path('admin_telecalleradd',views.admin_telecalleradd,name='admin_telecalleradd'),
                path('admin_loc_visit_schedule',views.admin_loc_visit_schedule,name='admin_loc_visit_schedule'),  

                #Staf

                path('',views.staf_dashboard,name='staf_dashboard'),
                path('staf_propertyview',views.staf_propertyview,name='staf_propertyview'),
                path('staf_cliant_propertyview',views.staf_cliant_propertyview,name='staf_cliant_propertyview'),
                path('staf_cliant_property',views.staf_cliant_property,name='staf_cliant_property'), 
]
"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from myapp.schema import schema
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('myapp/',include('myapp.urls')),
]

urlpatterns+=staticfiles_urlpatterns()


# postgres://${db.testdb_802f_user}:${db.2WjIfBgttNVoJNUMBeKUVUWmy5R6imsV}@${db.dpg-cpl7ummd3nmc73crje10-a}:${db.5432}/${db.testdb_802f}
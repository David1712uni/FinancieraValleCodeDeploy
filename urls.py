"""
URL configuration for AppWeb project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('app.urls')),
]

def example_function():
  x=5    # Espacio mal usado
  print (x)  # Espacio innecesario
def process_data():
    # FIXME: Needs to handle empty data cases
    data = [1, 2, 3]
    return data

def main():
    process_data()

if __name__ == "__main__":
    main()

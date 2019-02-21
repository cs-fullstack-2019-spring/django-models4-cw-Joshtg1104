# Exercise 1
# Create a model called Mom with mom_first_name, mom_last_name, and mom_phone_number.
# Create a second model called Child with child_first_name, child_last_name,
# and child_mom that is a ForeignKey that references Mom (deleting a Mom SHOULD delete all of their children)
# Add 3 Moms using the Django Admin console
# Add 3 Children using the Django Admin console
# Assign 1 Child to each Mom using the Django Admin console
# Add an endpoint children/ that will list all Children and their Mom by Child
# Add an endpoint moms/ that will list all Moms and their Children by Mom
# Add an endpoint addchild/ that will add a Child to each Mom
# Add an endpoint deletemom/ that will delete the first Mom and all of their their Children
# Confirm changes by using the children/ and moms/ endpoints

from django.urls import path

from . import views
# url paths
urlpatterns = [
    path('', views.index, name='index'),
    path('children/', views.children, name='child'),
    # path('moms/', views.moms, name='mom'),
    path('addchild/', views.addchild, name='addchild'),
    # path('deletemom/', views.deletemom, name='deletemom'),
]

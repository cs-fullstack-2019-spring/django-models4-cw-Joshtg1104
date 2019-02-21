from django.http import HttpResponse
from django.shortcuts import render
from .models import Mom, Child


# Create your views here.

def index(request):
    return HttpResponse("index")

#Endpoint iterates through children-parents
def children(request):
    kid = Child.objects.all()
    for k in kid:
        print(f'{k.child_first_name}')
        print(k.child_mom.mom_first_name)
        # for ma in Mom Child.objects.filter(child_mom__mom_first_name=ma.mom_first_name):
        #
        #     print(f'{ma.mom_first_name} {ma.mom_last_name}')

    return HttpResponse()

# Don't worry about this one
# def moms(request):
#     ma = Mom.objects.all()
#     for m in ma:
#         print(f'{m.mom_first_name}')
#         print(m.child_mom.kid_first_name)
#
#     return HttpResponse()

#Is broken, hopefully I get better at this
def addchild(request):
    # newKid = "Another Kid"
    mothers = Mom.objects.all()
    kid = Child(name="Aki")
    for eachElement in mothers:
        kid += eachElement.mom_first_name
        print(eachElement)

    return HttpResponse()

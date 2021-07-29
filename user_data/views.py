from django.shortcuts import render
from user_data.user_data_models import User
# Create your views here.
def from_Ruser_id_to_name(id):
    qs = User.objects.values()
    qs=qs.filter(用户ID=id)
    retlist = list(qs)
    name=retlist[0]["姓名"]
    return name

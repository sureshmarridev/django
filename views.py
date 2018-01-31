# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    webpages_list=AccessRecord.obects.order_by('date')
    date_dict={'access_records':webpages_list}
    my_dict={'insert_content':"Hello im from firstapp!"}
    return render(request,'first_app/index.html',context=my_dict)

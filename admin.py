from django.contrib import admin

# from .models import ADMIN
# from .models import CONTRACTOR
# from .models import END_USER
# from .models import LABOUR
# from .models import WORK
#from .models import FEEDBACK
# from .models import REQUEST
from .models import register1
from .models import profile1
from .models import work1
from .models import endwork1
from .models import requestsdata
from .models import contact1
from .models import LFEEDBACK
from .models import requestsdataforenduser

# Register your models here.
#

class showregister1(admin.ModelAdmin):
    list_display = ['name','email','phone','password','address','type_of_user']

class showreprofile1(admin.ModelAdmin):
    list_display = ['name','userid','phone','email','exp','address','des','img']

class showwork1(admin.ModelAdmin):
    list_display = ['name','phone','location','types_of_labour','no_of_labour','exp','Working_Hour','income_per_day','img','message']

class showrequestsdata(admin.ModelAdmin):
    list_display = ['workid','labourid','status','timestamp']

class showcontact1(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

class showendwork1(admin.ModelAdmin):
    list_display = ['userid','name','phone','location','types_of_labour','no_of_labour','exp','Working_Hour','income_per_day','img','message']

class showlfeedback(admin.ModelAdmin):
        list_display = ['Labour_name', 'C_ID', 'COMMENT', 'RATING']

class showrequestsdataforenduser(admin.ModelAdmin):
    list_display = ['workid','labourid','status','timestamp']



# class FEEDBACK(admin.ModelAdmin):
#    list_display = ['C_ID','L_ID','E_ID','COMMENT','RATING']



# admin.site.register(ADMIN,showadmin)
# admin.site.register(CONTRACTOR,showcont)
# admin.site.register(END_USER,showeu)
# admin.site.register(LABOUR,showlab)
# admin.site.register(WORK,showwork)
# admin.site.register(FEEDBACK,showfeed)
# admin.site.register(REQUEST,showreq)
admin.site.register(register1,showregister1)
admin.site.register(profile1,showreprofile1)
admin.site.register(work1,showwork1)
admin.site.register(endwork1,showendwork1)
admin.site.register(requestsdata,showrequestsdata)
admin.site.register(contact1,showcontact1)
admin.site.register(requestsdataforenduser,showrequestsdataforenduser)
admin.site.register(LFEEDBACK,showlfeedback)
# admin.site.register(FEEDBACK,showefeed)
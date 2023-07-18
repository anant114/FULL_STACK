from django.contrib import admin
# from myapp.models import signup


 
# admin.site.register(signup)

# Register your models here.
from django.contrib import admin
from myapp.models import UserList
from myapp.models import infos
from myapp.models import companydata
from myapp.models import marketdata
from myapp.models import clientname
from myapp.models import markettime
from myapp.models import operator
from myapp.models import oems
from myapp.models import activitylists
from myapp.models import Uploaded_file


    
class pushpendra(admin.ModelAdmin):
    list_display = ('firstname', 'secondname', 'companyid', 'role', 'email', 'phone', 'password' , 'image')    
    
class pushpendra2(admin.ModelAdmin):
    list_display = ('roleid','role')
 
class pushpendra1(admin.ModelAdmin):
    list_display = ('companyid','company')
    
class market(admin.ModelAdmin):
    list_display = ('clientid', 'operatorid', 'oemid', 'marketname', 'timeid', 'Specific_Market_Guidline', 'Ciq' , 'Call_test_info' , 'Call_test_files' , 'Site_access' , 'Guidelines', 'additional_Guidelines')    
    
class client(admin.ModelAdmin):
    list_display = ('clientid','cname')
    
class time(admin.ModelAdmin):
    list_display = ('timeid','mtime')
    
class opr(admin.ModelAdmin):
    list_display = ('operatorid','operatorname') 

class oem(admin.ModelAdmin):
    list_display = ('oemid','oem_name') 
    
    
class activitylist(admin.ModelAdmin):
    list_display = ('client', 'operator', 'oem', 'Ticket_Number', 'fa_location', 'site_ids', 'Added_Date',  'County', 'Activity',  'Ix_Date', 'G_IX_date', 'Ticket_Status', 'lite_site_id', 'three_g_site_id', 'Field_Installation', 'Alarm', 'Field_Integration', 'remote_Integration', 'five_g_site_id','site_name', 'market', 'address','zip_code','Added_By', 'IX_Status',  'CX_Status', 'latitude','longitude','mon_hours','tue_hours','wed_hours','thu_hours','fri_hours','sat_hours','sun_hours','key_comments' ,

                   'notice_needed','notice_comments','num_of_carrier','pace','ptn','sow_type','wo_cr_id','sow','ix_schedule_date', 'nest', 'mop_start_time', 'mop_end_time','assign_fe', 'ix_date_comment', 'equipment_pickup', 'five_g_ix_standalone', 'five_g_ix_schedule_date', 'call_test_date',   'market_state', 'crew_dispatch_date')



class uploaded_files(admin.ModelAdmin):
    list_display = ('file','processed_file') 
    



admin.site.register(Uploaded_file, uploaded_files)


admin.site.register(companydata, pushpendra1)
admin.site.register(infos, pushpendra)
admin.site.register(UserList, pushpendra2)
admin.site.register(marketdata, market)
admin.site.register(clientname, client)
admin.site.register(markettime, time)
admin.site.register(operator, opr)
admin.site.register(oems, oem)
admin.site.register(activitylists, activitylist)

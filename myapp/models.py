# Admin@123 ///








from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.db import models

class companydata(models.Model):
    companyid = models.AutoField(primary_key=True)
    company = models.CharField(max_length=255)   
   
class UserList(models.Model):
    roleid = models.AutoField(primary_key=True)
    role = models.CharField(max_length=255)    
    

    
 
class infos(models.Model):

 firstname=models.CharField(max_length=255)

 secondname=models.CharField(max_length=255)

 companyid = models.ForeignKey(companydata, on_delete=models.CASCADE)
 
 email = models.EmailField(max_length=255, unique=True)

 phone=models.CharField(max_length=255 , unique=True)
 
 image = models.ImageField(upload_to='media/', null=True)

 password=models.CharField(max_length=255)
 role = models.ForeignKey(UserList, on_delete=models.CASCADE)
 
#  --------------login

class clientname(models.Model):
    clientid = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    
class markettime(models.Model):
    timeid = models.CharField(max_length=255)
    mtime = models.CharField(max_length=255)        
    
 
class operator(models.Model):
    operatorid = models.CharField(max_length=255)
    operatorname = models.CharField(max_length=255)  
    
class oems(models.Model):
    oemid = models.CharField(max_length=255)
    oem_name = models.CharField(max_length=255)        

      
 
class Uploaded_file(models.Model):
    file = models.FileField(upload_to='downloads/')
    processed_file = models.FileField(upload_to='downloads/')

 

class marketdata(models.Model):
 
 clientid=models.ForeignKey(clientname, on_delete=models.CASCADE)

 operatorid = models.ForeignKey(operator, on_delete=models.CASCADE,)
 
 oemid = models.ForeignKey(oems, on_delete=models.CASCADE,)
 
 marketname=models.CharField(max_length=255)
 
 timeid=models.ForeignKey(markettime, on_delete=models.CASCADE)
 
#  contactperson=models.CharField(max_length=255)
 
#  contactemail = models.CharField(max_length=255 , unique=True)  
 Specific_Market_Guidline=models.CharField(max_length=255)
 
 Ciq = models.FileField(upload_to='marketdata', null=True)
  
 Call_test_info = models.FileField(upload_to='marketdata', null=True)
   
 Call_test_files = models.FileField(upload_to='marketdata', null=True)
    
 Site_access = models.FileField(upload_to='marketdata', null=True)
 Guidelines = models.FileField(upload_to='marketdata', null=True)
 additional_Guidelines = models.FileField(upload_to='marketdata', null=True)


 
 

#  password=models.CharField(max_length=255)
#  role = models.ForeignKey(UserList, on_delete=models.CASCADE)

class activitylists(models.Model):
    client = models.ForeignKey(clientname, on_delete=models.CASCADE)
    operator = models.ForeignKey(operator, on_delete=models.CASCADE)
    oem = models.CharField(choices=(('Nokia', 'Nokia'), ('Ericsson', 'Ericsson')), max_length=255)
    Ticket_Number = models.IntegerField()
    fa_location = models.TextField()
    site_ids = models.TextField()
    Added_Date = models.TextField()
    County = models.TextField()
    Activity = models.TextField(null=True)
    Ix_Date = models.TextField()
    G_IX_date = models.IntegerField()
    Ticket_Status = models.TextField()
    lite_site_id = models.TextField()
    three_g_site_id = models.TextField()
    Field_Installation = models.TextField()
    Alarm = models.TextField()
    Field_Integration = models.TextField()
    remote_Integration = models.TextField()
    five_g_site_id = models.TextField()
    site_name = models.TextField()
    market = models.TextField()
    address = models.TextField()
    zip_code = models.TextField()
    Added_By = models.TextField()
    IX_Status = models.TextField()
    CX_Status = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    mon_hours = models.TextField()
    tue_hours = models.TextField()
    wed_hours = models.TextField()
    thu_hours = models.TextField()
    fri_hours = models.TextField()
    sat_hours = models.TextField()
    sun_hours = models.TextField()
    key_comments = models.TextField()
    notice_needed = models.TextField()
    notice_comments = models.TextField()
    num_of_carrier = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')))
    pace = models.TextField()
    ptn = models.TextField()
    sow_type = models.TextField(choices=(('TroubleShooting ', 'TroubleShooting '), ('Maintainance', 'Maintainance '), ('Equipment change  ', 'Equipment change  ')))
    wo_cr_id = models.TextField()
    sow = models.TextField()
    ix_schedule_date = models.DateField()
    # dt = models.TextField(choices=(('DT', 'DT'), ('MT', 'MT')))
    nest = models.TextField(choices=(('Yes', 'Yes'), ('No', 'No')))
    mop_start_time = models.TimeField()
    mop_end_time = models.TimeField()
    assign_fe = models.CharField(max_length=255,choices=(
            ('Jacob Adams', 'Jacob Adams'),
            ('Neiol', 'Neiol'),
            ('Bhorjn', 'Bhorjn'),
            # Add more names as needed
        ))
    ix_date_comment = models.TextField()
    equipment_pickup = models.CharField(choices=(('yes', 'yes'), ('no', 'no')), max_length=255)
    five_g_ix_standalone = models.CharField(choices=(('yes', 'yes'), ('no', 'no')), max_length=255)
    five_g_ix_schedule_date = models.DateField()
    call_test_date = models.DateField()
    # construction_manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
    STATES = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
    ]

    market_state = models.TextField(choices=STATES)
    # assign_gc = models.ForeignKey('GroupCoordinator', on_delete=models.CASCADE)
    crew_dispatch_date = models.DateField()

    def __str__(self):
        return self.wo_cr_id
   
 
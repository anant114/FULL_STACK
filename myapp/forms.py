
# forms.py
from django import forms
from .models import marketdata
 
 
class Marketdata(forms.ModelForm):
 
    class Meta:
        model = marketdata
        fields = ['clientid', 'operatorid', 'oemid', 'marketname', 'timeid', 'Specific_Market_Guidline', 'Ciq' , 'Call_test_info' , 'Call_test_files' , 'Site_access' , 'Guidelines', 'additional_Guidelines']




from django import forms
from .models import Uploaded_file

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Uploaded_file
        fields = ['file']
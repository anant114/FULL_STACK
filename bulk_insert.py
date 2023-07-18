import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "table.settings")
django.setup()

from myapp.models import activitylists, clientname, operator  # Import your model

from random import choice

# Get all client and operator IDs
client_ids = clientname.objects.values_list('id', flat=True)
operator_ids = operator.objects.values_list('id', flat=True)

instances = []
num_entries = 500

for i in range(num_entries):
    client_id = choice(client_ids)
    operator_id = choice(operator_ids)

    client_instance = clientname.objects.get(pk=client_id)
    operator_instance = operator.objects.get(pk=operator_id)

    data_record = {
        'client': client_instance,
        'operator': operator_instance,
        'oem': 'Nokia',
        'Ticket_Number': '3045',
        'fa_location': 'California',
        'site_ids': 'UNL03357, UNL13357R',
        'Added_Date': '2023-06-01',
        'County': 'MIDDLESEX',
        'Activity': 'IX',
        'Ix_Date': '2023-06-10',
        'G_IX_date': '20230615',
        'Ticket_Status': 'Open',
        'lite_site_id': 'UNL01176',
        'three_g_site_id': 'CCL00378',
        'Field_Installation': 'FI',
        'Alarm': 'A',
        'Field_Integration': 'F',
        'remote_Integration': 'R',
        'five_g_site_id': 'CCL00778',
        'site_name': 'Qua-At&-Eri',
        'market': 'CPA',
        'address': '805 MOUNT AUBURN STREET  ,WATERTOWN ,MA',
        'zip_code': '12345',
        'Added_By': 'John Doe',
        'IX_Status': 'Completed',
        'CX_Status': 'Pending',
        'latitude': '123.456',
        'longitude': '78.901',
        'mon_hours': '8 AM - 5 PM',
        'tue_hours': '9 AM - 6 PM',
        'wed_hours': '8 AM - 5 PM',
        'thu_hours': '9 AM - 6 PM',
        'fri_hours': '8 AM - 5 PM',
        'sat_hours': 'Not working',
        'sun_hours': 'Not working',
        'key_comments': 'Some comments',
        'notice_needed': 'Yes',
        'notice_comments': 'Notice comments',
        'num_of_carrier': 2,
        'pace': 'Normal',
        'ptn': 'PTN 1',
        'sow_type': 'Option 1',
        'wo_cr_id': 'WO/CR 1',
        'sow': 'SOW 1',
        'ix_schedule_date': '2023-06-20',
        'nest': 'Yes',
        'mop_start_time': '10:00',
        'mop_end_time': '12:00',
        'ix_date_comment': 'Some comment',
        'equipment_pickup': 'Option 1',
        'five_g_ix_standalone': 'Option 2',
        'five_g_ix_schedule_date': '2023-06-25',
        'call_test_date': '2023-06-28',
        'market_state': 'State 1',
        'crew_dispatch_date': '2023-06-05',
    }
    # ...


    instance = activitylists(**data_record)
    instances.append(instance)

activitylists.objects.bulk_create(instances)
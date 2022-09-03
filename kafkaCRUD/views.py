from django.shortcuts import render

from .validations import onboarding_validation

# Create your views here.

def student_onboarding(request):
	response = {}
	if request.method == 'POST':
		v_status = True
		v_msg = ""
		v_msg, v_status = onboarding_validation(json.loads(request.body))

		if v_status:
			student = json.loads(request.body)
			f_name = student["f_name"]
			l_name = student["l_name"] or None
			roll_no = student["roll_no"]
			date_joining = datetime.strptime(student["date_joining"], '%Y-%m-%d')
			created_by = student["created_by"]
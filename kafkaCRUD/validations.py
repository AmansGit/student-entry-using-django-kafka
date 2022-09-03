
def onboarding_validation(request_json):
	status = True
	msg = ""
	if "f_name" not in request_json or not request_json["f_name"]:
		msg += "First name is missing\n"
		status = False
	if "roll_no" not in request_json or not request_json["roll_no"]:
		msg += "Roll no is missing\n"
		status = False
	if "date_joining" not in request_json or not request_json["date_joining"]:
		msg += "Date of joining not available\n"
		status = False
	if "created_by" not in request_json or not request_json["created_by"]:
		msg += "Please provide the creator name"
		status = False

	return msg, status
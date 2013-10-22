from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

def home(request):
	if request.META['REQUEST_METHOD'] == 'POST':
		user_month = request.POST['month']
		user_day = request.POST['day']
		user_year = request.POST['year']

		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)

		if month and day and year:
			return HttpResponseRedirect(reverse('result'))
		
		month_error = day_error = year_error = None
		if not month:
			month_error = "Invalid Month!"
		if not day:
			day_error = "Invalid Day!"
		if not year:
			year_error = "Invalid year!"
		return render(request,"blog/index.html", {
			'month' : user_month,
			'day' : user_day,
			'year' : user_year,
			'month_error' : month_error,
			'day_error' : day_error,
			'year_error' : year_error,
			})

	return render(request, "blog/index.html")

def result(request):
	return HttpResponse("It worked")

def testHandler(request):
	if request.META['REQUEST_METHOD'] == 'POST':
		response = HttpResponse(str(request.REQUEST))
		response['Content-Type'] = 'text/plain; charset=utf-8'
		return response
	return render(request,"blog/form.html")

months = [	'January',
			'February',
			'March',
			'April',
			'May',
			'June',
			'July',
			'August',
			'September',
			'October',
			'November',
			'December' ]

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day >= 1 and day <= 31:
			return day

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year > 1900 and year < 2020:
			return year

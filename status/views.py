from urllib.request import urlcleanup
from django.shortcuts import render
import requests
import validators
from validators import ValidationFailure




http_code = {
	100: "Continue",101: "Switching Protocols",103: "Checkpoint",
	200: "OK",201: "Created",202: "Accepted",203: "Non-Authoritative Information",204: "No Content",205: "Reset Content",206: "Partial Content",
	300: "Multiple Choices",301: "The Requested Page has moved permanently to a new URL",302: "The Requested Page has moved temporarily to a new URL",303: "The Requested Page can be found under a different URL",304: "Not Modified",306: "Switch Proxy: No longer used",
	400: "Bad Request",401: "Unauthorized",402: "Payment required",403: "Forbidden",404: "Not Found",408: "Request Timeout",
	500: "Internal Server Error",501: "Not Implemented",502: "Bad Gateway",503: "Service Unavailable",504: "Gateway Timeout"
}


def home(request):
	return render(request, 'index.html')

def status(request):
	url=request.POST['url']
	if url==" ":
		return render(request,"cross.html",{'message':"Enter Url."})
	else:
		valid=validators.url(url)
	if valid==True:
		try:
			source=requests.get(url)
		except:
			return render(request,"cross.html",{'message':"This url is invalid."})
		for key in http_code.keys():
				if source.status_code==key :
					if key==100 or key==200 or key==201 or key==202:
						return render(request,"tick.html",{'message':http_code[key]})
	elif valid != True:
		if url[:4] != "http":
			url = "https://"+url
			url = url+".com"
			url = url.split ('.')
			print (url)
			try:
				source=requests.get(url)
			except:
				return render(request,"cross.html",{'message':"This url is invalid."})
			for key in http_code.keys():
				if source.status_code==key :
					if key==100 or key==200 or key==201 or key==202:
						return render(request,"tick.html",{'message':http_code[key]})



	else:
		return render(request,"cross.html",{'message':http_code[key]})
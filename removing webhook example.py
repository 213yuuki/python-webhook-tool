import requests ## requests lib is needed to send message

webhook = "your webhook" ## define webhook link

delete = requests.request("DELETE", webhook) ## sendind delete request to webhook link

print(delete.status_code) ## printing status code received upon sending delete request
print(delete.ok) ## you can also use this one, it allows you to save some time by not writing unnecessary if statements
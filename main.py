import requests
import json

groups = [
    ['A',['+201144560665']],
    ['B',['+201144560665']], 
    ['C' ,['+201144560665']]
]

messages = [
    ['3adad0ca-01b8-48ef-8b6e-32ea89fd593c@2',"Done"],
    ['cad63085-242d-4e14-9ff7-fb3b4855e1f7@2',"Pending"], 
    ['d6be717b-3e33-4390-8082-042e33031508@2',"Failed"]
]
    

def createAgroup(group_name , members_list):
    url = "https://api2.kaiza.la/v1/groups"

    data = {
        'name': group_name,
        'welcomeMessage': "Welcome to group created programmatically via Postman", 
        'members': members_list,
        'groupType': "Group", 
        'ShortDescriptionString': "Short description", 
        'LongDescriptionString': "Long description"
    }

    data = json.dumps(data)

    headers = {
        'accessToken': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46bWljcm9zb2Z0OmNyZWRlbnRpYWxzIjoie1wicGhvbmVOdW1iZXJcIjpcIisyMDEwOTI4MDY3NjlcIixcImNJZFwiOlwiXCIsXCJ0ZXN0U2VuZGVyXCI6XCJmYWxzZVwiLFwiYXBwTmFtZVwiOlwiY29tLm1pY3Jvc29mdC5tb2JpbGUua2FpemFsYWFwaVwiLFwiYXBwbGljYXRpb25JZFwiOlwiZTBmNzBmZTctYjVjMS00ZDBjLTg4MzMtZjZlYzZjMzFjNzVlQDJcIixcInBlcm1pc3Npb25zXCI6XCIyLjMwOjMuMzA6NC4xMDo2LjIyOjUuNDo5LjI6MTUuMzA6MTQuMzA6MTkuMzA6MjQuMzBcIixcImFwcGxpY2F0aW9uVHlwZVwiOjMsXCJkYXRhXCI6XCJ7XFxcIkdyb3VwSWRcXFwiOlxcXCJkYmE5ZmU5Ni01OThlLTQ1OWQtYjgzYS02YTg1YWNmMzBhY2NAMlxcXCIsXFxcIkFwcE5hbWVcXFwiOlxcXCJtb2hhbWVkXFxcIixcXFwiVXNlclRlbmFudElkc1xcXCI6XFxcIltcXFxcXFxcIjMxYzU4ZDA4LTU0OWMtNDZlZi1iMTFlLTQzOWJmZDcyNmIwOEAyXFxcXFxcXCJdXFxcIn1cIn0iLCJ1aWQiOiJNb2JpbGVBcHBzU2VydmljZToyNTQyYjkzNS1kNzE5LTRmMWEtYTMzMC03MmFhMmNiMWY5ZjVAMiIsInZlciI6IjIiLCJuYmYiOjE1NjkwNjM1MjAsImV4cCI6MTU2OTE0OTkyMCwiaWF0IjoxNTY5MDYzNTIwLCJpc3MiOiJ1cm46bWljcm9zb2Z0OndpbmRvd3MtYXp1cmU6enVtbyIsImF1ZCI6InVybjptaWNyb3NvZnQ6d2luZG93cy1henVyZTp6dW1vIn0.TQRJS7Uiwi3BTRpeWBLj0V67hRsBwbkcvkwSTOsyu_w",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c3019259-7c2e-4283-bdfd-ab0b38deca16"
        }

    response = requests.post(url, data=data, headers=headers)
    print("-------------------------------")
    print(response.text)
    print("-------------------------------")


def send_message_to_groups(group_id , message):

    url = "https://api2.kaiza.la/v1/groups/{}/messages".format(group_id)

    payload = {
        'message': message
    }
    
    data = json.dumps(payload)

    headers = {
        'accessToken': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46bWljcm9zb2Z0OmNyZWRlbnRpYWxzIjoie1wicGhvbmVOdW1iZXJcIjpcIisyMDEwOTI4MDY3NjlcIixcImNJZFwiOlwiXCIsXCJ0ZXN0U2VuZGVyXCI6XCJmYWxzZVwiLFwiYXBwTmFtZVwiOlwiY29tLm1pY3Jvc29mdC5tb2JpbGUua2FpemFsYWFwaVwiLFwiYXBwbGljYXRpb25JZFwiOlwiZTBmNzBmZTctYjVjMS00ZDBjLTg4MzMtZjZlYzZjMzFjNzVlQDJcIixcInBlcm1pc3Npb25zXCI6XCIyLjMwOjMuMzA6NC4xMDo2LjIyOjUuNDo5LjI6MTUuMzA6MTQuMzA6MTkuMzA6MjQuMzBcIixcImFwcGxpY2F0aW9uVHlwZVwiOjMsXCJkYXRhXCI6XCJ7XFxcIkdyb3VwSWRcXFwiOlxcXCJkYmE5ZmU5Ni01OThlLTQ1OWQtYjgzYS02YTg1YWNmMzBhY2NAMlxcXCIsXFxcIkFwcE5hbWVcXFwiOlxcXCJtb2hhbWVkXFxcIixcXFwiVXNlclRlbmFudElkc1xcXCI6XFxcIltcXFxcXFxcIjMxYzU4ZDA4LTU0OWMtNDZlZi1iMTFlLTQzOWJmZDcyNmIwOEAyXFxcXFxcXCJdXFxcIn1cIn0iLCJ1aWQiOiJNb2JpbGVBcHBzU2VydmljZToyNTQyYjkzNS1kNzE5LTRmMWEtYTMzMC03MmFhMmNiMWY5ZjVAMiIsInZlciI6IjIiLCJuYmYiOjE1NjkwNjM1MjAsImV4cCI6MTU2OTE0OTkyMCwiaWF0IjoxNTY5MDYzNTIwLCJpc3MiOiJ1cm46bWljcm9zb2Z0OndpbmRvd3MtYXp1cmU6enVtbyIsImF1ZCI6InVybjptaWNyb3NvZnQ6d2luZG93cy1henVyZTp6dW1vIn0.TQRJS7Uiwi3BTRpeWBLj0V67hRsBwbkcvkwSTOsyu_w",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "271d3054-3194-4442-bf7a-ee66ad755a68"
    }

    response = requests.post(url, data=data, headers=headers)
    print('--------------------------------------')
    print(response.text)
    print('--------------------------------------')


for msg in messages:
    send_message_to_groups(msg[0] , msg[1])

print('Done')


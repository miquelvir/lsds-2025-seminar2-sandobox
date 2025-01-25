import requests

res = requests.get("http://localhost:8000/datanodes")
res_body = res.json()
print(res_body)


"""datanodes = res_body.get('datanodes')
for datanode in datanodes:
    print(datanode)"""

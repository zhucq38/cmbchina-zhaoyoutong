#coding:utf-8
import os 
import sys
import requests 

# 招商银行 招邮通
URL = "http://47.104.63.107:8080/fl/login"
#user = "test"
#password = "pass"
data = {"userName":"test","password":"Z5/f9T0aUupM0bOhVdXjcVPDxM3o0VSmFonMQVgmdZXwd8kCVhkxSUnDfVQlxf3D4Pgo7ed5bB5MJzJ6Muu+64EgkqGo6aB2R62Yg3f4bQLElOqBd2O+A/+QjmCNuRMOI/ZNdKy9wETQO42Qb0EXAWsuLDItQpXMkQSWUt0A7LM=","companyID":"CUSTOMER"}
req = requests.post(url,data=data,timeout=10)
if "sendmsg" in req.content:
    print("Success!")
else:
    print("Fail!")

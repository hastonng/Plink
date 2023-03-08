import requests
import datetime

class DD_Automation:
    """
    This class is an automation for P-Link system by dynamically creating tasks on the "Completed" section for
    Record Keeping.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = None
        self.current_time = datetime.datetime.utcnow().isoformat() + "Z"

        dueDate = datetime.datetime.now() + datetime.timedelta(hours=1)
        self.dueDate = dueDate.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        # self.dueDate = datetime.datetime.strptime(dueDate,"%Y-%m-%dT%H:%M:%S.%fZ")

    def w3_login(self):
        """
         Login into Huawei W3 Domain for authentication verification
        :param username: String
        :param password: String
        :return: requests.Session
        """
        print('\n')
        print('Login to W3 Domain as: ' + self.username)
        print('\n')
        session = requests.session()
        firstHeader = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en;q=0.6',
            'Connection': 'keep-alive',
            'Host': 'login.huawei.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        firstURL = 'https://login.huawei.com/login/'
        resultA = session.get(firstURL, headers=firstHeader)
        header1 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Host': 'login.huawei.com',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://login.huawei.com',
            'Referer': 'https://login.huawei.com/login/?redirect=https://cpq.huawei.com/isales/cpq/index/#/',
        }
        login_data = {
            'actionFlag': 'loginAuthenticate',
            'lang': 'en',
            'loginMethod': 'login',
            'loginPageType': 'mix',
            'redirect': None,
            'redirect_local': None,
            'redirect_modify': None,
            'scanedFinPrint': None,
            'uid': self.username,
            'password': self.password,
            'verifyCode': '2345'
        }
        URL1 = 'https://login.huawei.com/login/login.do'
        resultB = session.post(URL1, headers=header1, data=login_data, verify=False)

        self.session = session


    def create_task(self, Title, ToolID, Version, Small_Note):
        """
        Create task on Plink Completed
        :return:
        """

        header = {
            "Host": 'tb.project.admin.huawei.com',
            "Origin": 'http://tb.project.admin.huawei.com',
            "Referer": 'http://tb.project.admin.huawei.com/project/5fd89a9f98c68c0013b6286e/tasks/scrum/61f94177812252022d5abbf0',
            "Cookie": "HW3MS_think_language=zh-cn; duec_csrf_token=GWC340366FB8DEFFEA3954C4911855BCEBF03D5DB094B5F24AB308C17C488FB478; lang=en; JALOR5_LANG=en_US; projectNumber=5521220; teambition_lang=en; hwsso_am=77-22-F7-0E-84-9F-31-CD; login_failLoginCount=0; login_recycle=1#1661247608590; hwssot=42-63-67-FB-5E-4C-63-1C-F3-18-EA-20-E7-7A-D7-49; hwssot3=30131204553422; hwsso_login=V002YWRqb2Xzqlb0BmBY_alCSBDJl4KbDRtn8zgBpAFR2vRCC2Nc8jRORonp5t260Qe6E8KfMiKWK19BhigSoYtJZ4YC9KhrJyb7AXvldbxDoFxO2ygtgVDfd62AqX7Oq2Kmfc05Vk59JwHWwCO_bMkxnqbt0vsJ87seIpj2RrwAuPsgToGhnKKLSoVCkyjMfsOEIvT6Zo3iClUo5ri_aRRtcJaNV2hk8bFYseBxoyQ8_alvPpSgZlgD6pfZk4zoax_boous3rxd5DLhP3tOj7ompfN1bXiy_bVQwF8hhC_ammSoU2Es24UXC_a3wNp0hdsDPrd7wXdnqYt_ajPRrH6SsxyqkPEUKog_c_c; login_logFlag=in; suid=71-DC-30-46-39-C3-EE-F8-21-C1-D8-0F-2C-6F-31-03; w3Token=71-DC-30-46-39-C3-EE-F8-CB-50-87-75-14-B9-F8-84-8D-D2-F1-BF-DC-7C-EA-E1-03-C5-E3-83-66-A8-5E-F3; login_uid=71-DC-30-46-39-C3-EE-F8-21-C1-D8-0F-2C-6F-31-03; login_sip=8F-07-CA-78-61-23-F9-A7-6C-BB-66-2A-DA-F6-46-29-31-DD-35-52-A5-7C-E0-59; login_sid=6F-FC-83-D1-E8-91-DB-96-8F-44-D4-32-CA-27-EB-C2-2E-6A-BC-A5-36-DF-F2-12-66-A7-CC-0D-A4-67-2B-F9-C3-B9-24-1D-49-35-BC-B0; LtpaToken=xsOHrCTLIAlUVP2XBzryGj7RmkqVXxsnzNMFLll+GTgEu0OXWZRCnyBjIcA4T+1i3i4V0V8ShE0RiGddMiVmySkODyYtQWe2+NYrSSuI+4DkReRNRIXPvn8VxZsF+Qx9bSr3D19ZWQTQH9QkopCQh5iiM6Ici+5byVlDTOsjf8jbJRh5vzWQPSjz/wgp4RpmCbqdVWyoOjJjKD49Wif+kZ3puHqPPgu3Us8ME+qBUpYZRIXTPFe1TRz33RlgncMeoG276NFxjQVWeMALjjeeYBZlmh9RUxBUTTe9GcisZcrUrp8SVNzeZS095Yz2fd9aSXVTxqVjobHb0xTc55lf8JnTyLeLq/DN9QDu9loLpIMjheZJNHiBPwFC4GsAXlGr; _sid_=""; teambition_private_sid=eyJhdXRoVXBkYXRlZCI6MCwiaHdVc2VyIjp7ImVtYWlsIjoibmcud2FuLmhhc3RvbkBodWF3ZWkuY29tIiwicmVmSWQiOiJud3gxMTE2Njk2IiwidWlkIjoibnd4MTExNjY5NiIsIm5hbWUiOiJOZyBXYW4gSGFzdG9uIiwidXNlcm5hbWUiOiJud3gxMTE2Njk2IiwiYXZhdGFyVXJsIjoiaHR0cDovL3czLmh1YXdlaS5jb20vdzNsYWIvcmVzdC95ZWxsb3dwYWdlL2ZhY2UvV1gxMTE2Njk2LzEyMCIsImVtcGxveWVlTnVtIjoibldYMTExNjY5NiIsImxvY2F0aW9uIjoi6KW/5qyn6aG555uu566h55CG5Yqe5YWs5a6kIiwidG9rZW4iOnsiaHdzc29fYW0iOiI3Ny0yMi1GNy0wRS04NC05Ri0zMS1DRCIsImh3c3NvX2xvZ2luIjoiVjAwMllXUnFiMlh6cWxiMEJtQllfYWxDU0JESmw0S2JEUnRuOHpnQnBBRlIydlJDQzJOYzhqUk9Sb25wNXQyNjBRZTZFOEtmTWlLV0sxOUJoaWdTb1l0Slo0WUM5S2hySnliN0FYdmxkYnhEb0Z4TzJ5Z3RnVkRmZDYyQXFYN09xMkttZmMwNVZrNTlKd0hXd0NPX2JNa3hucWJ0MHZzSjg3c2VJcGoyUnJ3QXVQc2dUb0dobktLTFNvVkNreWpNZnNPRUl2VDZabzNpQ2xVbzVyaV9hUlJ0Y0phTlYyaGs4YkZZc2VCeG95UThfYWx2UHBTZ1psZ0Q2cGZaazR6b2F4X2Jvb3VzM3J4ZDVETGhQM3RPajdvbXBmTjFiWGl5X2JWUXdGOGhoQ19hbW1Tb1UyRXMyNFVYQ19hM3dOcDBoZHNEUHJkN3dYZG5xWXRfYWpQUnJINlNzeHlxa1BFVUtvZ19jX2MiLCJod3Nzb3QiOiI0Mi02My02Ny1GQi01RS00Qy02My0xQy1GMy0xOC1FQS0yMC1FNy03QS1ENy00OSIsImh3c3NvdDMiOiIzMDEzMTIwNDU1MzQyMiIsImxvZ2luX2xvZ0ZsYWciOiJpbiIsImxvZ2luX3NpZCI6IjZGLUZDLTgzLUQxLUU4LTkxLURCLTk2LThGLTQ0LUQ0LTMyLUNBLTI3LUVCLUMyLTJFLTZBLUJDLUE1LTM2LURGLUYyLTEyLTY2LUE3LUNDLTBELUE0LTY3LTJCLUY5LUMzLUI5LTI0LTFELTQ5LTM1LUJDLUIwIiwibG9naW5fc2lwIjoiOEYtMDctQ0EtNzgtNjEtMjMtRjktQTctNkMtQkItNjYtMkEtREEtRjYtNDYtMjktMzEtREQtMzUtNTItQTUtN0MtRTAtNTkiLCJsb2dpbl91aWQiOiI3MS1EQy0zMC00Ni0zOS1DMy1FRS1GOC0yMS1DMS1EOC0wRi0yQy02Ri0zMS0wMyIsIkx0cGFUb2tlbiI6InhzT0hyQ1RMSUFsVVZQMlhCenJ5R2o3Um1rcVZYeHNuek5NRkxsbCtHVGdFdTBPWFdaUkNueUJqSWNBNFQrMWkzaTRWMFY4U2hFMFJpR2RkTWlWbXlTa09EeVl0UVdlMitOWXJTU3VJKzREa1JlUk5SSVhQdm44Vnhac0YrUXg5YlNyM0QxOVpXUVRRSDlRa29wQ1FoNWlpTTZJY2krNWJ5VmxEVE9zamY4amJKUmg1dnpXUVBTanovd2dwNFJwbUNicWRWV3lvT2pKaktENDlXaWYra1ozcHVIcVBQZ3UzVXM4TUUrcUJVcFlaUklYVFBGZTFUUnozM1JsZ25jTWVvRzI3Nk5GeGpRVldlTUFMamplZVlCWmxtaDlSVXhCVVRUZTlHY2lzWmNyVXJwOFNWTnplWlMwOTVZejJmZDlhU1hWVHhxVmpvYkhiMHhUYzU1bGY4Sm5UeUxlTHEvRE45UUR1OWxvTHBJTWpoZVpKTkhpQlB3RkM0R3NBWGxHciIsInczVG9rZW4iOiI3MS1EQy0zMC00Ni0zOS1DMy1FRS1GOC1DQi01MC04Ny03NS0xNC1COS1GOC04NC04RC1EMi1GMS1CRi1EQy03Qy1FQS1FMS0wMy1DNS1FMy04My02Ni1BOC01RS1GMyJ9fSwibG9naW5Gcm9tIjoiIiwidWlkIjoiNjE5MjJhMTQxNTIyZTY3Yjk1M2VjMjdiIiwidXNlciI6eyJfaWQiOiI2MTkyMmExNDE1MjJlNjdiOTUzZWMyN2IiLCJuYW1lIjoiTmcgV2FuIEhhc3RvbiIsImVtYWlsIjoibmcud2FuLmhhc3RvbkBodWF3ZWkuY29tIiwiYXZhdGFyVXJsIjoiaHR0cDovL3czLmh1YXdlaS5jb20vdzNsYWIvcmVzdC95ZWxsb3dwYWdlL2ZhY2UvV1gxMTE2Njk2LzEyMCIsInJlZ2lvbiI6ImNuIiwibGFuZyI6IiIsImlzUm9ib3QiOmZhbHNlLCJvcGVuSWQiOiJody13ZWxpbms6bnd4MTExNjY5NiIsInBob25lRm9yTG9naW4iOiIifX0=; teambition_private_sid.sig=nVpyxo5DJFFBAHZPEk7-7RSEbEw"
        }

        body = {
            "_projectId": "5fd89a9f98c68c0013b6286e",
            "_organizationId": "",
            "_tasklistId": "61f94177812252022d5abbf0",
            "_stageId": "61f94177812252022d5abbf5",
            "content": Title,
            "_executorId": "61922a141522e67b953ec27b",
            "isDone": True,
            "startDate": self.current_time,
            "dueDate": self.dueDate,
            "priority": 0,
            "progress": 0,
            "recurrence": None,
            "reminder": {
                "rules": [],
                "members": []
            },
            "involveMembers": [
                "61922a141522e67b953ec27b"
            ],
            "involvers": [
                {
                    "name": "Ng Wan Haston",
                    "title": "",
                    "phone": "",
                    "location": "",
                    "website": "",
                    "birthday": None,
                    "email": "ng.wan.haston@huawei.com",
                    "avatar": "",
                    "emails": [
                        {
                            "state": 0,
                            "email": "ng.wan.haston@huawei.com",
                            "_id": "61922a14c839611c322c5d3c",
                            "id": "61922a14c839611c322c5d3c"
                        }
                    ],
                    "badge": 0,
                    "isGhost": False,
                    "_id": "61922a141522e67b953ec27b",
                    "avatarUrl": "http://w3.huawei.com/w3lab/rest/yellowpage/face/WX1116696/120",
                    "created": "2021-11-17T15:28:29.412Z",
                    "isActive": False,
                    "pinyin": "ng wan haston",
                    "py": "nwh",
                    "isNew": False,
                    "plan": {
                        "status": "paid",
                        "expired": "2023-08-31T15:46:08.705Z",
                        "payType": "org",
                        "paidCount": 1,
                        "membersCount": 1000000,
                        "trialType": "org",
                        "trialExpired": "2021-08-31T15:46:08.705Z",
                        "days": None,
                        "objectType": "user",
                        "_objectId": "61922a141522e67b953ec27b",
                        "isExpired": False,
                        "isTrialExpired": True
                    },
                    "notification": {
                        "comment": {
                            "mobile": True,
                            "email": False
                        },
                        "newpost": {
                            "mobile": True,
                            "email": False
                        },
                        "newtask": {
                            "mobile": True,
                            "email": False
                        },
                        "newwork": {
                            "mobile": True,
                            "email": False
                        },
                        "newevent": {
                            "mobile": True,
                            "email": False
                        },
                        "involve": {
                            "mobile": True,
                            "email": False
                        },
                        "update": {
                            "mobile": True,
                            "email": False
                        },
                        "daily": {
                            "email": True
                        },
                        "monthly": {
                            "email": True
                        }
                    },
                    "region": "cn",
                    "lastEntered": {
                        "web": "2022-08-31T15:46:08.699Z",
                        "third": "2022-02-07T14:13:22.584Z"
                    },
                    "fromTitle": "",
                    "_invitorId": "",
                    "language": "en",
                    "aliens": [],
                    "strikerAuth": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI2MTkyMmExNDE1MjJlNjdiOTUzZWMyN2IiLCJleHAiOjE2NjIwNDcxNjgsInN0b3JhZ2UiOiJzdHJpa2VyLWh6In0.thM4sSbQNECp6mcZJO0HnQBjAFjF400UQHCaXVnWzCk",
                    "phoneForLogin": "",
                    "enabledGoogleTwoFactor": False,
                    "snapperToken": "",
                    "tcmToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJRCI6IjVkODYxNzgwOWU0Zjk0NGEzM2QxYzI4ZSIsImV4cCI6MTY2MjM5Mjc2OCwiaWF0IjoxNjYxOTYwNzY4LCJqdGkiOiI2MzBmODI0MDYwNDI4ZjUzNDk5N2ViZDEiLCJzb3VyY2UiOiIiLCJ1c2VySWQiOiI2MTkyMmExNDE1MjJlNjdiOTUzZWMyN2IifQ.djiGhwh_pGX56onF_lUrkG7wE7JAHxl9XgwNcbQNh5o",
                    "crossNotify": {
                        "badge": 0
                    },
                    "openId": "hw-welink:nwx1116696",
                    "normal": 0,
                    "ated": 0,
                    "later": 0,
                    "private": 0,
                    "hasNormal": False,
                    "hasAted": False,
                    "hasLater": False,
                    "hasPrivate": False,
                    "inbox": 0,
                    "calLink": "webcal://tb.project.admin.huawei.com/api/events/2e48b76a407db0fa4eb0d16eb86b869c2b40b5cc1b61303164b6816e75e21714.ics",
                    "taskCalLink": "webcal://tb.project.admin.huawei.com/api/tasks/2e48b76a407db0fa4eb0d16eb86b869c2b40b5cc1b61303164b6816e75e21714.ics",
                    "joinedProjectsCount": 26,
                    "_emailId": "61922a14c839611c322c5d3c"
                }
            ],
            "visible": "members",
            "_scenariofieldconfigId": "5fd89a9f446473eadd8ea4aa",
            "tagIds": [],
            "note": Small_Note,
            "customfields": [
                {
                    "value": [
                        {
                            "title": self.current_time
                        }
                    ],
                    "_customfieldId": "6308d690019f571fef1062ca",
                    "type": "date"
                },
                {
                    "value": [
                        {
                            "title": ToolID
                        }
                    ],
                    "_customfieldId": "5fd8ef70446473eadd8ebc99",
                    "type": "text"
                },
                {
                    "value": [
                        {
                            "title": Version
                        }
                    ],
                    "_customfieldId": "5f22337a6d3ebf00017a810a",
                    "type": "text"
                },
                {
                    "value": [
                        {
                            "_id": "62ff4da4d67c051387943e24",
                            "title": "General Maintenance"
                        }
                    ],
                    "_customfieldId": "62ff4da4d67c051387943e24",
                    "type": "multipleChoice"
                }
            ],
            "storyPoint": None,
            "workTime": {
                "totalTime": 0,
                "usedTime": 0,
                "unit": ""
            }
        }

        URL = 'http://tb.project.admin.huawei.com/api/v2/tasks'
        result = self.session.post(URL, headers=header, json=body, verify=False)

        print(result.text)
        print('\n')
        print(result)


if __name__ == '__main__':
    pass
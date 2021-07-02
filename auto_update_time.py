import requests
from bs4 import BeautifulSoup
import re


def make_target():
    target = {
        #################################################################### Card ###############################################################################################################
        "KBpay": {
            "Android": "https://play.google.com/store/apps/details?id=com.kbcard.cxh.appcard&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/kb-pay/id695436326"
        },
        "HyundaiCard": {
            "Android": "https://play.google.com/store/apps/details?id=com.hyundaicard.appcard&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/%ED%98%84%EB%8C%80%EC%B9%B4%EB%93%9C/id702653088"
        },
        "Samsung": {
            "Android": "https://play.google.com/store/apps/details?id=kr.co.samsungcard.mpocket&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/%EC%82%BC%EC%84%B1%EC%B9%B4%EB%93%9C/id535125356"
        },
        "NHallonePay": {
            "Android": "https://play.google.com/store/apps/details?id=nh.smart.nhallonepay&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/%EC%98%AC%EC%9B%90%ED%8E%98%EC%9D%B4-nh%EC%95%B1%EC%B9%B4%EB%93%9C/id1177889176"
        },
        "SHCard": {
            "Android": "https://play.google.com/store/apps/details?id=com.shcard.smartpay&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/%EC%8B%A0%ED%95%9C%ED%8E%98%EC%9D%B4%ED%8C%90/id572462317"
        },
        "BCCard": {
            "Android": "https://play.google.com/store/apps/details?id=kvp.jjy.MispAndroid320&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/isp-%ED%8E%98%EC%9D%B4%EB%B6%81/id369125087"
        },
        "LcacApp": {
            "Android": "https://play.google.com/store/apps/details?id=com.lcacApp&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/%EB%A1%AF%EB%8D%B0%EC%B9%B4%EB%93%9C-%EC%95%B1%EC%B9%B4%EB%93%9C/id688047200"
        },
        "HanaskCard": {
            "Android": "https://play.google.com/store/apps/details?id=com.hanaskcard.paycla&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90-%ED%95%98%EB%82%98%EC%B9%B4%EB%93%9C-%EC%9B%90%ED%81%90%ED%8E%98%EC%9D%B4-%EC%95%B1%EC%B9%B4%EB%93%9C/id847268987"
        },
        ################################################################# PASS ##############################################################################################################
        "SKT": {
            "Android": "https://play.google.com/store/apps/details?id=com.sktelecom.tauth&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/pass-by-skt/id1141258007"
        },
        "KT": {
            "Android": "https://play.google.com/store/apps/details?id=com.kt.ktauth&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/pass-by-kt/id1134371550"
        },
        "LGU": {
            "Android": "https://play.google.com/store/apps/details?id=com.lguplus.smartotp&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/pass-by-u/id1147394645"
        },
        ################################################################# 아이핀 ##############################################################################################################
        "SCI": {
            "Android": "https://play.google.com/store/apps/details?id=com.sci.siren24.ipin&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/siren24-%EC%95%84%EC%9D%B4%ED%95%80/id960609828"
        },
        "KCB": {
            "Android": "https://play.google.com/store/apps/details?id=com.koreacb.kipinapp&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/kcb%EC%95%84%EC%9D%B4%ED%95%80-%EC%95%84%EC%9D%B4%ED%95%80-my-pin/id907376868"
        },
        "Nice": {
            "Android": "https://play.google.com/store/apps/details?id=com.niceid.nicemypin&hl=ko&gl=US",
            "iOS": "https://apps.apple.com/kr/app/%EB%82%98%EC%9D%B4%EC%8A%A4%EC%95%84%EC%9D%B4%ED%95%80-%EB%A7%88%EC%9D%B4%ED%95%80-mypin/id898176302"
        },
    }

    return target


def getKey(target):
    key_list = target.keys()
    key_list = (list(key_list))
    return key_list


def getURL(Device_Key):
    target = make_target()
    key_list = getKey(target)
    url_list = []

    for Key in key_list:
        url_list.append(target[Key][Device_Key])

    return url_list


def iOS_Update_Day_Pattern_Create():
    datetime = r'[^datetime="][0-9]*-[0-9]*-[0-9]*'
    pattern = re.compile(datetime)
    return pattern


def iOS_App_version_Pattern_create():
    appVer = r'version">.*?<'
    pattern = re.compile(appVer)
    return pattern


def Android_Update_Day_Pattern_Create():
    datetime = r'[^업데이트 날짜].*?년.*?월.*?일'
    pattern = re.compile(datetime)
    return pattern


def Android_App_version_Pattern_create():
    appVer = r'[버전].*?[필요]'
    pattern = re.compile(appVer)
    return pattern


def dectResult(Key_list, Update_list):
    dectResult = {}

    for index in range(len(Key_list)):
        dectResult[Key_list[index]] = Update_list[index]

    return dectResult


def data_format(Update_Day):
    time_list = Update_Day.split("-")
    time_list[0] = time_list[0].zfill(4)
    time_list[1] = time_list[1].zfill(2)
    time_list[2] = time_list[2].zfill(2)
    return '-'.join(time_list)


def getiOSRequest(Key_list):
    Device_Key = "iOS"
    URL_list = getURL(Device_Key)
    Update_list = []

    for URL in URL_list:

        getRequest = requests.get(URL)
        SoupRequest = BeautifulSoup(getRequest.text, 'html.parser').find(
            'div', class_='whats-new__content')

        Update_Day = iOS_Update_Day_Pattern_Create().search(str(SoupRequest)).group(0)
        AppVer = iOS_App_version_Pattern_create().search(
            str(SoupRequest)).group(0).split(" ")[1][:-1]

        Update_list.append([Update_Day, AppVer])

    return dectResult(Key_list, Update_list)


def getAndroidRequest(Key_list):
    Device_Key = "Android"
    URL_list = getURL(Device_Key)
    Update_list = []

    for URL in URL_list:

        getRequest = requests.get(URL)
        SoupRequest = BeautifulSoup(getRequest.text, 'html.parser').find(
            'div', class_='IxB2fe').text

        Update_Day = data_format(Android_Update_Day_Pattern_Create().search(
            str(SoupRequest)).group(0).replace("년 ", "-").replace("월 ", "-")[:-1])
        AppVer = Android_App_version_Pattern_create().search(
            str(SoupRequest)).group(0)[2:-1]

        Update_list.append([Update_Day, AppVer])

    return dectResult(Key_list, Update_list)


print("iOS")
print(getiOSRequest(getKey(make_target())))
print()
print("Android")
print(getAndroidRequest(getKey(make_target())))

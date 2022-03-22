from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
brave = "dw0cpqM3oBb_5FwRa4B2Ey:APA91bEDks0uEBJy8HlrIV6bbqjcFU7_pm3mZohahQ3YOckYqn9QAe1ukZFYINmyvunvPZqEEvLlIHoKt8preOfbs4LDXIxUhj8BTP2k-SP3FEZ_rz6WFDtawM2HxUNCiUAtVDyqGvjY"

def send(request):
    resgistration  = ["dNH_Lqf9yNL8TtffKR8puR:APA91bELuP5puSrbnQkbdOCPCSCJ8LV0wI5RNI29NoHuBi7e71TPd5HFSmaaN8byCweB67LdpQprJ3u15dgzT6bu3M6HmGYmeMe_dIv0ynVlb9h19--jTPkjaTgYmvEhcoIC0CQDJ93f",
                        "dNH_Lqf9yNL8TtffKR8puR:APA91bELuP5puSrbnQkbdOCPCSCJ8LV0wI5RNI29NoHuBi7e71TPd5HFSmaaN8byCweB67LdpQprJ3u15dgzT6bu3M6HmGYmeMe_dIv0ynVlb9h19--jTPkjaTgYmvEhcoIC0CQDJ93f",
                        brave,
                        "dw0cpqM3oBb_5FwRa4B2Ey:APA91bEsRs2O4aEK1eIikyv8tONoHtA_VGjFS4uh-gBTys04BwrwmtSMLr-yAjE58U1-LNCNYkCNbl4EhBg_WMYyXx8h892-yJGKIn-7cV0n3QoJ3sV1lQCmHiuI7p0UTHYrac81klmH"]
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")

def index(request):
    return render(request, 'index.html')

def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAA00x63V4:APA91bE-seBFbPXItSOm4VdNHMykGSvfJJi2p5FCwEJ0YRrAlrLYYKiJfxEG1kUyysXDP62wEQkCXqpft1tGGNld6OCtd-Z0ku0nIy2KENhdXilGbKZE217Pfi8kE5A2XVb3jBncm5As"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())
    print(result.status_code)
    # print(result.error)

def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyAeqvgSTqIrhKneOHWAX-kZPsClyhO5pMw",' \
         '        authDomain: "test-push-notification-65372.firebaseapp.com",' \
         '        projectId: "test-push-notification-6537",' \
         '        storageBucket: "test-push-notification-65372.appspot.com",' \
         '        messagingSenderId: "907521219934",' \
         '        appId: "1:907521219934:web:b12bd9712e371f79c903cf",' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")

# def test(request):
#     fcm_api = "AAAA00x63V4:APA91bE-seBFbPXItSOm4VdNHMykGSvfJJi2p5FCwEJ0YRrAlrLYYKiJfxEG1kUyysXDP62wEQkCXqpft1tGGNld6OCtd-Z0ku0nIy2KENhdXilGbKZE217Pfi8kE5A2XVb3jBncm5As"
#     headers = {
#             "Content-Type":"application/json",
#             "Authorization": 'key='+fcm_api
#             }
#     data = {
#         "message": {
#             "notification": {
#             "title": "Background Message Title",
#             "body": "Background message body"
#             },
#             "webpush": {
#             "fcm_options": {
#                 "link": "http://127.0.0.1:8000/test/"
#             }
#             }
#         }
#         }
#     url = "https://fcm.googleapis.com//v1/projects/test-push-notification-65372/messages:send"
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     print(response.content)
#     return HttpResponse("Status", response.content)
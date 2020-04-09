import datetime,time,sys,pyperclip,os
from twilio.rest import Client
from datetime import datetime
def time_exec():
    tz = pytz.timezone('Asia/Kolkata')
    kolkata_current_datetime = datetime.now(tz)
    return kolkata_current_datetime
    
account_sid='AC2f2468c989641b3d8067ee150c5ed79c'
auth_token="fd6ea242319f0d3df89d98a4d8286b07"
def send_msg(inputmsg):
	client=Client(account_sid,auth_token)
	client.messages.create(
    to='+91-8982592665',
    from_="(201) 575-4986",
    body=inputmsg
    )

a=0
while(a<10):
    x = str(time_exec())
    int_hr=int(x[11:13])
    if(int_hr > 9 and int_hr < 24):
        send_msg("SR_V3: Priyeeee Aap ne pani piya agar nhi to piligiye please... btana agar thappad ki jarurat h to")
    time.sleep(7200)


        

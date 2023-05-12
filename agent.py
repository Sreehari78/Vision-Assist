import datetime
from jarvis import speak
import pyjokes
import call_detection

def check_week(date):
    day = date.isoweekday()
    
    if day == 1:
        reply = 'Monday'
    elif day == 2:
        reply = 'Tuesday'
    elif day == 3:
        reply = 'Wednesday'
    elif day == 4:
        reply = 'Thursday'
    elif day == 5:
        reply = 'Friday'
    elif day == 6:
        reply = 'Saturday'
    elif day == 7:
        reply = 'Sunday'
    else:
        reply = 'Unable to fetch data'
    
    return reply

class ramanan:

    def date_check(date_check):
        today = datetime.date.today()

        if date_check == str(today):
            reply = f'YES today if {today.strftime("%B %d, %Y")}'
        else:
            reply = f"No Sir, today's date is {today.strftime('%B %d, %Y')}"
        
        speak(reply)


    def date_day_of_week():
        today = datetime.date.today()        
        reply = check_week(today)
        speak(reply)


    def date_get(date_check):

        today = datetime.date.today()

        if date_check == '':
            date_check = 'Today'
            reply_date = today
            reply_day  = check_week(today)

        elif date_check == 'yesterday':
            reply_date = today - datetime.timedelta(days=1)
            reply_day  = check_week(reply_date)


        elif date_check == 'tomorrow':
            reply_date = today + datetime.timedelta(days=1)
            reply_day  = check_week(reply_date)


        elif date_check == 'day_after_tomorrow':
            date_check = 'day after tomorrow'
            reply_date = today + datetime.timedelta(days=2)
            reply_day  = check_week(reply_date)
        
        reply = f"{date_check} is {reply_date} {reply_day}"
        speak(reply)
        
    def jokes_get():

        speak(pyjokes.get_joke())
 
    # def maps_current_location():

    #         api_key = os.environ['GOOGLE_MAPS_API_KEY']
    #         gmaps_client = googlemaps.Client(api_key)

    #         geocode_result = gmaps_client.geocode('1600 Amphitheatre Parkway,Mountain View,CA')
    #         result = geocode_result[0]

    #         print('Address:..',result['formatted_address'])
    #         print('Latitude:',result['geometry']['location']['lat'])
    #         print('Longitude:',result['geometry']['location']['Ing'])

    def time_check(check_time):
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        reply_yes =  f'YES it is {current_time}'
        reply_no = f'No it is {current_time}'

        if check_time[1].lower() == "o'clock":
            if check_time[0] == str(current_time.split(':')[0]):
                reply = reply_yes
            else:
                reply = reply_no
        else:
            if check_time[0] == str(current_time.split(':')[0]) and check_time[1] == str(current_time.split(' ')[1].lower()):
                reply = reply_yes
            else:
                reply = reply_no

        speak(reply)

    def time_get():
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak(current_time)
    
    def object_detection():
        object = call_detection.vision().lower()
        if object == 'person':
            speak("There is a person or a group of people in front of you")
        else:
            speak(f'You are looking at a {object.lower()}')
    
    def default(fulfillmentText):
        speak(fulfillmentText)
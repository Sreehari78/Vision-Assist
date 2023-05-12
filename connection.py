from intent import INTENT_LIST
from agent import ramanan as agent
from google.protobuf.json_format import MessageToDict

#constants
PROJECT_ID = 'smart-glasses-353005' 
SESSION_ID = '123456789'
LANG_CODE = 'en-US'

def processRequest(response):
    # dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
    # db = configureDataBase()

    result = response.get("queryResult")
    intent = result.get("intent").get('displayName')
    parameters = result.get("parameters")
    fulfillment = result.get('fulfillmentText')
    print(intent)

    for i in range(len(INTENT_LIST)):
        if INTENT_LIST[i] == intent:
                if i == 0: 
                    date_time = parameters.get('date').split('T')
                    date = date_time[0]
                    agent.date_check(date)

                elif i == 1:   
                    agent.date_day_of_week()    

                elif i == 2:
                    occurance = result.get('outputContexts')[0].get('parameters').get('date.original').replace(' ','_').lower()
                    agent.date_get(occurance)
                
                elif i == 3:
                    agent.jokes_get()

                elif i == 4:
                    # agent.maps_current_location()
                    pass

                elif i == 5:
                    occurance = result.get('outputContexts')[0].get('parameters').get('time.original').split(' ',)
                    if int(occurance[0]) > 0 and int(occurance[0]) < 10:
                        occurance[0] = f'0{occurance[0]}'
                    agent.time_check(occurance)
                
                elif i == 6:
                    agent.time_get()
                
                elif i == 7:
                    agent.object_detection()
                elif i == 8:
                    agent.default(fulfillment)

def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow

    session_client = dialogflow.SessionsClient.from_service_account_file('/home/sreehari/Python/Smart_glasses/Smart Glasses/smart-glasses-353005-0c00a3265d0b.json')

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        response_json = MessageToDict(response._pb)


        processRequest(response_json)

def get_query(query):
    query = [query]
    detect_intent_texts(PROJECT_ID, SESSION_ID, query, LANG_CODE)
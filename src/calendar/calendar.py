from typing import Any, Text, Dict, List

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle


class ActionBooking(Action):
    def name(self) -> Text:
        return "action_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Спасибо за информацию\!")
        print(tracker.slots)
        add_event(
            tracker.get_slot('event_name'),
            tracker.get_slot('date'),
            tracker.get_slot('time_start'),
            tracker.get_slot('time_end'),
            tracker.get_slot('hall'),
            tracker.get_slot('user_name'),
            tracker.get_slot('phone_number'),
            tracker.get_slot('desire'),
            'Рабочий')
        add_event(
            'Занято',
            tracker.get_slot('date'),
            tracker.get_slot('time_start'),
            tracker.get_slot('time_end'),
            tracker.get_slot('hall'),
            '',
            '',
            '',
            'Занятость')
        SlotSet(tracker, None)
        print(tracker.current_slot_values())
        return []

# If modifying these scopes, delete the file token.pickle.


SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'actions\credentials.json'


def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('actions/token.pickle'):
        with open('actions/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('actions/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def add_event(event_name: str, date: str, time_start: str, time_end: str, hall: str, user_name: str, phone_number: str, desire: str, calendar: str):
    service = get_calendar_service()
    time_start = datetime.datetime.strptime(
        date + " " + time_start, "%d.%m.%Y %H:%M").isoformat()
    print(time_start)
    time_end = datetime.datetime.strptime(
        date + " " + time_end, "%d.%m.%Y %H:%M").isoformat()
    print(time_end)
    if calendar == 'Занятость':
        if hall == 'Паттерн':
            hall = 'Большой зал'
        if hall == 'Знание':
            hall = 'Малый зал'
    event_result = service.events().insert(calendarId=cal_choose(calendar),
                                           body={
                                               "summary": f'{hall}_ {event_name}',
                                               "description": f'{user_name}: {phone_number};\n{desire}',
                                               "start": {"dateTime": time_start, "timeZone": 'Asia/Omsk'},
                                               "end": {"dateTime": time_end, "timeZone": 'Asia/Omsk'},
    }
    ).execute()


def cal_choose(calendar: str):
    service = get_calendar_service()
    page_token = None
    while True:
        cal = ''
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            if calendar in calendar_list_entry['summary']:
                cal = calendar_list_entry['id']
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    return cal

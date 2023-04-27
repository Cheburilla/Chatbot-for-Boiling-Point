import datetime
import os.path
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.utils.config_reader import config

# If modifying these scopes, delete the file token.pickle.


SCOPES = [config.scopes.get_secret_value()]

CREDENTIALS_FILE = config.credentials_path.get_secret_value()


def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(config.pickle_path.get_secret_value()):
        with open(config.pickle_path.get_secret_value(), 'rb') as token:
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
        with open(config.pickle_path.get_secret_value(), 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def add_event(calendar: str, event_name: str, date: str, time_start: str, time_end: str, hall: str, user_name: str, phone_number: str, desire: str):
    service = get_calendar_service()
    time_start = datetime.datetime.strptime(
        date + " " + time_start, "%d.%m.%Y %H:%M").isoformat()
    time_end = datetime.datetime.strptime(
        date + " " + time_end, "%d.%m.%Y %H:%M").isoformat()
    if calendar == 'Рабочий':
        if hall == 'Большой зал':
            hall = 'Паттерн'
        if hall == 'Малый зал':
            hall = 'Знание'
    else:
        event_name = "Занято"
        user_name = ''
        phone_number = ''
        desire = ''
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


def macro_add_event(*args):  # event_name: str, date: str, time_start: str, time_end: str, hall: str, user_name: str, phone_number: str, desire: str
    add_event("Рабочий", *args)
    add_event("Занятость", *args)

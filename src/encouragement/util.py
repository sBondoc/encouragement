from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from encouragement import DIR_DATA

PATH_TOKEN = DIR_DATA / Path('token.json')
PATH_CREDENTIAL = DIR_DATA / Path('credentials.json')

SCOPES = [
	'https://www.googleapis.com/auth/drive.readonly'
]

def contents_file(id_file: str):
	return build('drive', 'v3', credentials = credential()) \
		.files() \
		.get_media(
			fileId = id_file,
			supportsAllDrives = True) \
		.execute()
def credential(path: Path = DIR_DATA):
	cred = None
	if (PATH_TOKEN.exists()):
		cred = Credentials.from_authorized_user_file(str(PATH_TOKEN), SCOPES)
	if (not cred) or (not cred.valid):
		if cred and cred.expired and cred.refresh_token:
			cred.refresh(Request())
		else:
			cred = InstalledAppFlow \
			.from_client_secrets_file(
				str(PATH_CREDENTIAL), SCOPES) \
			.run_local_server(port = 0)
		PATH_TOKEN \
		.open('w') \
		.write(cred.to_json())
	return cred

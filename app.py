from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
#SCOPES = ['https://www.googleapis.com/auth/drive']
SCOPES = ['https://www.googleapis.com/auth/documents.readonly', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/documents'] 


KEY = 'IzaSyADiYXDXUk3FzdF68vHzH8NKZAyAptkbKc'

# The ID of a sample document.
DOCUMENT_ID = '1XGfAYJof_L0ZfDG3RicXzSD11tGtrkEO27jXkb30hMc'
#DOCUMENT_ID = '1vMJ3Bt5w-A0i7Yz99RMwDPwLhUXpuw6kUgblS4XotnU' 


def authenticate():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'cred4.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('docs', 'v1', credentials=creds)

        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        
        print('The title of the document is: {}'.format(document.get('title')))
        return service 
    except HttpError as err:
        print(err)


def getInfo():
    print("Enter a new name for the Google Doc:", end="")
    title = input() 
    print("The title you entered is:", title)
    return title

def createDoc(d, t):
    title = t
    body = {
        'title':title
    }
    d.documents().create(body=body).execute()
    print("Created document with title: {0}".format(doc.get('title')))

if __name__ == '__main__':
    document  = authenticate()
#    title = getInfo()

#    createDoc(document, title)    

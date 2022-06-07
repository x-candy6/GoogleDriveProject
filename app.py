from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive'] 

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


def getDocInfo(ser):
    print("Enter doc id:", end="")
    docID = input()
    document = ser.documents().get(documentId=docID).execute()
    print('The title of the document is: {}'.format(document.get('title')))
    print("\n****************\n")
def getDocInfo(ser, dID):
    document = ser.documents().get(documentId=dID).execute()
    print('The title of the document is: {}'.format(document.get('title')))
    print("\n****************\n")

def establishDocID():
    print("Enter doc id:")
    docID = input()
    print("\n****************\n")

    return docID 

def createDoc(d, t):
    title = t
    body = {
        'title':title
    }
    d.documents().create(body=body).execute()
    print("Created document with title: {0}".format(doc.get('title')))

def startMenu(s):
    print("1)Establish a Document ID")
    print("2)Get Document Info:")
    print("3)Get Document info on different ID ")
    print("9)Clear Document ID")
    print("0)Exit Program") 
    print("Please enter a menu item:")
    global docID    
    x = input()
    x = int(x)
    if x==1:
        print("You have chosen: Establish a Document ID")
        docID = establishDocID()
        print("New doc ID:", docID)
        startMenu(s)        
    elif x==2:
        print("You have chosen: Get Document Info")
        getDocInfo(s, docID)
        startMenu(s)
    elif x==3:
        print("You have chosen: Get Document info on different ID")
        getDocInfo(s)
        startMenu(s)
    elif x==9:
        print("You have chosen: Clear Document ID")
        docID = ""
        startMenu(s)
    elif x==0:
        print("Now exiting...")
        return
if __name__ == '__main__':
    docID = ""
    service  = authenticate()
    startMenu(service)
#    title = getInfo()

#    createDoc(document, title)    

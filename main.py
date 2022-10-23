from fastapi import FastAPI, Request, Query
from urllib import request
from fastapi.middleware.cors import CORSMiddleware
from urllib import request
from email.message import EmailMessage
import smtplib
import ssl

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/getInfo")
async def getInfo(info: Request):
    req_info = await info.json()
    req_info = dict(req_info)
    Pemail = req_info["pEmail"]
    PhoneNo = req_info['pPhone']
    Name = req_info['pName']
    Grade = req_info['sGrade']

    email_sender = 'chethan.tekie@gmail.com'
    email_password = "davqtpvnpnzfwbcl"

    subject = "Trail Class Request"
    body = '''
    You have a new free trial request from: 
    Parent Name: %s
    Paren Email: %s
    Phone:%s
    Student of Grade:%s
    '''%(Name,Pemail, PhoneNo,Grade)

    email_receiver = "Shobhayadav@robogems.com"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return {
        "Status" : "Successfull"
    }

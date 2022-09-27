from django.core import mail
from django.core.mail.backends.smtp import EmailBackend
from environs import Env

env = Env()
env.read_env()

test_email_backend = EmailBackend(
    host = 'mail5.hostingplatform.com',
    port = 587,
    username = 'conference@grandstrandapna.org',
    password = env.str("EMAIL_PASSWORD"),
    use_tls=True
)

def testSendEmail():
    test_email_backend.open()
    mail.EmailMessage(
        subject = 'Lecture at the Beach 2022 - Wednesday Evaluations',
        body = """This is a test email. Please do not reply.""",
        from_email = '"Lecture at the Beach 2022" <conference@grandstrandapna.org>',
        to = ['xoxojohnnyutah@gmail.com', 'camswee@gmail.com'],
        connection = test_email_backend
    ).send()
    test_email_backend.close()

def mailMergeByDay(data):
    test_email_backend.open()
    for current_registrant in data['queried']:
        #print(current_registrant)
        name = f"{current_registrant['content']['First Name']} {current_registrant['content']['Last Name']}"
        #if current_registrant['content']['E-mail Address'] not in retry_Friday:
        #    print(f"SKIPPING {current_registrant['content']['E-mail Address']}")
        #    continue
        print(f"SENDING EMAIL TO {current_registrant}")
        body = f"    Dear {name},\n"
        body += """
            Thank you for attending the 19th Annual Lecture at the Beach today!

            We would be very grateful if you could fill out an evaluation form about your experience today. It shouldn't take more than 5 minutes!

            Please click the link below to access the evaluation:
        """
        body += f"            https://request.cam/cams/LectureattheBeach/" + str(current_registrant['id']) + "/eval?" + data['day']
        body += """
    - Lecture at the Beach 2022
    - http://grandstrandapna.org/
        """

        valid = mail.EmailMessage(
            subject = f"Lecture at the Beach 2022 - {data['day']} Evaluations",
            body = body,
            from_email = '"Lecture at the Beach 2022" <conference@grandstrandapna.org>',
            to = [current_registrant['content']['E-mail Address']],
            bcc = ['conference@grandstrandapna.org'],
            connection = test_email_backend
        ).send()
        if not valid:
            print("!!! FAILED TO SEND EMAIL DESCRIBED ABOVE")
    test_email_backend.close()


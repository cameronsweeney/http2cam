from django.core import mail
from django.core.mail.backends.smtp import EmailBackend
from environs import Env

env = Env()
env.read_env()

sent_Wednesday = [
    "Alicia Pendergrass",
"Evelyn Coe",
"La' Quandra Rampersant",
"Shankana Johnson",
"Travis Crawford",
"Tammy Ward",
"Jenna Gordon",
"Elmira Obrien",
"Catherine Thomas",
"Jill Newman",
"Kellie Foxworth",
"Courtney Sturgill",
"Teresa Hathcox",
"Floella Shupe",
"Sarah Rudder",
"Dayna Wilder",
"Sara Lara",
"Laurrie Rumpp",
"Amanda Langford",
"Kim Ford",
"Cheryl Ward",
"Kristi Miller",
"Hailey Lanford",
"Krystal Hill",
"Crystal Leoffler",
"Betsey Scruggs",
"Kathy Cox",
"Kimberly Spires",
"Mojirola Oguntoyinbo",
"Zola Driggers",
"Rebecka Rollins",
"Misty Corrigan",
"Vickie Blackburn",
"Michele Lively",
"Charnele Jackson",
"Brandi Russ",
"Darlene Batastini",
"Maresa Butler",
"Ana Yanes",
"Carla Armstrong",
"Dee Griffin",
"Kimberly Hunsucker",
"Camille Wilkinson",
"Jacqueline Mintz",
"Stephanie Burgess",
"Ellen Mishra",
"Michelle Gilchrist",
"Irene Hallock",
"Sheryl Aiken",
"Whittle-Merchant",
"Joe Reynolds",
"Linda Alwine",
"Kathleen Boone"
]

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
        print(current_registrant)
        name = f"{current_registrant['content']['First Name']} {current_registrant['content']['Last Name']}"
        if name in sent_Wednesday:
            print(f"SKIPPING {current_registrant}")
            continue
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

        mail.EmailMessage(
            subject = f"Lecture at the Beach 2022 - {data['day']} Evaluations",
            body = body,
            from_email = '"Lecture at the Beach 2022" <conference@grandstrandapna.org>',
            to = [current_registrant['content']['E-mail Address']],
            connection = test_email_backend
        ).send()
    test_email_backend.close()


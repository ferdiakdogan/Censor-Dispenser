# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def phrase_censor(mail, phrase):
    mail_remaining = mail
    censored_mail = ""

    while phrase in mail_remaining:
        phrase_start_index = mail_remaining.find(phrase)
        phrase_end_index = phrase_start_index + len(phrase)
        censored_mail += mail_remaining[:phrase_start_index] + "&&&" + mail_remaining[phrase_start_index:phrase_end_index] + "&&&"
        mail_remaining = mail_remaining[phrase_end_index:]

    censored_mail += mail_remaining

    return censored_mail


censored_mail = phrase_censor(email_one, "learning algorithms")
print(censored_mail)

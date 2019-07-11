# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def phrase_censor(mail, phrase):
    mail_remaining = mail
    censored_mail_one = ""

    while phrase in mail_remaining:
        phrase_start_index = mail_remaining.find(phrase)
        phrase_end_index = phrase_start_index + len(phrase)
        censored_mail_one += mail_remaining[:phrase_start_index] + "&&&" + mail_remaining[phrase_start_index:phrase_end_index] + "&&&"
        mail_remaining = mail_remaining[phrase_end_index:]

    censored_mail_one += mail_remaining

    return censored_mail_one


censored_mail = phrase_censor(email_one, "learning algorithms")
#print(censored_mail)


def list_of_words_censor(mail, phrase_list):
    censored_mail_two = mail
    for phrase in phrase_list:
        censored_mail_two = phrase_censor(censored_mail_two, phrase)

    return censored_mail_two


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]
censored_mail_listed = list_of_words_censor(email_two, proprietary_terms)
print(censored_mail_listed)

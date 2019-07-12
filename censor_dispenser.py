# These are the emails you will be censoring. The open() function is opening the text file that the emails are
# contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def phrase_censor(mail, phrase):
    mail_remaining = mail
    censored_mail_one = ""

    while phrase in mail_remaining:
        censor = ""
        for letter in phrase:
            censor += 'X'
        phrase_start_index = mail_remaining.find(phrase)
        phrase_end_index = phrase_start_index + len(phrase)
        censored_mail_one += mail_remaining[:phrase_start_index] + censor
        mail_remaining = mail_remaining[phrase_end_index:]

    censored_mail_one += mail_remaining

    return censored_mail_one


censored_mail = phrase_censor(email_one, "learning algorithms")
# print(censored_mail)


def list_of_words_censor(mail, phrase_list):
    censored_mail_two = mail
    for phrase in phrase_list:
        censored_mail_two = phrase_censor(censored_mail_two, phrase)

    return censored_mail_two


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]
censored_mail_listed = list_of_words_censor(email_two, proprietary_terms)
# print(censored_mail_listed)


def negative_word_detector(mail, negative_words):
    censored_first = list_of_words_censor(mail, proprietary_terms)
    count = 0
    list_of_words = censored_first.split()
    for i in range(len(list_of_words)):
        if list_of_words[i] in negative_words:
            count += 1
            if count == 3:
                remaining_mail = ' '.join(list_of_words[i + 1:])
                head_of_mail = ' '.join(list_of_words[:i + 1])
            if count > 2:
                censored_remaining = list_of_words_censor(remaining_mail, negative_words)

    censored_mail = head_of_mail + ' ' + censored_remaining
    return censored_mail


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]

# print(negative_word_detector(email_three, negative_words))

punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_four(input_text, censored_list):
  input_text_words = []
  for x in input_text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      input_text_words.append(word)
  for i in range(0,len(input_text_words)):
    checked_word = input_text_words[i].lower()
    for x in punctuation:
      checked_word = checked_word.strip(x)
    if checked_word in censored_list:

      # Censoring the targeted word
      word_clean = input_text_words[i]
      censored_word = ""
      for x in punctuation:
        word_clean = word_clean.strip(x)
      for x in range(0,len(word_clean)):
        censored_word = censored_word + "X"
      input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)

      # Censoring the word before the targeted word
      word_before = input_text_words[i-1]
      for x in punctuation:
        word_before = word_before.strip(x)
      censored_word_before = ""
      for x in range(0,len(word_before)):
        censored_word_before = censored_word_before + "X"
      input_text_words[i-1] = input_text_words[i-1].replace(word_before, censored_word_before)

      # Censoring the word after the targeted word
      word_after = input_text_words[i+1]
      for x in punctuation:
        word_after = word_after.strip(x)
      censored_word_after = ""
      for x in range(0,len(word_after)):
        censored_word_after = censored_word_after + "X"
      input_text_words[i+1] = input_text_words[i+1].replace(word_after, censored_word_after)
  return " ".join(input_text_words)

censor_all = proprietary_terms + negative_words
print(censor_four(email_four, censor_all))
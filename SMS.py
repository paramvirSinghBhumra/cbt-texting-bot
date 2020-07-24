import smtplib
carriers = {
    'att': '@mms.att.net',
    'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send_message(email, password, message):
    send_to = '713-855-2667{}'.format(carriers['att'])

    #establishing secure connection with server
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(email, password)
    # with smtplib.SMTP("smtp.gmail.com", 587) as server:
    #     server.ehlo()
    #     server.starttls()
    #     server.ehlo()
    #     server.login(email, password)
    #
    #     server.sendmail(email, send_to, message)
    #     print("successfully sent message to %s".format(to_number))

""" Script will send an email via smtp show in email if backup wath succussfull or not. """

#!/usr/bin/env python3
import sys


def send_emailreport(email, date, time, success):
    message = email.message.EmailMAssage()
    weekay = dow(date)
    message['Subject'] = f'Backup Report ' + date + " " + success
    message.set_content("Lets try report out!")


def send_report(message, emails):
    smtp = smtplib.SMTP('localhost')
    message['From'] = 'noreplay@example.com'
    for email in emails.split(','):
        del message['To']
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass


def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = send_emailreport((email, date, time, success))
        print("Successfully send to: ", emails)
    except Exception as e:
        print("Failure to send emails", file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())

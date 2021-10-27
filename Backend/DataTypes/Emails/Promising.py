from flask import render_template


def send_promising(name, track):
    subject = "Your application for DPS has been reviewed"
    body = render_template('SendPromisingEmail.html',
                           applicantName=name, applicantTrack=track)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}

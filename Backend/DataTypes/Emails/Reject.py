from flask import render_template


def reject(name, track):
    subject = "Your application for Digital Product School"
    body = render_template('SendRejectionEmail.html',
                           applicantName=name, applicantTrack=track)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}

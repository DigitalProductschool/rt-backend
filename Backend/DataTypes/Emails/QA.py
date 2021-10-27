from flask import render_template

def send_qa(name, track, qaLink):
    subject = "Invitation to Q&A"
    body = render_template('SendQ&AEmail.html', applicantName=name,
                           applicantTrack=track, qaLink=qaLink)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}

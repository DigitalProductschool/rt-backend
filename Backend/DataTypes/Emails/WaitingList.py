from flask import render_template


def send_waiting_list(name, track, batch, batchStart, coreTeamName):
    subject = "Your application for Digital Product School"
    body = render_template('SendWaitingListEmail.html',
                           applicantName=name, applicantTrack=track, batch=batch, batchStart=batchStart, coreTeamName=coreTeamName)
    footer = render_template('Footer.html', coreTeamName=coreTeamName)
    return {"subject": subject, "body": body + footer}

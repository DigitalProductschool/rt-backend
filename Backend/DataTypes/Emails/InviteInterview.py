from flask import render_template


def invite_to_interview(name, track, coreTeamLink, coreTeamName):
    subject = "Invitation to Interview"
    body = render_template('SendInvitationEmail.html', applicantName=name,
                           applicantTrack=track, coreTeamLink=coreTeamLink)
    footer = render_template('Footer.html', coreTeamName=coreTeamName)
    return {"subject": subject, "body": body + footer}

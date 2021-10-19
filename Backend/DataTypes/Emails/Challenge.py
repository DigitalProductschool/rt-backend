from flask import render_template


def send_challenge(name, track, challengeLink):
    subject = "DPS Challenge Assessment"
    body = render_template('SendChallengeEmail.html', applicantName=name,
                           applicantTrack=track, challengeLink=challengeLink)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}

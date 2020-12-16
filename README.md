# Secret Santa

This is a simple script to assign a Secret Santa for each participant who signed
up via Google Forms.

The form must contain the following fields to be considered valid by this script:

* Name (required) - Name of the participant
* Email (required) - Email address of the participant
* Address (required) - Residence of the participant
* Note (optional) - Note from the participant to the assigned Secret Santa

## Environmental Variables

This script makes use of three environmental variables and loads them via
[`python-dotenv`](https://pypi.org/project/python-dotenv/).

The variables are:

* `GMAIL_USERNAME` - Gmail log-in username
* `GMAIL_PASSWORD` - Gmail log-in password
* `CONTACT_INFO_FILE_ID` - File ID of the spreadsheet created by Google Forms

Because this script is dependent on `smtplib` to connect to the server, the Google
account being used must have "Less secure app access" setting turned _ON_.

See ["Less secure apps & your Google Account"](https://support.google.com/accounts/answer/6010255)
for more information.

## Testing the Script

To test the script, leave the `test` variable set to `True` and execute `hohoho.py`.
Every email will be sent to the test account instead of the actual participants.
Each test email can be differentiated by checking the recipient of the email, which
will be formatted as `"<test user>+<original recipient>@gmail.com"`.

## When You Are Ready...

Execute the `hohoho.py` with `test` variable set to `False`. Merry Christmas!

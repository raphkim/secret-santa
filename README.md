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
* `GMAIL_PASSWORD` - Gmail app password (**NOT** the account password)
* `CONTACT_INFO_FILE_ID` - File ID of the spreadsheet created by Google Forms

Change the visibility of the spreadsheet to be accessible to those with URL.

Google stopped supporting "Less secure app access" in May 2022, which makes the script
unable to log-in to Gmail account with just the account password. In order to successfully
authenticate this script, please enable 2-Step-Verification and generate an "App Password"
to be used by this app.

See ["Sign in with App Passwords"](https://support.google.com/accounts/answer/185833)
for more information.

## Testing the Script

To test the script, leave the `test` variable set to `True` and execute `hohoho.py`.
Every email will be sent to the test account instead of the actual participants.
Each test email can be differentiated by checking the recipient of the email, which
will be formatted as `"<test user>+<original recipient>@gmail.com"`.

## When You Are Ready...

Execute the `hohoho.py` with `test` variable set to `False`. Merry Christmas!

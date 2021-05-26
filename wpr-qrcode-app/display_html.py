def display_html(count,arguments):
    if (count != 100):
            message_body = "<h3> Thank you for the submission.</h3> <p></p> <i>The issue with '"+arguments+"' has been reported to the WPR team.</i><p></p>"
    else:
        message_body = "<h3> ERROR submitting the issue to Webex Teams!!. Kindly try again after sometime!! </h3>"
        message = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width; initial-scale=1.0;">
            <meta charset="UTF-8">
            <link rel="stylesheet" href="reportissue.css">
            <title>
                Thank you for the submission. 
            </title>
        </head>
        <body>
        """ + message_body + "</h3></body></html>"
        return message
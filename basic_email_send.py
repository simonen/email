from email import message_from_string
import smtplib


### Basic email send with custom header

def add_tls_info_to_headers(raw_email):
    msg = message_from_string(raw_email)
    # tls_info = "TLS information here"  # Replace with actual TLS info
    # msg['X-TLS-Info'] = tls_info
    print(msg.as_string())
    return msg.as_string()


# Example usage
raw_email = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"  # Fetch this from Postfix queue or source
modified_email = add_tls_info_to_headers(raw_email)

with smtplib.SMTP('192.168.137.9') as server:
    server.sendmail('MAIL FROM:', 'RCPT TO:', modified_email)

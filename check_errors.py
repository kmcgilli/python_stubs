import os
import smtplib
from email.mime.text import MIMEText
import sys
import socket
hostname = socket.gethostname()
def check_errors():
    file_name=sys.argv[1]
    errors=sys.argv[2]
    recipient=sys.argv[3]
    error_file=file_name+".err"
    filehandle=open(error_file,"w")
    errors=errors.split("|")
    for lines in open(file_name):
            lines=lines.strip()
            for error in errors:
                    if error.upper() in lines.upper():
                                    #print(lines)
                                    filehandle.write(lines+'\n')
    filehandle.close()

    if os.path.getsize(error_file) > 0:
            fp = open(error_file, 'rb')
            msg = MIMEText(fp.read())
            fp.close()
            msg['Subject'] = 'Errors found in %s please check!' % file_name 
            msg['From'] = hostname 
            msg['To'] = recipient
            s = smtplib.SMTP('localhost')
            s = smtplib.SMTP('localhost')
            s.sendmail(hostname, [recipient], msg.as_string())
            s.quit
            os.remove(error_file)
if len(sys.argv) == 4:
        check_errors()
else:
        print("Invalid parameters");
	print("Usage: check_errors.py 'file_path' 'error1|error2|error...' 'Email'")
        sys.exit(1)
sys.exit(0)

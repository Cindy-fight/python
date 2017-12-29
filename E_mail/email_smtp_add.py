from email import encoders
from email.header import  Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart, MIMEBase

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEMultipart('alternative')  # alternative的作用是：如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# 邮件正文是MIMEText
# 发送正文
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 发送带有图片的正文
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('/Users/admin/Desktop/test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
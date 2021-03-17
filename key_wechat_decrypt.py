import hashlib

UIN1 = '-1995855133'.encode()
UIN2 = '2299112163'.encode()
IMEI = '358534060102270'.encode()
Account = 'wxid_u6dapn2wehqw12'.encode()

En_key = IMEI+UIN1
FTS_key = UIN2+IMEI+Account
Priority_key = UIN2+Account+IMEI

En = hashlib.md5(En_key).hexdigest()
FTS = hashlib.md5(FTS_key).hexdigest()
Priority = hashlib.md5(Priority_key).hexdigest()

print('En*.db key :', En[:7])
print('FTS5IndexMicroMsg_encrypt.db key :', FTS[:7])
print('MicroMsgPriority.db key :', Priority[:7])

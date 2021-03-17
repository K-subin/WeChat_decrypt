from pysqlcipher3 import dbapi2 as sqlite

conn = sqlite.connect( "EnMicroMsg.db" )
c = conn.cursor()		
c.execute( "PRAGMA key = '6b2a05c';" )
c.execute( "PRAGMA cipher_use_hmac = OFF;" )
c.execute( "PRAGMA cipher_page_size = 1024;" )
c.execute( "PRAGMA kdf_iter = 4000;" )
c.execute( "ATTACH DATABASE 'EnMicroMsg-decrypted.db' AS wechatdecrypted KEY '';" )
c.execute( "SELECT sqlcipher_export( 'wechatdecrypted' );" )
c.execute( "DETACH DATABASE wechatdecrypted;" )
c.close()

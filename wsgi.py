import flaskb
import ssl

# 即使在近端仍希望以 https 模式下執行
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('keys/localhost.crt', 'keys/localhost.key')

app = flaskb.create_app()
app.run(
        host='127.0.0.1', port=8443, debug=True,
        ssl_context=context
    )
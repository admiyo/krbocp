import os

def application(environ, start_response):
    status = '200 OK'
    output = b'<html><head><title>Environment Variables</title></head><body>'
    path =  '/var/kerberos/krb5/%d/client.keytab' % os.geteuid()
    line =  "<p>Looking for %s</p>" % path
    line =  "<p>Looking for %s</p>" % path
    output += line.encode('utf-8')

    try:
        f = open(path)
        line =  "<p>Able to open %s</p>" % path
        f.close()
    except FileNotFoundError:
        line =  "<p>cannot  open %s</p>" % path
    output += line.encode('utf-8')




    output = output + b'<dl>'
    line = '<dt>%s</dt><dd> %s</dd>\n' % ('euid', os.geteuid())
    output += line.encode('utf-8')

    
    keys = environ.keys()
    for key in keys:
        line = '<dt>%s</dt><dd> %s</dd>\n' % (key, repr(environ[key]))
        output += line.encode('utf-8')
    output += b'</dl></body></html>'

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

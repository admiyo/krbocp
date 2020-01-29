import os

def application(environ, start_response):
    status = '200 OK'
    output = b'<html><head><title>Environemnt Variables</title></head><body><dl>'
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

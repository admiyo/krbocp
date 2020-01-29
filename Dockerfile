FROM centos:latest

MAINTAINER Adam Young

RUN yum -y install httpd mod_wsgi

COPY index.html /var/www/html/
COPY hello.py   /var/www/cgi-bin/myapp.wsgi
RUN chmod a+rx  /var/www/cgi-bin/myapp.wsgi
COPY hello.conf /etc/httpd/conf.d/

CMD /usr/sbin/httpd -D FOREGROUND

EXPOSE 80

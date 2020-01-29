FROM centos:latest

MAINTAINER Adam Young

RUN yum -y install httpd mod_wsgi
RUN sed -i.bak 's/Listen 80/Listen 8080/' /etc/httpd/conf/httpd.conf
RUN sed -i.bak 's/    CustomLog/#    CustomLog/' /etc/httpd/conf/httpd.conf


COPY index.html /var/www/html/
COPY envvars.py   /var/www/cgi-bin/envvars.wsgi
RUN  chmod a+rx   /var/www/cgi-bin/envvars.wsgi
COPY krbocp.conf /etc/httpd/conf.d/

CMD /usr/sbin/httpd -D FOREGROUND

EXPOSE 8080

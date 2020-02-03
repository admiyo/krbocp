FROM centos:latest

MAINTAINER Adam Young

RUN yum -y install httpd mod_wsgi mod_auth_gssapi
RUN yum -y install krb5-workstation
RUN sed -i.bak 's/Listen 80/Listen 8080/' /etc/httpd/conf/httpd.conf
RUN sed -i.bak 's/    CustomLog/#    CustomLog/' /etc/httpd/conf/httpd.conf
COPY tools.py /tools.py
RUN mkdir /var/www/html/gssapi
RUN mkdir /etc/httpd/conf/secrets
RUN chown apache:apache /etc/httpd/conf/secrets
RUN chmod 600 /etc/httpd/conf/secrets
COPY index.html /var/www/html/gssapi
COPY index.html /var/www/html/
COPY envvars.py   /var/www/cgi-bin/envvars.wsgi
RUN  chmod a+rx   /var/www/cgi-bin/envvars.wsgi
COPY krbocp.conf /etc/httpd/conf.d/
COPY krb5.conf /etc/krb5.conf
CMD /usr/sbin/apachectl -DFOREGROUND

EXPOSE 8080

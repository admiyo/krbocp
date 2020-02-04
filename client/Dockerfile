FROM centos:latest

MAINTAINER Adam Young

RUN yum -y install krb5-workstation strace curl sssd-client
RUN chmod a+rwx /var/kerberos/krb5/user
COPY krb5.conf /etc/krb5.conf


USER 1001
#CMD touch /tmp/test ; ls -la /tmp/test

#CMD ls -la /var/kerberos/krb5/user/1001/client.keytab
#CMD KRB5_TRACE=/dev/stderr   kinit -V testuser@REDHATFSI.COM  -t /var/kerberos/krb5/user/0/client.keytab ; curl -k --negotiate -u : https://idm.redhatfsi.com/ipa
CMD KRB5_TRACE=/dev/stderr  curl -k --negotiate -u : https://idm.redhatfsi.com/ipa 
#CMD whoami
#CMD echo $EUID
#CMD cat /var/kerberos/krb5/user/0/client.keytab
#CMD curl -k --negotiate -u : https://idm.redhatfsi.com/ipa
#CMD cat /etc/krb5.conf

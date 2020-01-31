podman run -P --name krbocp --mount type=bind,source=/home/ayoung/user,destination=/var/kerberos/krb5/user --rm admiyo:curlkrb
#podman run -P --name krbocp --mount type=bind,source=/home/ayoung/user/0/client.keytab,destination=/etc/krb5.keytab --rm admiyo:curlkrb

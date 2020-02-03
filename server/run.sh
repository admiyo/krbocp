podman run -P --name krbocp --mount type=bind,source=/home/ayoung/keytabs/HTTP/localdev.redhatfsi.com@REDHATFSI.COM.keytab,destination=/etc/httpd/secrets/apache.keytab --rm admiyo:krbocp

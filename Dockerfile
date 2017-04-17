FROM python:2


ENV WORK_DIR=/opt/powerdns-admin

ENV PDNS_DB_HOST=mysql \
    PDNS_DB_NAME=pdns \
    PDNS_API_URL=http://pdns:8081/

RUN apt-get update && apt-get install -y unzip libldap2-dev libsasl2-dev && rm -rf /var/lib/apt/lists/*

RUN pip install MySQL-python

ADD https://github.com/ngoduykhanh/PowerDNS-Admin/archive/master.zip /tmp/powerdns-admin.zip

RUN mkdir -p "$WORK_DIR/.." && \
    unzip /tmp/powerdns-admin.zip -d "/tmp/" && \
    mv -T "/tmp/PowerDNS-Admin-master" "$WORK_DIR"

RUN pip install -r "$WORK_DIR/requirements.txt"

ADD config.py "$WORK_DIR/"

ADD entrypoint.sh /

RUN chmod +x /entrypoint.sh

EXPOSE 9393

CMD ["/entrypoint.sh"]

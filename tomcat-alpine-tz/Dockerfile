FROM tomcat:8-jre8-alpine

# Online, make cache dir for copying packages out
# RUN mkdir -p /var/cache/apk && \
#     ln -s /var/cache/apk /etc/apk/cache && \
#     apk add tzdata

COPY tzdata-2018d-r1.476fcf5e.apk /tmp/tzdata-2018d-r1.476fcf5e.apk
RUN apk add --allow-untrusted /tmp/tzdata-2018d-r1.476fcf5e.apk && \
    rm -f /tmp/tzdata-2018d-r1.476fcf5e.apk

# https://wiki.alpinelinux.org/wiki/Setting_the_timezone
ENV TZ=Asia/Shanghai


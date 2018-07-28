FROM tomcat:8-jre8-alpine

# Online, make cache dir for copying packages out
# RUN apk add tzdata

COPY tzdata-2018d-r1.476fcf5e.apk /tmp/tzdata-2018d-r1.476fcf5e.apk
RUN apk add --allow-untrusted /tmp/tzdata-2018d-r1.476fcf5e.apk && \
    rm -f /tmp/tzdata-2018d-r1.476fcf5e.apk

COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
COPY server.xml /usr/local/tomcat/conf/server.xml

# https://wiki.alpinelinux.org/wiki/Setting_the_timezone
ENV TZ=Asia/Shanghai


ADD spring-mvc-showcase.war /usr/local/tomcat/webapps/
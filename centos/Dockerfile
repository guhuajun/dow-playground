FROM centos:6.9

RUN localedef -i zh_CN -f UTF-8 zh_CN.UTF-8

ENV LANG=zh_CN.UTF-8
ENV LANGUAGE=zh_CN.UTF-8
ENV LC_ALL=zh_CN.UTF-8

ADD test.sh /tmp/

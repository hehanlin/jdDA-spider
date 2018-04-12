#
# Dockerfile for scrapyd:py3
#

FROM python:3.6
MAINTAINER hehanlin <china.hehanlin@gmail.com>

RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ scrapy scrapyd scrapy-splash pymongo chardet --trusted-host mirrors.aliyun.com
COPY scrapyd.conf /etc/scrapyd/
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
EXPOSE 6800

CMD ["scrapyd"]

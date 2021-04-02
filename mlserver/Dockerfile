ARG TAG
FROM python3baseimage:${TAG}

WORKDIR /template

COPY ./mlserver /template/mlserver
COPY ./ai /template/ai
COPY ./utils /template/utils

EXPOSE 9011 
RUN groupadd -r template && useradd --no-log-init -r -g template template
RUN chown -R template:template /template

WORKDIR /template/mlserver

CMD [ "bash", "start_uwsgi.sh"]
# CMD [ "uwsgi", "--ini", "uwsgi.ini"]

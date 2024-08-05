FROM python:3.11.4-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip


COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
# RUN python manage.py collectstatic

COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

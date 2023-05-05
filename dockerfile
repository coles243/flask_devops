FROM python:3.8-alpine

WORKDIR /pydoc


COPY ./requirements.txt /pydoc/requirements.txt


COPY . /pydoc

EXPOSE 3000

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
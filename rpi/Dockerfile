FROM python:slim

ADD main.py /
ADD relay.py /
ADD smartlet_request.py ''
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "pismartlet_api.py"]
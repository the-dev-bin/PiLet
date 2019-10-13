FROM python:slim

ADD pismartlet_api.py /
ADD data.json /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "pismartlet_api.py"]

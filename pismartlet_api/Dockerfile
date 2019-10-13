FROM python:slim

ADD pismartlet_api.py /
ADD data.json /
add requirements.txt /
RUN pip install requiremnts.txt

CMD ["python", "pismartlet_api.py"]

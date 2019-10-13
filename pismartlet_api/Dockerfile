FROM python:slim

ADD pismartlet_api.py /
ADD data.json /
add requiremnts.txt /
RUN pip install requiremnts.txt

CMD ["python", "pismartlet_api.py"]

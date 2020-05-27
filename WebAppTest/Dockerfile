FROM python:3

ADD app.py /
ADD sentiment.py /
ADD DataExtractor.py /
ADD tab_1.py /
ADD tab_2.py /
ADD tab_3.py /
ADD Views.py /

RUN pip install dash
RUN pip install numpy
RUN pip install plotly
RUN pip install requests
RUN pip install textblob
RUN pip install regex
RUN pip install couchdb

CMD [ "python", "./app.py" ]

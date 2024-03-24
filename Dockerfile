FROM python:3.9.4

RUN apt-get update
RUN apt-get -y install open-jtalk open-jtalk-mecab-naist-jdic

WORKDIR /tmp

RUN git clone https://github.com/icn-lab/htsvoice-tohoku-f01.git

RUN ln -s /var/lib/mecab/dic/open-jtalk/naist-jdic /usr/local/share/open_jtalk_dic

RUN mkdir /usr/local/share/hts_voice
RUN ln -s /tmp/htsvoice-tohoku-f01 /usr/local/share/hts_voice/htsvoice-tohoku-f01

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install -r requirements.txt
ENV FLASK_APP main

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

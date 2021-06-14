FROM python:3.9
WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y sudo wget ffmpeg libffi-dev libnacl-dev python3-dev

RUN pip install --upgrade pip && \
    pip install pytz 'discord.py[voice]' matplotlib numpy Pillow SQLAlchemy psycopg2 google-auth google-cloud-texttospeech google-api-python-client PyNaCl

RUN chown -R root:root /usr/local/lib/python3.9/site-packages

RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/6.2.4/flyway-commandline-6.2.4-linux-x64.tar.gz | tar xvz && sudo ln -s `pwd`/flyway-6.2.4/flyway /usr/local/bin

COPY ./ipag.ttf .
RUN cp ./ipag.ttf /usr/local/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/

COPY . .

RUN rm -rf ./google-credentials.json
# RUN echo "font.family: IPAGothic" >> /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc
# /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc/fonts/ttf/ipag.ttf

#>>> import matplotlib
#>>> matplotlib.matplotlib_fname()
#>>> matplotlib.get_configdir()
#'/root/.config/matplotlib'

RUN chmod +x CLGHouseBot.sh

CMD ["./CLGHouseBot.sh"]

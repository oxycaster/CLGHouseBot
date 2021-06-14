FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && \
  apt-get install -y sudo wget ffmpeg

RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/6.2.4/flyway-commandline-6.2.4-linux-x64.tar.gz | tar xvz && sudo ln -s `pwd`/flyway-6.2.4/flyway /usr/local/bin

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN cp ./ipag.ttf /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/

# RUN echo "font.family: IPAGothic" >> /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc
# /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc/fonts/ttf/ipag.ttf

#>>> import matplotlib
#>>> matplotlib.matplotlib_fname()
#>>> matplotlib.get_configdir()
#'/root/.config/matplotlib'

RUN chmod +x CLGHouseBot.sh

CMD ["./CLGHouseBot.sh"]

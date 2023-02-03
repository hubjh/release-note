FROM docker.items.com/ubuntu-hadoop:3.3.4
RUN pip3 install packaging
RUN pip3 install bs4
RUN apt update -y 
RUN apt install unzip -y
RUN wget -P / https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install /google-chrome-stable_current_amd64.deb -y
RUN wget -P / https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
RUN unzip /chromedriver_linux64.zip
RUN pip3 install selenium

COPY app /app
WORKDIR /app
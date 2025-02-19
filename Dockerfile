FROM movecrew/one4ubot:alpine-latest

RUN mkdir /One4uBot && chmod 777 /One4uBot
ENV PATH="/One4uBot/bin:$PATH"
WORKDIR /One4uBot

RUN git clone https://github.com/4amparaboy/One4uBot /One4uBot
RUN mkdir /4amparaboy && chmod 777 /4amparaboy
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install wget
#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /One4uBot/

#
# Make open port TCP
#
EXPOSE 80 443

#
# Finalization
#
CMD ["python3","-m","userbot"]

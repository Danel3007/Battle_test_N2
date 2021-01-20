FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 \
    python

RUN apt -y install curl tar

RUN mkdir -p /opt/gotty && \ 
    curl -SL https://github.com/yudai/gotty/releases/download/v1.0.1/gotty_linux_amd64.tar.gz \
    | tar -xzC /opt/gotty && \
    cp /opt/gotty/gotty /bin/gotty && chmod +x /bin/gotty && \
    rm -rf /opt/gotty

ENV LANG="ru_RU.UTF-8" \
    LC_COLLATE="ru_RU.UTF-8" \
    LC_CTYPE="ru_RU.UTF-8" \
    LC_MESSAGES="ru_RU.UTF-8" \
    LC_MONETARY="ru_RU.UTF-8" \
    LC_NUMERIC="ru_RU.UTF-8" \
    LC_TIME="ru_RU.UTF-8" 

ENV PYTHONIOENCODING=utf-8

WORKDIR /opt/app

# COPY Battle_test_N2.py /opt/app
# COPY FnialBoss.py /opt/app
# COPY [ "Test SN4.py",  "/opt/app" ]
# COPY state.py /opt/app

COPY *.py /opt/app/

CMD [ "gotty", "-w", "--port", "80", "python3", "Test SN4.py" ]
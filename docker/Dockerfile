FROM python:3.6

RUN pip install circus chaussette
RUN apt-get -y update
RUN apt-get -y install libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl make wget
RUN wget https://openresty.org/download/openresty-1.11.2.3.tar.gz

RUN tar xzvf openresty-1.11.2.3.tar.gz && \
    cd openresty-1.11.2.3 && \
    ./configure -j2 && \
    make -j2 && \
    make install

ENV PATH "/usr/local/openresty/bin:/usr/local/openresty/nginx/sbin:$PATH"

COPY docker/circus.ini /app/circus.ini
COPY docker/nginx.conf /app/nginx.conf
COPY . /app

RUN pip install -r /app/requirements.txt
RUN pip install /app/

EXPOSE 8080
CMD circusd /app/circus.ini

FROM postgres:12.3

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install dos2unix

COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

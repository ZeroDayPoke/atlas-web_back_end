FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root_user_pass
ENV PERSONAL_DATA_DB_HOST=%
ENV PERSONAL_DATA_DB_NAME=personal_data_db
ENV PERSONAL_DATA_DB_USERNAME=personal_data_root
ENV PERSONAL_DATA_DB_PASSWORD=root_pass

COPY my.cnf /etc/mysql/conf.d/my.cnf
ADD main.sql /docker-entrypoint-initdb.d

EXPOSE 3333

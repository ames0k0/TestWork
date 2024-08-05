FROM unit:1.32.1-python3.11

COPY ./deploy/config/config.json /docker-entrypoint.d/config.json

RUN mkdir build
COPY ./src/web ./build
COPY ./src/web/pyproject.toml ./src/web/poetry.lock* ./build/

WORKDIR /build

# NOTE: не стал использовать `poetry`
RUN apt update && apt install -y python3-pip                                  \
    && pip3 install poetry                                                    \
    && poetry export -f requirements.txt --output /build/requirements.txt --without-hashes \
    && pip3 install --no-cache-dir --upgrade -r /build/requirements.txt       \
    && apt remove -y python3-pip                                              \
    && apt autoremove --purge -y                                              \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

EXPOSE 80

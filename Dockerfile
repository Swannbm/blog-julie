FROM python:3.9.7

EXPOSE 8000

# ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV PATH = "${PATH}:/root/.poetry/bin"


RUN pip install --upgrade pip
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN alias ll="ls -alh"

COPY . ./app
WORKDIR /app

RUN poetry config virtualenvs.create false
RUN poetry install

# setup ssh for git
RUN mkdir -p /root/.ssh
COPY id_rsa /root/.ssh/id_rsa
RUN chmod 700 /root/.ssh/id_rsa
RUN ssh-keyscan -t rsa github.com > ~/.ssh/known_hosts

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]
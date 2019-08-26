FROM {{ cookiecutter.docker_base_image }}

RUN mkdir -p /opt/src /input /output

WORKDIR /opt/src

COPY requirements.txt /opt/src/
RUN python -m pip install -r requirements.txt

ADD src /opt/src/

ENTRYPOINT "python" "-m" "run_{{ cookiecutter.container_type }}"

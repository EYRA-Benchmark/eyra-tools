FROM {{ cookiecutter.docker_base_image }}

RUN mkdir -p /opt/{{ cookiecutter.container_type }} /input /output

WORKDIR /opt/{{ cookiecutter.container_type }}

COPY requirements.txt /opt/{{ cookiecutter.container_type }}/
RUN python -m pip install -r requirements.txt

ADD {{ cookiecutter.container_type }}_src /opt/{{ cookiecutter.container_type }}/

ENTRYPOINT "python" "-m" "{{ cookiecutter.container_type }}"

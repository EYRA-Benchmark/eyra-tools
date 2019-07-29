FROM {{ cookiecutter.docker_base_image }}

RUN mkdir -p /opt/{{ cookiecutter.src_prefix }} /input /output

WORKDIR /opt/{{ cookiecutter.src_prefix }}

COPY requirements.txt /opt/{{ cookiecutter.src_prefix }}/
RUN python -m pip install -r requirements.txt

ADD {{ cookiecutter.src_prefix }}_src /opt/{{ cookiecutter.src_prefix }}/

ENTRYPOINT "python" "-m" "{{ cookiecutter.src_prefix }}"

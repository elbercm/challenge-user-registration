FROM backend_python39:centos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend;
WORKDIR /backend
FROM python:3.6-alpine

# Install tools
RUN apk add --update build-base
RUN apk add --update libxslt-dev libxml2-dev

# Install modules
RUN pip install -U grpcio
RUN pip install -U grpcio-tools
RUN pip install -U beautifulsoup4
RUN pip install -U captcha_solver
RUN pip install -U urllib3
RUN pip install -U requests
RUN pip install -U lxml

# Create app directory
WORKDIR /usr/src/app

# Bundle app source
COPY . .

# Build grpc
RUN sh scripts.sh build

# Expose the port
EXPOSE 5000

# Run command
CMD [ "python", "server.py" ]
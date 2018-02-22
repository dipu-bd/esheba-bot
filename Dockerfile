FROM python:3.6-alpine

RUN pip install -U grpcio
RUN pip install -U grpcio-tools
RUN pip install -U beautifulsoup4
RUN pip install -U captcha_solver

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

# Esheba BOT

Auto crawl train route and other information from https://www.esheba.cnsbd.com

## Install Requirements

- lxml: `pip install -U lxml`
- urllib3: `pip install -U urllib3`
- Requests: `pip install -U requests`
- BeautifulSoup4: `pip install -U beautifulsoup4`
- GRPC Tools: `pip install -U grpcio-tools`
- GRPC: `pip install -U grpcio`

- Docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Build

- To build grpc files: `sh build.sh`
- To and run docker: `sh build.sh docker`
- Stop docker: `sh build.sh _docker`

## Usage

- Open terminal in the project directory.
- Build GRPC modules: `sh build.sh`
- Run `python .`

```bash
EshebaBot:
  python . <user-email> <password>
  python . --server
  python . --test [<user-mail>] [<password>]

OPTIONS:
 user-email Email of the user to login.
 password   Password to login
 --server    Starts the grpc server
 --test      Runs grpc test client

```

### Start GRPC server

Run `python . --server` to start the server.

### Test the server

Run `python . --test-grpc` to test the server

### Test methods directly

Run `python . --test` to test directly without a server

## Disclaimer

This is just a personal fun project. No harm intended.

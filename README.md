# Esheba BOT

Auto crawl train route and other information from https://www.esheba.cnsbd.com

## Install Requirements

- GRPC: `pip install -U grpcio`
- GRPC Tools: `pip install -U grpcio-tools`
- BeautifulSoup4: `pip install -U beautifulsoup4`
- CaptchaSolver: `pip install -U captcha_solver`

## Usage

In the project directory open terminal and write `python .` to display help.

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

Run `python . --test <your email> <your password>` to test the server

## Disclaimer

This is just a personal fun project. No harm intended.

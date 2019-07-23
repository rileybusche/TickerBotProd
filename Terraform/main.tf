provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "Ticker" {
  count         = 0
  ami           = "ami-026c8acd92718196b"
  instance_type = "t2.micro"
  key_name      = "${aws_key_pair.ticker_alert_key.key_name}"

  #user_data       = "${file("setup.sh")}"

  tags = {
    Name = "TickerAlert"
  }
}

resource "aws_key_pair" "ticker_alert_key" {
  key_name   = "ticker_alert_key"
  public_key = "${file("ticker_alert_key.pub")}"
}
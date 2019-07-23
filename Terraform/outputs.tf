output "ip" {
  value = aws_instance.Ticker[0].public_ip
}
log_channel_id = 673205358600388672

def write_log(message, client):
    log_channel = client.get_channel(log_channel_id)
    await log_channel.send(message)
    
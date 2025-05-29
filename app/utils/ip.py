from fastapi import Request


def get_client_ip(request: Request):
    x_forward_for = request.headers.get("X-Forwarded-For")
    if x_forward_for:
        ip_address = x_forward_for.split(",")[0]
    else:
        ip_address = request.client.host
    return ip_address

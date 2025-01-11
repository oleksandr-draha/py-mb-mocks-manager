def http(url: str) -> str:
    if url.startswith('http'):
        return url
    else:
        return f'http://{url}'

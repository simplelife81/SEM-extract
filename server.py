import re

async def sanitize_bname(name, max_length=50):
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    return name[:max_length]

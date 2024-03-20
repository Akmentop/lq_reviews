
MAX_STR_LEN = 100


def use_br(msg: str) -> str:
    return msg.replace('\n', '<br />')


def shorten(msg: str) -> str:
    return use_br(
        msg[:MAX_STR_LEN] + ('...' if len(msg) > MAX_STR_LEN else ''))


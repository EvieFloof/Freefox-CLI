import hashlib
import hmac


def hmac_sha1(app_token, challenge):
    return hmac.new(
        app_token.encode("utf-8"), challenge.encode("utf-8"), hashlib.sha1
    ).hexdigest()

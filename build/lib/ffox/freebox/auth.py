import socket
import time

import requests

import ffox.utils.config as config
import ffox.utils.logs as logger
from ffox.utils.hash import hmac_sha1


class FreeboxConnection:
    def __init__(
        self,
        freebox_address: str = "http://mafreebox.freebox.fr",
    ):
        self.address = freebox_address

    def endpoint(self, path):
        return self.address + path

    def close_session(self):
        r = requests.post(self.endpoint("/api/v8/login/logout")).json()
        if not r["success"]:
            return True
        else:
            logger.error(f"Failed to close the session: {r}")

    def get_session_challenge(self):
        response = requests.get(self.endpoint("/api/v8/login"))

        if response.json()["success"]:
            return response.json()["result"]["challenge"]
        else:
            logger.critical("Invalid response from /api/v8/login")

    def get_session_token(self):
        if config.Contains("SessionToken"):
            if (time.time() - config.Read("SessionTokenTime")) < 25 * 60:
                logger.debug("Using cached token")
                return config.Read("SessionToken")

        logger.warn("Session token expired or missing. Generating a new one")

        password = hmac_sha1(
            self.get_authentication_token(), self.get_session_challenge()
        )

        auth_request = requests.post(
            self.endpoint("/api/v8/login/session/"),
            json={
                "app_id": "dev.freefox.cli",
                "password": password,
            },
        )

        if not auth_request.json()["success"]:
            logger.error("Invalid Token")

        config.Edit(
            {
                "SessionToken": auth_request.json()["result"]["session_token"],
                "SessionTokenTime": time.time(),
            }
        )

        logger.log("Fetched token from Freebox Server")
        logger.success(f"Using new session token : {config.Read('SessionToken')}")

        return auth_request.json()["result"]["session_token"]

    def get_authentication_token(self):
        if config.Contains("AuthenticationToken"):
            return config.Read("AuthenticationToken")

        # Ask the Freebox Server an auth token
        authentification_request = requests.post(
            self.endpoint("/api/v8/login/authorize/"),
            json={
                "app_id": "dev.freefox.cli",
                "app_name": "FreeFox CLI",
                "app_version": "0.0.1",
                "device_name": socket.gethostname(),
            },
        )

        response = authentification_request.json()

        self.auth_token = response["result"]["app_token"]

        authentification_status = requests.get(
            self.endpoint(f"/api/v8/login/authorize/{response['result']['track_id']}")
        )

        if authentification_status.json()["result"]["status"] == "pending":
            logger.show("Please press the allow button on your Freebox Server")

            attempt = 1
            while authentification_status.json()["result"]["status"] == "pending":
                logger.show(
                    "\033[FPlease press the allow button on your Freebox Server"
                    + "." * attempt
                )
                attempt += 1
                authentification_status = requests.get(
                    self.endpoint(
                        f"/api/v8/login/authorize/{response['result']['track_id']}"
                    )
                )
                time.sleep(3)

            match authentification_status.json()["result"]["status"]:
                case "timeout":
                    logger.error(
                        "The user did not confirmed the authorization within the given time"
                    )
                case "denied":
                    logger.error("The user denied the authorization request")
                case "unknown":
                    logger.critical("Given app_token is invalid or expired")
                case "granted":
                    logger.success("Successfully got a valid token")
                    logger.secondary(f"Token: {self.auth_token}")
                    logger.secondary(f"Track ID: {response['result']['track_id']}")

                    config.Edit(
                        {
                            "AuthenticationToken": response["result"]["app_token"],
                            "TrackID": response["result"]["track_id"],
                        }
                    )
                case _:
                    logger.critical(
                        "Unknown response, please consider opening an issue"
                    )
        elif authentification_status.json()["result"]["status"] == "granted":
            logger.secondary(f"Auth Token: {self.auth_token}")
        else:
            logger.critical("Unknown error while trying to authenticate")

        return self.auth_token

    def authenticated_request(self, path, mode="GET", json=None):
        match mode:
            case "GET":
                req = requests.get(
                    self.endpoint(path),
                    headers={"X-Fbx-App-Auth": config.Read("SessionToken")},
                    json=json,
                )
            case "POST":
                req = requests.get(
                    self.endpoint(path),
                    headers={"X-Fbx-App-Auth": config.Read("SessionToken")},
                    json=json,
                )
            case _:
                logger.error("Request malformed or missing")
                exit(1)

        if not req.json()["success"]:
            logger.error(f"Request to {path} failed")
            return {"result": {}}

        return req.json()

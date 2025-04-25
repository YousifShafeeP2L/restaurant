class CustomError(Exception):
    def __init__(self, detail: str, status_code: int = 400, error_from: str = ""):
        self.status_code = status_code
        self.set_detail(detail)
        if error_from:
            self.detail = f"{error_from}: {self.detail}"

    def set_detail(self, detail):
        if isinstance(detail, dict):
            if detail.get("message", None):
                return self.set_detail(detail.get("message"))
            elif detail.get("error", None):
                return self.set_detail(detail.get("error"))
            else:
                _, value = detail.popitem()
                return self.set_detail(value)
        elif isinstance(detail, list):
            return self.set_detail(detail[0])
        else:
            self.detail = str(detail)[:150]

from app.helper_classes.exception_handler import CustomError
from fastapi import Request


def get_param(request: Request, param_name: str, param_type: type = None, default=None):
    param = request.query_params.get(param_name, default)
    if not param:
        raise CustomError(f"Missing {param_name} parameter in request!")
    if param_type:
        try:
            param = param_type(param)
        except:
            raise CustomError(f"Invalid {param_name} parameter in request!")
    return param

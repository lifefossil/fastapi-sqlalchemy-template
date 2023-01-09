from src.enums.StateEnums import StateEnums

class ResponseVo:
    fail_code: int = StateEnums.ERROR
    success_code: int = StateEnums.SUCCESS

    @staticmethod
    def of(code: int, msg: str, data=None):
        if data is None:
            data = []
        return {"code": code, "msg": msg, "data": data}

    @staticmethod
    def success(data=None, msg='success'):
        return ResponseVo.of(code=ResponseVo.success_code, msg=msg, data=data)

    @staticmethod
    def fail(data=None, msg='operation failed'):
        return ResponseVo.of(code=ResponseVo.fail_code, msg=msg, data=data)
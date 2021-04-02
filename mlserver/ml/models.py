class ErrorResponse(BaseException):
    def __init__(self, http_status, error_reason, error_description, error):
        self.http_status = http_status
        self.error_reason = error_reason
        self.error_description = error_description
        self.error = error

    def to_dict(self):
        return self.__dict__


class BadRequestErrorResponse(ErrorResponse):
    def __init__(self, error_reason, error_description):

        super(BadRequestErrorResponse, self).__init__(
            http_status=400,
            error='Bad Request',
            error_description=error_description,
            error_reason=error_reason,
        )


class InternalErrorResponse(ErrorResponse):
    def __init__(self, error_reason, error_description):
        super(InternalErrorResponse, self).__init__(
            http_status=500,
            error='Internal Error',
            error_description=error_description,
            error_reason=error_reason
        )


class NotFoundResponse(ErrorResponse):
    def __init__(self, error_reason, error_description):
        super(NotFoundResponse, self).__init__(
            http_status=404,
            error='Not Found',
            error_description=error_description,
            error_reason=error_reason
        )


class Languages:
    def __init__(self):
        self.FINNISH = "finnish"
        self.DANISH = "danish"
        self.SWEDISH = "swedish"
        self.NORWEGIAN = "norwegian"

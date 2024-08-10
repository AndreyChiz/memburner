from api import DetailedHTTPException
from .__constants import ApiV1ExceptionDetails


class DocumentNotFound(DetailedHTTPException):
    status_code = 404
    detail = ApiV1ExceptionDetails.document.NOT_FOUND


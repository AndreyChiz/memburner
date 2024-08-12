from api.exceptions import NotFoundException, BadRequestException
from .__constants import ApiV1ExceptionDetails



class DocumentNotFound(NotFoundException):
    DETAIL = ApiV1ExceptionDetails.document.NOT_FOUND



class DocumentAlreadyExistsException(BadRequestException):
    DETAIL = ApiV1ExceptionDetails.document.ALREADY_EXIST



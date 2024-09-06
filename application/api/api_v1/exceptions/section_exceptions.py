from api.exceptions import NotFoundException, BadRequestException
from .__constants import ApiV1ExceptionDetails



class SectionNotFound(NotFoundException):
    DETAIL = ApiV1ExceptionDetails.section.NOT_FOUND



class SectionAlreadyExistsException(BadRequestException):
    DETAIL = ApiV1ExceptionDetails.section.ALREADY_EXIST



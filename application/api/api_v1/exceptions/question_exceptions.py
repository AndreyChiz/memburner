from api.exceptions import NotFoundException, BadRequestException
from .__constants import ApiV1ExceptionDetails



class QuestionNotFound(NotFoundException):
    DETAIL = ApiV1ExceptionDetails.question.NOT_FOUND



class QuestionAlreadyExistsException(BadRequestException):
    DETAIL = ApiV1ExceptionDetails.question.ALREADY_EXIST



class DocumentExceptionDetails:
    NOT_FOUND = "Document not found"
    ALREADY_EXIST= "This user already haves a document with this name"


class ApiV1ExceptionDetails:
    document: DocumentExceptionDetails = DocumentExceptionDetails()


    # DOCUMENT_NOT_FOUND = "Document not found"
    # SECTION_NOT_FOUND = "Section not found"
    # QUESTION_NOT_FOUND = "Question not found"
    # DOCUMENT_ALREADY_EXISTS = "Document already exists"
    # SECTION_ALREADY_EXISTS = "Section already exists"
    # QUESTION_ALREADY_EXISTS = "Question already exists"
    # DOCUMENT_NOT_FOUND_IN_SECTION = "Document not found in section"
    # SECTION_NOT_FOUND_IN_DOCUMENT = "Section not found in document"
    # QUESTION_NOT_FOUND_IN_SECTION = "Question not found in section"
    # DOCUMENT_NOT_FOUND_IN_QUESTION = "Document not found in question"
    # SECTION_NOT_FOUND_IN_QUESTION = "Section not found in question"
    # QUESTION_NOT_FOUND_IN_DOCUMENT = "Question not found in document"
    # DOCUMENT_NOT_FOUND_IN_QUESTION_ANSWER = "Document not found in question answer"
    # SECTION_NOT_FOUND_IN_QUESTION_ANSWER = "Section not found in question answer"

from winky import HTTPMessage


def response_status_code_validation(expected_code: int, response: HTTPMessage):
    """
    Проверка кода ответа сервиса
    :param expected_code: ожидаемый код ответа
    :param response: ответ сервиса
    :raises Exception: код ответа не соответствует ожидаемому
    """
    if response.code != expected_code:
        raise Exception(
            f'''response code is not valid. expected: {expected_code}, actual: {response.code}.
            Response body:
            {response.body}
            '''
        )

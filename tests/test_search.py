import winky
import pytest
import config
from jsonschema.validators import validate
from schemas.search import SOUR_CREAM, BREAD, MILK
from data import Api, InputData
from helpers.common_helper import response_status_code_validation
from enums.content_type import ContentType


@pytest.mark.parametrize("test_input,expected", [(InputData.SOUR_CREAM, SOUR_CREAM),
                                                 (InputData.BREAD, BREAD),
                                                 (InputData.MILK, MILK)])
def test_search(test_input, expected):
    request = winky.HTTPMessage()
    request.headers["Content-Type"] = ContentType.APPLICATION_JSON.value

    '''можно было бы передать через параметры, но наблюдается проблема на стороне фреймворка при отправке'''
    # request.headers["q"] = "смет"
    # request.headers["sid"] = "387"
    # request.headers["tenant_id"] = "sbermarket"

    '''отправка запроса'''
    response = request.get(config.sber_host, config.sber_port,
                           f"{Api.suggests}"
                           f"?q={test_input}&sid=387&tenant_id=sbermarket")

    '''Валидация ответа'''
    response_status_code_validation(200, response)
    template = winky.TemplateJSON(response.body).json
    validate(template, expected)

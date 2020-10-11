# -*- coding: utf-8 -*-
import pytest
from iamport.exceptions import ResponseError


def test_customer_get(iamport):
    customer_uid = '000000'
    with pytest.raises(ResponseError) as e:
        iamport.customer_get(customer_uid)
        assert u'요청하신 customer_uid(000000)로 등록된 정보를 찾을 수 없습니다.' == e.message


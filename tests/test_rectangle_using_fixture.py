import sys
from os.path import join, dirname, abspath
import pytest
import os

sys.path.append(join(abspath(dirname(__file__)), "../src"))

from rectangle import RectangleShape

class myapp:
    def readenv(self):
        return os.environ.get("DA")

okay = []

@pytest.fixture(scope="session")
def rectangle_1():
    # print("Setting")
    rect = RectangleShape(2,3)
    # global okay
    # okay.append((rect, ))
    return rect

@pytest.fixture(scope="session")
def rectangle_2():
    print("Setting")
    rect = RectangleShape(4,3)
    yield rect

@pytest.fixture(scope="session")
def rectangle_3():
    print("Setting")
    rect = RectangleShape(8,8)
    yield rect



@pytest.mark.parametrize("rect, result",
                         [
                             (6, 6),
                             # (rectangle_2(), 12),
                             # (rectangle_3(), 64)
                         ])
def test_area_of_rectangle(rect, result, rectangle_1):
    # print(okay)
    assert result == rectangle_1.get_area()
#
# @pytest.mark.parametrize("rect, result",
#                          [
#                              (rectangle_1(), 10),
#                              (rectangle_2(), 14),
#                              (rectangle_3(), 32)
#                          ])
# def test_peri_of_rectangle(rect, result):
#     area_of_rectangle = rect.get_perimeter()
#     assert area_of_rectangle == result

def test_envreading(monkeypatch):
    monkeypatch.setenv('DA', '456', prepend="qa_")
    val = myapp().readenv()
    assert val == '456'



def test_envreading_2(monkeypatch):
    monkeypatch.setenv('DA', '123')
    val = myapp().readenv()
    assert val == '123'


# class DocxtractDynamoDBConnection(DynamoDBConnectionBase):
#     """
#     Wrapper around the DynamoDB table Document
#     """
#     def __init__(self) -> None:
#         super(DocxtractDynamoDBConnection, self).__init__(DynamoDBCommonUtils.DOCXTRACT, DocxtractDynamoDBModel)
#
#     def get(self, document_id) -> Optional[DocxtractDynamoDBModel]:
#         get_object: dict = self.connection.get(document_id=document_id)
#         docxtract_dynamodbmodel_obj: Optional[DocxtractDynamoDBModel] = None
#
#         try:
#             document_item = get_object["Item"]
#             docxtract_dynamodbmodel_obj = DocxtractDynamoDBModel._get_object(document_item)
#         except KeyError:
#             # IF the Item we are looking up for does not exist we will get a KeyError.
#             pass
#
#         return docxtract_dynamodbmodel_obj
#
#     def create(self, docxtract_dynamodbmodel_obj) -> None:
#         item_dict:dict = docxtract_dynamodbmodel_obj.__dict__
#
#         self.connection.create(item_dict)
#         logging.info("Successfully Created the item")
#
#     def update(self, docxtract_dynamodbmodel_obj) -> None:
#
#         item_dict: dict = docxtract_dynamodbmodel_obj.__dict__
#         key_dict: dict = dict()
#
#         for key_field in self.connection.key_fields:
#             key_dict[key_field] = item_dict[key_field]
#
#         self.connection.update(key_dict, item_dict)
#         logging.info("Successfully Updated the item")
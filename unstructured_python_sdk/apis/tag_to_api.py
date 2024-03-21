import typing_extensions

from unstructured_python_sdk.apis.tags import TagValues
from unstructured_python_sdk.apis.tags.general_api import GeneralApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.GENERAL: GeneralApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.GENERAL: GeneralApi,
    }
)

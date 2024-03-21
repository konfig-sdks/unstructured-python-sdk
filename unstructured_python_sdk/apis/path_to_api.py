import typing_extensions

from unstructured_python_sdk.paths import PathValues
from unstructured_python_sdk.apis.paths.general_v0_general import GeneralV0General

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.GENERAL_V0_GENERAL: GeneralV0General,
    }
)

path_to_api = PathToApi(
    {
        PathValues.GENERAL_V0_GENERAL: GeneralV0General,
    }
)

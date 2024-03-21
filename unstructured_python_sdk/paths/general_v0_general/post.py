# coding: utf-8

"""
    Unstructured Pipeline API

    At Unstructured, we're on a mission to give organizations access to all of their data. We know the world runs on documents—from research reports and memos, to quarterly filings and plans of action, documents are the unit of information that companies depend on. And yet, 80% of this information is trapped in inaccessible formats, and businesses have long struggled to unlock this data, leading to information silos, inefficient decision-making, and repetitive work. Until now.  Unstructured captures this unstructured data wherever it lives and transforms it into AI-friendly JSON files for companies who are eager to fold AI into their business.

    The version of the OpenAPI document: 0.0.1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from unstructured_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from unstructured_python_sdk.api_response import AsyncGeneratorResponse
from unstructured_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unstructured_python_sdk import schemas  # noqa: F401

from unstructured_python_sdk.model.partition_parameters_skip_infer_table_types import PartitionParametersSkipInferTableTypes as PartitionParametersSkipInferTableTypesSchema
from unstructured_python_sdk.model.partition_parameters import PartitionParameters as PartitionParametersSchema
from unstructured_python_sdk.model.partition_parameters_extract_image_block_types import PartitionParametersExtractImageBlockTypes as PartitionParametersExtractImageBlockTypesSchema
from unstructured_python_sdk.model.partition_parameters_languages import PartitionParametersLanguages as PartitionParametersLanguagesSchema
from unstructured_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from unstructured_python_sdk.model.elements import Elements as ElementsSchema

from unstructured_python_sdk.type.http_validation_error import HTTPValidationError
from unstructured_python_sdk.type.partition_parameters_languages import PartitionParametersLanguages
from unstructured_python_sdk.type.partition_parameters_skip_infer_table_types import PartitionParametersSkipInferTableTypes
from unstructured_python_sdk.type.partition_parameters_extract_image_block_types import PartitionParametersExtractImageBlockTypes
from unstructured_python_sdk.type.partition_parameters import PartitionParameters
from unstructured_python_sdk.type.elements import Elements

from ...api_client import Dictionary
from unstructured_python_sdk.pydantic.partition_parameters_languages import PartitionParametersLanguages as PartitionParametersLanguagesPydantic
from unstructured_python_sdk.pydantic.partition_parameters import PartitionParameters as PartitionParametersPydantic
from unstructured_python_sdk.pydantic.elements import Elements as ElementsPydantic
from unstructured_python_sdk.pydantic.partition_parameters_extract_image_block_types import PartitionParametersExtractImageBlockTypes as PartitionParametersExtractImageBlockTypesPydantic
from unstructured_python_sdk.pydantic.partition_parameters_skip_infer_table_types import PartitionParametersSkipInferTableTypes as PartitionParametersSkipInferTableTypesPydantic
from unstructured_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

from . import path

# body param
SchemaForRequestBodyMultipartFormData = PartitionParametersSchema


request_body_partition_parameters = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
_auth = [
    'ApiKeyAuth',
]
SchemaFor200ResponseBodyApplicationJson = ElementsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Elements


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Elements


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_pipeline_mapped_args(
        self,
        files: typing.Optional[typing.IO] = None,
        strategy: typing.Optional[str] = None,
        gz_uncompressed_content_type: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        coordinates: typing.Optional[bool] = None,
        encoding: typing.Optional[str] = None,
        hi_res_model_name: typing.Optional[str] = None,
        include_page_breaks: typing.Optional[bool] = None,
        languages: typing.Optional[PartitionParametersLanguages] = None,
        pdf_infer_table_structure: typing.Optional[bool] = None,
        skip_infer_table_types: typing.Optional[PartitionParametersSkipInferTableTypes] = None,
        xml_keep_tags: typing.Optional[bool] = None,
        chunking_strategy: typing.Optional[str] = None,
        multipage_sections: typing.Optional[bool] = None,
        combine_under_n_chars: typing.Optional[int] = None,
        new_after_n_chars: typing.Optional[int] = None,
        max_characters: typing.Optional[int] = None,
        overlap: typing.Optional[int] = None,
        overlap_all: typing.Optional[bool] = None,
        extract_image_block_types: typing.Optional[PartitionParametersExtractImageBlockTypes] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if files is not None:
            _body["files"] = files
        if strategy is not None:
            _body["strategy"] = strategy
        if gz_uncompressed_content_type is not None:
            _body["gz_uncompressed_content_type"] = gz_uncompressed_content_type
        if output_format is not None:
            _body["output_format"] = output_format
        if coordinates is not None:
            _body["coordinates"] = coordinates
        if encoding is not None:
            _body["encoding"] = encoding
        if hi_res_model_name is not None:
            _body["hi_res_model_name"] = hi_res_model_name
        if include_page_breaks is not None:
            _body["include_page_breaks"] = include_page_breaks
        if languages is not None:
            _body["languages"] = languages
        if pdf_infer_table_structure is not None:
            _body["pdf_infer_table_structure"] = pdf_infer_table_structure
        if skip_infer_table_types is not None:
            _body["skip_infer_table_types"] = skip_infer_table_types
        if xml_keep_tags is not None:
            _body["xml_keep_tags"] = xml_keep_tags
        if chunking_strategy is not None:
            _body["chunking_strategy"] = chunking_strategy
        if multipage_sections is not None:
            _body["multipage_sections"] = multipage_sections
        if combine_under_n_chars is not None:
            _body["combine_under_n_chars"] = combine_under_n_chars
        if new_after_n_chars is not None:
            _body["new_after_n_chars"] = new_after_n_chars
        if max_characters is not None:
            _body["max_characters"] = max_characters
        if overlap is not None:
            _body["overlap"] = overlap
        if overlap_all is not None:
            _body["overlap_all"] = overlap_all
        if extract_image_block_types is not None:
            _body["extract_image_block_types"] = extract_image_block_types
        args.body = _body
        return args

    async def _acreate_pipeline_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Pipeline 1
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/general/v0/general',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_partition_parameters.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_pipeline_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Pipeline 1
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/general/v0/general',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_partition_parameters.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreatePipelineRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_pipeline(
        self,
        files: typing.Optional[typing.IO] = None,
        strategy: typing.Optional[str] = None,
        gz_uncompressed_content_type: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        coordinates: typing.Optional[bool] = None,
        encoding: typing.Optional[str] = None,
        hi_res_model_name: typing.Optional[str] = None,
        include_page_breaks: typing.Optional[bool] = None,
        languages: typing.Optional[PartitionParametersLanguages] = None,
        pdf_infer_table_structure: typing.Optional[bool] = None,
        skip_infer_table_types: typing.Optional[PartitionParametersSkipInferTableTypes] = None,
        xml_keep_tags: typing.Optional[bool] = None,
        chunking_strategy: typing.Optional[str] = None,
        multipage_sections: typing.Optional[bool] = None,
        combine_under_n_chars: typing.Optional[int] = None,
        new_after_n_chars: typing.Optional[int] = None,
        max_characters: typing.Optional[int] = None,
        overlap: typing.Optional[int] = None,
        overlap_all: typing.Optional[bool] = None,
        extract_image_block_types: typing.Optional[PartitionParametersExtractImageBlockTypes] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_pipeline_mapped_args(
            files=files,
            strategy=strategy,
            gz_uncompressed_content_type=gz_uncompressed_content_type,
            output_format=output_format,
            coordinates=coordinates,
            encoding=encoding,
            hi_res_model_name=hi_res_model_name,
            include_page_breaks=include_page_breaks,
            languages=languages,
            pdf_infer_table_structure=pdf_infer_table_structure,
            skip_infer_table_types=skip_infer_table_types,
            xml_keep_tags=xml_keep_tags,
            chunking_strategy=chunking_strategy,
            multipage_sections=multipage_sections,
            combine_under_n_chars=combine_under_n_chars,
            new_after_n_chars=new_after_n_chars,
            max_characters=max_characters,
            overlap=overlap,
            overlap_all=overlap_all,
            extract_image_block_types=extract_image_block_types,
        )
        return await self._acreate_pipeline_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_pipeline(
        self,
        files: typing.Optional[typing.IO] = None,
        strategy: typing.Optional[str] = None,
        gz_uncompressed_content_type: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        coordinates: typing.Optional[bool] = None,
        encoding: typing.Optional[str] = None,
        hi_res_model_name: typing.Optional[str] = None,
        include_page_breaks: typing.Optional[bool] = None,
        languages: typing.Optional[PartitionParametersLanguages] = None,
        pdf_infer_table_structure: typing.Optional[bool] = None,
        skip_infer_table_types: typing.Optional[PartitionParametersSkipInferTableTypes] = None,
        xml_keep_tags: typing.Optional[bool] = None,
        chunking_strategy: typing.Optional[str] = None,
        multipage_sections: typing.Optional[bool] = None,
        combine_under_n_chars: typing.Optional[int] = None,
        new_after_n_chars: typing.Optional[int] = None,
        max_characters: typing.Optional[int] = None,
        overlap: typing.Optional[int] = None,
        overlap_all: typing.Optional[bool] = None,
        extract_image_block_types: typing.Optional[PartitionParametersExtractImageBlockTypes] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_pipeline_mapped_args(
            files=files,
            strategy=strategy,
            gz_uncompressed_content_type=gz_uncompressed_content_type,
            output_format=output_format,
            coordinates=coordinates,
            encoding=encoding,
            hi_res_model_name=hi_res_model_name,
            include_page_breaks=include_page_breaks,
            languages=languages,
            pdf_infer_table_structure=pdf_infer_table_structure,
            skip_infer_table_types=skip_infer_table_types,
            xml_keep_tags=xml_keep_tags,
            chunking_strategy=chunking_strategy,
            multipage_sections=multipage_sections,
            combine_under_n_chars=combine_under_n_chars,
            new_after_n_chars=new_after_n_chars,
            max_characters=max_characters,
            overlap=overlap,
            overlap_all=overlap_all,
            extract_image_block_types=extract_image_block_types,
        )
        return self._create_pipeline_oapg(
            body=args.body,
        )

class CreatePipeline(BaseApi):

    async def acreate_pipeline(
        self,
        files: typing.Optional[typing.IO] = None,
        strategy: typing.Optional[str] = None,
        gz_uncompressed_content_type: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        coordinates: typing.Optional[bool] = None,
        encoding: typing.Optional[str] = None,
        hi_res_model_name: typing.Optional[str] = None,
        include_page_breaks: typing.Optional[bool] = None,
        languages: typing.Optional[PartitionParametersLanguages] = None,
        pdf_infer_table_structure: typing.Optional[bool] = None,
        skip_infer_table_types: typing.Optional[PartitionParametersSkipInferTableTypes] = None,
        xml_keep_tags: typing.Optional[bool] = None,
        chunking_strategy: typing.Optional[str] = None,
        multipage_sections: typing.Optional[bool] = None,
        combine_under_n_chars: typing.Optional[int] = None,
        new_after_n_chars: typing.Optional[int] = None,
        max_characters: typing.Optional[int] = None,
        overlap: typing.Optional[int] = None,
        overlap_all: typing.Optional[bool] = None,
        extract_image_block_types: typing.Optional[PartitionParametersExtractImageBlockTypes] = None,
        validate: bool = False,
        **kwargs,
    ) -> ElementsPydantic:
        raw_response = await self.raw.acreate_pipeline(
            files=files,
            strategy=strategy,
            gz_uncompressed_content_type=gz_uncompressed_content_type,
            output_format=output_format,
            coordinates=coordinates,
            encoding=encoding,
            hi_res_model_name=hi_res_model_name,
            include_page_breaks=include_page_breaks,
            languages=languages,
            pdf_infer_table_structure=pdf_infer_table_structure,
            skip_infer_table_types=skip_infer_table_types,
            xml_keep_tags=xml_keep_tags,
            chunking_strategy=chunking_strategy,
            multipage_sections=multipage_sections,
            combine_under_n_chars=combine_under_n_chars,
            new_after_n_chars=new_after_n_chars,
            max_characters=max_characters,
            overlap=overlap,
            overlap_all=overlap_all,
            extract_image_block_types=extract_image_block_types,
            **kwargs,
        )
        if validate:
            return RootModel[ElementsPydantic](raw_response.body).root
        return api_client.construct_model_instance(ElementsPydantic, raw_response.body)
    
    
    def create_pipeline(
        self,
        files: typing.Optional[typing.IO] = None,
        strategy: typing.Optional[str] = None,
        gz_uncompressed_content_type: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        coordinates: typing.Optional[bool] = None,
        encoding: typing.Optional[str] = None,
        hi_res_model_name: typing.Optional[str] = None,
        include_page_breaks: typing.Optional[bool] = None,
        languages: typing.Optional[PartitionParametersLanguages] = None,
        pdf_infer_table_structure: typing.Optional[bool] = None,
        skip_infer_table_types: typing.Optional[PartitionParametersSkipInferTableTypes] = None,
        xml_keep_tags: typing.Optional[bool] = None,
        chunking_strategy: typing.Optional[str] = None,
        multipage_sections: typing.Optional[bool] = None,
        combine_under_n_chars: typing.Optional[int] = None,
        new_after_n_chars: typing.Optional[int] = None,
        max_characters: typing.Optional[int] = None,
        overlap: typing.Optional[int] = None,
        overlap_all: typing.Optional[bool] = None,
        extract_image_block_types: typing.Optional[PartitionParametersExtractImageBlockTypes] = None,
        validate: bool = False,
    ) -> ElementsPydantic:
        raw_response = self.raw.create_pipeline(
            files=files,
            strategy=strategy,
            gz_uncompressed_content_type=gz_uncompressed_content_type,
            output_format=output_format,
            coordinates=coordinates,
            encoding=encoding,
            hi_res_model_name=hi_res_model_name,
            include_page_breaks=include_page_breaks,
            languages=languages,
            pdf_infer_table_structure=pdf_infer_table_structure,
            skip_infer_table_types=skip_infer_table_types,
            xml_keep_tags=xml_keep_tags,
            chunking_strategy=chunking_strategy,
            multipage_sections=multipage_sections,
            combine_under_n_chars=combine_under_n_chars,
            new_after_n_chars=new_after_n_chars,
            max_characters=max_characters,
            overlap=overlap,
            overlap_all=overlap_all,
            extract_image_block_types=extract_image_block_types,
        )
        if validate:
            return RootModel[ElementsPydantic](raw_response.body).root
        return api_client.construct_model_instance(ElementsPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        files: typing.Optional[typing.IO] = None,
        strategy: typing.Optional[str] = None,
        gz_uncompressed_content_type: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        coordinates: typing.Optional[bool] = None,
        encoding: typing.Optional[str] = None,
        hi_res_model_name: typing.Optional[str] = None,
        include_page_breaks: typing.Optional[bool] = None,
        languages: typing.Optional[PartitionParametersLanguages] = None,
        pdf_infer_table_structure: typing.Optional[bool] = None,
        skip_infer_table_types: typing.Optional[PartitionParametersSkipInferTableTypes] = None,
        xml_keep_tags: typing.Optional[bool] = None,
        chunking_strategy: typing.Optional[str] = None,
        multipage_sections: typing.Optional[bool] = None,
        combine_under_n_chars: typing.Optional[int] = None,
        new_after_n_chars: typing.Optional[int] = None,
        max_characters: typing.Optional[int] = None,
        overlap: typing.Optional[int] = None,
        overlap_all: typing.Optional[bool] = None,
        extract_image_block_types: typing.Optional[PartitionParametersExtractImageBlockTypes] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_pipeline_mapped_args(
            files=files,
            strategy=strategy,
            gz_uncompressed_content_type=gz_uncompressed_content_type,
            output_format=output_format,
            coordinates=coordinates,
            encoding=encoding,
            hi_res_model_name=hi_res_model_name,
            include_page_breaks=include_page_breaks,
            languages=languages,
            pdf_infer_table_structure=pdf_infer_table_structure,
            skip_infer_table_types=skip_infer_table_types,
            xml_keep_tags=xml_keep_tags,
            chunking_strategy=chunking_strategy,
            multipage_sections=multipage_sections,
            combine_under_n_chars=combine_under_n_chars,
            new_after_n_chars=new_after_n_chars,
            max_characters=max_characters,
            overlap=overlap,
            overlap_all=overlap_all,
            extract_image_block_types=extract_image_block_types,
        )
        return await self._acreate_pipeline_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        files: typing.Optional[typing.IO] = None,
        strategy: typing.Optional[str] = None,
        gz_uncompressed_content_type: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        coordinates: typing.Optional[bool] = None,
        encoding: typing.Optional[str] = None,
        hi_res_model_name: typing.Optional[str] = None,
        include_page_breaks: typing.Optional[bool] = None,
        languages: typing.Optional[PartitionParametersLanguages] = None,
        pdf_infer_table_structure: typing.Optional[bool] = None,
        skip_infer_table_types: typing.Optional[PartitionParametersSkipInferTableTypes] = None,
        xml_keep_tags: typing.Optional[bool] = None,
        chunking_strategy: typing.Optional[str] = None,
        multipage_sections: typing.Optional[bool] = None,
        combine_under_n_chars: typing.Optional[int] = None,
        new_after_n_chars: typing.Optional[int] = None,
        max_characters: typing.Optional[int] = None,
        overlap: typing.Optional[int] = None,
        overlap_all: typing.Optional[bool] = None,
        extract_image_block_types: typing.Optional[PartitionParametersExtractImageBlockTypes] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_pipeline_mapped_args(
            files=files,
            strategy=strategy,
            gz_uncompressed_content_type=gz_uncompressed_content_type,
            output_format=output_format,
            coordinates=coordinates,
            encoding=encoding,
            hi_res_model_name=hi_res_model_name,
            include_page_breaks=include_page_breaks,
            languages=languages,
            pdf_infer_table_structure=pdf_infer_table_structure,
            skip_infer_table_types=skip_infer_table_types,
            xml_keep_tags=xml_keep_tags,
            chunking_strategy=chunking_strategy,
            multipage_sections=multipage_sections,
            combine_under_n_chars=combine_under_n_chars,
            new_after_n_chars=new_after_n_chars,
            max_characters=max_characters,
            overlap=overlap,
            overlap_all=overlap_all,
            extract_image_block_types=extract_image_block_types,
        )
        return self._create_pipeline_oapg(
            body=args.body,
        )


<div align="left">

[![Visit Unstructured](./header.png)](https://unstructured.io)

# Unstructured<a id="unstructured"></a>

At Unstructured, we're on a mission to give organizations access to all of their data. We know the world runs on documents—from research reports and memos, to quarterly filings and plans of action, documents are the unit of information that companies depend on. And yet, 80% of this information is trapped in inaccessible formats, and businesses have long struggled to unlock this data, leading to information silos, inefficient decision-making, and repetitive work. Until now.

Unstructured captures this unstructured data wherever it lives and transforms it into AI-friendly JSON files for companies who are eager to fold AI into their business.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`unstructured.general.create_pipeline`](#unstructuredgeneralcreate_pipeline)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Unstructured&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from unstructured_python_sdk import Unstructured, ApiException

unstructured = Unstructured(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Pipeline 1
    create_pipeline_response = unstructured.general.create_pipeline(
        files="{summary=File to be partitioned, externalValue=https://github.com/Unstructured-IO/unstructured/blob/98d3541909f64290b5efb65a226fc3ee8a7cc5ee/example-docs/layout-parser-paper.pdf}",
        strategy="hi_res",
        gz_uncompressed_content_type="application/pdf",
        output_format="application/json",
        coordinates=True,
        encoding="utf-8",
        hi_res_model_name="yolox",
        include_page_breaks=True,
        languages=["[eng]"],
        pdf_infer_table_structure=True,
        skip_infer_table_types=["string_example"],
        xml_keep_tags=True,
        chunking_strategy="by_title",
        multipage_sections=True,
        combine_under_n_chars=500,
        new_after_n_chars=1500,
        max_characters=1500,
        overlap=25,
        overlap_all=True,
        extract_image_block_types=["image", "table"],
    )
    print(create_pipeline_response)
except ApiException as e:
    print("Exception when calling GeneralApi.create_pipeline: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["detail"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from unstructured_python_sdk import Unstructured, ApiException

unstructured = Unstructured(
    api_key_auth="YOUR_API_KEY",
)


async def main():
    try:
        # Pipeline 1
        create_pipeline_response = await unstructured.general.acreate_pipeline(
            files="{summary=File to be partitioned, externalValue=https://github.com/Unstructured-IO/unstructured/blob/98d3541909f64290b5efb65a226fc3ee8a7cc5ee/example-docs/layout-parser-paper.pdf}",
            strategy="hi_res",
            gz_uncompressed_content_type="application/pdf",
            output_format="application/json",
            coordinates=True,
            encoding="utf-8",
            hi_res_model_name="yolox",
            include_page_breaks=True,
            languages=["[eng]"],
            pdf_infer_table_structure=True,
            skip_infer_table_types=["string_example"],
            xml_keep_tags=True,
            chunking_strategy="by_title",
            multipage_sections=True,
            combine_under_n_chars=500,
            new_after_n_chars=1500,
            max_characters=1500,
            overlap=25,
            overlap_all=True,
            extract_image_block_types=["image", "table"],
        )
        print(create_pipeline_response)
    except ApiException as e:
        print("Exception when calling GeneralApi.create_pipeline: %s\n" % e)
        pprint(e.body)
        if e.status == 422:
            pprint(e.body["detail"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from unstructured_python_sdk import Unstructured, ApiException

unstructured = Unstructured(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Pipeline 1
    create_pipeline_response = unstructured.general.raw.create_pipeline(
        files="{summary=File to be partitioned, externalValue=https://github.com/Unstructured-IO/unstructured/blob/98d3541909f64290b5efb65a226fc3ee8a7cc5ee/example-docs/layout-parser-paper.pdf}",
        strategy="hi_res",
        gz_uncompressed_content_type="application/pdf",
        output_format="application/json",
        coordinates=True,
        encoding="utf-8",
        hi_res_model_name="yolox",
        include_page_breaks=True,
        languages=["[eng]"],
        pdf_infer_table_structure=True,
        skip_infer_table_types=["string_example"],
        xml_keep_tags=True,
        chunking_strategy="by_title",
        multipage_sections=True,
        combine_under_n_chars=500,
        new_after_n_chars=1500,
        max_characters=1500,
        overlap=25,
        overlap_all=True,
        extract_image_block_types=["image", "table"],
    )
    pprint(create_pipeline_response.body)
    pprint(create_pipeline_response.headers)
    pprint(create_pipeline_response.status)
    pprint(create_pipeline_response.round_trip_time)
except ApiException as e:
    print("Exception when calling GeneralApi.create_pipeline: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["detail"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `unstructured.general.create_pipeline`<a id="unstructuredgeneralcreate_pipeline"></a>

Pipeline 1

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_pipeline_response = unstructured.general.create_pipeline(
    files="{summary=File to be partitioned, externalValue=https://github.com/Unstructured-IO/unstructured/blob/98d3541909f64290b5efb65a226fc3ee8a7cc5ee/example-docs/layout-parser-paper.pdf}",
    strategy="hi_res",
    gz_uncompressed_content_type="application/pdf",
    output_format="application/json",
    coordinates=True,
    encoding="utf-8",
    hi_res_model_name="yolox",
    include_page_breaks=True,
    languages=["[eng]"],
    pdf_infer_table_structure=True,
    skip_infer_table_types=["string_example"],
    xml_keep_tags=True,
    chunking_strategy="by_title",
    multipage_sections=True,
    combine_under_n_chars=500,
    new_after_n_chars=1500,
    max_characters=1500,
    overlap=25,
    overlap_all=True,
    extract_image_block_types=["image", "table"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### files: `IO`<a id="files-io"></a>

The file to extract

##### strategy: `str`<a id="strategy-str"></a>

The strategy to use for partitioning PDF/image. Options are fast, hi_res, auto. Default: auto

##### gz_uncompressed_content_type: `str`<a id="gz_uncompressed_content_type-str"></a>

If file is gzipped, use this content type after unzipping

##### output_format: `str`<a id="output_format-str"></a>

The format of the response. Supported formats are application/json and text/csv. Default: application/json.

##### coordinates: `bool`<a id="coordinates-bool"></a>

If true, return coordinates for each element. Default: false

##### encoding: `str`<a id="encoding-str"></a>

The encoding method used to decode the text input. Default: utf-8

##### hi_res_model_name: `str`<a id="hi_res_model_name-str"></a>

The name of the inference model used when strategy is hi_res

##### include_page_breaks: `bool`<a id="include_page_breaks-bool"></a>

If True, the output will include page breaks if the filetype supports it. Default: false

##### languages: [`PartitionParametersLanguages`](./unstructured_python_sdk/type/partition_parameters_languages.py)<a id="languages-partitionparameterslanguagesunstructured_python_sdktypepartition_parameters_languagespy"></a>

##### pdf_infer_table_structure: `bool`<a id="pdf_infer_table_structure-bool"></a>

If True and strategy=hi_res, any Table Elements extracted from a PDF will include an additional metadata field, 'text_as_html', where the value (string) is a just a transformation of the data into an HTML <table>.

##### skip_infer_table_types: [`PartitionParametersSkipInferTableTypes`](./unstructured_python_sdk/type/partition_parameters_skip_infer_table_types.py)<a id="skip_infer_table_types-partitionparametersskipinfertabletypesunstructured_python_sdktypepartition_parameters_skip_infer_table_typespy"></a>

##### xml_keep_tags: `bool`<a id="xml_keep_tags-bool"></a>

If True, will retain the XML tags in the output. Otherwise it will simply extract the text from within the tags. Only applies to partition_xml.

##### chunking_strategy: `str`<a id="chunking_strategy-str"></a>

Use one of the supported strategies to chunk the returned elements. Currently supports: by_title

##### multipage_sections: `bool`<a id="multipage_sections-bool"></a>

If chunking strategy is set, determines if sections can span multiple sections. Default: true

##### combine_under_n_chars: `int`<a id="combine_under_n_chars-int"></a>

If chunking strategy is set, combine elements until a section reaches a length of n chars. Default: 500

##### new_after_n_chars: `int`<a id="new_after_n_chars-int"></a>

If chunking strategy is set, cut off new sections after reaching a length of n chars (soft max). Default: 1500

##### max_characters: `int`<a id="max_characters-int"></a>

If chunking strategy is set, cut off new sections after reaching a length of n chars (hard max). Default: 1500

##### overlap: `int`<a id="overlap-int"></a>

A prefix of this many trailing characters from prior text-split chunk is applied to second and later chunks formed from oversized elements by text-splitting. Default: None

##### overlap_all: `bool`<a id="overlap_all-bool"></a>

When True, overlap is also applied to 'normal' chunks formed by combining whole elements. Use with caution as this can introduce noise into otherwise clean semantic units. Default: None

##### extract_image_block_types: [`PartitionParametersExtractImageBlockTypes`](./unstructured_python_sdk/type/partition_parameters_extract_image_block_types.py)<a id="extract_image_block_types-partitionparametersextractimageblocktypesunstructured_python_sdktypepartition_parameters_extract_image_block_typespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PartitionParameters`](./unstructured_python_sdk/type/partition_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Elements`](./unstructured_python_sdk/pydantic/elements.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/general/v0/general` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)

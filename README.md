## Open Photogrammetry Format (OPF)

This repository contains the specification for the _Open Photogrammetry Format_, also known as _OPF_.

The _Open Photogrammetry Format_ is an open format for interchange of photogrammetry data.
The specification defines the core elements of photogrammetry projects, such as the input and output of photogrammetric calibration and dense reconstruction. The format is designed to be [extensible](#extensions).

The following are defined in this specification:

- [Project structure][2]
- Cameras
  - [Camera list][3]
  - [Input Cameras][4]
  - [Projected Cameras][5]
  - [Calibrated Cameras][6]
- [Control points][7]
- [Geo-referencing information][8]
- [Calibration][9]
  - [Calibrated Cameras][6]
  - [Calibrated control points][10]
  - [GPS bias][11]
- [Point cloud and tracks][12]

A [glossary][1] is provided.

[1]: https://pix4d.github.io/opf-spec/specification/glossary.html "Glossary"
[2]: https://pix4d.github.io/opf-spec/specification/project.html "Project format specification"
[3]: https://pix4d.github.io/opf-spec/specification/camera_list.html "Camera list format"
[4]: https://pix4d.github.io/opf-spec/specification/input_cameras.html "Input camera format"
[5]: https://pix4d.github.io/opf-spec/specification/projected_input_cameras.html "Projected input camera format"
[6]: https://pix4d.github.io/opf-spec/specification/calibrated_cameras.html "Calibrated camera format"
[7]: https://pix4d.github.io/opf-spec/specification/control_points.html "Control Points"
[8]: https://pix4d.github.io/opf-spec/specification/scene_reference_frame.html "Scene reference frame format"
[9]: https://pix4d.github.io/opf-spec/specification/calibration.html "Calibration scene item"
[10]: https://pix4d.github.io/opf-spec/specification/control_points.html#format-specification-calibrated-control-points "Calibrated control points"
[11]: https://pix4d.github.io/opf-spec/specification/gps_bias.html "GPS bias"
[12]: https://pix4d.github.io/opf-spec/specification/point_cloud.html "Point cloud"


Examples of OPF files are available under the `examples` subfolder.

## JSON encoding

JSON files used throught this specification have the following restrictions on formatting and encoding.

1. JSON must use UTF-8 encoding
2. All strings defined in this spec (properties names, enums) use only ASCII charset and must be written as plain text.
3. Names (keys) within JSON objects must be unique, i.e., duplicate keys aren't allowed.

## URIs

This specification uses [URI references (RFC3986)](https://tools.ietf.org/html/rfc3986#section-4.1) to reference content.

## Extensions

### Purpose of extensions

OPF extensions enable OPF implementers to create new functionalities or to expand functionalities of the OPF core specification.
Extensions may expose features supported by a single vendor, but they can have multiple implementations.
To ease discovery, vetted extensions may become part of the OPF extension registry.
Extensions are written against a specific version of the OPF specification and may be promoted to the core OPF specification in a later OPF specification version.

### Extension mechanism

Extensions extend the base model format. Extensions can introduce new properties (including properties that reference external data, and the extension can define the format of those data).

All object properties have an optional `extensions` object property that can contain new extension-specific properties. This allows extensions to extend any part of OPF.

Extensions can't remove or redefine existing properties to mean something else.

Extensions may add new properties and values.
As much as possible these feature additions are designed to allow safe fallback consumption in tools that do not recognize an extension.
In case an application imports a OPF project with an unknown extension and re-exports it, it is desirable to preserve the extension. Extensions should be designed to be resilient to changes to their parent objects.

An example of a hypothetical `PIX4D_spatial_ref_sys` extension of [geo-referencing information][7] to add the URI of the grid used would be this: [scene-reference-frame-extension.json](examples/scene-reference-frame-extension.json).

### Creating Extensions

As per convention, the extension schema should allow additional properties to allow future extensibility of the extension.

Where an extension is meant to share data between teams or with a third party, its format should be specified and documented.
The specification of the extenstion should be documented under the "/extensions/<extension name>/" folder.

### Naming

Extensions names must be of the form:

`<UPPERCASE prefix>_<extension name>`

Names MUST use lowercase snake-case following the prefix, e.g. `OPF_some_extension`.

## JSON schema

[JSON schema](https://json-schema.org/) is the source of truth regarding conformance with the specification, with the caveat that not all the semantics in the specification can be captured in a schema. The schemas are located in the `schema` directory.

Note that by convention schemas of this specification always allow additional properties, this is required to suppport forward compatibility of the format. Such additionnal properties are strictly reserved for future version of the specification and shall not be used for the purpose of extensions. Extensions of the specification are provided through the [extensions mechanism](#extensions) exclusively.

### Custom extensions to JSON schema

In some instances we have slightly extended the JSON schema vocabularies in order to add additional data that may be used to further validate a compliance with the specification.
These extensions are described below:

- New properties in project.schema.json : `required_resources_per_item_type`, `optional_resources_per_item_type`, `required_sources_per_item_type` and `optional_sources_per_item_type` dictionnaries describe which _resources_ and which _sources_ are required and optional for a given item type.

In addition, in the spirit of forward compatibility, we relax the requirement of JSON schemas with respect to the `enum` keyword, which we redefine as an open-ended list of values for the purpose of this specification.

## Citation

If you use the OPF specification in your research or projects, we kindly request that you cite it as follows:

`The Open Photogrammetry Format Specification, Grégoire Krähenbühl, Klaus Schneider-Zapp, Bastien Dalla Piazza, Juan Hernando, Juan Palacios, Massimiliano Bellomo, Mohamed-Ghaïth Kaabi, Christoph Strecha, Pix4D, 2023, retrived from https://pix4d.github.io/opf-spec/`

## License

Copyright (c) 2023 Pix4D SA

This specification and all the associated files, including but not limited to the markdown files, json schemas and any automatically generated HTML and PDF files are licensed under the Creative Commons Attribution 4.0 International License (CC BY-SA 4.0).

All scripts and/or code contained in this repository are licensed under Apache License 2.0.

Third party documents or tools that are used or referred to in this specification are licensed under their own terms by their respective copyright owners.

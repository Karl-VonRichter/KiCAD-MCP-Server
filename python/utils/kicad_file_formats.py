"""File-format versions for newly generated KiCad files.

These date stamps are independent of the application version. KiCad 10.0.6
writes schematic version 20260306 (variant BOM semantics), as defined in
eeschema/sch_file_versions.h at the upstream 10.0.6 tag and confirmed with
``kicad-cli sch upgrade --force``. Existing files retain their own versions;
changing a header alone is not a format migration.
"""

SCHEMATIC_VERSION = 20260306
SCHEMATIC_HEADER = (
    f'(kicad_sch (version {SCHEMATIC_VERSION}) (generator "eeschema")'
    ' (generator_version "10.0")\n\n'
)

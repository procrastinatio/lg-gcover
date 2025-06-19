"""
Schema management module for gcover.

This module provides tools for:
- Extracting schemas from ESRI geodatabases (requires arcpy)
- Comparing schemas and tracking changes
- Generating documentation and diagrams
- Transforming between different schema formats
"""

# Import des classes principales
from .models import (ESRISchema, Field, FeatureClass, RelationshipClass, Table, Index, RelationshipClass, Subtype,
   SubtypeValue, RangeDomain,CodedDomain, CodedValue)
from .differ import (SchemaDiff, ChangeType,FieldChange,DomainChange, TableChange, RelationshipChange, SubtypeChange)
from .transformer import transform_esri_json
from .exporters.json import export_esri_schema_to_json
from .exporters.plantuml import  generate_plantuml_from_schema
from .reporter import generate_report

# Import conditionnel de l'extracteur (nécessite arcpy)
try:
    from .extractor import extract_schema, can_extract_schema
except ImportError:
    # arcpy n'est pas disponible
    def extract_schema(*args, **kwargs):
        raise ImportError("extract_schema requires arcpy")

    def can_extract_schema():
        return False

# Import des exporteurs
# TODO
'''from .exporters import (
    export_esri_schema_to_json,
    export_schema_diff_to_json,
    generate_plantuml_from_schema
)'''

__all__ = [
    # Classes principales
    "ESRISchema",
    "Field",
    "FeatureClass",
    "Table",
    "Index",
    "RelationshipClass",
    "Subtype",
    "SubtypeValue",
    "RangeDomain",
    "CodedDomain",
    "CodedValue",
    "SchemaDiff",


    # Fonctions
    "extract_schema",
    "can_extract_schema",
    "transform_esri_json",
    "export_esri_schema_to_json",
    # "export_schema_diff_to_json",
    "generate_plantuml_from_schema",
    "generate_report"
]
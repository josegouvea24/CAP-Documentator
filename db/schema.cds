namespace sap.capdocumentator;

using {
    cuid,
} from '@sap/cds/common';

entity VecSummaries: cuid {
  filePath    : String(255);
  capSection  : String(64);
  fileType    : String(32);
  content     : LargeString;
  summary     : LargeString;
  metadata    : LargeString;
  embedding   : Vector(1536);
}
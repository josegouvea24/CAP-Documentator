namespace sap.capdocumentator;

using {
    cuid
} from '@sap/cds/common';

entity VecSummaries {
  summary     : LargeString;
  metadata    : LargeString;
  embedding  : Vector;
}
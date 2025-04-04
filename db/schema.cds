namespace sap.capdocumentator;

using {
    cuid,
} from '@sap/cds/common';

entity Repository : cuid {
      name   : String;
      url    : String;
      files  : Association to many File 
                  on files.repo = $self;
}

entity File : cuid {
      name           : String;
      relativePath   : String;
      type           : String;
      repo   : Association to one Repository;
}
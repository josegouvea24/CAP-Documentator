using { sap.capdocumentator as db } from '../db/schema';

@path: 'DocumentationService'
service DocumentationService {
    // Views
    entity Repositories as projection on db.Repository;
    entity Files        as projection on db.File;

    // Actions
    action fetchReadMeFromGitHub(repoUrl: String) returns String;
}
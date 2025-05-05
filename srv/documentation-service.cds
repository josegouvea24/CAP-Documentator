using { sap.capdocumentator as db } from '../db/schema';

@path: 'DocumentationService'
service DocumentationService {

    // Actions
    action fetchReadMeFromGitHub(repoUrl: String) returns String;
}
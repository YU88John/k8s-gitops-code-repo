#!/bin/bash

repositoryOwner="YU88John"  
repositoryName="k8s-gitops-manifests-repo"  
baseBranch="main"  
headBranch="dev"  
pullRequestTitle="Updated image version - Build #${BUILD_NUMBER}"
pullRequestBody="Please pull these awesome changes in! Check it out!"

apiUrl="https://api.github.com/repos/${repositoryOwner}/${repositoryName}/pulls"
payload="{
    \"title\": \"${pullRequestTitle}\",
    \"body\": \"${pullRequestBody}\",
    \"head\": \"${repositoryOwner}:${headBranch}\",
    \"base\": \"${baseBranch}\"
}"

curl -L \
    -X POST \
    -H 'Accept: application/vnd.github+json' \
    -H 'Authorization: Bearer '${GITHUB_TOKEN} \
    -H 'X-GitHub-Api-Version: 2022-11-28' \
    ${apiUrl} \
    -d "${payload}"

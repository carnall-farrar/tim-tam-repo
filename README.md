# CF template repository

This repository is a template for analytical and product projects at CF, written in Python.

It comprises a recommended folder structure, git configuration and utilities.

Click `Use this template` above to create a new repo in GitHUb which use this template.

## Things to change
Once you have created the new repo, the following actions are important:

#### Rename the `src` directory

To stick to python convention, name the main code folder after the name of the project. 
Choose a name that is short and easy for others to find when searching. 

#### Rename the project in the `pyproject.toml`
The `name` attribute in the `pyproject.toml` is currently set to the template name, but must be set to the new project name.

Please also update the project description in the `pyproject.toml`.

#### Add `.env` file with AWS credentials
A `.env` file contains environment variables, including things like passwords for interacting with our data in AWS.
By default, any `.env` file is not tracked by git, as it is listed in the `.gitignore`
Never commit a `.env` file to git, as this risks sharing secret AWS login information outside the organisation.

Usual contents of `.env` are:

  export AWS_ACCESS_KEY="my-access-key"
  export AWS_SECRET_KEY="my-secrete-key"
  export AWS_ATHENA_S3_STAGING_DIR="my-staging-dir"
  export AWS_REGION="my-region"
  export AWS_ATHENA_SCHEMA_NAME="my-schema-name"

#### Github actions
Note GitHub actions have been deactivated by default.
Actions will bill the CF account each time they run, so please don't re-enable them unless you know they are needed.

#### Replace this README.md
Use a readme that explains your project, e.g. using `template_readme.md`.


## General documentation

#### `data` vs `static` directories
The `data` directory is for storing raw data, processed data (produced by this code but not final) and output data.
The contents of these folders should not be tracked by git,
because they may contain sensitive information and may be large in size.

The `static` directory is for static (unchanging) data that is needed for the code to run and is not sensitive,
such as lookup tables. These need to be shared between developers using the code, and should be tracked by git.


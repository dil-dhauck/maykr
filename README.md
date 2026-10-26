# Maykr

Generate realistic test Excel files for development and testing the AI assistant made by Quake team.


## Installation

Install the required dependency:

```bash
pip install typer
pip install openpyxl
pip install faker
```

Than simply install maykr:
```bash
git clone https://github.com/dil-dhauck/maykr.git
cd maykr && pip install -e .
```

## Configuration

Create the following configuration file:

```text
~/.config/maykr/config.json
```

On Windows, this corresponds to:

```text
%USERPROFILE%\.config\maykr\config.json
```

Example configuration:

```json
{
    "output_directory": "~/Documents/test_files",
    "number_of_files": 10
}
```

`output_directory` is where generated files will be saved.

## Usage

Generate test files:

```bash
maykr create
```

This command creates the files in:

```text
$output_directory/generated/
```

For the example configuration above, the files would be generated in:

```text
~/Documents/test_files/generated/
```

for more QA info about Data Import, check out our confluence page:

[Confluence Page](https://diligentbrands.atlassian.net/wiki/spaces/BPOW/folder/7412810128?atlOrigin=eyJpIjoiMzc1Zjc0OTEwZTYwNDIyZTk5Mjg0OWQxZmM1ZTdkZWEiLCJwIjoiYyJ9)

# Maykr

Generate realistic test Excel files for development and testing.

## Installation

Install the required dependency:

```bash
pip install typer
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
    "output_directory": "~/Documents/test_files"
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

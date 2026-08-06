#dependencies:
- typer

#config

create this:
%HOME%/.config/maykr/config.json

like this for example:
```json
{
    "output_directory": "~/Documents/test_files"
}
```

#usage
generate test files into the folder you put in config:
```
maykr run
```

It puts generates 5 files in $output_directory/generated/

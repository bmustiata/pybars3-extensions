# pybars3_extensions

pybars3_extensions library.

This introduces `#each`, `#case` and `#default` for building `switch`/`case`
statements.

## Usage

Template:

```hbs
{{#each cool.items}}
{{#switch this.type}}
{{#case '1'}}MATCH: {{this}}{{/case}}
{{#default}}NO MATCH{{/default}}
{{/switch}}
{{/each}}
```

Python code:

```py
from pybars3_extensions import helpers

# ...

hbs = pybars.Compiler().compile(source=template)
print(hbs(data, helpers=helpers))
```

## Installation

```sh
pip install pybars3_extensions
```


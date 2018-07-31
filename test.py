from typing import List
import pybars
from pybars3_extensions import helpers


class Cool(object):
    """
    Some items holder
    """
    items: List[str]

    def __init__(self,
                 items: List[str]) -> None:
        self.items = items


data = {
    "cool" : Cool(items=[
        {"type": "1", "value": "one"},
        {"type": "2", "value": "two"},
        {"type": "3", "value": "three"},
    ])
}

template = """\
{{#each cool.items}}
{{#switch this.type}}
{{#case '1'}}MATCH: {{this}}{{/case}}
{{#default}}NO MATCH: {{this}}{{/default}}
{{/switch}}
# the switch is done.
{{this}}
{{#if this}}
yay
{{else}}
nay
{{/if}}{{/each}}
"""


import traceback
import sys


hbs = pybars.Compiler().compile(source=template)
print(hbs(data, helpers=helpers))


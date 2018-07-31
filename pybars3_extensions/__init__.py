from typing import Any, List


class SwitchEntry(object):
    """
    A Switch entry that is executing in the handlebars
    template.
    """
    switch_value: Any
    matched: bool

    def __init__(self,
                 switch_value: Any,
                 matched: bool = False) -> None:
        self.switch_value = switch_value
        self.matched = matched


switch_values: List[SwitchEntry] = []


def switch_call(scope, partials, value: object) -> Any:
    switch_values.append(SwitchEntry(switch_value=value))
    result = partials['fn'](scope)
    switch_values.pop()

    return result


def case_call(scope, partials, value: object) -> Any:
    if switch_values[-1].switch_value == value:
        switch_values[-1].matched = True
        return partials['fn'](scope)


def default_call(scope, partials) -> Any:
    if not switch_values[-1].matched:
        return partials['fn'](scope)


helpers = {
    "switch": switch_call,
    "case": case_call,
    "default": default_call
}


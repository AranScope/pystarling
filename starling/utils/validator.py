from collections import namedtuple

from starling.errors import TypeValidationError

ParameterDefinition = namedtuple("Validation", ("name", "definitions"))


def _run_validations(pos, name, validations, value=None):

    if validations[0] == "optional":
        if value is not None and not isinstance(value, validations[1]):
            return "{name} parameter in position {pos} is an optional {rule} but was {value_type}".format(
                name=name,
                pos=pos,
                rule=validations[1],
                value_type=type(value)
            )

    if validations[0] == "required":
        if value is not None and not isinstance(value, validations[1]):
            return "{name} parameter in position {pos} is an optional {rule} but was {value_type}".format(
                name=name,
                pos=pos,
                rule=validations[1],
                value_type=type(value)
            )
        elif value is None:
            return "{name} parameter in position {pos} is an optional {rule} but was {value}".format(
                name=name,
                pos=pos,
                rule=validations[1],
                value=value
            )

    return None


def type_validation(arguments, definitions):
    problems = []

    for pos, definition in enumerate(definitions):

        if arguments:
            problem = _run_validations(pos, definition["name"], definition["validations"], arguments[pos])
        else:
            problem = _run_validations(pos, definition["name"], definition["validations"])

        if problem is not None:
            problems.append(problem)

    if problems:
        raise TypeValidationError(problems)


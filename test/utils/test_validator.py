from starling.errors import TypeValidationError
from starling.utils.validator import type_validation

rule_set = [
    {"name": "iAmRequiredObject", "validations": ["required", object]},
    {"name": "iAmRequiredNumber", "validations": ["required", int]},
    {"name": "iAmRequiredString", "validations": ["required", str]}
]

second_rule_set = [
    {"name": "iAmRequiredNumber", "validations": ["required", int]},
    {"name": "iAmRequiredString", "validations": ["required", str]},
    {"name": "iAmRequiredString", "validations": ["optional", str]}
]

wonky_rule_set = [
    {"name": "iAmRequiredNumber", "validations": ["required", int]},
    {"name": "iAmRequiredString", "validations": ["optional", str]},
    {"name": "iAmRequiredString", "validations": ["required", str]}
]


def test_correct_types():
    try:
        type_validation([{"a": 1}, 42, "HAI"], rule_set)
    except TypeValidationError:
        assert False


def test_correct_types_and_additional_types():
    try:
        type_validation([{"a": 1}, 42, "HAI", 1, 2, 3, 4], rule_set)
    except TypeValidationError:
        assert False


def test_correct_types_with_excluded_optionals():
    try:
        type_validation([42, "HAI", None], second_rule_set)
    except TypeValidationError:
        assert False


def test_undefined_input_required():
    try:
        type_validation([], second_rule_set)
        assert False
    except TypeValidationError:
        assert True


def test_accept_less_args_than_defs():
    try:
        type_validation([None, None, None], wonky_rule_set)
        assert False
    except TypeValidationError as e:
        assert len(e.validation_errors) == 2


def test_optional_args_of_wrong_type():
    try:
        type_validation([1, 3, "sd"], second_rule_set)
        assert False
    except TypeValidationError as e:
        assert len(e.validation_errors) == 1

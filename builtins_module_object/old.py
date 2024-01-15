import inspect
import pprint
import pandas as pd
import numpy as np

__version__ = '0.4.2'

def categorize_identifiers_dict(obj=None, second=object, unique_only=False, consistent_only=False, has_parameter=''):
    """ 
    Categorize identifiers from an object into different groups.

    Parameters:
    - obj: The object to inspect. If None, it defaults to the global namespace at runtime.
    - second: An optional second class for comparison, normally a parent class.
    - unique_only: Show only identifiers that are unique to the first class.
    - consistent_only: Show identifiers in the first class that also occur in the second class.
                     These are inherited from the second class when the second class is a parent class.
    - has_parameter: Filter functions by whether they have a specific parameter.

    Returns:
    - A dictionary with categories as keys and lists of identifiers as values.
    """
    
    if obj is None:
        frame = inspect.currentframe().f_back
        obj = frame.f_globals.copy()
        del frame

    if inspect.isclass(obj):
        obj = vars(obj)
    elif hasattr(obj, '__dict__'):
        obj = vars(obj)
    
    try:
        identifiers = list(obj.keys())
    except AttributeError:
        # If obj doesn't have keys, it may not be a dictionary-like object.
        identifiers = []

    if isinstance(second, list):
        second_identifiers = []
        for identifier in second:
            second_identifiers.extend(dir(identifier))
        second_identifiers = list(set(second_identifiers))
        second_identifiers.sort()
    else:
        second_identifiers = dir(second)
    
    if not (unique_only or consistent_only):
        identifiers_to_examine = identifiers
    else:
        unique_identifiers = set(identifiers) - set(second_identifiers)
        inherited_identifiers = set(identifiers) & set(second_identifiers) 
        if not consistent_only:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in unique_identifiers]
        else:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in inherited_identifiers]

    grouping_dict = {
        'attribute': [],
        'constant': [],
        'module': [],
        'method': [],
        'lower_class': [],
        'upper_class': [],
        'datamodel_attribute': [],
        'datamodel_method': [],
        'internal_attribute': [],
        'internal_method': [],
    }

    for identifier in identifiers_to_examine:
        is_method = callable(obj[identifier])
        is_class = type(obj[identifier]) == type
        is_upper = identifier[0].isupper()
        is_datamodel = identifier[0:2] == '__' and len(identifier) > 3
        is_internal = ((identifier[0:1] == '_') and not is_datamodel)

        if is_method and is_datamodel:
            grouping_dict['datamodel_method'].append(identifier)
        if not is_method and is_datamodel and not is_internal:
            grouping_dict['datamodel_attribute'].append(identifier)
        if is_upper and is_class and not is_datamodel and not is_internal:
            grouping_dict['upper_class'].append(identifier)
        if not is_upper and is_class and not is_datamodel and not is_internal:
            grouping_dict['lower_class'].append(identifier)
        if is_method and not is_upper and not is_class and not is_datamodel and not is_internal:
            grouping_dict['method'].append(identifier)
        if not is_method and is_upper and not is_datamodel and not is_internal:
            grouping_dict['constant'].append(identifier)
        if not is_method and not is_upper and not is_class and not is_datamodel and not is_internal:
            grouping_dict['attribute'].append(identifier)
        if is_method and is_internal:
            grouping_dict['internal_method'].append(identifier)
        if not is_method and is_internal:
            grouping_dict['internal_attribute'].append(identifier)
        if is_class and is_method and identifier not in grouping_dict['module']:
            try:
                is_module = inspect.ismodule(obj[identifier])
                if is_module:
                    grouping_dict['module'].append(identifier)
            except AttributeError:
                pass

    if has_parameter != '':
        function_with_parameter = []
        for identifier in grouping_dict['method']:
            try:
                signature = inspect.signature(obj[identifier])
                if has_parameter in signature.parameters:
                    function_with_parameter.append(identifier)
            except Exception:
                pass  # ignore any errors, continue with the next identifier
        grouping_dict['method'] = function_with_parameter

    return grouping_dict

def categorize_identifiers_print(obj=None, second=object, unique_only=False, consistent_only=False, has_parameter=''):
    """ 
    Categorize identifiers from an object into different groups.

    Parameters:
    - obj: The object to inspect. If None, it defaults to the global namespace at runtime.
    - second: An optional second class for comparison, normally a parent class.
    - unique_only: Show only identifiers that are unique to the first class.
    - consistent_only: Show identifiers in the first class that also occur in the second class.
                     These are inherited from the second class when the second class is a parent class.
    - has_parameter: Filter functions by whether they have a specific parameter.

    Prints:
    - A dictionary with categories as keys and lists of identifiers as values.
    """
    
    if obj is None:
        frame = inspect.currentframe().f_back
        obj = frame.f_globals.copy()
        del frame

    if inspect.isclass(obj):
        obj = vars(obj)
    elif hasattr(obj, '__dict__'):
        obj = vars(obj)
    
    try:
        identifiers = list(obj.keys())
    except AttributeError:
        # If obj doesn't have keys, it may not be a dictionary-like object.
        identifiers = []

    if isinstance(second, list):
        second_identifiers = []
        for identifier in second:
            second_identifiers.extend(dir(identifier))
        second_identifiers = list(set(second_identifiers))
        second_identifiers.sort()
    else:
        second_identifiers = dir(second)
    
    if not (unique_only or consistent_only):
        identifiers_to_examine = identifiers
    else:
        unique_identifiers = set(identifiers) - set(second_identifiers)
        inherited_identifiers = set(identifiers) & set(second_identifiers) 
        if not consistent_only:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in unique_identifiers]
        else:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in inherited_identifiers]

    grouping_dict = {
        'attribute': [],
        'constant': [],
        'module': [],
        'method': [],
        'lower_class': [],
        'upper_class': [],
        'datamodel_attribute': [],
        'datamodel_method': [],
        'internal_attribute': [],
        'internal_method': [],
    }

    for identifier in identifiers_to_examine:
        is_method = callable(obj[identifier])
        is_class = type(obj[identifier]) == type
        is_upper = identifier[0].isupper()
        is_datamodel = identifier[0:2] == '__' and len(identifier) > 3
        is_internal = ((identifier[0:1] == '_') and not is_datamodel)

        if is_method and is_datamodel:
            grouping_dict['datamodel_method'].append(identifier)
        if not is_method and is_datamodel and not is_internal:
            grouping_dict['datamodel_attribute'].append(identifier)
        if is_upper and is_class and not is_datamodel and not is_internal:
            grouping_dict['upper_class'].append(identifier)
        if not is_upper and is_class and not is_datamodel and not is_internal:
            grouping_dict['lower_class'].append(identifier)
        if is_method and not is_upper and not is_class and not is_datamodel and not is_internal:
            grouping_dict['method'].append(identifier)
        if not is_method and is_upper and not is_datamodel and not is_internal:
            grouping_dict['constant'].append(identifier)
        if not is_method and not is_upper and not is_class and not is_datamodel and not is_internal:
            grouping_dict['attribute'].append(identifier)
        if is_method and is_internal:
            grouping_dict['internal_method'].append(identifier)
        if not is_method and is_internal:
            grouping_dict['internal_attribute'].append(identifier)
        if is_class and is_method and identifier not in grouping_dict['module']:
            try:
                is_module = inspect.ismodule(obj[identifier])
                if is_module:
                    grouping_dict['module'].append(identifier)
            except AttributeError:
                pass

    if has_parameter != '':
        function_with_parameter = []
        for identifier in grouping_dict['method']:
            try:
                signature = inspect.signature(obj[identifier])
                if has_parameter in signature.parameters:
                    function_with_parameter.append(identifier)
            except Exception:
                pass  # ignore any errors, continue with the next identifier
        grouping_dict['method'] = function_with_parameter

    pprint.pprint(grouping_dict, sort_dicts=False)



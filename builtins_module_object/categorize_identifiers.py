"""dir gives a list of identifiers. This module has the function categorize_identifiers_dict which categorizes these identifiers 
into groups within a dict and the function categorize_identifiers_dict which pretty prints this dict."""

import inspect
import pprint

__version__ = '0.9.9'

def categorize_identifiers_dict(obj='default', second=object, unique_only=False, consistent_only=False, parameter=''):
    """ 
    Categorize identifiers from an object into different groups.

    Parameters:
    - obj: The object to inspect. If None, it defaults to the global namespace at runtime.
    - second: An optional second class for comparison, normally a parent class.
    - unique_only: Show only identifiers that are unique to the first class.
    - consistent_only: Show identifiers in the first class that also occur in the second class.
                     These are inherited from the second class when the second class is a parent class.
    - parameter: Filter functions by whether they have a specific parameter.

    Returns:
    - A dictionary with categories as keys and lists of identifiers as values.
    """
    
    if obj == 'default':
        frame = inspect.currentframe().f_back
        obj = frame.f_globals.copy()
        del frame
    else:
        try: 
            obj.__dict__.keys()
            if hasattr(obj.__dict__.keys(), '__package__'):
                identifiers = list(obj.__dict__.keys())
            else:
                identifiers = dir(obj)
        except:    
            identifiers = dir(obj)

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
        try:
            is_method = callable(getattr(obj, identifier))
            is_class = inspect.isclass(getattr(obj, identifier))
        except Exception:
            continue  # Ignore errors and continue with the next identifier

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
                is_module = inspect.ismodule(getattr(obj, identifier))
                if is_module:
                    grouping_dict['module'].append(identifier)
            except AttributeError:
                pass

    if parameter != '':
        function_with_parameter = []
        for identifier in grouping_dict['method']:
            try:
                signature = inspect.signature(getattr(obj, identifier))
                if parameter in signature.parameters:
                    function_with_parameter.append(identifier)
            except Exception:
                pass  # Ignore any errors and continue with the next identifier
        
        grouping_dict.clear()
        grouping_dict['method'] = function_with_parameter

    return grouping_dict

def categorize_identifiers_print(obj='default', second=object, unique_only=False, consistent_only=False, parameter=''):
    """ 
    Categorize identifiers from an object into different groups.

    Parameters:
    - obj: The object to inspect. If None, it defaults to the global namespace at runtime.
    - second: An optional second class for comparison, normally a parent class.
    - unique_only: Show only identifiers that are unique to the first class.
    - consistent_only: Show identifiers in the first class that also occur in the second class.
                     These are inherited from the second class when the second class is a parent class.
    - parameter: Filter functions by whether they have a specific parameter.

    Prints:
    - A dictionary with categories as keys and lists of identifiers as values.
    """
    
    if obj == 'default':
        frame = inspect.currentframe().f_back
        obj = frame.f_globals.copy()
        del frame
    else:
        try: 
            obj.__dict__.keys()
            if hasattr(obj.__dict__.keys(), '__package__'):
                identifiers = list(obj.__dict__.keys())
            else:
                identifiers = dir(obj)
        except:    
            identifiers = dir(obj)

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
        try:
            is_method = callable(getattr(obj, identifier))
            is_class = inspect.isclass(getattr(obj, identifier))
        except Exception:
            continue  # Ignore errors and continue with the next identifier

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
                is_module = inspect.ismodule(getattr(obj, identifier))
                if is_module:
                    grouping_dict['module'].append(identifier)
            except AttributeError:
                pass

    if parameter != '':
        function_with_parameter = []
        for identifier in grouping_dict['method']:
            try:
                signature = inspect.signature(getattr(obj, identifier))
                if parameter in signature.parameters:
                    function_with_parameter.append(identifier)
            except Exception:
                pass  # Ignore any errors and continue with the next identifier
        
        grouping_dict.clear()
        grouping_dict['method'] = function_with_parameter

    pprint.pprint(grouping_dict, sort_dicts=False)
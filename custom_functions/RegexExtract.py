def RegexExtract(input_string=None, input_pattern=None, **kwargs):
    """
    Args:
        input_string: The input string from which to extract the desired values.
        input_pattern: The regex pattern to use to extract the desired value(s) from the input_string.
    
    Returns a JSON-serializable object that implements the configured data paths:
        match_list: A list containing all of the regex-extracted values.
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import re
        
    outputs = []
    match_list = []
    if input_string and input_pattern:
        matches = re.findall(input_pattern, input_string)
        for group in set(matches):
            match_list.append(group)
    if match_list:
        for matc in set(match_list):
            outputs.append({"match_list": matc})
    else:
        outputs.append({"match_list": None})

    phantom.debug("RegexExtract extracted: {}".format(outputs))
    
    # Return a JSON-serializable object
    assert isinstance(outputs, list)  # Will raise an exception if the :outputs: object is not a list
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs

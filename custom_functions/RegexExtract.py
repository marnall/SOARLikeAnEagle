def RegexExtract(input_string=None, regex=None, regex_flags=None, **kwargs):
    """
    This function extracts a substring from a string using a regex expression.
    
    Args:
        input_string: The input string(s) from which to extract the desired values.
        regex: The regex pattern to use to extract the desired value(s) from the input_string.
        regex_flags: Flags as a parameter to the python re function. If using multiple flags, then separate them with a comma or | character.
            
            Examples:
            
            re.ASCII
            re.IGNORECASE
            re.MULTILINE
            re.DOTALL
            re.VERBOSE
            re.LOCALE
    
    Returns a JSON-serializable object that implements the configured data paths:
        *.match: The regex extracted section of the input string.
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import re
        
    outputs = []
    match_list = []
    
    # --- Custom code below ---
    funcname = "RegexExtract"
    phantom.debug("--- STARTING {} ---".format(funcname))
    
    # Error checking
    if input_string == None:
        phantom.debug("ERROR: Need input_string")
        return 1
    if regex == None:
        phantom.debug("ERROR: Need regex")
        return 1
    if "(" not in regex:
        phantom.debug("ERROR: regex does not have a capture group ()")
        return 1
    
    # Since SOAR auto escapes string inputs, the backslashes need to be un-escaped \\ -> \
    regex = regex.replace('\\\\','\\')
    
    if regex_flags != None:
        regex_flags = regex_flags.replace(",","|")
    
    matches = []
    # For each string in the input list, grab all 
    if regex_flags != None:   
        matches = re.findall(regex, input_string, flags=regex_flags)
    else:
        matches = re.findall(regex, input_string)
        
    for mat in matches:
        outputs.append({'match': mat})       
    
    phantom.debug("RegexExtract extracted: {}".format(outputs))
    phantom.debug("--- FINISHED {} ---".format(funcname))
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs

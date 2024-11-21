def String_RegexReplace(string_in=None, regex_pattern=None, string_replace_with=None, regex_flags=None, **kwargs):
    """
    This function replaces a substring from a string, with another string, using a regex expression.
    
    Args:
        string_in: The input string from which to extract the desired values.
        regex_pattern: The regex pattern to use to extract the desired value(s) from the input_string. Must have a capture group!
        string_replace_with: The string to insert in place of the matched group of the regex pattern. Can be left blank to simply delete the matched text.
        regex_flags: Flags as a parameter to the python re function. If using multiple flags, then separate them with a comma or | character.
            
            Examples:
            
            re.ASCII
            re.IGNORECASE
            re.MULTILINE
            re.DOTALL
            re.VERBOSE
            re.LOCALE
    
    Returns a JSON-serializable object that implements the configured data paths:
        string_out: The output string, after the regex has made the replacement.
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    
    # Write your custom code here...
    import re
    outputs = []
    match_list = []
    funcname = "String_RegexReplace"
    phantom.debug("--- STARTING {} ---".format(funcname))
    
    # Error checking
    if string_in == None:
        phantom.debug("ERROR: Need input_string")
        return 1
    if regex_pattern == None:
        phantom.debug("ERROR: Need regex")
        return 1
    if "(" not in regex_pattern or ")" not in regex_pattern:
        phantom.debug("ERROR: regex does not have a capture group ()")
        return 1
    if string_replace_with == None:
        string_replace_with = ""
    
    # Since SOAR auto escapes string inputs, the backslashes need to be un-escaped \\ -> \
    regex_pattern = regex_pattern.replace('\\\\','\\')
    
    # Regex flags:
    # From the python source code:
    #define SRE_FLAG_IGNORECASE 2
    #define SRE_FLAG_LOCALE 4
    #define SRE_FLAG_MULTILINE 8
    #define SRE_FLAG_DOTALL 16
    #define SRE_FLAG_VERBOSE 64
    #define SRE_FLAG_ASCII 256
    
    string_out = ""
    if regex_flags != None:
        flagsum = 0
        if "re.I" in regex_flags or "re.IGNORECASE" in regex_flags:
            flagsum += 2
        if "re.L" in regex_flags or "re.LOCALE" in regex_flags:
            flagsum += 4
        if "re.M" in regex_flags or "re.MULTILINE" in regex_flags:
            flagsum += 8
        if "re.S" in regex_flags or "re.DOTALL" in regex_flags:
            flagsum += 16
        if "re.A" in regex_flags or "re.ASCII" in regex_flags:
            flagsum += 256
        if "re.X" in regex_flags or "re.VERBOSE" in regex_flags:
            flagsum += 64
        string_out = re.sub(regex_pattern, string_replace_with, string_in, flags=flagsum)
    else:
        string_out = re.sub(regex_pattern, string_replace_with, string_in)
        
    outputs = {'string_out': string_out}    
    
    phantom.debug("{0} extracted: {1}".format(funcname,outputs))
    phantom.debug("--- FINISHED {} ---".format(funcname))
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs

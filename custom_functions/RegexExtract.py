def RegexExtract(input=None, pattern=None, flags=None, **kwargs):
    """
    Args:
        input
        pattern
        flags
    
    Returns a JSON-serializable object that implements the configured data paths:
        group1
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs

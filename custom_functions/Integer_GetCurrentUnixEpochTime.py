def Integer_GetCurrentUnixEpochTime(integer_offset=None, **kwargs):
    """
    This function outputs the current unix time. Can also take an optional integer offset.
    
    Args:
        integer_offset: An offset to add to the current timestamp. Should be an integer. Can be negative. Defaults to 0.
    
    Returns a JSON-serializable object that implements the configured data paths:
        integer_unixtime: The current unixtime. E.g. 1711573836
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    from datetime import datetime
    
    if integer_offset == None:
        integer_offset = 0
    
    outputs['integer_unixtime'] = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() + int(integer_offset)
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs

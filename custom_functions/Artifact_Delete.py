def Artifact_Delete(id_artifact=None, **kwargs):
    """
    Given an input artifact ID, this function will delete the artifact.
    WARNING: This action is permanent. Be sure that the input artifact IDs are correct!
    
    Args:
        id_artifact: The ID of the artifact to delete. 
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.delete_artifact(id_artifact)
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs

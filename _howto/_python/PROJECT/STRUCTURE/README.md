```
@function (*args: <type>, **kwargs: <type>) -> <type> {
  __doc__ = {
    Parameters
    ----------
    <param_name> : <param_type>
      <param_description>

    Returns | Yields
    ----------------
    <param_type>
      <param_descripton>
  }

  @input_type_check
  <not_required_type>
    convert
  </not_required_type>

  <code>

    @try_catch
    <undefined_errors>
      raise
    </undefined_errors>

  </code>

  @convert_output to the next function required type
}


**class (*init) {
  __doc__

  @execute_queries (...) {
    executing all functions for this class
  }

}
```

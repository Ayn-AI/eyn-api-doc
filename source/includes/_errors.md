# Errors

The EYN API uses the following error codes:

Error Code | Meaning
---------- | -------
400 | Bad Request -- Your request is invalid. Investigate the parameters of your API call. The error message contains pointers what has gone wrong.
401 | Unauthorized -- Your Cognito Id Token is wrong. Every query must contain a header with a valid Cognito Id Token (see [Authentication](#authentication) for details.)
503 | Service Unavailable -- We're temporarily offline for maintenance. Please try again later.

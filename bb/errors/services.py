from bb.apis.api import api


class ServiceUnavailableError(Exception):
    """Example of some custom exception that can be raised in any of the APIs that will trigger a specific handler"""
    pass


@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, exc):
    return api.create_response(
        request,
        {"message": "Please retry later"},
        status=503,
    )

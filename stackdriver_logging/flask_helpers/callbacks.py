from flask import request

from stackdriver_logging.jsonlog import get_logger
from stackdriver_logging.tracing import start_traced_span, end_traced_span


def before_request(excluded_routes=None, excluded_routes_partial=None):
    """
    Start a span and log the incoming request.

    For use with flask `before_request`, see readme for example usage.
    """

    def execute_before_request():
        if not _is_path_excluded(request.path, excluded_routes, excluded_routes_partial):
            start_traced_span(request.headers, request.path)
            get_logger().info(f'{request.method} - {request.url}')

    return execute_before_request


def after_request(excluded_routes=None, excluded_routes_partial=None):
    """
    Log the response status.

    For use with flask `after_request`, see readme for example usage.
    """

    def execute_after_request(response):
        if not _is_path_excluded(request.path, excluded_routes, excluded_routes_partial):
            get_logger().info(f'{response.status} - {request.url}')
        return response

    return execute_after_request


def teardown_request(excluded_routes=None, excluded_routes_partial=None):
    """
    Close the span when the request is torn down (finished). Will log an exception if one caught.

    For use with flask `teardown_request`, see readme for example usage.
    """

    def execute_on_teardown(exception):
        if exception:
            get_logger().exception(exception)
        if not _is_path_excluded(request.path, excluded_routes, excluded_routes_partial):
            end_traced_span()

    return execute_on_teardown


def _is_path_excluded(path, excluded_routes, excluded_routes_partial):
    """
    Work out if the Flask route should be traced & logged or not.

    Args:
        path (str):                         Flask route being accessed
        excluded_routes ([str,]):           _full_ routes to exclude
        excluded_routes_partial ([str,]):   partial routes to explore, useful if the route has path variales,
            eg use ['/app-config/config/'] to match '/app-config/<platform>/<version>/config.json'
    Returns:
        exclude (bool): True if exclude
    """
    exclude = False
    if excluded_routes and path in excluded_routes:
        exclude = True
    elif excluded_routes_partial:
        for excluded_route_partial in excluded_routes_partial:
            if excluded_route_partial in request.path:
                exclude = True
                break
    return exclude

# app/metrics.py

from prometheus_client import Counter, Summary

REQUEST_COUNT = Counter(
    "todo_requests_total", "Total number of requests", ["method", "endpoint"]
)

REQUEST_LATENCY = Summary(
    "todo_request_latency_seconds", "Latency of requests in seconds"
)

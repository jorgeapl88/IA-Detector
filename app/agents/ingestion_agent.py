def process_logs(log):

    failed_logins = int(log["failed_logins"])
    requests_per_minute = int(log["requests_per_minute"])

    return {
        "failed_logins": failed_logins,
        "requests_per_minute": requests_per_minute
    }

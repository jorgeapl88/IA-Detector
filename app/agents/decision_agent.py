def decide_action(prediction, failed_logins):

    if prediction == -1:

        if failed_logins >= 20:
            return "BLOCK"

        return "ALERT"

    return "IGNORE"

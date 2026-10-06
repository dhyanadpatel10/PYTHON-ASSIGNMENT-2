from collections import deque, defaultdict

def parse_time(t):
    h, m = map(int, t.split(":"))
    return h*60 + m

def detect_anomalies(X, T, logs):
    failures = defaultdict(deque)
    suspicious = {}

    for time, user, ip, status in logs:
        minutes = parse_time(time)
        if status == "FAIL":
            failures[user].append(minutes)
            # remove old failures outside window
            while failures[user] and minutes - failures[user][0] > T:
                failures[user].popleft()
        else:  # SUCCESS
            if len(failures[user]) >= X:
                # check if IP is different
                if ip != logs[0][2]:  # simplistic check: different from first fail IP
                    if user not in suspicious:
                        suspicious[user] = time

    for user in sorted(suspicious.keys()):
        print(user, suspicious[user])


# ---------------- SAMPLE INPUT ----------------
X, T = 2, 5
logs = [
    ("09:00", "u1", "1.1.1.1", "FAIL"),
    ("09:03", "u1", "1.1.1.1", "FAIL"),
    ("09:04", "u1", "2.2.2.2", "SUCCESS"),
    ("09:05", "u2", "3.3.3.3", "FAIL"),
    ("09:07", "u2", "4.4.4.4", "SUCCESS"),
]

detect_anomalies(X, T, logs)

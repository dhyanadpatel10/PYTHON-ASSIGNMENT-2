import json

def read_jsonl(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()

def process_records(lines):
    stats = {}
    for line in lines:
        try:
            record = json.loads(line)
            device = record.get("device_id")
            temp = record.get("temperature_c")
            if device not in stats:
                stats[device] = {"count":0,"min":float("inf"),"max":float("-inf"),"sum":0,"corrupted":0}
            try:
                temp = float(temp)
                stats[device]["count"] += 1
                stats[device]["min"] = min(stats[device]["min"], temp)
                stats[device]["max"] = max(stats[device]["max"], temp)
                stats[device]["sum"] += temp
            except:
                stats[device]["corrupted"] += 1
        except:
            continue
    return stats

def summarize(stats):
    for device, s in stats.items():
        if s["count"] > 0:
            avg = s["sum"]/s["count"]
            print(f"{device} count={s['count']} min={s['min']} max={s['max']} avg={avg:.2f} corrupted={s['corrupted']}")
        else:
            print(f"{device} count=0 corrupted={s['corrupted']}")

# ---------------- SAMPLE INPUT ----------------
# jsonl file "sensors.jsonl":
# {"device_id":"D2","temperature_c":25,"humidity":40}
# {"device_id":"D2","temperature_c":"bad","humidity":50}
# {"device_id":"D3","temperature_c":28,"humidity":55}

lines = read_jsonl("sensors.jsonl")
stats = process_records(lines)
summarize(stats)

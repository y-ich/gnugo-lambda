import os
import json
from subprocess import Popen, PIPE, TimeoutExpired

#PATH = "/usr/local/bin"
PATH = "./gnugo/bin"
TIMEOUT = 30

def gnugo(event, context):
    query = json.loads(event["body"])
    if query["move"] != "est":
        return { "statusCode": 400 }

    sgf = query["sgf"]
    method = query.get("method", "estimate")
    args = [
        os.path.join(PATH, "gnugo"),
        "--{}-rules".format(query.get("rule", "japanese")),
        "--score", method,
        '--infile', '-'
    ]
    if "mn" in query:
        args.extend(["--until", query["mn"]])
    timeout = query.get("time", TIMEOUT)
    p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False, encoding="utf-8")
    try:
        outs, error = p.communicate(input=sgf, timeout=timeout)
        return {
            "statusCode": 200,
            "headers": {},
            "body": json.dumps({
                "stdout": outs,
                "stderr": error
            })
        }
    except TimeoutExpired:
        p.kill()
        return { "statusCode": 408 }

if __name__ == "__main__":
    e = { "body": json.dumps({
        "move": "est",
        "sgf": "(;FF[4]GM[1]SZ[19]KM[6.5])"
    })}
    print(gnugo(e, None))
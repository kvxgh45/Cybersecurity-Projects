import hashlib, sys, os

def file_hash(path, algo='sha256'):
    h = hashlib.new(algo)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file> [algo]")
        sys.exit(1)
    path = sys.argv[1]
    algo = sys.argv[2] if len(sys.argv) > 2 else 'sha256'
    if os.path.isfile(path):
        print(f"{algo.upper()} hash of {path}: {file_hash(path, algo)}")
    else:
        print(f"File not found: {path}")

import platform, sys, subprocess, json
from pathlib import Path

info = {
    "python": sys.version,
    "platform": platform.platform(),
}
try:
    import rebound
    info["rebound"] = rebound.__version__
except Exception as e:
    info["rebound_error"] = repr(e)

Path("environment_runtime.json").write_text(json.dumps(info, indent=2))
with open("pip_freeze.txt","w") as f:
    subprocess.run([sys.executable,"-m","pip","freeze"],stdout=f,text=True)
print(json.dumps(info,indent=2))

import time
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler

TEMP_DIR = Path("./tmp")
TEMP_DIR.mkdir(exist_ok=True)

def clean_old_files():
    now = time.time()
    limit = now - (30 * 60)

    for f in TEMP_DIR.iterdir():
        if f.is_file():
            if f.stat().st_mtime < limit:
                try:
                    f.unlink()
                    print(f"Deleted: {f}")
                except Exception as e:
                    print(e)

def start_cleanup_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(clean_old_files, "interval", minutes=10)
    scheduler.start()
    print("Cleanup scheduler started")
    return scheduler

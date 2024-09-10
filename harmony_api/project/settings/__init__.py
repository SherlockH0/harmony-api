from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENVAR_SETTINGS_PREFIX = "HARMONY_API_SETTING_"  # implement this

LOCAL_SETTINGS_PATH = os.getenv(  # pyright: ignore
    f"{ENVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH", "local/settings/settings.dev.py"
)

if not os.path.isabs(LOCAL_SETTINGS_PATH):  # pyright: ignore
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

include(
    "base.py",
    "custom.py",
    optional(LOCAL_SETTINGS_PATH),
    "envvars.py",
)

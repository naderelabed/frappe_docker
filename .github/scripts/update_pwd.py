import os
import re


def get_versions():
    frappe_version = os.getenv("FRAPPE_VERSION")
    erpnext_version = os.getenv("ERPNEXT_VERSION")
    assert frappe_version, "No Frappe version set"
    assert erpnext_version, "No ERPNext version set"
    return frappe_version, erpnext_version


def update_pwd(frappe_version: str, erpnext_version: str):
    with open("pwd.yml", "r+") as f:
        content = f.read()
        for image, version in (
            ("naderelabed/frappe-socketio", frappe_version),
            ("naderelabed/erpnext-worker", erpnext_version),
            ("naderelabed/erpnext-nginx", erpnext_version),
        ):
            content = re.sub(rf"{image}:.*", f"{image}:{version}", content)
        f.seek(0)
        f.truncate()
        f.write(content)


def main() -> int:
    update_pwd(*get_versions())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

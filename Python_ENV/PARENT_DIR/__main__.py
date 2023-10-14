"""..."""

try:
    print("[PACKAGE]:\tRunning main code execution")
except KeyboardInterrupt:
    print("[SYSTEM]:\tKeyboard interuption has been called!")
finally:
    print("[SYSTEM]:\tFinished running main code execution",
        "[SYSTEM]:\tClosing package...",
        sep="\n")

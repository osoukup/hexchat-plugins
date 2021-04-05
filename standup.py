import hexchat

__module_name__ = "standup"
__module_version__ = "1.0"
__module_description__ = "stand up"


TIMEOUT = 1800000

standup_hook = None


def enable_standup(word, word_eol, userdata):
    global standup_hook
    if standup_hook is None:
        standup_hook = hexchat.hook_timer(TIMEOUT, standup)
        print("standup pluging enabled")
    return hexchat.EAT_ALL


def disable_standup(word, word_eol, userdata):
    global standup_hook
    if standup_hook is not None:
        hexchat.unhook(standup_hook)
        standup_hook = None
        print("standup pluging disabled")
    return hexchat.EAT_ALL


def standup(userdata):
    print("osoukup: stand up")
    return True  # keep the timeout going


standup_hook = hexchat.hook_timer(TIMEOUT, standup)
hexchat.hook_command("standup", enable_standup)
hexchat.hook_command("standdown", disable_standup)
print("standup plugin loaded")

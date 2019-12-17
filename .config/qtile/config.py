import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

from typing import List  

alt = "mod1"
windows = "mod4"
color1 = "705A37"
color2 = "48381F"
color3 = "A89984"

keys = [
    # Switch between windows in current stack pane
    Key([alt], "h", lazy.layout.left()),
    Key([alt], "l", lazy.layout.right()),
    Key([alt], "j", lazy.layout.down()),
    Key([alt], "k", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([alt, "shift"], "h", lazy.layout.swap_left()),
    Key([alt, "shift"], "l", lazy.layout.swap_right()),
    Key([alt, "shift"], "j", lazy.layout.shuffle_down()),
    Key([alt, "shift"], "k", lazy.layout.shuffle_up()),
    
    # Shrink/grow windows
    Key([alt], "i", lazy.layout.grow()),
    Key([alt], "m", lazy.layout.shrink()),
    Key([alt], "n", lazy.layout.normalize()),
    Key([alt], "o", lazy.layout.maximize()),
    Key([alt, "shift"], "space", lazy.layout.flip()),
    

    # Switch window focus to other pane(s) of stack
    Key([alt], "Tab", lazy.layout.next()),
    Key([windows], "Tab", lazy.layout.next()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([alt, "shift"], "Return", lazy.layout.toggle_split()),
    
    # Application Hotkeys
    Key([alt], "r", lazy.spawn("rofi -show run")),
    Key([alt], "w", lazy.spawn("rofi -show window")),
    Key([alt], "Return", lazy.spawn("terminator")),

    # Toggle between different layouts as defined below
#   Key([alt], "Tab", lazy.next_layout()),

    Key([alt], "F4", lazy.window.kill()),

    Key([alt, "control"], "r", lazy.restart()),
    Key([alt, "control"], "q", lazy.shutdown()),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # alt1 + letter of group = switch to group
        Key([alt], i.name, lazy.group[i.name].toscreen()),

        # alt1 + shift + letter of group = switch to & move focused window to group
        Key([alt, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

layouts = [
    layout.MonadTall(border_normal=color1, border_focus=color2, border_width=12, single_border_width=12, margin=40, single_margin=40, change_ratio=0.05),
]

widget_defaults = dict(
    font='sans',
    fontsize=18,
    kadding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(),
                widget.CurrentLayout(),
                widget.TextBox("my config", name="taylor-config-1"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            32,
            background=color1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([alt], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([alt], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([alt], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

#   @hook.subscribe.startup_once
#   def start_once():
#       subprocess.call("nitrogen --restore")

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

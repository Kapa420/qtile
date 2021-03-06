from libqtile import widget
from .theme import colors
from libqtile.command import lazy
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

US = 'us altgr-intl'

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def layout_keyboard(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        'display_map': {'us altgr-intl': 'us'},
    }

def layout_menu(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        'iconsize': 9,
        'mouse_callbacks' : {"Button1": lazy.spawn('jgmenu_run')},
        'filename': '/home/ankar/.config/qtile/icons/qtilelogo.png',
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.Image(**layout_menu(bg='dark')),
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Fantasque Sans Mono Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),
    
    powerline('color4','dark'),
    
    icon(bg='color4', fontsize=17, text=' '),
    
    widget.KeyboardLayout(**layout_keyboard(bg='color4'), configured_keyboards=['ru', US]),
    
    powerline('color2', 'color4'),

    icon(bg='color2', fontsize=17, text='蓼'),

    widget.PulseVolume(**base(bg='color2')),

    powerline('color1', 'color2'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color3', 'color1'),

    icon(bg="color3", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color3'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color3'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg='color4', fontsize=17, text=' '),

    widget.KeyboardLayout(**layout_keyboard(bg='color4'),
                          configured_keyboards=['ru', US]),

    powerline('color2', 'color4'),

    icon(bg='color2', fontsize=17, text='蓼'),

    widget.PulseVolume(**base(bg='color2')),

    powerline('color1', 'color2'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color3', 'color1'),

    icon(bg="color3", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color3'), format='%d/%m/%Y - %H:%M '),
]

widget_defaults = {
    'font': 'FantasqueSansMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

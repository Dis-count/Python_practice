~lbutton & enter::
exitapp
~WheelUp::
if (existclass("ahk_class Shell_TrayWnd")=1)
Send,{Volume_Up}
Return
~WheelDown::
if (existclass("ahk_class Shell_TrayWnd")=1)
Send,{Volume_Down}
Return
~MButton::
if (existclass("ahk_class Shell_TrayWnd")=1)
Send,{Volume_Mute}
Return

Existclass(class)
{
MouseGetPos,,,win
WinGet,winid,id,%class%
if win = %winid%
Return,1
Else
Return,0
}

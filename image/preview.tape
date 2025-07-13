Output preview.gif

Require devgrep
Require devopen
Require devmanage

Set Shell "bash"
Set FontSize 16
Set Width 1200
Set Height 600
Set Padding 10
Set Theme "Hivacruz"

Type@.1 "devopen --preview std::swap" Sleep 2 Enter
Sleep 5 Up Sleep 5 Down Sleep 5
Ctrl+C
Sleep 2
Enter

Type@.1 "devgrep --preview c++ std::" Sleep 2 Enter
Sleep 5
Up@1 5
Sleep 3
Backspace@.1 5
Ctrl+C
Sleep 5

Output showcase.gif

Require devgrep
Require devopen
Require devmanage

Set Shell "bash"
Set FontSize 16
Set Width 1200
Set Height 600
Set Padding 10
Set Theme "Hivacruz"

Type@.1 "devopen c" Sleep 2 Enter
Sleep 5
Type@.2 "JJJJJ"
Sleep 1
Down@.3 6
Sleep 2
Enter
Sleep 3
Type@.1 "JJJJJJJJJJJJJJJJJJJJJJJJJJJJ"
Sleep 3
Ctrl+C
Sleep 2

Enter
Type@.1 "devmanage --install rust" Sleep .5 Enter
Sleep 3

Enter
Type@.1 "devmanage --local" Sleep 2 Enter
Sleep 5

Enter
Type@.1 "devgrep rust" Sleep 2 Enter
Sleep 5
Type@.5 "std::any"
Sleep 3
Enter
Sleep 5
Type@.1 "JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ"
Sleep 2
Type@.1 "KKKKKKKKKK"
Sleep 3
Ctrl+C
Sleep 2
Backspace@.1 8
Ctrl+C
Sleep 5

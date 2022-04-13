#Imports
import webbrowser, time
import sys
import os



print('''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

                              
--~~BioXsec Website Tool~~ ->	https://github.com/BioXsec
''')


print('[ Initializing program ]')
url = input("Enter url: ") 

time.sleep(0.5)

print(
    '[ Setting up program ]')
views = input("Enter amount of views: ")

time.sleep(0.5)

print('[ Setting up duration ]')
duration = input("Enter duration before opening another site (in seconds): ")

toolbar_width = 50
# setting up toolbar [-------------------------------------]
sys.stdout.write("[%s]"%(("-")*toolbar_width))
sys.stdout.flush()
for i in range(toolbar_width):
    sys.stdout.write("\r") 
    sys.stdout.flush()
    sys.stdout.write("[")
    sys.stdout.write("."*(i+1))
    sys.stdout.flush()
    time.sleep(0.1)





for i in range(int(views)):
    webbrowser.open_new(url)
    time.sleep(int(duration))

    print('Finisch!')

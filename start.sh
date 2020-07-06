clear
echo '''
 _   _   ___  _   _ _____ _   _ 
| \ | | / _ \| | | |_   _| \ | | Author    : Navin Hariharan
|  \| |/ /_\ \ | | | | | |  \| | Github    : navin-hariharan
| . ` ||  _  | | | | | | | . ` | Instagram : navin_hariharan
| |\  || | | \ \_/ /_| |_| |\  | Linkedin  : navin-hariharan
\_| \_/\_| |_/\___/ \___/\_| \_/ Whatsapp  : +917305574234
''' | lolcat
echo ''
printf "I WILL USE FOR EDUCATIONAL PURPOSES ONLY [Y/Yes] : " | lolcat
read -r option
if [ $option == 'y' ] || [ $option == 'Y' ]|| [ $option == 'yes' ]|| [ $option == 'Yes' ]
then
python2 main.py
else
exit
fi

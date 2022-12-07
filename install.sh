echo "Starting installation..."
sleep 1
pkg install python -y 
clear
pip install colorama 
clear
pip install tqdm 
clear
echo "installation complated."
var1="1"
echo "Do you wanna run script?"
echo "[1] Yes"
echo "[2] No"
read -p ">> " resp
if [ "$resp" == "$var1" ]
then
python3 DosS.py
else
echo "you can run script by typing : python DosS"
echo "~~Sqlost~~"
fi
